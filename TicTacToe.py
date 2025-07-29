#Author: Ben Archer
#Date: 07/21/2025
#Assignment: Final Project SDEV 120
from operator import truediv
from tkinter import *
from tkinter import messagebox
from types import LambdaType

root = Tk()
root.title('SDEV 120 Tic-Tac-Toe')
#root.geometry("1200x710")

# X starts so true
clicked = True
count = 0

# disable all the buttons
def disable_all_buttons():
    pass

# Check to see if someone won
def checkIfWon():
    global winner
    winner = False
#CHECK X WINS
    # winner across
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()

# Winner vertical
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()

# Winner Diagnol
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()

# CHECK 0 WINS
        # winner across
        if b1["text"] == "X" and b2["text"] == "O" and b3["text"] == "O":
            b1.config(bg="green")
            b2.config(bg="green")
            b3.config(bg="green")
            winner = True
            messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
            disable_all_buttons()
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4.config(bg="green")
            b5.config(bg="green")
            b6.config(bg="green")
            winner = True
            messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
            disable_all_buttons()
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7.config(bg="green")
            b8.config(bg="green")
            b9.config(bg="green")
            winner = True
            messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
            disable_all_buttons()

        # Winner vertical
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1.config(bg="green")
            b4.config(bg="green")
            b7.config(bg="green")
            winner = True
            messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
            disable_all_buttons()
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2.config(bg="green")
            b5.config(bg="green")
            b8.config(bg="green")
            winner = True
            messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
            disable_all_buttons()
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3.config(bg="green")
            b6.config(bg="green")
            b9.config(bg="green")
            winner = True
            messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
            disable_all_buttons()

        # Winner Diagnol
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1.config(bg="green")
            b5.config(bg="green")
            b9.config(bg="green")
            winner = True
            messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
            disable_all_buttons()
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b1.config(bg="green")
            b4.config(bg="green")
            b7.config(bg="green")
            winner = True
            messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
            disable_all_buttons()


def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! Someone already chose this box!\n          Pick somewhere else!")
#Build buttons
b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

#Grid our buttons to the screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


root.mainloop()

