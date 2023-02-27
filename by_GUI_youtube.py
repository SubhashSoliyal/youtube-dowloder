from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from pydub import AudioSegment
import os


# Create the GUI window
root = Tk()
root.geometry('500x400')
root.title('YouTube Downloader')

# Create the widgets
label_url = Label(root, text='Enter the YouTube video URL:')
entry_url = Entry(root, width=50)
label_path = Label(root, text='Choose the path to save the video:')
button_path = Button(root, text='Select Path', command=lambda: get_path())
label_progress = Label(root, text='')
button_download = Button(root, text='Download Video', command=lambda: download_video())
button_download1 = Button(root, text='Download Audio', command=lambda: download_Audio())
button_play = Button(root, text='Play Audio', command=lambda: play_audio())
button_play.pack()


# Add the widgets to the window
label_url.pack()
entry_url.pack()
label_path.pack()
button_path.pack()
label_progress.pack()
button_download.pack()
button_download1.pack()

# Function to get the file path from the user
def get_path():
    path = filedialog.askdirectory()
    label_path.config(text=path)

# Function to download the video
def download_video():
    url = entry_url.get()
    path = label_path.cget('text')

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        label_progress.config(text='Downloading...')
        stream.download(output_path=path)
        label_progress.config(text='Download Complete')
    except:
        label_progress.config(text='Download Failed')

def download_Audio():
    url = entry_url.get()
    path = label_path.cget('text')

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).order_by('bitrate').desc().first()
        label_progress.config(text='Downloading...')
        stream.download(output_path=path)
        label_progress.config(text='Download Complete')
    except:
        label_progress.config(text='Download Failed')


# Function to play the audio of the downloaded video
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

# Run the GUI window
root.mainloop()
