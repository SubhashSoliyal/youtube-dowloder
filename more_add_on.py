import os
import subprocess
from tkinter import Tk, Frame, Label, Entry, Button, Listbox, Scrollbar
import youtube_dl

# Initialize GUI
root = Tk()
root.title('YouTube Downloader')
root.geometry('800x600')
root.config(bg='white')

# Define functions
def download_video():
    url = entry_url.get()
    if not url:
        label_progress.config(text='Please enter a valid URL')
        return

    ydl_opts = {'outtmpl': '%(title)s.%(ext)s', 'format': 'bestvideo[height<=720]+bestaudio/best'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    filename = get_most_recent_file()
    listbox_downloads.insert(0, filename)
    label_progress.config(text='Video downloaded successfully')

def download_audio():
    url = entry_url.get()
    if not url:
        label_progress.config(text='Please enter a valid URL')
        return

    ydl_opts = {'outtmpl': '%(title)s.%(ext)s', 'format': 'bestaudio/best'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    filename = get_most_recent_file()
    listbox_downloads.insert(0, filename)
    label_progress.config(text='Audio downloaded successfully')

def play_audio():
    selected = listbox_downloads.curselection()
    if not selected:
        label_progress.config(text='Please select a file to play')
        return

    filename = listbox_downloads.get(selected[0])
    subprocess.Popen(['afplay', filename])

def play_video():
    selected = listbox_downloads.curselection()
    if not selected:
        label_progress.config(text='Please select a file to play')
        return

    filename = listbox_downloads.get(selected[0])
    subprocess.Popen(['open', '-a', 'VLC', filename])

def get_most_recent_file():
    files = os.listdir()
    files.sort(key=os.path.getmtime)
    return files[-1]

# Define GUI elements
frame_left = Frame(root, bg='white')
frame_left.pack(side=LEFT, padx=10)

label_url = Label(frame_left, text='Enter YouTube URL:', font=('Arial', 14), bg='white')
label_url.pack(pady=10)

entry_url = Entry(frame_left, width=50, font=('Arial', 12), bg='#eeeeee')
entry_url.pack(pady=10)

button_download_video = Button(frame_left, text='Download Video', command=download_video, width=20, font=('Arial', 12), bg='#4caf50', fg='white')
button_download_video.pack(pady=10)

button_download_audio = Button(frame_left, text='Download Audio', command=download_audio, width=20, font=('Arial', 12), bg='#2196f3', fg='white')
button_download_audio.pack(pady=10)

button_play_audio = Button(frame_left, text='Play Audio', command=play_audio, width=20, font=('Arial', 12), bg='#f44336', fg='white')
button_play_audio.pack(pady=10)

button_play_video = Button(frame_left, text='Play Video', command=play_video, width=20, font=('Arial', 12), bg='#9c27b0', fg='white')
button_play_video.pack(pady=10)

label_progress = Label(frame_left, text='', font=('Arial', 12), bg='white')
label_progress.pack(pady=10)

frame_right = Frame(root, bg='white')
frame_right.pack(side=RIGHT, padx=10)

label_downloads = Label(frame_right, text='Downloaded Files:', font=('Arial', 14), bg='white')
label_downloads.pack(pady=10)

scrollbar_downloads = Scrollbar(frame_right)
scrollbar_downloads.pack(side=RIGHT, fill=Y)

listbox_downloads = Listbox(frame_right, width=50, font=('Arial', 12), bg='#eeeeee', yscrollcommand=scrollbar_downloads.set)
listbox_downloads.pack(pady=10)

scrollbar_downloads.config(command=listbox_downloads.yview)

# Populate downloaded files list
files = [f for f in os.listdir() if os.path.isfile(f) and not f.endswith('.py')]
files.sort(key=os.path.getmtime, reverse=True)
for file in files:
    listbox_downloads.insert(END, file)

# Start GUI
root.mainloop()

