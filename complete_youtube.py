# from tkinter import *
# from tkinter import messagebox, filedialog
# from pytube import YouTube
# from moviepy.editor import * #pip install moviepy
# import os

# # Create GUI
# root = Tk()
# root.title("YouTube Downloader")
# root.geometry("800x600")
# root.config(bg='white')

# # Create frames
# frame_top = Frame(root, bg='white')
# frame_top.pack(pady=30)

# frame_left = Frame(root, bg='white')
# frame_left.pack(side=LEFT, padx=10)

# frame_right = Frame(root, bg='white')
# frame_right.pack(side=RIGHT, padx=10)

# # Create top label
# label_top = Label(frame_top, text='YouTube Downloader', font=('Arial', 24), bg='white')
# label_top.pack()

# # Create input box and search button
# input_var = StringVar()
# input_box = Entry(frame_top, textvariable=input_var, font=('Arial', 16), width=50)
# input_box.pack(side=LEFT, padx=10)

# history = []

# def search():
#     query = input_var.get()
#     if query == '':
#         messagebox.showerror('Error', 'Please enter a search query')
#     else:
#         history.append(query)
#         input_box.delete(0, END)
#         progress_label.config(text='Searching...')
#         search_results = search_youtube(query)
#         show_results(search_results)

# def search_youtube(query):
#     results = []
#     try:
#         videos = YouTube.search(query, max_results=10)
#         for video in videos:
#             result = {'title': video.title, 'url': video.watch_url}
#             results.append(result)
#     except:
#         messagebox.showerror('Error', 'Failed to retrieve search results')
#     return results

# def show_results(search_results):
#     for widget in frame_left.winfo_children():
#         widget.destroy()
#     for result in search_results:
#         title = result['title']
#         url = result['url']
#         button = Button(frame_left, text=title, font=('Arial', 12), bg='#eeeeee', width=60, command=lambda url=url: download(url))
#         button.pack(pady=5)
#     progress_label.config(text='')

# search_button = Button(frame_top, text='Search', font=('Arial', 16), bg='#eeeeee', command=search)
# search_button.pack(side=LEFT)

# # Create progress label
# progress_label = Label(frame_top, text='', font=('Arial', 16), bg='white')
# progress_label.pack(side=LEFT)

# # Create download function
# def download(url):
#     result = messagebox.askyesno('Download', 'Are you sure you want to download this video?')
#     if result:
#         try:
#             progress_label.config(text='Downloading...')
#             path = filedialog.askdirectory()
#             if path == '':
#                 return
#             video = YouTube(url)
#             video_stream = video.streams.get_highest_resolution()
#             video_stream.download(path)
#             progress_label.config(text='Download complete')
#             filename = video_stream.default_filename
#             listbox_downloads.insert(0, filename)
#             play_button.config(state='normal')
#         except:
#             progress_label.config(text='Failed to download video')

# # Create downloads label and listbox
# downloads_label = Label(frame_right, text='Downloads', font=('Arial', 18), bg='white')
# downloads_label.pack(pady=10)

# listbox_downloads = Listbox(frame_right, font=('Arial', 12), height=15, width=40)
# listbox_downloads.pack()

# # Create play button
# # Create a function to play the selected item
# def play():
#     selected = listbox_downloads.curselection()
#     if selected:
#         filename = listbox_downloads.get(selected)
#         path = os.path.join(download_folder, filename)
#         if path.endswith('.mp3') or path.endswith('.wav'):
#             try:
#                 audio = AudioSegment.from_file(path)
#                 play_obj = audio.export(format='wav')
#                 pygame.mixer.music.load(play_obj)
#                 pygame.mixer.music.play()
#             except:
#                 messagebox.showerror('Error', 'Failed to play audio')
#         elif path.endswith('.mp4') or path.endswith('.avi') or path.endswith('.mov'):
#             try:
#                 video = VideoFileClip(path)
#                 video.preview()
#             except:
#                 messagebox.showerror('Error', 'Failed to play video')
#         else:
#             messagebox.showerror('Error', 'Unknown file type')

# # Create audio and video playback functions
# def play_audio():
#     selected = listbox_downloads.curselection()
#     if selected:
#         filename = listbox_downloads.get(selected)
#         path = os.path.join(download_folder, filename)
#         try:
#             audio = AudioFileClip(path)
#             audio.preview()
#         except:
#             messagebox.showerror('Error', 'Failed to play audio')

# def play_video():
#     selected = listbox_downloads.curselection()
#     if selected:
#         filename = listbox_downloads.get(selected)
#         path = os.path.join(download_folder, filename)
#         try:
#             video = VideoFileClip(path)
#             video.preview()
#         except:
#             messagebox.showerror('Error', 'Failed to play video')

# play_button = Button(frame_right, text='Play', font=('Arial', 16), bg='#eeeeee', state='disabled', command=play_video)
# play_button.pack(pady=10)

# # Create audio button
# audio_button = Button(frame_right, text='Play Audio', font=('Arial', 16), bg='#eeeeee', state='disabled', command=play_audio)
# audio_button.pack(pady=10)

# # Create download folder
# download_folder = os.path.join(os.path.expanduser("~"), "Downloads", "YouTube Downloads")
# if not os.path.exists(download_folder):
#     os.makedirs(download_folder)

# # Populate downloads listbox with previously downloaded files
# for file in os.listdir(download_folder):
#     if file.endswith('.mp4') or file.endswith('.webm'):
#         listbox_downloads.insert(0, file)

# # Set up scrollbar for downloads listbox
# scrollbar = Scrollbar(frame_right, orient=VERTICAL)
# scrollbar.pack(side=RIGHT, fill=Y)

