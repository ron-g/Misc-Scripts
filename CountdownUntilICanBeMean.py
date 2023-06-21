#!/usr/bin/python3

from tkinter import *
from time import sleep
import datetime

def countdown():
    kids18thBday = datetime.datetime(kidsBday.year + 18, kidsBday.month, kidsBday.day)
    timeRemaining = kids18thBday - datetime.datetime.now()
    timeRemaining = timeRemaining.days*1440 + timeRemaining.seconds // 60
    timeRemaining = f"{timeRemaining} loooong minutes left."
    global bdayLabel
    bdayLabel['text'] = timeRemaining


root = Tk()

kidsBday = datetime.datetime(2005,1,1)

bdayLabel = Label(root, text=kidsBday.strftime('%Y-%m-%d'))
bdayLabel.pack()
calculateRemainingTimeButton = Button(root, text="Update", bg='blue', fg='black', command=countdown)
calculateRemainingTimeButton.pack()


root.mainloop()
