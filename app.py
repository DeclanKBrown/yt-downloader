from tkinter.ttk import Combobox
from customtkinter import *
from pytube import YouTube
import os

def download():
    url = url_field.get()
    resolution = resolution_selected.get()

    progress_label.pack(pady=('10p', '5p'))
    progress_bar.pack(pady=('10p', '5p'))
    status_label.pack(pady=('10p', '5p'))

    try:
        status_label.configure(text='Downloading')
        progress_bar.set(0)

        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolution).first()

        downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads', f'{yt.title}.mp4')
        stream.download(output_path=downloads_folder)

        status_label.configure(text='Downloaded', text_color='green')
    except Exception as e:
        status_label.configure(text=f'Error {str(e)}', text_color='red')
        progress_label.pack_forget()
        progress_bar.pack_forget()

def on_progress(stream, chunks, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    
    progress_label.configure(text= str(int(percentage)) + '%')
    progress_label.update()
    
    progress_bar.set(float(percentage / 100))



# Create Root Window
app = CTk()
set_default_color_theme('blue')

# Title of Window
app.title('Youtube Downloader')

# Set Size of Window
app.geometry('720x480')
app.minsize(720, 480)
app.maxsize(1080, 720)

# Create The Frame
frame = CTkFrame(app)
frame.pack(fill='both', expand=True, padx=10, pady=10)

# Create Components
label = CTkLabel(frame, text='Enter Url Here: ', font=('Arial', 24))
label.pack(pady=('10p', '5p'))

url_field = CTkEntry(frame, width=400, height=40, font=('Arial', 16))
url_field.pack(pady=('10p', '5p'))

button = CTkButton(frame, text='Download', font=('Arial', 16), command=download)
button.pack(pady=('10p', '5p'))

resolutions = ['1080p', '720p', '480p', '360p', '240p', '144p']
resolution_selected = StringVar()
resolution_dropdown = Combobox(frame, values=resolutions, textvariable=resolution_selected)
resolution_dropdown.pack(pady=('10p', '5p'))
resolution_dropdown.set('1080p')


progress_label = CTkLabel(frame, text='0%', font=('Arial', 16))

progress_bar = CTkProgressBar(frame, width=400)
progress_bar.set(0)

status_label = CTkLabel(frame, text='Downloaded', font=('Arial', 16))

app.mainloop()