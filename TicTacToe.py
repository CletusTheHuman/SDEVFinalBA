#Author: Ben Archer
#Date: 07/21/2025
#Assignment: Final Project SDEV 120
from operator import truediv
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime
import sys


# X starts so true
clicked = True
count = 0
winner = False

LEADERBOARD_FILE = "leaderboard.txt"

def center_window(window, width, height):
    """Center the tkinter window on the screen."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x}+{y}")

# Start the game over
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        b.config(text=" ", bg="SystemButtonFace", state=NORMAL)

#reset button takes you back to start menu
def reset_to_start_menu():
    global root
    root.destroy()
    start_menu()

# disable all the buttons
def disable_all_buttons():
    for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        b.config(state=DISABLED)

def prompt_for_initials():
    """Popup window to get exactly 3-letter initials from user, max length 3 enforced"""
    popup = Toplevel()
    popup.title("Enter your initials")
    center_window(popup, 300, 150)

    Label(popup, text="Winner! Please Enter your initials:").pack(pady=10)

    initials_var = StringVar()

    entry = Entry(popup, textvariable=initials_var, width=5, font=("Helvetica", 18))
    entry.pack(pady=5)
    entry.focus_set()

    def on_key(event):
        value = initials_var.get()
        if len(value) > 3:
            initials_var.set(value[:3])
    entry.bind("<KeyRelease>", on_key)

    def submit():
        val = initials_var.get().upper()
        if len(val) == 3 and val.isalpha():
            popup.destroy()
        else:
            messagebox.showerror("Error", "Please enter exactly 3 letters.")

    Button(popup, text="Submit", command=submit).pack(pady=10)

    popup.grab_set()
    popup.wait_window()

    val = initials_var.get().upper()
    if len(val) == 3 and val.isalpha():
        return val
    return None

def save_winner_to_leaderboard(winner):
    """Save winner initials, winner X/O, and datetime to leaderboard file, then return to start menu"""
    initials = prompt_for_initials()
    if initials:
        timestamp = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p")
        with open(LEADERBOARD_FILE, "a") as f:
            f.write(f"{timestamp} - {initials}\n")
    global root
    if root:
        root.destroy()
    start_menu()

def show_leaderboard():
    """Show leaderboard window reading from leaderboard file"""
    lb_win = Toplevel()
    lb_win.title("Game History")
    center_window(lb_win, 550, 650)  # Slightly wider to fit the scrollbar

    # Image at the top
    image = Image.open("trophy.jpg")
    image = image.resize((350, 350))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(lb_win, image=photo)
    image_label.image = photo
    image_label.pack(pady=5)

    Label(lb_win, text="Past Winners", font=("Helvetica", 16, "bold")).pack(pady=5)

    # Frame to hold text box and scrollbar side by side
    frame = Frame(lb_win)
    frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

    # Scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Text box with attached scrollbar
    text_box = Text(frame, width=40, height=15, font=("Helvetica", 12), yscrollcommand=scrollbar.set)
    text_box.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=text_box.yview)

    # Load leaderboard data
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = "No leaderboard records found."

    text_box.insert(END, content)
    text_box.config(state=DISABLED)

    Button(lb_win, text="Close", command=lb_win.destroy).pack(pady=5)



def checkIfWon():
    global winner
    winner = False

    # CHECK X WINS
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("X")
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("X")
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("X")
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("X")
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("X")
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("X")
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("X")
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "X wins!\nO is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("X")

    # CHECK O WINS
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("O")
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("O")
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("O")
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("O")
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("O")
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("O")
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("O")
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic tac Toe", "O wins!\nX is a loser!")
        disable_all_buttons()
        save_winner_to_leaderboard("O")

    # check if tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "You tied! You both lose!")
        disable_all_buttons()
        # Go back to start menu after tie
        global root
        if root:
            root.destroy()
        start_menu()


# Button clicked function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        b["bg"]="blue"
        clicked = False
        count += 1
        checkIfWon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        b["bg"]="red"
        clicked = True
        count += 1
        checkIfWon()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! Someone already chose this box!\n          Pick somewhere else!")

def run_game():
    global root, b1, b2, b3, b4, b5, b6, b7, b8, b9
    root = Tk()
    root.title('SDEV 120 Tic-Tac-Toe')

    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    my_menu = Menu(root)
    root.config(menu=my_menu)
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Start Menu", menu=options_menu)
    options_menu.add_command(label="Back", command=reset_to_start_menu)

    reset()

    root.update()  # Update "requested size" from geometry manager

    # Now center window based on real window size
    width = root.winfo_width()
    height = root.winfo_height()
    center_window(root, width, height)

    root.mainloop()


def start_menu():
    start_win = Tk()
    start_win.title("Tic-Tac-Toe Game Menu")
    start_win.geometry("300x400")  # made taller for the image
    center_window(start_win, 300, 350)

    # Load and display the image
    image = Image.open("toeboard.jpg")
    image = image.resize((150, 150))  # resize if needed
    photo = ImageTk.PhotoImage(image)

    image_label = Label(start_win, image=photo)
    image_label.image = photo  # prevent garbage collection
    image_label.pack(pady=10)


    Button(start_win, text="Start Game", font=("Helvetica", 14), width=15, command=lambda: [start_win.destroy(), run_game()]).pack(pady=5)
    Button(start_win, text="Game History", font=("Helvetica", 14), width=15, command=show_leaderboard).pack(pady=5)
    Button(start_win, text="Quit", font=("Helvetica", 14), width=15, command=sys.exit).pack(pady=5)

    start_win.mainloop()


# Start from the start menu
start_menu()
