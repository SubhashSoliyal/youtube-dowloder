# import os
# import tkinter as tk
# from tkinter import filedialog

# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.select_file_button = tk.Button(self)
#         self.select_file_button["text"] = "Select File"
#         self.select_file_button["command"] = self.select_file
#         self.select_file_button.pack(side="top")

#         self.play_button = tk.Button(self)
#         self.play_button["text"] = "Play"
#         self.play_button["state"] = "disabled"
#         self.play_button["command"] = self.play_file
#         self.play_button.pack(side="top")

#         self.quit_button = tk.Button(self, text="Quit", fg="red",
#                                      command=self.master.destroy)
#         self.quit_button.pack(side="bottom")

#     def select_file(self):
#         self.file_path = filedialog.askopenfilename()
#         if self.file_path:
#             self.play_button["state"] = "normal"

#     def play_file(self):
#         if os.path.exists(self.file_path):
#             os.startfile(self.file_path)
#         else:
#             tk.messagebox.showerror("File Not Found", "The selected file could not be found.")

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()




import os
import tkinter as tk
from tkinter import filedialog
import vlc  # pip install python-vlc

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        self.player = None
        self.media = None

    def create_widgets(self):
        self.select_file_button = tk.Button(self)
        self.select_file_button["text"] = "Select File"
        self.select_file_button["command"] = self.select_file
        self.select_file_button.pack(side="top")

        self.play_button = tk.Button(self)
        self.play_button["text"] = "Play"
        self.play_button["state"] = "disabled"
        self.play_button["command"] = self.play_file
        self.play_button.pack(side="top")

        self.quit_button = tk.Button(self, text="Quit", fg="red",
                                     command=self.master.destroy)
        self.quit_button.pack(side="bottom")

        self.video_frame = tk.Frame(self)
        self.video_frame.pack(side="top")

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.play_button["state"] = "normal"
            self.create_player()

    def create_player(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.media = self.instance.media_new(self.file_path)

        self.player.set_media(self.media)
        self.player.set_hwnd(self.video_frame.winfo_id())

    def play_file(self):
        if self.player is None:
            self.create_player()

        self.player.play()

root = tk.Tk()
app = Application(master=root)
app.mainloop()

