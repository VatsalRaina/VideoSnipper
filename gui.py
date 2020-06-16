from backend import make_snips
import tkinter
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog
from tkinter import scrolledtext

# Create the root window
window = Tk()

# Set window title
window.title('Video Snipper')

# Set window size
window.geometry("700x600")

# Global variables
bobname=''
noChange = True

def browseFiles():
    global bobname
    global noChange
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                         "*.mov*"),
                                                        ("all files", 
                                                         "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Selected: "+filename)
    bobname = filename
    noChange = False


# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "Video Snipper",
                            width = 100, height = 4,
                            fg = "blue")
label_file_explorer.grid(column = 1, row = 1)


button_explore = Button(window,
                        text = "Select video",
                        font=("Arial Bold", 14),
                        bg = "lightblue",
                        command = browseFiles)
button_explore.grid(column = 1, row = 2)


lab_len = tkinter.Label(window, text = "Length of each clip (in seconds):", font=("Arial Bold", 16))
lab_len.grid(column=1, row=3)
clipLen = tkinter.Entry(window, width=15)
clipLen.grid(column=1, row=4)

lab_times = tkinter.Label(window, text = "Start times:", font=("Arial Bold", 16))
lab_times.grid(column=1, row=5)
txt = scrolledtext.ScrolledText(window, width=60,height=10)
txt.grid(column=1, row=6)
toPrint = "00:21.98 02:05.88"
txt.insert("1.0", toPrint)
# v = StringVar(window, value='00:21.98 02:05.88')
# times = tkinter.Entry(window, textvariable=v)
# times.grid(column=1, row=6, ipadx=30, ipady=30)

def genFiles():
    if noChange:
        label_file_explorer.configure(text="Please select a file first!")
    else:
        # Save at same location as 'filename'
        label_file_explorer.configure(text="File saved in current directory!")
        make_snips(bobname, txt.get("1.0", END),  clipLen.get())
        print(bobname)
        print(txt.get("1.0", END))

button_generate = Button(window,
                        text = "Generate clips",
                        font=("Arial Bold", 14),
                        bg = "lightgreen",
                        command = genFiles)
button_generate.grid(column=1, row=7)

# Let the window wait for any events
window.mainloop()
