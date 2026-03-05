import tkinter as tk
import yt_dlp
from pathlib import Path

# Define options
downloads_path = Path.home() / "Downloads"
file_path = downloads_path.__str__() + '/%(title)s.%(ext)s'

print(file_path)

ydl_opts = {
    'format': 'best',           # Choose the best quality
    'outtmpl': file_path,  # Output filename template
}

def download_video(video_url):
    try:
        error_output_lbl.config(text="Downloading video")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        error_output_lbl.config(text="Video downloaded")
    except Exception as e:
        error_output_lbl.config(text=str(e))


def submit_click(video_url):
    error_output_lbl.config(text="")
    # if video_url == "":
    #     error_output_lbl.config(text="URL can't be empty")
    #     return
    download_video(video_url)

# frame = tk.Frame

class Root:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Tkinter YTDLPY')


root = tk.Tk()
root.title('Tkinter YTDLPY')

root.geometry('500x500')

# menubar = tk.Menu(root)
# filemenu = tk.Menu(menubar, tearoff=0)
# filemenu.add_command(label="Settings")
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)

# root.config(menu=menubar)

# Video URL Input
video_url_lbl = tk.Label(root, text='Video URL:')
video_url_lbl.pack()
video_url_txt_inp = tk.Entry(root, width=50)  # TODO: Implement shortcuts.
video_url_txt_inp.pack()

error_output_lbl = tk.Label(root, fg='red', wraplength=325)
error_output_lbl.pack()

submit_btn = tk.Button(
    root,
    text='Submit',
    command=lambda: download_video(video_url_txt_inp.get())
)
submit_btn.pack()

root.mainloop()
