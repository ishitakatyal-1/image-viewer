# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:41:34 2019

@author: Ishita
"""

from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

mainframe1 = tk.Tk()
mainframe1.title("Image Viewer")
#root.iconbitmap("icon.ico")

img = ImageTk.PhotoImage(Image.open("C:\\Users\\Ishita\\Pictures\\Saved Pictures\\1.jpeg"))

label_img = tk.Label(image = img)
button_quit = tk.Button(mainframe1, text="Quit", command=mainframe1.destroy)

label_img.grid(row=0, column=0, sticky=tk.W, pady=4)
button_quit.grid(row=1, column=0, sticky=tk.W, pady=4)

mainframe1.mainloop()