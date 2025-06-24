from pytube import YouTube
import os

def normalize_url(url):
    # Convert Shorts URL to normal watch format
    if "youtube.com/shorts/" in url:
        url = url.replace("youtube.com/shorts/", "youtube.com/watch?v=")
    return url

def get_streams(yt):
    try:
        # Get only progressive mp4 streams (video + audio)
        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        return list(streams)
    except Exception as e:
        print(f"Error retrieving streams: {e}")
        return []

def main():
    url = input("Enter the YouTube video URL (press Enter to use example): ").strip()
    
    # Use example Shorts URL if no input is given
    if not url:
        url = "https://www.youtube.com/shorts/juaOK3B14CM"
        print(f"Using example URL: {url}")
    
    url = normalize_url(url)

    try:
        yt = YouTube(url)
    except Exception as e:
        print(f"Error loading video: {e}")
        return

    print(f"\nTitle   : {yt.title}")
    print(f"Author  : {yt.author}")
    print(f"Duration: {yt.length // 60} minutes")

    streams = get_streams(yt)
    if not streams:
        print("No downloadable video streams found.")
        return

    print("\nAvailable Video Streams:")
    for i, stream in enumerate(streams, start=1):
        size_mb = round(stream.filesize / (1024 * 1024), 2)
        print(f"{i}. {stream.resolution} - {size_mb} MB")

    try:
        choice = int(input("\nSelect the number of the stream to download: "))
        stream = streams[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    output_path = input("Enter output folder (leave empty for current directory): ").strip()
    if not output_path or not os.path.isdir(output_path):
        output_path = os.getcwd()

    print("\nDownloading...")
    try:
        stream.download(output_path=output_path)
        print("✅ Download completed successfully!")
    except Exception as e:
        print(f"❌ Download failed: {e}")

if __name__ == "__main__":
    main()

