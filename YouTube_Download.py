import os
import subprocess
import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s-%(id)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s-%(id)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    info = yt_dlp.YoutubeDL().extract_info(url, download=False)
    input_file = f'downloads/{info["title"]}-{info["id"]}.{info["ext"]}'
    output_file = f'downloads/{info["title"].split(" - ")[0]} - {info["title"].split(" - ")[1]}.mp3'
    subprocess.run(["ffmpeg", "-i", input_file, "-ab", "320k", output_file])

while True:
    action = input("Enter '1' to download videos, '2' to convert videos to MP3, or 'q' to quit: ")

    if action in ['1', '2']:
        urls_input = input("Enter a URL or the path to a file containing multiple URLs: ")

        if os.path.isfile(urls_input):
            with open(urls_input, 'r') as f:
                urls = [line.strip() for line in f.readlines()]
        else:
            urls = [urls_input]

        for url in urls:
            if action == '1':
                download_video(url)
            elif action == '2':
                download_mp3(url)
    elif action == 'q':
        break
    else:
        print("Invalid input. Please enter '1', '2', or 'q'.")

