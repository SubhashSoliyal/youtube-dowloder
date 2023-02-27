from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
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
        messagebox.showinfo('Download Complete', 'Video downloaded successfully!')
    except:
        label_progress.config(text='Video Download Failed')
        messagebox.showerror('Download Failed', 'Failed to download video. Please check the URL and download location.')

# Function to download YouTube audio and play it
def download_audio():
    url = entry_url.get()
    path = label_path.cget('text')

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).order_by('bitrate').desc().first()
        label_progress.config(text='Downloading Audio...')
        stream.download(output_path=path, filename='audio')
        label_progress.config(text='Extracting Audio...')
        audio = AudioSegment.from_file(os.path.join(path, 'audio.mp4'), 'mp4')
        with open(os.path.join(path, 'audio.mp3'), 'wb') as f:
            audio.export(f, format='mp3')
        label_progress.config(text='Audio Download Complete')
        messagebox.showinfo('Download Complete', 'Audio downloaded successfully!')
    except:
        label_progress.config(text='Audio Download Failed')
        messagebox.showerror('Download Failed', 'Failed to download audio. Please check the URL and download location.')

# Function to play downloaded audio
def play_audio():
    url = entry_url.get()
    path = label_path.cget('text')

    try:
        audio_path = os.path.join(path, 'audio.mp3')
        if os.path.exists(audio_path):
            os.system(f'start "" "{audio_path}"')
            label_progress.config(text='Audio Playback Started')
        else:
            label_progress.config(text='No Audio Found')
    except:
        label_progress.config(text='Audio Playback Failed')

# Create GUI
root = Tk()
root.title('YouTube Downloader')
root.geometry('400x400')
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

button_download_video = Button(root, text='Download Video', command=download_video, bg='blue', fg='white', font=('Arial', 12))
button_download_video.pack(pady=20)

button_download_audio = Button(root, text='Download Audio', command=download_audio,bg='green', fg='white', font=('Arial', 12))
button_download_audio.pack(pady=10)

button_play_audio = Button(root, text='Play Audio', command=play_audio, bg='purple', fg='white', font=('Arial', 12))
button_play_audio.pack(pady=10)

label_progress = Label(root, text='', font=('Arial', 12), bg='white')
label_progress.pack(pady=20)

# Run GUI
root.mainloop()
