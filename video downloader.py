import tkinter as tk
from pytube import YouTube
from tkinter import messagebox

def download_video():
    url = url_entry.get()
    if not url.strip():
        messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo("Success", f"Downloaded:\n{yt.title}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video:\n{e}")

# Set up the GUI window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x150")

# URL input
tk.Label(root, text="Enter YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Download button
download_btn = tk.Button(root, text="Download Video", command=download_video)
download_btn.pack(pady=10)

# Start the GUI event loop
root.mainloop()
