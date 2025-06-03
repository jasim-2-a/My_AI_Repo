import qrcode

# Data you want to encode
data = "https://www.youtube.com"

# Create QR Code object
qr = qrcode.QRCode(
    version=1,  # size of the QR Code: 1 is 21x21
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save it
img.save("my_qr_code.png")
print("QR Code saved as 'my_qr_code.png'")

