# Python Video Downloader

I wrote this tool to simplify the process of downloading and converting YouTube videos. It uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) to download the video as a webm file, then ffmpeg to convert to either an `mp4` or `mkv`, or `mp3` if using option 2. Feel free to use it and even contribute if you find it helpful. It can download videos for watching later, or download videos and convert as MP3. 

<img width="580" alt="image" src="https://user-images.githubusercontent.com/41294610/233874563-947c3a0b-c54c-4b62-84fc-1413641317c5.png">


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

You can install yt-dlp and [youtube-dl](https://github.com/ytdl-org/youtube-dl) using pip:

```
pip install yt-dlp youtube_dl
```
For [ffmpeg](https://ffmpeg.org/download.html), follow the installation instructions for your operating system. Or for MacOS:

```
brew install ffmpeg
```

## Usage

Getting started is straightforward:

Clone this repository or download the `.py` script.

```
git clone https://github.com/hackerman-jpeg/YouTube_Downloader.git

```

Run the script using Python:

```
python3 YouTube_Downloader.py
```

You'll be prompted with the following options:

`Enter '1' to download videos, '2' to convert videos to MP3, or 'q' to quit:`

Enter 1, 2, or q depending on what you want to do.


If you choose to download videos or convert videos to MP3, you'll be asked to enter a URL or the path to a file containing multiple URLs:

`Enter a URL or the path to a file containing multiple URLs:`

Enter the URL of the YouTube video you want to download or the path to a file with multiple YouTube video URLs. You can download entire playlists as well, as long as you navigate to the player that has the playlist on the right (usually by clicking a video in a playlist), and then copying the URL in the search bar. Generally a playlist URL from YouTube might look like this: 

https://www.youtube.com/watch?v=uJt4dOKmaQY&`list=PLDB42220DEE96FD9`

>  The URL might need to be the full URL shown in web address bar, usually has `watch=` near the end. 


Watch the script work its magic. 🎉 Your video(s) will be downloaded or converted to MP3 based on your choice.
