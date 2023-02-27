import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import os

# Create a window object
window = tk.Tk()
window.title("Download YouTube Videos/Audios")
window.geometry("800x600")




# Define function for Downloading
def download():
    # Get the link from the user
    link = entry.get()
    # Create a YouTube object
    yt = YouTube(link)
    # Get the available streams
    streams = yt.streams.filter(progressive=True).all()
    # Ask the user to select the stream
    print("Please select the stream")
    listbox.insert(0,"Please select the stream")
    
    for stream in streams:
        print(stream)
        listbox.insert(0,stream)
        
    # Ask the user to select the format
    stream_index = 2#int(input("Please select the stream index : "))
    
    # Get the selected stream
    selected_stream = streams[stream_index]
    # Get the location of download
    location = filedialog.askdirectory()
    # Download the stream
    selected_stream.download(location)
    # Print the path of the downloaded video/audio
    print(f"{selected_stream.default_filename} was downloaded successfully at {location}")


# Create the label
label = tk.Label(text="Welcome to the YouTube Downloader")
label.pack()

# Create the entry
entry = tk.Entry(width=50)
entry.pack()


# Create the button
button = tk.Button(text="Download", command=download)
button.pack()

# Create the listbox
listbox = tk.Listbox(width=50)
listbox.pack()



# Run the window
window.mainloop()