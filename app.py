import tkinter as tk
import yt_dlp

# Define options
ydl_opts = {
    'format': 'best',           # Choose the best quality
    'outtmpl': '%(title)s.%(ext)s',  # Output filename template
}

def download_video(video_url):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
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

# Video URL Input
video_url_lbl = tk.Label(root, text='Video URL:')
video_url_lbl.pack()
video_url_txt_inp = tk.Entry(root, width=42)  # TODO: Implement shortcuts.
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


# Use the API



print("done")