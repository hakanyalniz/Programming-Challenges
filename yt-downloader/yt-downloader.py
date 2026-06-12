import os
from typing import Any

import yt_dlp


def download_youtube_video(video_url: str, output_path: str = "./downloads"):
    """
    Downloads a YouTube video in MP4 format at the best available quality.
    """
    # Ensure output directory exists, if not create
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Configuration options for yt-dlp
    ydl_opts: Any = {
        # 'bestvideo+bestaudio/best' merges the highest quality video and audio.
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
    }

    try:
        print(f"Fetching video information for: {video_url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_youtube_video(url)
