from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from pydub import AudioSegment
import os

# Define GUI Functions

# Function to select download location
def select_location():
    location = filedialog.askdirectory()
    label_path.config(text=location)

# Function to download YouTube video
def download_video():
    url = entry_url.get()
    path = label_path.cget('text')
    
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        label_progress.config(text='Downloading Video...')
        stream.download(output_path=path)
        label_progress.config(text='Video Download Complete')
    except:
        label_progress.config(text='Video Download Failed')

# Function to download YouTube audio and play it
def play_audio():
    url = entry_url.get()
    path = label_path.cget('text')

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).order_by('bitrate').desc().first()
        label_progress.config(text='Downloading Audio...')
        stream.download(output_path=path, filename='audio')
        label_progress.config(text='Extracting Audio...')
        audio = AudioSegment.from_file(os.path.join(path, 'audio.mp4'), 'mp4')
        label_progress.config(text='Playing Audio...')
        with open(os.path.join(path, 'audio.mp3'), 'wb') as f:
            audio.export(f, format='mp3')
        os.system('open ' + os.path.join(path, 'audio.mp3'))
        label_progress.config(text='Audio Playback Complete')
    except:
        label_progress.config(text='Audio Playback Failed')

# Create GUI
root = Tk()
root.title('YouTube Downloader')
root.geometry('400x300')
root.resizable(False, False)
root.config(bg='white')

# Add GUI Components
label_title = Label(root, text='YouTube Downloader', font=('Arial', 16, 'bold'), bg='white')
label_title.pack(pady=10)

label_url = Label(root, text='Enter YouTube URL:', font=('Arial', 12), bg='white')
label_url.pack(pady=10)

entry_url = Entry(root, width=50, font=('Arial', 12))
entry_url.pack()

label_path = Label(root, text='Download Path:', font=('Arial', 12), bg='white')
label_path.pack(pady=10)

button_browse = Button(root, text='Browse', command=select_location)
button_browse.pack()

button_download = Button(root, text='Download Video', command=download_video, bg='blue', fg='white', font=('Arial', 12))
button_download.pack(pady=20)

button_play = Button(root, text='Play Audio', command=lambda: play_audio(), bg='green', fg='white', font=('Arial', 12))
button_play.pack()

label_progress = Label(root, text='', font=('Arial', 12), bg='white')
label_progress.pack(pady=10)

# Start GUI
root.mainloop()
