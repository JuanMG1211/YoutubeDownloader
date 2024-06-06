from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def downloadVideo(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Downloaded successfully")
    except Exception as e:
        print(e)

def openFileExplorer():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    
    return folder

def main():
    url = input("Enter the video URL: ")
    save_path = openFileExplorer()

    if save_path:
        print("Download started. Please wait.")
        downloadVideo(url, save_path)
    else:
        print("No folder selected. Exiting program.")

main()