# listbox_downloads.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox_downloads.yview)

# # Add history button
# def show_history():
#     messagebox.showinfo('Search History', '\n'.join(history))

# history_button = Button(frame_top, text='History', font=('Arial', 16), bg='#eeeeee', command=show_history)
# history_button.pack(side=LEFT, padx=10)

# # Run GUI
# root.mainloop()






from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import *
import os

# Create root window
root = Tk()
root.title('YouTube Downloader')
root.geometry('800x600')
root.resizable(False, False)

# Create frames
frame_top = Frame(root)
frame_top.pack(side=TOP, pady=20)

frame_left = Frame(root)
frame_left.pack(side=LEFT, padx=20)

frame_right = Frame(root)
frame_right.pack(side=RIGHT, padx=20)

# Create entry field for YouTube URL
url_label = Label(frame_top, text='Enter YouTube URL:', font=('Arial', 16))
url_label.pack(side=LEFT)

url_entry = Entry(frame_top, width=40, font=('Arial', 16))
url_entry.pack(side=LEFT)

# Create history listbox
history_label = Label(frame_left, text='Search History:', font=('Arial', 16))
history_label.pack()

listbox_history = Listbox(frame_left, width=40, font=('Arial', 16))
listbox_history.pack(pady=10)

# Create downloads listbox
downloads_label = Label(frame_right, text='Downloads:', font=('Arial', 16))
downloads_label.pack()

listbox_downloads = Listbox(frame_right, width=40, font=('Arial', 16))
listbox_downloads.pack(pady=10)

# Create download button
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror('Error', 'Please enter a valid URL')
        return

    try:
        yt = YouTube(url)
    except:
        messagebox.showerror('Error', 'Failed to download video')

    video = yt.streams.get_highest_resolution()
    filename = video.default_filename
    download_path = os.path.join(download_folder, filename)

    if os.path.exists(download_path):
        messagebox.showinfo('Download', f'{filename} already exists')
    else:
        video.download(download_folder)
        listbox_downloads.insert(0, filename)

    listbox_history.insert(0, url)

download_button = Button(frame_top, text='Download', font=('Arial', 16), bg='#eeeeee', command=download_video)
download_button.pack(side=LEFT, padx=10)

# Create audio and video playback functions
def play_audio():
    selected = listbox_downloads.curselection()
    if selected:
        filename = listbox_downloads.get(selected)
        path = os.path.join(download_folder, filename)
        try:
            audio = AudioFileClip(path)
            audio.preview()
        except:
            messagebox.showerror('Error', 'Failed to play audio')

def play_video():
    selected = listbox_downloads.curselection()
    if selected:
        filename = listbox_downloads.get(selected)
        path = os.path.join(download_folder, filename)
        try:
            video = VideoFileClip(path)
            video.preview()
        except:
            messagebox.showerror('Error', 'Failed to play video')

play_button = Button(frame_right, text='Play', font=('Arial', 16), bg='#eeeeee', state='disabled', command=play_video)
play_button.pack(pady=10)

# Create audio button
audio_button = Button(frame_right, text='Play Audio', font=('Arial', 16), bg='#eeeeee', state='disabled', command=play_audio)
audio_button.pack(pady=10)

# # Create audio playback function
# def play_audio():
#     selected = listbox_downloads.curselection()
#     if selected:
#         filename = listbox_downloads.get(selected)
#         path = os.path.join(download_folder, filename)
       

# Create audio and video playback functions
def play_audio():
    selected = listbox_downloads.curselection()
    if selected:
        filename = listbox_downloads.get(selected)
        path = os.path.join(download_folder, filename)
        try:
            audio = AudioFileClip(path)
            audio.preview()
        except:
            messagebox.showerror('Error', 'Failed to play audio')

def play_video():
    selected = listbox_downloads.curselection()
    if selected:
        filename = listbox_downloads.get(selected)
        path = os.path.join(download_folder, filename)
        try:
            video = VideoFileClip(path)
            video.preview()
        except:
            messagebox.showerror('Error', 'Failed to play video')

# Update download button function to enable play button
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror('Error', 'Please enter a valid URL')
    else:

        try:
            yt = YouTube(url)
        except:
            messagebox.showerror('Error', 'Failed to download video')

        video = yt.streams.get_highest_resolution()
        filename = video.default_filename
        download_path = os.path.join(download_folder, filename)

        if os.path.exists(download_path):
            messagebox.showinfo('Download', f'{filename} already exists')
        else:
            video.download(download_folder)
            listbox_downloads.insert(0, filename)
            play_button.config(state='normal')
            audio_button.config(state='normal')

        listbox_history.insert(0, url)

# Update delete button function to remove item from downloads listbox and delete file
def delete_item():
    selected = listbox_downloads.curselection()
    if selected:
        filename = listbox_downloads.get(selected)
        path = os.path.join(download_folder, filename)
        os.remove(path)
        listbox_downloads.delete(selected)

# Create delete button
delete_button = Button(frame_right, text='Delete', font=('Arial', 16), bg='#eeeeee', state='disabled', command=delete_item)
delete_button.pack(pady=10)

# Create function to update delete button state based on selection
def update_delete_button_state(event):
    if listbox_downloads.curselection():
        delete_button.config(state='normal')
    else:
        delete_button.config(state='disabled')

# Bind selection event to listbox_downloads
listbox_downloads.bind('<<ListboxSelect>>', update_delete_button_state)

# Set download folder
download_folder = 'D:\\vs_code\\youtube download vedio'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Main loop
root.mainloop()
