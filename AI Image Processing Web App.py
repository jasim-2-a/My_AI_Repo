import os
import io
from PIL import Image
from flask import Flask, render_template_string, request, send_file, jsonify

try:
    from rembg import remove # type: ignore
    REMBG_AVAILABLE = True
except ImportError:
    REMBG_AVAILABLE = False

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AI Image Processing App</title>
    <style>
        body { font-family: Arial; margin: 40px; display: flex; gap: 40px; }
        input, select { margin: 10px 0; display: block; }
        #left { flex: 1; }
        #right { flex: 1; border-left: 1px solid #ccc; padding-left: 20px; }
        img { max-width: 100%; margin-top: 10px; }
    </style>
</head>
<body>
<div id="left">
<h2>AI Image Processing Tools</h2>
<form id="imageForm" action="/process" method="post" enctype="multipart/form-data">
    <label>Upload an image:</label>
    <input type="file" name="image" id="imageInput" required>

    <label>Choose operation:</label>
    <select name="operation">
        <option value="resize">Resize by Dimensions</option>
        <option value="aspect">Resize by Aspect Ratio</option>
        <option value="compress">Compress to Target File Size</option>
        <option value="resolution">Change DPI</option>
        <option value="grayscale">Convert to Grayscale</option>
        <option value="crop">Crop Image</option>
        <option value="removebg">Remove Background (AI)</option>
    </select>

    <div id="resize-params">
        <label>Width:</label><input type="number" name="width">
        <label>Height:</label><input type="number" name="height">
    </div>
    <label>Target File Size (KB):</label><input type="number" name="filesize">
    <label>DPI (e.g. 72,150):</label><input type="text" name="dpi">

    <label>Crop (x, y, width, height):</label>
    <input type="text" name="crop" placeholder="e.g. 10,10,200,200">

    <button type="submit">Submit</button>
</form>
</div>
<div id="right">
    <h3>Image Preview & Properties</h3>
    <div id="imageInfo"></div>
    <img id="preview" />
</div>
<script>
    const imageInput = document.getElementById('imageInput');
    const preview = document.getElementById('preview');
    const info = document.getElementById('imageInfo');

    imageInput.addEventListener('change', () => {
        const file = imageInput.files[0];
        if (!file) return;

        const formData = new FormData();
        formData.append('image', file);

        const reader = new FileReader();
        reader.onload = e => preview.src = e.target.result;
        reader.readAsDataURL(file);

        fetch('/preview', { method: 'POST', body: formData })
            .then(res => res.json())
            .then(data => {
                info.innerHTML = `
                    <strong>Filename:</strong> ${data.filename}<br>
                    <strong>Dimensions:</strong> ${data.width} × ${data.height} px<br>
                    <strong>Format:</strong> ${data.format}<br>
                    <strong>Mode:</strong> ${data.mode}<br>
                    <strong>DPI:</strong> ${data.dpi} dpi<br>
                    <strong>File size:</strong> ${data.size_kb} KB<br>
                `;
            });
    });
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/preview', methods=['POST'])
def preview():
    file = request.files['image']
    image = Image.open(file.stream)
    dpi = image.info.get('dpi', (72, 72))
    if isinstance(dpi, tuple):
        if len(dpi) == 2:
            dpi_str = f"{dpi[0]} × {dpi[1]}"
        elif len(dpi) == 1:
            dpi_str = f"{dpi[0]}"
        else:
            dpi_str = "N/A"
    else:
        dpi_str = "N/A"
    file.seek(0, os.SEEK_END)
    size_kb = round(file.tell() / 1024, 2)

    return jsonify({
        'filename': file.filename,
        'width': image.width,
        'height': image.height,
        'format': image.format,
        'mode': image.mode,
        'dpi': dpi_str,
        'size_kb': size_kb
    })

@app.route('/process', methods=['POST'])
def process():
    file = request.files['image']
    operation = request.form['operation']
    image = Image.open(file.stream)

    output = io.BytesIO()
    filename = f"processed_{operation}.png"

    if operation == 'resize':
        width = int(request.form.get('width', 0))
        height = int(request.form.get('height', 0))
        if width > 0 and height > 0:
            image = image.resize((width, height), Image.LANCZOS)
            image.save(output, format='PNG')

    elif operation == 'aspect':
        new_width = int(request.form.get('width', 0))
        if new_width > 0:
            w_percent = (new_width / float(image.size[0]))
            new_height = int((float(image.size[1]) * float(w_percent)))
            image = image.resize((new_width, new_height), Image.LANCZOS)
            image.save(output, format='PNG')

    elif operation == 'compress':
        target_kb = int(request.form.get('filesize', 0))
        quality = 95
        while quality > 10:
            buffer = io.BytesIO()
            image.save(buffer, format='JPEG', quality=quality)
            if buffer.tell() / 1024 <= target_kb:
                output = buffer
                break
            quality -= 5

    elif operation == 'resolution':
        dpi_text = request.form.get('dpi', '72')
        dpi = tuple(map(int, dpi_text.split(',')))
        image.save(output, format='PNG', dpi=dpi)

    elif operation == 'grayscale':
        image = image.convert('L')
        image.save(output, format='PNG')

    elif operation == 'crop':
        crop_vals = request.form.get('crop', '')
        try:
            x, y, w, h = map(int, crop_vals.split(','))
            image = image.crop((x, y, x + w, y + h))
            image.save(output, format='PNG')
        except:
            return 'Invalid crop values', 400

    elif operation == 'removebg':
        if not REMBG_AVAILABLE:
            return 'Background removal requires the rembg module. Please install with: pip install rembg', 500
        image = image.convert("RGBA")
        image_data = io.BytesIO()
        image.save(image_data, format='PNG')
        image_data.seek(0)
        result = remove(image_data.read())
        output.write(result)

    output.seek(0)
    return send_file(output, as_attachment=True, download_name=filename, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
