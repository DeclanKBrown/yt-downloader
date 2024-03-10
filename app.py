from tkinter.ttk import Combobox
from customtkinter import *

def download():
    print('Downloading...')

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

field = CTkEntry(frame, width=400, height=40, font=('Arial', 16))
field.pack(pady=('10p', '5p'))

button = CTkButton(frame, text='Download', font=('Arial', 16), command=download)
button.pack(pady=('10p', '5p'))

resolutions = ['1080p', '720p', '480p', '360p', '240p', '144p']
resolution_selected = StringVar()
resolution_dropdown = Combobox(frame, values=resolutions, textvariable=resolution_selected)
resolution_dropdown.pack(pady=('10p', '5p'))
resolution_dropdown.set('1080p')

progress_label = CTkLabel(frame, text='0%', font=('Arial', 16))
progress_label.pack(pady=('10p', '5p'))

progress_bar = CTkProgressBar(frame, width=400)
progress_bar.set(0)
progress_bar.pack(pady=('10p', '5p'))

status_label = CTkLabel(frame, text='Downloaded', font=('Arial', 16))
status_label.pack(pady=('10p', '5p'))

app.mainloop()