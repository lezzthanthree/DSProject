from tkinter import *
from pathlib import Path
import random

class GameScreen(Frame):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        canvas = Canvas(self, bg="#000000", height=600, width=800, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        self.random = Label()
        print(self.random["text"])

        self.characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.attempts = 0

        self.bg = PhotoImage(file="GameScreen\\assets\\bg.png")
        canvas.create_image(0, 0, anchor="nw", image=self.bg)

        self.createNewRandom()
        
        self.response = Label(canvas, text="", fg="#FF0000", bg="#000000", font=("Determination Mono", 28), justify='center')
        self.response.place(x=55, y=500)

        # locks
        self.redlock = PhotoImage(file="GameScreen\\assets\\redlock.png")
        self.greenlock = PhotoImage(file="GameScreen\\assets\\greenlock.png")
        self.yellowlock = PhotoImage(file="GameScreen\\assets\\yellowlock.png")
        self.whitelock = PhotoImage(file="GameScreen\\assets\\whitelock.png")
        
        self.lock1 = Label(self, image=self.whitelock, borderwidth=0, highlightthickness=0)
        self.lock1.place(x=147.0, y=203.0)
        self.valid1 = StringVar()
        self.digit1 = Entry(self, font=("Determination Mono", 65), justify='center', textvariable=self.valid1, borderwidth=0, highlightthickness=0, bg="#707070")
        self.digit1.place(x=165.0, y=263.0, width=78.0, height=78.0)
        self.valid1.trace("w", lambda *args: self.characterCheck(self.valid1, 0))

        self.lock2 = Label(self, image=self.whitelock, borderwidth=0, highlightthickness=0)
        self.lock2.place(x=283.0, y=203.0)
        self.valid2 = StringVar()
        self.digit2 = Entry(self, font=("Determination Mono", 65), justify='center', textvariable=self.valid2, borderwidth=0, highlightthickness=0, bg="#707070")
        self.digit2.place(x=303.0, y=263.0, width=78.0, height=78.0)
        self.valid2.trace("w", lambda *args: self.characterCheck(self.valid2, 1))

        self.lock3 = Label(self, image=self.whitelock, borderwidth=0, highlightthickness=0)
        self.lock3.place(x=420.0, y=203.0)
        self.valid3 = StringVar()
        self.digit3 = Entry(self, font=("Determination Mono", 65), justify='center', textvariable=self.valid3, borderwidth=0, highlightthickness=0, bg="#707070")
        self.digit3.place(x=441.0, y=263.0, width=78.0, height=78.0)
        self.valid3.trace("w", lambda *args: self.characterCheck(self.valid3, 2))

        self.lock4 = Label(self, image=self.whitelock, borderwidth=0, highlightthickness=0)
        self.lock4.place(x=556.0, y=203.0)
        self.valid4 = StringVar()
        self.digit4 = Entry(self, font=("Determination Mono", 65), justify='center', textvariable=self.valid4, borderwidth=0, highlightthickness=0, bg="#707070")
        self.digit4.place(x=574.0, y=263.0, width=78.0, height=78.0)
        self.valid4.trace("w", lambda *args: self.characterCheck(self.valid4, 3))

        # attempt keys
        self.whitekey = PhotoImage(file="GameScreen\\assets\\whitekey.png")
        self.yellowkey = PhotoImage(file="GameScreen\\assets\\yellowkey.png")

        self.key1 = Label(self, image=self.whitekey, borderwidth=0, highlightthickness=0)
        self.key2 = Label(self, image=self.whitekey, borderwidth=0, highlightthickness=0)
        self.key3 = Label(self, image=self.whitekey, borderwidth=0, highlightthickness=0)
        self.key4 = Label(self, image=self.whitekey, borderwidth=0, highlightthickness=0)
        self.key5 = Label(self, image=self.whitekey, borderwidth=0, highlightthickness=0)
        self.key6 = Label(self, image=self.whitekey, borderwidth=0, highlightthickness=0)

        self.key1.place(x=302.0, y=380.0)
        self.key2.place(x=340.0, y=380.0)
        self.key3.place(x=378.0, y=380.0)
        self.key4.place(x=416.0, y=380.0)
        self.key5.place(x=454.0, y=380.0)
        self.key6.place(x=492.0, y=380.0)
        
        # history
        self.before = Label(canvas, text="", fg="#FFFFFF", bg="#171717", font=("Determination Mono", 34), justify='center')
        self.before.place(x=554, y=59)

        self.imgBtnValidate = PhotoImage(file="GameScreen\\assets\\crack.png")
        self.btnValidate = Button(self, image=self.imgBtnValidate, borderwidth=0, highlightthickness=0, command=lambda: self.validate(), relief="flat")
        self.btnValidate.place(x=334.0, y=460.0)

        self.imgBtnNew = PhotoImage(file="GameScreen\\assets\\new.png")
        btnNew = Button(self, image=self.imgBtnNew, borderwidth=0, highlightthickness=0, command=lambda: self.newGame(controller.id), relief="flat")
        btnNew.place(x=22.0, y=33.0)

        self.imgBtnHelp = PhotoImage(file="GameScreen\\assets\\help.png")
        btnHelp = Button(self, image=self.imgBtnHelp, borderwidth=0, highlightthickness=0, command=lambda: controller.show_frame("HelpScreen"), relief="flat")
        btnHelp.place(x=22.0, y=122.0)

        self.imgBtnHome = PhotoImage(file="GameScreen\\assets\\home.png")
        btnHome = Button(self, image=self.imgBtnHome, borderwidth=0, highlightthickness=0, command=lambda: controller.show_frame("TitleScreen"), relief="flat")
        btnHome.place(x=22.0, y=209.0)
    
    def createNewRandom(self):
        stringnumber = list("    ")
        stringnumber[0] = self.characters[random.randint(0, len(self.characters)-1)]
        stringnumber[1] = self.characters[random.randint(0, len(self.characters)-1)]
        stringnumber[2] = self.characters[random.randint(0, len(self.characters)-1)]
        stringnumber[3] = self.characters[random.randint(0, len(self.characters)-1)]

        stringnumber = ''.join(stringnumber)
        
        self.random["text"] = stringnumber
        print(self.random["text"])
        return

    def validate(self):
        boxes = [self.digit1, self.digit2, self.digit3, self.digit4]
        locks = [self.lock1, self.lock2, self.lock3, self.lock4]
        keys = [self.key1, self.key2, self.key3, self.key4, self.key5, self.key6]

        self.before["text"] = ""

        for i in range(len(boxes)):
            getdigit = boxes[i].get().lower()
            correct = 0
            self.before["text"] = self.before["text"] + getdigit + " "
            boxes[i]["bg"] = "#b20000"
            locks[i]["image"] = self.redlock

            if getdigit in self.random["text"] and not getdigit == "":
                boxes[i]["bg"] = "#bcc41c"
                locks[i]["image"] = self.yellowlock

            if getdigit == self.random["text"][i]:
                boxes[i]["bg"] = "#03b200"
                locks[i]["image"] = self.greenlock
                correct += 1

        self.clearText()
        self.digit1.focus()

        self.response["text"] = ""

        if not self.attempts >= 6:
            keys[self.attempts]["image"] = self.yellowkey
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
        boxes = [self.digit1, self.digit2, self.digit3, self.digit4]
        locks = [self.lock1, self.lock2, self.lock3, self.lock4]
        keys = [self.key1, self.key2, self.key3, self.key4, self.key5, self.key6]

        for i in range(len(boxes)):
            boxes[i]["bg"] = "#707070"
            locks[i]["image"] = self.whitelock

        for i in range(len(keys)):
            keys[i]["image"] = self.whitekey

    def newGame(self, controller):
        self.clearText()
        self.clearColors()
        self.createNewRandom()
        self.response["text"] = "New Number Initiated!"
        self.digit1.focus()
        self.attempts = 0
        self.before["text"] = ""

        if (controller == 0):
            self.characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        elif (controller == 1):
            self.characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']