#Author: Ben Archer
#Date: 07/21/2025
#Assignment: Final Project SDEV 120
from operator import truediv
from tkinter import *  # Import tkinter modules for GUI elements
from tkinter import messagebox  # For pop-up message boxes
from PIL import Image, ImageTk  # For image handling and display
import datetime  # For date/time to timestamp leaderboard entries
import sys  # For program exit and system-level operations


# X starts so true
clicked = True  # Boolean to track current turn (True for X, False for O)
count = 0  # Count of moves made during current game
winner = False  # Flag to indicate if a winner has been found

LEADERBOARD_FILE = "leaderboard.txt"  # File to store winners' initials and timestamps

def center_window(window, width, height):
    """Center the tkinter window on the screen."""
    screen_width = window.winfo_screenwidth()  # Get screen width
    screen_height = window.winfo_screenheight()  # Get screen height
    x = int((screen_width / 2) - (width / 2))  # Calculate x position for centering
    y = int((screen_height / 2) - (height / 2))  # Calculate y position for centering
    window.geometry(f"{width}x{height}+{x}+{y}")  # Set window size and position

# Start the game over
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9  # Game buttons
    global clicked, count  # Game state variables
    clicked = True  # Reset turn to X
    count = 0  # Reset move count
    for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        b.config(text=" ", bg="SystemButtonFace", state=NORMAL)  # Clear button text and enable them

#reset button takes you back to start menu
def reset_to_start_menu():
    global root  # Main window variable
    root.destroy()  # Close current game window
    start_menu()  # Show the start menu window

# disable all the buttons
def disable_all_buttons():
    for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        b.config(state=DISABLED)  # Disable buttons to prevent clicking after game ends

def prompt_for_initials():
    """Popup window to get exactly 3-letter initials from user, max length 3 enforced"""
    popup = Toplevel()  # Create new pop-up window
    popup.title("Enter your initials")
    center_window(popup, 300, 150)  # Center popup window

    Label(popup, text="Winner! Please Enter your initials:").pack(pady=10)

    initials_var = StringVar()  # Variable to store initials input

    entry = Entry(popup, textvariable=initials_var, width=5, font=("Helvetica", 18))
    entry.pack(pady=5)
    entry.focus_set()  # Focus on the entry box for immediate typing

    def on_key(event):
        value = initials_var.get()
        if len(value) > 3:
            initials_var.set(value[:3])  # Limit input length to 3

    entry.bind("<KeyRelease>", on_key)

    def submit():
        val = initials_var.get().upper()  # Convert to uppercase
        if len(val) == 3 and val.isalpha():
            popup.destroy()  # Close popup on valid input
        else:
            messagebox.showerror("Error", "Please enter exactly 3 letters.")  # Show error for invalid input

    Button(popup, text="Submit", command=submit).pack(pady=10)

    popup.grab_set()  # Make popup modal
    popup.wait_window()  # Wait until popup closes

    val = initials_var.get().upper()
    if len(val) == 3 and val.isalpha():
        return val
    return None

def save_winner_to_leaderboard(winner):
    """Save winner initials, winner X/O, and datetime to leaderboard file, then return to start menu"""
    initials = prompt_for_initials()  # Ask for winner initials
    if initials:
        timestamp = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p")  # Current timestamp
        with open(LEADERBOARD_FILE, "a") as f:
            f.write(f"{timestamp} - {initials}\n")  # Append initials and timestamp to file
    global root
    if root:
        root.destroy()  # Close current window
    start_menu()  # Return to start menu

def show_leaderboard():
    """Show leaderboard window reading from leaderboard file"""
    lb_win = Toplevel()  # New window for leaderboard
    lb_win.title("Game History")
    center_window(lb_win, 550, 650)  # Center window on screen

    # Image at the top of leaderboard window
    image = Image.open("trophy.jpg")
    image = image.resize((350, 350))  # Resize for display
    photo = ImageTk.PhotoImage(image)
    image_label = Label(lb_win, image=photo)
    image_label.image = photo  # Keep a reference to prevent garbage collection
    image_label.pack(pady=5)

    Label(lb_win, text="Past Winners", font=("Helvetica", 16, "bold")).pack(pady=5)

    # Frame containing the leaderboard text and scrollbar
    frame = Frame(lb_win)
    frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_box = Text(frame, width=40, height=15, font=("Helvetica", 12), yscrollcommand=scrollbar.set)
    text_box.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=text_box.yview)

    try:
        with open(LEADERBOARD_FILE, "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = "No leaderboard records found."  # Show if no records exist

    text_box.insert(END, content)
    text_box.config(state=DISABLED)  # Make text box read-only

    Button(lb_win, text="Close", command=lb_win.destroy).pack(pady=5)

def checkIfWon():
    global winner
    winner = False  # Reset winner flag

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
        b["text"] = "X"  # Mark this button as X
        b["bg"]="blue"  # Set button background blue for X
        clicked = False  # Switch turn to O
        count += 1  # Increment move count
        checkIfWon()  # Check for winner or tie
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"  # Mark button as O
        b["bg"]="red"  # Set button background red for O
        clicked = True  # Switch turn to X
        count += 1
        checkIfWon()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! Someone already chose this box!\n          Pick somewhere else!")

def run_game():
    global root, b1, b2, b3, b4, b5, b6, b7, b8, b9
    root = Tk()
    root.title('SDEV 120 Tic-Tac-Toe')

    # Create 9 buttons for the Tic Tac Toe grid, each calls b_click with itself
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    # Position buttons in a 3x3 grid layout
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    # Add menu with option to return to start menu
    my_menu = Menu(root)
    root.config(menu=my_menu)
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Start Menu", menu=options_menu)
    options_menu.add_command(label="Back", command=reset_to_start_menu)

    reset()  # Reset the board at start

    root.update()  # Update window info to get proper width and height

    # Center the window on the screen after sizing
    width = root.winfo_width()
    height = root.winfo_height()
    center_window(root, width, height)

    root.mainloop()  # Run the main event loop


def start_menu():
    # Create start menu window
    start_win = Tk()
    start_win.title("Tic-Tac-Toe Game Menu")
    start_win.geometry("300x400")  # Set fixed size
    center_window(start_win, 300, 350)  # Center it on screen

    # Load and display image at the top
    image = Image.open("toeboard.jpg")
    image = image.resize((150, 150))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(start_win, image=photo)
    image_label.image = photo  # Keep reference to image
    image_label.pack(pady=10)

    # Buttons for menu options
    Button(start_win, text="Start Game", font=("Helvetica", 14), width=15, command=lambda: [start_win.destroy(), run_game()]).pack(pady=5)
    Button(start_win, text="Game History", font=("Helvetica", 14), width=15, command=show_leaderboard).pack(pady=5)
    Button(start_win, text="Quit", font=("Helvetica", 14), width=15, command=sys.exit).pack(pady=5)

    start_win.mainloop()

# Start the program by showing the start menu
start_menu()
