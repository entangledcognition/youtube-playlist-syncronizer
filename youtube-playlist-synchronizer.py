from PIL import Image, ImageTk
from tkinter import Tk, Text, BOTH, W, N, E, S,filedialog,messagebox
from tkinter.ttk import Frame, Button, Label, Style, Progressbar
from youtube_login import loginToGoogle
from utils import createFolderForPlaylist

class YoutubeFrame(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.master.title("Youtube Synchronizer")
        self.pack(fill=BOTH, expand=True)

        # self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=1)

        lbl = Label(self, text="Welcome to Youtube playlist Synchronizer")
        lbl.grid(sticky=W, pady=4, padx=5)
        
        bar = Progressbar(self, length=200, style='black.Horizontal.TProgressbar')
        
        # img = Image.open("icon.png")
        # img = img.resize((300, 300), Image.ANTIALIAS)
        # ytpl = ImageTk.PhotoImage(img)
        # area = Label(self, image=ytpl)
        # area.image = ytpl
        self.logArea = Text(self,state="disabled")
        self.logArea.grid(row=1, column=0, columnspan=3, rowspan=4,
                  padx=5, sticky=E+W+S+N)
        
        self.appendLog(self.logArea,"Steps to follow \n")
        self.appendLog(self.logArea,"1) Select root directory \n ")
        self.appendLog(self.logArea,"2) Give permission for google to get playlist automatically \n")
        self.appendLog(self.logArea,"3) start syncing into your selected folder\n")
        cbtn = Button(self, text="Choose Directory", command=lambda: self.chooseRootDirectory(cbtn))
        cbtn.grid(row=5, column=0, pady=2)

        hbtn = Button(self, text="Google Permission", command=lambda: self.clicked(hbtn))
        hbtn.grid(row=5, column=1, padx=2)

        obtn = Button(self, text="Start Sync", command=self.startSyncing)
        obtn.grid(row=5, column=3)

    def clicked(self,event):
        googlePermissionUrl = loginToGoogle()
        event.grid_forget()
        label = Label(self, text="Google Permissions Granted")
        label.grid(row=5, column=1, pady=2)
        self.appendLog(self.logArea,"Thanks for granting Google Permission")
        

    def chooseRootDirectory(self,event):
        self.rootDirectory = filedialog.askdirectory()
        event.grid_forget()
        label = Label(self, text=self.rootDirectory)
        label.grid(row=5, column=0, pady=2)
        self.appendLog(self.logArea,"You have selected "+  self.rootDirectory +" as your root directory")
        
    def appendLog(self, textBox,text):
        textBox.configure(state='normal')
        textBox.insert('end', text+'\n')
        textBox.configure(state='disabled')
        

    def startSyncing(self):
        self.response = messagebox.askquestion("Confirmation", "you have selected: " + self.rootDirectory +
                                               " as root Directory and youtube playlist will be added as sub folders inside " + self.rootDirectory + "/, are you sure?")
        if self.response == 'yes':
            createFolderForPlaylist(self.rootDirectory)
        else:
            print("You are concious")


def main():
    root = Tk()
    app = YoutubeFrame()
    root.mainloop()


if __name__ == '__main__':
    main()
