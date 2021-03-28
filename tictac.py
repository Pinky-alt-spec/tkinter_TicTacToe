from tkinter import *
from tkinter import messagebox

# Basic tkinter starter
root = Tk()
root.title('Tic Tac Toe')
root.iconbitmap('')
# root.geometry(1200x710)

# If X is true that means is O's turn to click and vice vesa
# This means the first player to click will be X
# X starts = True
clicked = True
count = 0


# Disable all Buttons
def disable_all_buttons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)

    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)

    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)


# check to see if X has won in each row(going across the grid)
def if_won():
    global winner
    winner = False

    if btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X":
        btn1.config(bg="#45bfad")
        btn2.config(bg="#45bfad")
        btn3.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! X Won!!!")
        disable_all_buttons()

    elif btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X":
        btn4.config(bg="#45bfad")
        btn5.config(bg="#45bfad")
        btn6.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! X Won!!!")
        disable_all_buttons()

    elif btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X":
        btn7.config(bg="#45bfad")
        btn8.config(bg="#45bfad")
        btn9.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! X Won!!!")
        disable_all_buttons()

    # check to see if X has won in each column(going down the grid)
    elif btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X":
        btn1.config(bg="#45bfad")
        btn4.config(bg="#45bfad")
        btn7.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! X Won!!!")
        disable_all_buttons()

    elif btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X":
        btn2.config(bg="#45bfad")
        btn5.config(bg="#45bfad")
        btn8.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! X Won!!!")
        disable_all_buttons()

    elif btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X":
        btn3.config(bg="#45bfad")
        btn6.config(bg="#45bfad")
        btn9.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! X Won!!!")
        disable_all_buttons()

    # check to see if X has won in each diagonal
    elif btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X":
        btn1.config(bg="#45bfad")
        btn5.config(bg="#45bfad")
        btn9.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! X Won!!!")
        disable_all_buttons()

    elif btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X":
        btn3.config(bg="#45bfad")
        btn5.config(bg="#45bfad")
        btn7.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! X Won!!!")
        disable_all_buttons()

    # CHeck if O's has won across the grid
    elif btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O":
        btn1.config(bg="#45bfad")
        btn2.config(bg="#45bfad")
        btn3.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! O Won!!!")
        disable_all_buttons()

    elif btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O":
        btn4.config(bg="#45bfad")
        btn5.config(bg="#45bfad")
        btn6.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! O Won!!!")
        disable_all_buttons()

    elif btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O":
        btn7.config(bg="#45bfad")
        btn8.config(bg="#45bfad")
        btn9.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! O Won!!!")
        disable_all_buttons()

    # check to see if O has won in each column(going down the grid)
    elif btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O":
        btn1.config(bg="#45bfad")
        btn4.config(bg="#45bfad")
        btn7.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! O Won!!!")
        disable_all_buttons()

    elif btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O":
        btn2.config(bg="#45bfad")
        btn5.config(bg="#45bfad")
        btn8.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! O Won!!!")
        disable_all_buttons()

    elif btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O":
        btn3.config(bg="#45bfad")
        btn6.config(bg="#45bfad")
        btn9.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! O Won!!!")
        disable_all_buttons()

    # check to see if "O" has won in each diagonal
    elif btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O":
        btn1.config(bg="#45bfad")
        btn5.config(bg="#45bfad")
        btn9.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! O Won!!!")
        disable_all_buttons()

    elif btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O":
        btn3.config(bg="#45bfad")
        btn5.config(bg="#45bfad")
        btn7.config(bg="#45bfad")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Job!!! O Won!!!")
        disable_all_buttons()

    # Check if tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "Its A Tie!\nNo One Wins!")
        disable_all_buttons()


# Button clicked function
def b_click(btn):
    global clicked, count

    # Check if any player has clicked any button
    if btn["text"] == " " and clicked == True:
        btn["text"] = "X"
        # clicked is false, then its O's turn
        clicked = False
        # Count started at 0, We need to keep track of how many moves there are
        # Everytime player makes a move we add 1 to the count
        count += 1
        # everytime player clicks we need to check if they won by calling the if_won function
        if_won()

    elif btn["text"] == " " and clicked == False:
        btn["text"] = "O"
        clicked = True
        count += 1
        if_won()
    else:
        messagebox.showerror("Tic tac Toe", "Oopsy!!! That box has already been Clicked\nSelect Another Box")


# reset the Game and start over!
def reset():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    global clicked, count
    clicked = True
    count = 0

    # Build buttons for the ui
    btn1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                  command=lambda: b_click(btn1))
    btn2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                  command=lambda: b_click(btn2))
    btn3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                  command=lambda: b_click(btn3))

    btn4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                  command=lambda: b_click(btn4))
    btn5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                  command=lambda: b_click(btn5))
    btn6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                  command=lambda: b_click(btn6))

    btn7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                  command=lambda: b_click(btn7))
    btn8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                  command=lambda: b_click(btn8))
    btn9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                  command=lambda: b_click(btn9))

    # Put our buttons in a Grid on the screen
    btn1.grid(row=0, column=0)
    btn2.grid(row=0, column=1)
    btn3.grid(row=0, column=2)

    btn4.grid(row=1, column=0)
    btn5.grid(row=1, column=1)
    btn6.grid(row=1, column=2)

    btn7.grid(row=2, column=0)
    btn8.grid(row=2, column=1)
    btn9.grid(row=2, column=2)


# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()

root.mainloop()
