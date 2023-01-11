from tkinter import *
from pathlib import Path
from PIL import ImageTk, Image
import pygame

class TitleScreen(Frame):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        # Play Music in a loop
        pygame.mixer.music.load("TitleScreen\\assets\\mus.mp3")
        pygame.mixer.music.play(loops=-1)

        # Create a canvas for this screen
        canvas = Canvas(self, bg="#000000", height=600, width=800, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # Place a background
        self.bg = PhotoImage(file="TitleScreen\\assets\\bg.png")
        canvas.create_image(0, 0, anchor="nw", image=self.bg)

        # Create a start button
        self.imgBtnStart = PhotoImage(file="TitleScreen\\assets\\startbutton.png")
        btnStart = Button(self, image=self.imgBtnStart, borderwidth=0, highlightthickness=0, command=lambda: self.changeFrame(controller), relief="flat")
        btnStart.place(x=245.0, y=222.0)

    # A fuuntion to change the frame to the difficulty screen
    def changeFrame(self, controller):
        controller.show_frame("DifficultyScreen")
        return
