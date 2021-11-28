# Morse code program (Without GUI) - Kareena Patel - 27/11/2021

# Importing modules
import winsound
import time

""" Function converts string into visual morse code"""
def letterInMorse(string):
    morseLetterDict = {"a":" O-", "b":"-OOO", "c":"-O-O",                 # Created dictionary to store letters in visual morse code
                       "d":"-OO", "e":"O", "f":"OO-O",
                       "g":"--O", "h":"OOOO", "i":"OO",
                       "j":"O---", "k":"-O-", "l":"O-OO",
                       "m":"--", "n":"-O", "o":"---",
                       "p":"O--O", "q":"--O-", "r":"O-O",
                       "s":"OOO", "t":"-", "u":"OO-",
                       "v":"OOO-", "w":"O--", "x":"-OO-",
                       "y":"-O--", "z":"--OO", " ":" "}                   # Whitespace included to avoid errors using multiple words
    
    # Goes through each letter in string to convert
    global conversion                                                     # Creating a global variable (used in morseInSound)
    conversion = ""
    for letter in string:
        x = morseLetterDict.get(letter)
        conversion = conversion + "|" + x                                 #'|' - characters are readable and concatenate
    return conversion

""" Function converts visual morse code into sound"""
def morseInSound(conversion):
    sep = conversion.replace("|", " ")                                    # Changes '|' into spaces for conversion
    print(sep)
    for char in sep:
        if char == "O":
            winsound.Beep(500,100)                                        # Uses system bell at set frequency and duration (depending on char)
        elif char == "-":
            winsound.Beep(500,300)
        elif char == " ":
            time.sleep(3)                                                 # Whitespace shown by pause (sleep) 
        else:
            time.sleep(2)

while True:                                                               # Continuous execution of program until vaild string output (break)
    try:
        string = str.lower(input("Enter a string to convert to morse: "))
        letterInMorse(string)
        morseInSound(conversion)
        break
    except TypeError:                                                     # Catching error and handling it using try and accept
        print("You cannot use special characters or numbers")
