from tkinter import *
from PIL import ImageTk, Image

top = Tk()
top.title("Sudoku")
top.config(width=550, height=370, padx=2)
top.maxsize(width=550, height=370)

bgImage = Image.open('images\\bg.jpg')
displayBgImage = ImageTk.PhotoImage(bgImage)
lbBg = Label(top, image=displayBgImage).place(x=0, y=0)


def newGame():
    top.destroy()
    import menuForSudoku
#finished

#for continue
def cont():
    top.destroy()

def personal():
    top.destroy()
    import personal
#finished

def quit():
    top.destroy()
#finished

lbSudoku = Label(top, text="Sudoku", fg="#000000", font=("Helvetica", 30, "bold"))
lbSudoku.place(x=20, y=20)

bNewGame = Button(top, text="New Game", fg="#000000", font=("Helvetica", 13, "bold"), command=newGame)
bNewGame.place(x=45, y=100)

bContinue = Button(top, text="Continue", fg="#000000", font=("Helvetica", 13, "bold"), command=cont)
bContinue.place(x=50, y=145)

bPersonal = Button(top, text="Personal", fg="#000000", font=("Helvetica", 13, "bold"), command=personal)
bPersonal.place(x=51, y=190)

bQuit = Button(top, text="X", bg="#FF0000", fg="#000000", font=("Helvetica", 13, "bold"), command=quit)
bQuit.place(x=5, y=325)

top.mainloop()
