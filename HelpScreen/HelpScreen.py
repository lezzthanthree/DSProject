from tkinter import *
from pathlib import Path

class HelpScreen(Frame):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        canvas = Canvas(self, bg="#000000", height=480, width=640, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        self.instructions = PhotoImage(file="HelpScreen\\assets\\instructions.png")
        canvas.create_image(0, 0, anchor="nw", image=self.instructions)

        self.imgBtnBack = PhotoImage(file="HelpScreen\\assets\\back.png")
        btnBack = Button(self, image=self.imgBtnBack, borderwidth=0, highlightthickness=0, command=lambda: controller.show_frame("GameScreen"), relief="flat")
        btnBack.place(x=15.0, y=440.0)

        