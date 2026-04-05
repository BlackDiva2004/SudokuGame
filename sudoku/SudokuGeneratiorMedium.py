from tkinter import *
import random
from PIL import ImageTk, Image

topGeneratorMedium = Tk()
topGeneratorMedium.title("Sudoku Easy")
topGeneratorMedium.config(width=550, height=380)
topGeneratorMedium.maxsize(width=550, height=380)

bgImage = Image.open('images\\purple-flowers.png')
displayBgImage = ImageTk.PhotoImage(bgImage)
lbBg = Label(topGeneratorMedium, image=displayBgImage).place(x=0, y=0)

def update_timer():
    current_time = int(timer_label["text"])
    current_time += 1
    timer_label["text"] = str(current_time)
    topGeneratorMedium.after(1000, update_timer)
def sudoku_grid(draw):
    size = 32
    thick = 3
    not_thick = 1

    for i in range(10):
        line = None
        if i % 3 == 0:
            line = thick
        else:
            line = not_thick
        sx1 = (i * size) + 10
        sy1 = 10
        ex1 = (i * size) + 10
        ey1 = (size * 9) + 10
        draw.create_line(sx1, sy1, ex1, ey1, width=line)

        sx2 = 10
        sy2 = (i * size) + 10

        ex2 = (size * 9) + 10
        ey2 = (i * size) + 10
        draw.create_line(sx2, sy2, ex2, ey2, width=line)

# Function to generate a Sudoku puzzle with 38 random numbers
def generate_sudoku():
    sudoku = []
    for _ in range(9):
        row = [0] * 9
        sudoku.append(row)
    for _ in range(28):
        while True:
            row= random.randint(0, 8)
            col= random.randint(0, 8)
            num = random.randint(1, 9)
            if is_valid_move(sudoku, row, col, num):
                sudoku[row][col] = num
                break
    return sudoku


def is_valid_move(sudoku, row, col, num):
    # Check if num is in the same row
    for i in range(9):
        if sudoku[row][i] == num:
            return False

    # Check if num is in the same column
    for i in range(9):
        if sudoku[i][col] == num:
            return False

    # Check if num is in the same 3x3 subgrid
    subgrid_start_row = (row // 3) * 3
    subgrid_start_col = (col // 3) * 3
    for i in range(subgrid_start_row, subgrid_start_row + 3):
        for j in range(subgrid_start_col, subgrid_start_col + 3):
            if sudoku[i][j] == num:
                return False

    # If num is not found in the row, column, or subgrid, it's a valid move
    return True


def draw_numbers(canvas, grid):
    distance = 28
    space = 32
    font = ("Arial", 16)

    for row in range(9):
        for col in range(9):
            output = grid[row][col]
            if output != 0:
                canvas.create_text((col * space) + distance,(row * space) + distance - 2,text=str(output),font=font,fill="black")

def fill_cell():
    row = int(entry_row.get())
    col = int(entry_col.get())
    num = int(entry_num.get())

    if 1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9:
        if is_valid_move(sudoku_grid_data, row - 1, col - 1, num):
            sudoku_grid_data[row - 1][col - 1] = num
            draw_numbers(draw, sudoku_grid_data)
            entry_num.delete(0, END)
            check_correctness(row - 1, col - 1)
        else:
            entry_num.delete(0, END)
            entry_num.insert(0, "Invalid")
    else:
        entry_num.delete(0, END)
        entry_num.insert(0, "Invalid")

def check_correctness(row, col):
    if sudoku_grid_data[row][col] == original_sudoku[row][col]:
        draw.create_rectangle(
            col * 32 + 10,
            row * 32 + 10,
            (col + 1) * 32 + 10,
            (row + 1) * 32 + 10,
            outline="green",
            width=2
        )
    else:
        draw.create_rectangle(
            col * 32 + 10,
            row * 32 + 10,
            (col + 1) * 32 + 10,
            (row + 1) * 32 + 10,
            outline="red",
            width=2
        )

def home():
    topGeneratorMedium.destroy()
    import main

def saveProgress():

    f = open("medium", "w")
    for row in sudoku_grid_data:
        row_str = ""
        for num in row:
            row_str += str(num) + " "
        row_str = row_str.strip()  # Remove the trailing space
        row_str += "\n"
        f.write(row_str)

    # Save the timer value
    timer_value = timer_label["text"]
    f.write(timer_value)

    # Close the file
    f.close()


def newGame():
    topGeneratorMedium.destroy()
    import menuForSudoku

def resetGame():
    global sudoku_grid_data
    sudoku_grid_data = generate_sudoku()
    draw.delete("all")
    sudoku_grid(draw)
    draw_numbers(draw, sudoku_grid_data)
    timer_label.config(text="0")

def close():
    topGeneratorMedium.destroy()

draw = Canvas(topGeneratorMedium, width=305, height=305, bg="#FFE4D1")
draw.place(x=110, y=30)

sudoku_grid_data = generate_sudoku()
original_sudoku = [row[:] for row in sudoku_grid_data]

sudoku_grid(draw)
draw_numbers(draw, sudoku_grid_data)


entry_row = Entry(topGeneratorMedium)
entry_row.place(x=110, y=350)
entry_row_label = Label(topGeneratorMedium, text="Row:")
entry_row_label.place(x=80, y=350)

entry_col = Entry(topGeneratorMedium)
entry_col.place(x=210, y=350)
entry_col_label = Label(topGeneratorMedium, text="Column:")
entry_col_label.place(x=160, y=350)

entry_num = Entry(topGeneratorMedium)
entry_num.place(x=310, y=350)
entry_num_label = Label(topGeneratorMedium, text="Number:")
entry_num_label.place(x=260, y=350)

fill_button = Button(topGeneratorMedium, text="Fill", command=fill_cell)
fill_button.place(x=410, y=346)

timer_label = Label(topGeneratorMedium, text="0", font=("Helvetica", 15))
timer_label.place(x=30, y=10)

update_timer()

menu_bar = Menu(topGeneratorMedium, font=("Arial", 10))
topGeneratorMedium.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0, font=("Arial", 10))
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Home", command=home)
file_menu.add_command(label="Save", command=saveProgress)
file_menu.add_separator()
file_menu.add_command(label="New", command=newGame)
file_menu.add_command(label="Reset", command=resetGame)
file_menu.add_command(label="Exit", command=close)


topGeneratorMedium.mainloop()
