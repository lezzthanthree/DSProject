from tkinter import *
from pathlib import Path
from PIL import ImageTk, Image
import pygame

class TitleScreen(Frame):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        pygame.mixer.music.load("TitleScreen\\assets\\mus.ogg")
        pygame.mixer.music.play(loops=-1)

        canvas = Canvas(self, bg="#000000", height=480, width=640, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        self.title = PhotoImage(file="TitleScreen\\assets\\title.png")
        canvas.create_image(320.0, 150.0, image=self.title)

        self.imgBtnStart = PhotoImage(file="TitleScreen\\assets\\start.png")
        btnStart = Button(self, image=self.imgBtnStart, borderwidth=0, highlightthickness=0, command=lambda: self.changeFrame(controller), relief="flat")
        btnStart.place(x=190.0, y=300.0)

        # btnChange = Button(self, text="Change", command=lambda: controller.show_frame("GameScreen"), relief="flat")
        # btnChange.place(x=200.0, y=100.0, width=100.0, height=45.0)

    def changeFrame(self, controller):
        pygame.mixer.music.load("TitleScreen\\assets\\mus2.ogg")
        pygame.mixer.music.play(loops=-1)
        controller.show_frame("DifficultyScreen")
        return
