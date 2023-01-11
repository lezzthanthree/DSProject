from tkinter import *
from pathlib import Path

class HelpScreen(Frame):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # Create a canvas for this screen
        canvas = Canvas(self, bg="#000000", height=600, width=800, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # Show the instructions
        self.instructions = PhotoImage(file="HelpScreen\\assets\\instructions.png")
        canvas.create_image(0, 0, anchor="nw", image=self.instructions)

        # Create a back button
        self.imgBtnBack = PhotoImage(file="HelpScreen\\assets\\back.png")
        btnBack = Button(self, image=self.imgBtnBack, borderwidth=0, highlightthickness=0, command=lambda: controller.show_frame("GameScreen"), relief="flat")
        btnBack.place(x=334.0, y=456.0)

        #