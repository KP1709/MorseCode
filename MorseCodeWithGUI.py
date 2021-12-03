# Morse Code Program with GUI - 03/12/2021 - Kareena Patel

from tkinter import *
import tkinter as tk
import time
import winsound

window = tk.Tk()
window.title("Morse code translator")
window.geometry("600x650")
window.resizable(0,0)

def letterInMorse(string):
    morseLetterDict = {"a":" .-", "b":"-...", "c":"-.-.",                 # Created dictionary to store letters in visual morse code
                       "d":"-..", "e":".", "f":"..-.",
                       "g":"--.", "h":"....", "i":"..",
                       "j":".---", "k":"-.-", "l":".-..",
                       "m":"--", "n":"-.", "o":"---",
                       "p":".--.", "q":"--.-", "r":".-.",
                       "s":"...", "t":"-", "u":"..-",
                       "v":"...-", "w":".--", "x":"-..-",
                       "y":"-.--", "z":"--..", " ":"   "}

    global conversion                                                     # Creating a global variable (used in SoundInMorse)
    conversion = ""
    for letter in string:
        x = morseLetterDict.get(letter.lower())
        value = conversion + "|" + x                                      #'|' - characters are readable and concatenate
        conversion = value.replace("|", "  ")                             # Changes '|' into spaces for conversion
    return conversion

def getTranslation(conversion):
    string = plainTextBox.get("1.0","end-1c")                             # 'end-1c' removes extra line
    global morseText
    morseText = letterInMorse(string) 
    morseTextBox.config(state = "normal")                                 # Opens text box for editing
    morseTextBox.delete(1.0,END)                                          # Removes text in box  
    morseTextBox.insert(1.0,morseText)                                    # Inserts conversion into textbox
    morseTextBox.config(state = "disabled")                               # Updates text to output in text box             
    return morseText                                                      # Disables editing so user cannot type in box

def playTranslation(conversion):                                                
    for char in morseText:                                                # The morse code is stored in var morseText
        if char == ".":
            winsound.Beep(500,100)                                        # Plays winsound (problem: freezes GUI - cannot exit midway)
        elif char == "-":
            winsound.Beep(500,300)
        elif char == " ":
            time.sleep(2)                                                 # Whitespace shown by pause (sleep) 
        else:
            time.sleep(3)


heading = tk.Label(
    window,
    text = "Morse code translator",
    fg = "orange",
    width = 30,
    height = 1,
    font = ("Arial",20))
heading.grid(padx=10, pady=5)

instructions = tk.Label(
    master = window,
    text = "Instructions:\n"
            "Type what you want to be converted into Morse code.\n"                   
            "Press 'convert' to convert the text.\n"
            "Press 'Listen to the translation' to hear the Morse code.\n",
    fg = "black",
    width = 45,
    height = 5,
    font = ("Arial",12))
instructions.grid(padx=10, pady=10)

plainTextBox = tk.Text(
    window,
    width = 72,
    height = 10,
    wrap = WORD)
plainTextBox.grid(padx = 10, pady= 5)

submitButton = tk.Button(window,
    width = 73, 
    height = 2, 
    text = "Submit", 
    bg= "#99ccff")
submitButton.grid(padx = 10, pady = 10)
submitButton.bind("<Button-1>", getTranslation)                          # Button links to function called getTranslation for event

morseTextBox = tk.Text(
    window,
    width = 72,
    height = 10,
    wrap = WORD)                                                         # Wraps text so it is readable to user
morseTextBox.config(state = "disabled")
morseTextBox.grid(padx=10, pady=10)

hearButton = tk.Button(window, 
    width = 73, 
    height = 2, 
    text = "Listen to the translation", 
    bg = "#99ccff")
hearButton.grid(padx = 20, pady= 10)
hearButton.bind("<Button-1>", playTranslation)

window.mainloop()                                                                                                                                
