from tkinter import *
from pathlib import Path
import random

class GameScreen(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        canvas = Canvas(self, bg="#000000", height=480, width=640, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)
        
        # self.bg = PhotoImage(file=self.relative_to_assets("test.png"))
        # canvas.create_image(0, 0, anchor="nw", image=self.bg)

        # self.amesprite = self.resizeImage(self.relative_to_assets("ame2.png"))
        # canvas.create_image(0, 0, anchor="nw", image=self.amesprite)

        self.random = Label()

        self.response = Label(canvas, text=self.random["text"])
        self.response.place(x=10, y=10)

        self.valid1 = StringVar()
        self.digit1 = Entry(self, font=("Determination Mono", 90), justify='center', textvariable=self.valid1)
        self.digit1.place(x=53.0, y=125.0, width=115.0, height=115.0)
        self.valid1.trace("w", lambda *args: self.characterCheck(self.valid1, 1))

        self.valid2 = StringVar()
        self.digit2 = Entry(self, font=("Determination Mono", 90), justify='center', textvariable=self.valid2)
        self.digit2.place(x=193.0, y=125.0, width=115.0, height=115.0)
        self.valid2.trace("w", lambda *args: self.characterCheck(self.valid2, 2))

        self.valid3 = StringVar()
        self.digit3 = Entry(self, font=("Determination Mono", 90), justify='center', textvariable=self.valid3)
        self.digit3.place(x=333.0, y=125.0, width=115.0, height=115.0)
        self.valid3.trace("w", lambda *args: self.characterCheck(self.valid3, 3))

        self.valid4 = StringVar()
        self.digit4 = Entry(self, font=("Determination Mono", 90), justify='center', textvariable=self.valid4)
        self.digit4.place(x=473.0, y=125.0, width=115.0, height=115.0)
        self.valid4.trace("w", lambda *args: self.characterCheck(self.valid4, 4))

        self.imgBtnValidate = PhotoImage(file=self.relative_to_assets("crack.png"))
        self.btnValidate = Button(self, image=self.imgBtnValidate, borderwidth=0, highlightthickness=0, command=lambda: self.validate(), relief="flat")
        self.btnValidate.place(x=190.0, y=300.0)

        self.imgBtnRandom = PhotoImage(file=self.relative_to_assets("button.png"))
        btnRandom = Button(self, image=self.imgBtnRandom, command=lambda: self.createNewRandom(), relief="flat")
        btnRandom.place(x=190.0, y=400.0, width=100.0, height=45.0)
        return
    
    def createNewRandom(self):
        x = random.randint(0, 9999)
        stringnumber = ""
        if x >= 0 and x <= 9:
            stringnumber = "000" + str(x)
        elif x >= 10 and x <= 99:
            stringnumber = "00" + str(x)
        elif x >= 100 and x <= 999:
            stringnumber = "0" + str(x)
        else:
            stringnumber = str(x)

        self.random["text"] = stringnumber
        self.response["text"] = self.random["text"]
        return

    def validate(self):
        digit1 = self.digit1.get()
        digit2 = self.digit2.get()
        digit3 = self.digit3.get()
        digit4 = self.digit4.get()

        self.digit1["bg"] = "white"
        self.digit2["bg"] = "white"
        self.digit3["bg"] = "white"
        self.digit4["bg"] = "white"

        if digit1 in self.random["text"]:
            self.digit1["bg"] = "yellow"
        if digit2 in self.random["text"]:
            self.digit2["bg"] = "yellow"
        if digit3 in self.random["text"]:
            self.digit3["bg"] = "yellow"
        if digit4 in self.random["text"]:
            self.digit4["bg"] = "yellow"
        
            
        if digit1 == self.random["text"][0]:
            self.digit1["bg"] = "green"
        if digit2 == self.random["text"][1]:
            self.digit2["bg"] = "green"
        if digit3 == self.random["text"][2]:
            self.digit3["bg"] = "green"
        if digit4 == self.random["text"][3]:
            self.digit4["bg"] = "green"

        self.clearText()
        self.digit1.focus()

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def characterCheck(self, entry_text, controller):
        if not entry_text.get().isnumeric():
            entry_text.set("")
            self.response["text"] = "Not a number!"
            return
        if len(entry_text.get()) > 1:
            entry_text.set(entry_text.get()[-1])

        boxes = [self.digit1, self.digit2, self.digit3, self.digit4, self.btnValidate]
        boxes[controller].focus()
        boxes[controller]
    
    def clearText(self):
        self.digit1.delete(0, END)
        self.digit2.delete(0, END)
        self.digit3.delete(0, END)
        self.digit4.delete(0, END)

    # def resizeImage(self, img):
    #     image = Image.open(img)
    #     image = image.resize((640, 417), Image.ANTIALIAS)
    #     resized = ImageTk.PhotoImage(image)
    #     return resized