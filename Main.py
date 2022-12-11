from tkinter import *
from TitleScreen import TitleScreen as ts
from GameScreen import GameScreen as gs

import pygame

class MainFrame(Tk):
    def __init__(self, *args, **kwargs):
        # init method of the tk class
        Tk.__init__(self, *args, **kwargs)
        pygame.mixer.init()

        # creating a container for all
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # creating a dictionary for page objects
        self.frames = {}
        
        for screens in {ts.TitleScreen, gs.GameScreen}:
            page_name = screens.__name__
            frame = screens(container, self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[page_name] = frame

        self.show_frame("TitleScreen")

    def show_frame(self, page_name, id=None):
        self.id = id
        frame = self.frames[page_name]
        
        frame.tkraise()


window = MainFrame()

screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

x = (screenwidth/2) - 640/2
y = (screenheight/2) - 480/2

window.geometry('640x480+%d+%d' % (x, y))
window.title("Crack The Code")
icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)

window.resizable(0, 0)
window.mainloop()