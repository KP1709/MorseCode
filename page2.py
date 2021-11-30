import tkinter as tk

window = tk.Tk()
window.title("Morse code translator")
window.geometry("600x500")
window.resizable(0,0)

def getTranslation():
    pass

def playTranslation():
    pass

plainTextBox = tk.Text(window, width = 72, height = 10 )
plainTextBox.grid(padx = 10, pady= 10)

submitButton = tk.Button(window, width = 73, height = 2, text = "Submit", bg= "#99ccff")
submitButton.grid(padx = 10, pady = 10)

morseLabel = tk.Label(window, text = "This is conversion into morse code" )
morseLabel.grid(padx = 10, pady = 20)

hearButton = tk.Button(window, width = 73, height = 2, text = "Listen to the translation", bg = "#99ccff")
hearButton.grid(padx = 20, pady= 20)

window.mainloop()
