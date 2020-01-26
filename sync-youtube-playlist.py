
import sys
import os
import platform

  
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from youtube_login import loginToGoogle
from utils import createFolderForPlaylist


# Platforms
WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")
MAC = (platform.system() == "Darwin")

window = Tk()


window.title("Youtube Playlist Synchronizer")

lbl = Label(window, text="Welcome to Youtube Playlist Synchronizer", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)


def clicked():
    googlePermissionUrl = loginToGoogle()

def startSyncing():
    window.directory = filedialog.askdirectory()
    response = messagebox.askquestion("Confirmation","you have selected: "+ window.directory +" as root Directory and youtube playlist will be added as sub folders inside "+ window.directory +"/, Sre you sure ")
    if response == 1:
        createFolderForPlaylist(window.directory)
    else:
        print ("You are concious")
    print (window.directory)

btn = Button(window, text="Google Login to sync playlist from ", bg="#06c", fg="white", command=clicked)
btn.grid( row=2,columnspan = 1)
btn = Button(window, text="Start Syncing", bg="#06c", fg="white", command=startSyncing)
btn.grid( row=3)


window.mainloop()


