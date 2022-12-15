from tkinter import *
from pathlib import Path
from PIL import Image, ImageTk
import random
from GameScreen import GameScreen as gs

class DifficultyScreen(Frame):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        canvas = Canvas(self, bg="#000000", height=600, width=800, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # self.btnNormal = Button(self, borderwidth=0, highlightthickness=0,)
        # self.normal = Image.open('DifficultyScreen\\assets\\normal.png')
        # self.button_img = ImageTk.PhotoImage(self.normal)
        # self.btnNormal.config(image=self.button_img)
        # self.btnNormal.pack()

        # self.btnNormal = canvas.create_image(320, 170, image=self.normal)
        # canvas.tag_bind(self.btnNormal, "<Button-1>", controller.show_frame("GameScreen"))

        self.bg = PhotoImage(file="DifficultyScreen\\assets\\bg.png")
        canvas.create_image(0, 0, anchor="nw", image=self.bg)

        self.imgBtnNormal = PhotoImage(file="DifficultyScreen\\assets\\normal.png")
        btnNormal = Button(self, image=self.imgBtnNormal, borderwidth=0, highlightthickness=0, command=lambda: controller.show_frame("GameScreen", 0), relief="flat")
        btnNormal.place(x=194.0, y=430.0)

        self.imgBtnHard = PhotoImage(file="DifficultyScreen\\assets\\hard.png")
        btnHard = Button(self, image=self.imgBtnHard, borderwidth=0, highlightthickness=0, command=lambda: controller.show_frame("GameScreen", 1), relief="flat")
        btnHard.place(x=451.0, y=430.0)

    
