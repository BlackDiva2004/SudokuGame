from tkinter import *
from PIL import ImageTk, Image

topMenu = Tk()
topMenu.title("Sudoku")
topMenu.config(width=300, height=300, padx=2, bg="#FFE4D1")
topMenu.maxsize(width=300, height=300)

def easyGenerator():
    topMenu.destroy()
    import SudokuGeneratiorEasy
#finished

def mediumGenerator():
    topMenu.destroy()
    import SudokuGeneratiorMedium
#finished

def hardGenerator():
    topMenu.destroy()
    import SudokuGeneratiorHard
#finished

def returnBack():
    topMenu.destroy()
    import main
#finished

lbSudoku = Label(topMenu, text="Sudoku", fg="#000000", font=("Helvetica", 20, "bold"))
lbSudoku.place(x=90, y=20)

easy = Button(topMenu, text="Easy", fg="#000000", font=("Helvetica", 13, "bold"), command=easyGenerator)
easy.place(x=110, y=75)

medium = Button(topMenu, text="Medium", fg="#000000", font=("Helvetica", 13, "bold"), command=mediumGenerator)
medium.place(x=98, y=115)

hard = Button(topMenu, text="Hard", fg="#000000", font=("Helvetica", 13, "bold"), command=hardGenerator)
hard.place(x=110, y=155)

bReturn= Button(topMenu, text="Return", bg="#008000", fg="#000000", font=("Helvetica", 10, "bold"), command=returnBack)
bReturn.place(x=2, y=270)

topMenu.mainloop()