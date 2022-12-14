from tkinter import *
from pathlib import Path
import random

class GameScreen(Frame):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        canvas = Canvas(self, bg="#000000", height=480, width=640, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        self.random = Label()

        self.characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.attempts = 0

        self.debug = Label(canvas, text=self.random["text"])
        self.debug.place(x=10, y=10)

        self.createNewRandom()
        
        self.response = Label(canvas, text="", fg="#FF0000", bg="#000000", font=("Determination Mono", 28), justify='center')
        self.response.place(x=55, y=70)

        self.valid1 = StringVar()
        self.digit1 = Entry(self, font=("Determination Mono", 90), justify='center', textvariable=self.valid1)
        self.digit1.place(x=53.0, y=125.0, width=115.0, height=115.0)
        self.valid1.trace("w", lambda *args: self.characterCheck(self.valid1, 0))

        self.valid2 = StringVar()
        self.digit2 = Entry(self, font=("Determination Mono", 90), justify='center', textvariable=self.valid2)
        self.digit2.place(x=193.0, y=125.0, width=115.0, height=115.0)
        self.valid2.trace("w", lambda *args: self.characterCheck(self.valid2, 1))

        self.valid3 = StringVar()
        self.digit3 = Entry(self, font=("Determination Mono", 90), justify='center', textvariable=self.valid3)
        self.digit3.place(x=333.0, y=125.0, width=115.0, height=115.0)
        self.valid3.trace("w", lambda *args: self.characterCheck(self.valid3, 2))

        self.valid4 = StringVar()
        self.digit4 = Entry(self, font=("Determination Mono", 90), justify='center', textvariable=self.valid4)
        self.digit4.place(x=473.0, y=125.0, width=115.0, height=115.0)
        self.valid4.trace("w", lambda *args: self.characterCheck(self.valid4, 3))

        self.imgBtnValidate = PhotoImage(file="GameScreen\\assets\\crack.png")
        self.btnValidate = Button(self, image=self.imgBtnValidate, borderwidth=0, highlightthickness=0, command=lambda: self.validate(), relief="flat")
        self.btnValidate.place(x=190.0, y=300.0)

        self.imgBtnNew = PhotoImage(file="GameScreen\\assets\\new.png")
        btnNew = Button(self, image=self.imgBtnNew, borderwidth=0, highlightthickness=0, command=lambda: self.newGame(controller.id), relief="flat")
        btnNew.place(x=15.0, y=440.0)

        self.imgBtnHelp = PhotoImage(file="GameScreen\\assets\\help.png")
        btnHelp = Button(self, image=self.imgBtnHelp, borderwidth=0, highlightthickness=0, command=lambda: controller.show_frame("HelpScreen"), relief="flat")
        btnHelp.place(x=550.0, y=440.0)
        return
    
    def createNewRandom(self):
        stringnumber = list("    ")
        stringnumber[0] = self.characters[random.randint(0, len(self.characters)-1)]
        stringnumber[1] = self.characters[random.randint(0, len(self.characters)-1)]
        stringnumber[2] = self.characters[random.randint(0, len(self.characters)-1)]
        stringnumber[3] = self.characters[random.randint(0, len(self.characters)-1)]

        stringnumber = ''.join(stringnumber)
        
        self.random["text"] = stringnumber
        self.debug["text"] = self.random["text"]
        return

    def validate(self):
        digit1 = self.digit1.get().lower()
        digit2 = self.digit2.get().lower()
        digit3 = self.digit3.get().lower()
        digit4 = self.digit4.get().lower()

        self.digit1["bg"] = "red"
        self.digit2["bg"] = "red"
        self.digit3["bg"] = "red"
        self.digit4["bg"] = "red"

        if digit1 in self.random["text"] and not digit1 == "":
            self.digit1["bg"] = "yellow"
        if digit2 in self.random["text"] and not digit2 == "":
            self.digit2["bg"] = "yellow"
        if digit3 in self.random["text"] and not digit3 == "":
            self.digit3["bg"] = "yellow"
        if digit4 in self.random["text"] and not digit4 == "":
            self.digit4["bg"] = "yellow"
        
        correct = 0

        if digit1 == self.random["text"][0]:
            self.digit1["bg"] = "green"
            correct += 1
        if digit2 == self.random["text"][1]:
            self.digit2["bg"] = "green"
            correct += 1
        if digit3 == self.random["text"][2]:
            self.digit3["bg"] = "green"
            correct += 1
        if digit4 == self.random["text"][3]:
            self.digit4["bg"] = "green"
            correct += 1
        # lastinput = digit1 + ... + digit4
        # textboxlast = lastinput


        self.clearText()
        self.digit1.focus()
        # self.debug["text"] = self.random["text"] + " - " + digit1 + digit2 + digit3 + digit4

        self.response["text"] = ""
        self.attempts += 1

        if correct == 4 :
            self.response["text"] = "You cracked the code!"
            return
        if self.attempts >= 6:
            self.response["text"] = "You have failed."

    def characterCheck(self, entry_text, controller):
        boxes = [self.digit1, self.digit2, self.digit3, self.digit4, self.btnValidate]
        if not entry_text.get().lower() in self.characters:
            entry_text.set("")
            self.response["text"] = "Yo, that's not a number!"
            return
        if len(entry_text.get()) > 1:
            entry_text.set(entry_text.get()[-1])

        boxes[controller + 1].focus()
        self.response["text"] = ""

    def clearText(self):
        self.digit1.delete(0, END)
        self.digit2.delete(0, END)
        self.digit3.delete(0, END)
        self.digit4.delete(0, END)
    
    def clearColors(self):
        self.digit1["bg"] = "white"
        self.digit2["bg"] = "white"
        self.digit3["bg"] = "white"
        self.digit4["bg"] = "white"

    def newGame(self, controller):
        self.clearText()
        self.clearColors()
        self.createNewRandom()
        self.response["text"] = "New Number Initiated!"
        self.digit1.focus()
        self.attempts = 0

        if (controller == 0):
            self.characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        elif (controller == 1):
            self.characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']