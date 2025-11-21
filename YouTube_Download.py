import os
import yt_dlp
import re

def sanitize_filename(title):
    """Sanitize the title to create a valid filename"""
    return re.sub(r'[\\/*?:"<>|]', '', title)

def ensure_download_dir():
    os.makedirs("downloads", exist_ok=True)

def download_video(url):
    ensure_download_dir()
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "downloads/%(title)s-%(id)s.%(ext)s",
        "writesubtitles": True,
        "writeautomaticsub": True,
        "embedsubtitles": True,
        "subtitleslangs": ["en"],
        "postprocessors": [
            {"key": "FFmpegEmbedSubtitle"},
        ],
        "restrictfilenames": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_mp3(url):
    ensure_download_dir()
    ydl_opts = {
        "format": "bestaudio/best",
        # let yt_dlp pick a safe filename and do the conversion
        "outtmpl": "downloads/%(title)s-%(id)s.%(ext)s",
        "restrictfilenames": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # this both downloads and converts to mp3
        ydl.download([url])

while True:
    action = input("Enter '1' to download videos (with subtitles if available), '2' to convert videos to MP3, or 'q' to quit: ")

    if action in ["1", "2"]:
        urls_input = input("Enter a URL or the path to a file containing multiple URLs: ")

        if os.path.isfile(urls_input):
            with open(urls_input, "r") as f:
                urls = [line.strip() for line in f if line.strip()]
        else:
            urls = [urls_input]

        for url in urls:
            try:
                if action == "1":
                    download_video(url)
                elif action == "2":
                    download_mp3(url)
            except Exception as e:
                print(f"An error occurred: {e}")
    elif action == "q":
        break
    else:
        print("Invalid input. Please enter '1', '2', or 'q'.")
