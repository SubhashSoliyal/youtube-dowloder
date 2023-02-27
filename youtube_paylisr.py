import tkinter as tk
from tkinter import filedialog
from pytube import YouTube, Playlist

class YouTubePlaylistDownloaderGUI:
    def __init__(self, master):
        self.master = master
        master.title("YouTube Playlist Downloader")

        # Create input fields for playlist URL and download directory
        self.playlist_url_label = tk.Label(master, text="Playlist URL:")
        self.playlist_url_label.pack()
        self.playlist_url_entry = tk.Entry(master, width=50)
        self.playlist_url_entry.pack()

        self.download_dir_label = tk.Label(master, text="Download Directory:")
        self.download_dir_label.pack()
        self.download_dir_frame = tk.Frame(master)
        self.download_dir_frame.pack()

        self.download_dir_entry = tk.Entry(self.download_dir_frame, width=50)
        self.download_dir_entry.pack(side=tk.LEFT)
        self.download_dir_entry.insert(tk.END, "./downloads")

        self.download_dir_button = tk.Button(self.download_dir_frame, text="Choose", command=self.choose_download_dir)
        self.download_dir_button.pack(side=tk.LEFT)

        # Create a button to initiate the download process
        self.download_button = tk.Button(master, text="Download", command=self.download_playlist)
        self.download_button.pack()

    def choose_download_dir(self):
        # Ask the user to select the download directory
        download_dir = filedialog.askdirectory()
        self.download_dir_entry.delete(0, tk.END)
        self.download_dir_entry.insert(tk.END, download_dir)

    def download_playlist(self):
        # Get the playlist URL and download directory
        playlist_url = self.playlist_url_entry.get()
        download_dir = self.download_dir_entry.get()

        # Create an instance of the YouTube class for the playlist
        playlist = YouTube(playlist_url)
        playlist = Playlist(playlist_url)

        # Get the list of videos in the playlist
        videos = playlist.video_urls

        # Loop through the list of videos and download each video
        for i, video_url in enumerate(videos):
            video = YouTube(video_url)

            # Set the output filename to include the serial number
            filename = f"{i+1}. {video.title}"

            # Download the video
            video.streams.get_highest_resolution().download(output_path=download_dir, filename=filename)

        # Display a message box when the download is complete
        tk.messagebox.showinfo("Download Complete", "The playlist has been downloaded.")

# Create the main window and run the GUI
root = tk.Tk()
gui = YouTubePlaylistDownloaderGUI(root)
root.mainloop()
