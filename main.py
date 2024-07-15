import base64
import tempfile
import zlib
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk

from downloadtheimage import download_the_image


def enter_path():
    global path
    path = fd.askdirectory()
    pathing.replace("1.0", "2.0", path)
    return path


def download_btn():
    global url_link
    download_the_image(url_link.get().split(), path)


path = ""
root = Tk()
url_link = StringVar(value="")
root.title("COOMER.SU IMAGE DOWNLOADER")
root.geometry("310x200+800+400")
root.minsize(width=270, height=200)
# Icon
ICON = zlib.decompress(base64.b64decode("eJxjYGAEQgEBBiDJwZDBysAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="))
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, "wb") as icon_file:
    icon_file.write(ICON)

instruction1 = ttk.Label(text="Instruction: ", font=("Helvetica", 11, "bold"))
instruction1.pack()
instruction2 = ttk.Label(
    text="1. Enter the url of the post in the first field\n2. Choose the directory and press the \"Download\" button")
instruction2.pack()

url_entry = ttk.Entry(width="43", textvariable=url_link, foreground="red")
url_entry.place(x=10, y=72)

pathing = Text(height="1", width="23", wrap="none")
pathing.place(x=10, y=102)

path_button = ttk.Button(text="Browse", command=enter_path)
path_button.place(x=200, y=100)

dwn_button = ttk.Button(text="Download", command=download_btn)
dwn_button.place(x=100, y=140)

scrollbar = ttk.Scrollbar(orient="horizontal", command=pathing.xview)
scrollbar.place(width=200, x=2, y=120)

root.iconbitmap(default=ICON_PATH)
root.update_idletasks()
root.mainloop()
