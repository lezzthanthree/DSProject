from tkinter import *
from pathlib import Path
import random
import pygame

class GameScreen(Frame):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # Create a canvas for this screen
        canvas = Canvas(self, bg="#000000", height=600, width=800, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # Create a label for a random number but don't display it.
        self.random = Label()

        # A valid character for the code/locks
        self.characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Set number of attempts to 0
        self.attempts = 0

        # Place a background
        self.bg = PhotoImage(file="GameScreen\\assets\\bg.png")
        canvas.create_image(0, 0, anchor="nw", image=self.bg)

        # Create a new game
        self.createNewRandom()
        
        # A response label
        self.response = Label(canvas, text="", fg="#FF0000", bg="#171717", font=("Determination Mono", 10), justify='center')
        self.response.place(x=120, y=500)

        # locks
        self.redlock = PhotoImage(file="GameScreen\\assets\\redlock.png")
        self.greenlock = PhotoImage(file="GameScreen\\assets\\greenlock.png")
        self.yellowlock = PhotoImage(file="GameScreen\\assets\\yellowlock.png")
        self.whitelock = PhotoImage(file="GameScreen\\assets\\whitelock.png")
        
        # lock #1
        self.lock1 = Label(self, image=self.whitelock, borderwidth=0, highlightthickness=0)
        self.lock1.place(x=147.0, y=203.0)
        self.valid1 = StringVar()
        self.digit1 = Entry(self, font=("Determination Mono", 65), justify='center', textvariable=self.valid1, borderwidth=0, highlightthickness=0, bg="#707070")
        self.digit1.place(x=165.0, y=263.0, width=78.0, height=78.0)
        self.valid1.trace("w", lambda *args: self.characterCheck(self.valid1, 0))

        # lock #2
        self.lock2 = Label(self, image=self.whitelock, borderwidth=0, highlightthickness=0)
        self.lock2.place(x=283.0, y=203.0)
        self.valid2 = StringVar()
        self.digit2 = Entry(self, font=("Determination Mono", 65), justify='center', textvariable=self.valid2, borderwidth=0, highlightthickness=0, bg="#707070")
        self.digit2.place(x=303.0, y=263.0, width=78.0, height=78.0)
        self.valid2.trace("w", lambda *args: self.characterCheck(self.valid2, 1))

        # lock #3
        self.lock3 = Label(self, image=self.whitelock, borderwidth=0, highlightthickness=0)
        self.lock3.place(x=420.0, y=203.0)
        self.valid3 = StringVar()
        self.digit3 = Entry(self, font=("Determination Mono", 65), justify='center', textvariable=self.valid3, borderwidth=0, highlightthickness=0, bg="#707070")
        self.digit3.place(x=441.0, y=263.0, width=78.0, height=78.0)
        self.valid3.trace("w", lambda *args: self.characterCheck(self.valid3, 2))

        # lock #4
        self.lock4 = Label(self, image=self.whitelock, borderwidth=0, highlightthickness=0)
        self.lock4.place(x=556.0, y=203.0)
        self.valid4 = StringVar()
        self.digit4 = Entry(self, font=("Determination Mono", 65), justify='center', textvariable=self.valid4, borderwidth=0, highlightthickness=0, bg="#707070")
        self.digit4.place(x=574.0, y=263.0, width=78.0, height=78.0)
        self.valid4.trace("w", lambda *args: self.characterCheck(self.valid4, 3))

        # attempt keys
        self.whitekey = PhotoImage(file="GameScreen\\assets\\whitekey.png")
        self.yellowkey = PhotoImage(file="GameScreen\\assets\\yellowkey.png")

        # create a key attempts and place them
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

        # A screen for the win and lose condition
        self.imgNone = PhotoImage(file="GameScreen\\assets\\null.png")
        self.imgWin = PhotoImage(file="GameScreen\\assets\\success.png")
        self.imgLose = PhotoImage(file="GameScreen\\assets\\fail.png")
        self.imgReady = PhotoImage(file="GameScreen\\assets\\ready.png")
        
        self.winloseConditiion = Label(self, image=self.imgReady, borderwidth=0, highlightthickness=0)
        self.winloseConditiion.place(x=0, y=0)

        # A crack button
        self.imgBtnValidate = PhotoImage(file="GameScreen\\assets\\crack.png")
        self.btnValidate = Button(self, image=self.imgBtnValidate, borderwidth=0, highlightthickness=0, command=lambda: self.validate(), relief="flat")
        self.btnValidate.place(x=334.0, y=460.0)

        # A button for the new game
        self.imgBtnNewLose = PhotoImage(file="GameScreen\\assets\\newlose.png")
        self.imgBtnNew = PhotoImage(file="GameScreen\\assets\\new.png")
        self.btnNew = Button(self, image=self.imgBtnNew, borderwidth=0, highlightthickness=0, command=lambda: self.newGame(controller.id), relief="flat")
        self.btnNew.place(x=22.0, y=33.0)

        # A button for the help screen
        self.imgBtnHelpLose = PhotoImage(file="GameScreen\\assets\\helplose.png")
        self.imgBtnHelp = PhotoImage(file="GameScreen\\assets\\help.png")
        self.btnHelp = Button(self, image=self.imgBtnHelp, borderwidth=0, highlightthickness=0, command=lambda: controller.show_frame("HelpScreen"), relief="flat")
        self.btnHelp.place(x=22.0, y=122.0)

        # A button for the home screen
        self.imgBtnHomeLose = PhotoImage(file="GameScreen\\assets\\homelose.png")
        self.imgBtnHome = PhotoImage(file="GameScreen\\assets\\home.png")
        self.btnHome = Button(self, image=self.imgBtnHome, borderwidth=0, highlightthickness=0, command=lambda: self.titlescreen(controller), relief="flat")
        self.btnHome.place(x=22.0, y=209.0)

        # Button separate for the win and lose screen
        self.imgCrackMore = PhotoImage(file="GameScreen\\assets\\crackmore.png")
        self.btnCrackMore = Button(self, image=self.imgCrackMore, borderwidth=0, highlightthickness=0, command=lambda: self.newGame(controller.id), relief="flat")

        # Button separate for the first new game
        self.imgReadyUp = PhotoImage(file="GameScreen\\assets\\startgame.png")
        self.btnReady = Button(self, image=self.imgReadyUp, borderwidth=0, highlightthickness=0, command=lambda: self.newGame(controller.id), relief="flat")
        self.btnReady.place(x=334.0, y=460.0)

    # A function to create a new game
    def createNewRandom(self):
        # Create a random number on each digit
        stringnumber = list("    ")
        stringnumber[0] = self.characters[random.randint(0, len(self.characters)-1)]
        stringnumber[1] = self.characters[random.randint(0, len(self.characters)-1)]
        stringnumber[2] = self.characters[random.randint(0, len(self.characters)-1)]
        stringnumber[3] = self.characters[random.randint(0, len(self.characters)-1)]
        
        stringnumber = ''.join(stringnumber)
        
        self.random["text"] = stringnumber
        return

    # A function to check if the user clicked CRACK
    def validate(self):
        # Put all locks, textbox, and keys in a list
        boxes = [self.digit1, self.digit2, self.digit3, self.digit4]
        locks = [self.lock1, self.lock2, self.lock3, self.lock4]
        keys = [self.key1, self.key2, self.key3, self.key4, self.key5, self.key6]

        # Clear the history
        self.before["text"] = ""

        # Set Correct answers to 0
        correct = 0
        
        # Validating Algorithm
        for i in range(len(boxes)):
            # Get the digit on the lock
            getdigit = boxes[i].get().lower()

            # Put the digit on the history
            self.before["text"] = self.before["text"] + getdigit + " "

            # Change the textbox and the lock to red.
            boxes[i]["bg"] = "#b20000"
            locks[i]["image"] = self.redlock

            # If the digit is in the correct answer, change textbox and the lock to yellow
            if getdigit in self.random["text"] and not getdigit == "":
                boxes[i]["bg"] = "#bcc41c"
                locks[i]["image"] = self.yellowlock

            # If the digit is equal to the correct answer's position, change textbox and the lock to green.
            if getdigit == self.random["text"][i]:
                boxes[i]["bg"] = "#03b200"
                locks[i]["image"] = self.greenlock
                correct += 1

        # Clear the textboxes
        self.clearText()

        # Put the text cursor to the first digit
        self.digit1.focus()

        # Clear the response text
        self.response["text"] = ""

        # If the player is still below six attempts, add one yellow key
        if not self.attempts >= 6:
            keys[self.attempts]["image"] = self.yellowkey
            self.attempts += 1

        # If the player got all the correct numbers
        if correct == 4:
            self.successscreen()
            return

        # If the player exceeds six attempts
        if self.attempts >= 6:
            self.failscreen()

    # A function to check if the player inputted a correct character on the textbox
    def characterCheck(self, entry_text, controller):
        # Put all the textbox on the list
        boxes = [self.digit1, self.digit2, self.digit3, self.digit4, self.btnValidate]

        # If the player inputted a character that is invalid, notify the user it's invalid and clear the lock.
        if not entry_text.get().lower() in self.characters:
            entry_text.set("")
            self.response["text"] = "invalid character"
            return

        # Limit the player with one character.
        if len(entry_text.get()) > 1:
            entry_text.set(entry_text.get()[-1])

        # Place the textbox cursor to the next lock
        boxes[controller + 1].focus()

        # Clear the response text
        self.response["text"] = ""


    # A function to clear the text
    def clearText(self):
        self.digit1.delete(0, END)
        self.digit2.delete(0, END)
        self.digit3.delete(0, END)
        self.digit4.delete(0, END)
        
    # A function to clear all the colors
    def clearColors(self):
        # Put all locks, textbox, and keys in a list
        boxes = [self.digit1, self.digit2, self.digit3, self.digit4]
        locks = [self.lock1, self.lock2, self.lock3, self.lock4]
        keys = [self.key1, self.key2, self.key3, self.key4, self.key5, self.key6]

        # Change everything with white
        for i in range(len(boxes)):
            boxes[i]["bg"] = "#707070"
            locks[i]["image"] = self.whitelock
        for i in range(len(keys)):
            keys[i]["image"] = self.whitekey

    # Create a new game
    def newGame(self, controller):
        # Clear the text and colors
        self.clearText()
        self.clearColors()

        # Create a new random code
        self.createNewRandom()

        # Clear the screen
        self.screenclean()
        self.winloseConditiion["image"] = self.imgNone

        # Notify the player the new code has been generated
        self.response["text"] = "new code"

        # Put the textbox cursor on the first digit
        self.digit1.focus()

        # Set all attempts to 0
        self.attempts = 0

        # Clear history
        self.before["text"] = ""

        # Check for the difficulty 
        if (controller == 0):
            self.characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        elif (controller == 1):
            self.characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

        print(self.random["text"])

    # A function to return to the title screen
    def titlescreen(self, controller):
        pygame.mixer.music.load("TitleScreen\\assets\\mus.mp3")
        pygame.mixer.music.play(loops=-1)
        self.readyupscreen()
        controller.show_frame("TitleScreen")
        return

    # A function to show the success screen
    def successscreen(self):
        self.winloseConditiion["image"] = self.imgWin
        self.btnCrackMore.place(x=334.0, y=460.0)
        return

    # A function to show the fail screen
    def failscreen(self):
        self.winloseConditiion["image"] = self.imgLose
        self.btnNew["image"] = self.imgBtnNewLose
        self.btnHelp["image"] = self.imgBtnHelpLose
        self.btnHome["image"] = self.imgBtnHomeLose
        self.btnCrackMore.place(x=334.0, y=460.0)
        return
    
    # A function to show the ready up screen
    def readyupscreen(self):
        self.winloseConditiion["image"] = self.imgReady
        self.btnReady.place(x=334.0, y=460.0)
        return

    # A function to clear the win and lose screen
    def screenclean(self):
        self.winloseConditiion["image"] = self.imgNone
        self.btnCrackMore.place_forget()
        self.btnReady.place_forget()
        self.btnNew["image"] = self.imgBtnNew
        self.btnHelp["image"] = self.imgBtnHelp
        self.btnHome["image"] = self.imgBtnHome
        return