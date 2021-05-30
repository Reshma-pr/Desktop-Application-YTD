import tkinter as tk
import tkinter.font
from tkinter import *
import requests
from pytube import YouTube

root = tk.Tk()
root.geometry("500x250")
root.title("Youtube Video Downloader")
root.configure(bg="silver")
urlY = StringVar()


def ytd():
    url = urlY.get()
    getVideo = YouTube(url)
    print(getVideo.views)
    videoStream=getVideo.streams.first()
    videoStream.download()
    root.configure(bg="black")
    button.place_forget()
    l = Label(root, text="Video Downloaded Sucessfully!!!", bg="black", fg="white",width=30,font=tkinter.font.Font(family='Helvetica',size=18)).place(x=100, y=100)


label = tk.Label(root, text="Paste Video URL :", bg="gray", fg="white")
label.place(x=10, y=20)
eurl = tk.Entry(root, textvariable=urlY, width=40)
eurl.place(x=90, y=50)
button = tk.Button(root, text="DOWNLOAD", command=ytd, highlightbackground="black", width=24)
button.place(x=120, y=100)
root.mainloop()
