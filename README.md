# YouTube Video Downloader

I wrote this tool to simplify the process of downloading and converting YouTube videos. Feel free to use it and even contribute if you find it helpful. It can download videos for watching later, or download videos and convert as MP3. 

## Features

- Download YouTube videos in high-quality formats
- Convert downloaded videos to MP3 format
- User-friendly command-line interface
- Supports single video URLs and files containing multiple URLs
- Installation

Before getting started, ensure you have Python 3 installed on your system. You can download it from the official website.

Next, you will need to install a couple of dependencies:

`yt-dlp`: A powerful command-line tool for downloading videos from YouTube and other sites.

`youtube-dl`: A popular alternative to yt-dlp for downloading videos.

`ffmpeg`: A versatile tool for handling video, audio, and other multimedia files and streams (install via brew for Mac).

You can install yt-dlp and youtube-dl using pip:

```
pip install yt-dlp youtube_dl
```
For ffmpeg, follow the installation instructions for your operating system:

Windows
macOS
Linux
Usage

Getting started is straightforward:

Clone this repository or download the youtube_video_downloader.py script.

```
git clone https://github.com/your_username/YouTube-Video-Downloader.git
```
Navigate to the directory containing the script:

```
cd YouTube-Video-Downloader
```
Run the script using Python:
```
python youtube_video_downloader.py
```
You'll be prompted with the following options:

`Enter '1' to download videos, '2' to convert videos to MP3, or 'q' to quit:`
`Enter 1, 2, or q depending on what you want to do.`

If you choose to download videos or convert videos to MP3, you'll be asked to enter a URL or the path to a file containing multiple URLs:

`Enter a URL or the path to a file containing multiple URLs:`
Enter the URL of the YouTube video you want to download or the path to a file with multiple YouTube video URLs.

Watch the script work its magic. 🎉 Your video(s) will be downloaded or converted to MP3 based on your choice.
