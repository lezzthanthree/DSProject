from tkinter import *
from pathlib import Path
from PIL import Image, ImageTk
from GameScreen import GameScreen as gs
import pygame
from idlelib.tooltip import Hovertip

class DifficultyScreen(Frame):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # Create a canvas for this screen
        canvas = Canvas(self, bg="#000000", height=600, width=800, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)
        
        # Place a background
        self.bg = PhotoImage(file="DifficultyScreen\\assets\\bg.png")
        canvas.create_image(0, 0, anchor="nw", image=self.bg)

        # Create a Normal Difficulty Button
        self.imgBtnNormal = PhotoImage(file="DifficultyScreen\\assets\\normal.png")
        btnNormal = Button(self, image=self.imgBtnNormal, borderwidth=0, highlightthickness=0, command=lambda: self.normal(controller), relief="flat")
        btnNormal.place(x=194.0, y=430.0)
        self.myTip = Hovertip(btnNormal,'Includes only the numbers.')

        # Create a Difficult Difficulty Button
        self.imgBtnHard = PhotoImage(file="DifficultyScreen\\assets\\hard.png")
        btnHard = Button(self, image=self.imgBtnHard, borderwidth=0, highlightthickness=0, command=lambda: self.difficult(controller), relief="flat")
        btnHard.place(x=451.0, y=430.0)
        self.myTip = Hovertip(btnHard,'Feeling challenged?\nThis includes hexadecimal characters!')
    
    # A change frame function for the normal difficulty
    def normal(self, controller):
        pygame.mixer.music.load("DifficultyScreen\\assets\\mus.mp3")
        pygame.mixer.music.play(loops=-1)
        controller.show_frame("GameScreen", 0)
        return

    # A change frame function for the difficult difficulty
    def difficult(self, controller):
        pygame.mixer.music.load("DifficultyScreen\\assets\\mus.mp3")
        pygame.mixer.music.play(loops=-1)
        controller.show_frame("GameScreen", 1)
        return

    
