import tkinter as tk

window = tk.Tk()
window.title("Morse code translator")
window.geometry("600x500")
window.resizable(0,0)

def next():
    window.destroy()
    import page2

frame1 = tk.Frame(master=window,padx=30, pady=30)
frame1.pack(padx=10, pady = 5)
label1 = tk.Label(
    master = frame1,
    text = "Morse code translator",
    fg = "blue",
    width = 75,
    height = 1,
    font = ("Arial",25))

label1.place(x=300, y=0)
label1.pack()

frame2 = tk.Frame(master=window,padx = 30, pady = 30)
frame2.pack()
label2 = tk.Label(
    master = frame2,
    text = "Instructions:\n"
            "Type what you want to be converted into Morse code.\n"
            "Press 'convert' to convert the text.\n"
            "Press 'hear' to hear the Morse code.\n",
    fg = "black",
    width = 75,
    height = 5,
    font = ("Arial",14))

label2.place(x=300, y=100)
label2.pack()

frame3 = tk.Frame(master=window)
frame3.pack()
nextButton = tk.Button(
    master = frame3,
    text = "Next",
    width = 25,
    height = 5,
    bg = "#99ccff",
    command = lambda:next(),
    font = ("Arial",14))

nextButton.place(x=300, y=600)
nextButton.pack()

window.mainloop()
