from email.utils import collapse_rfc2231_value
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# count is the number of turns. When it reaches 9, the game ends in a tie.
count = 0
winner = False
tictactoe = Tk()
tictactoe.title("Tic Tac Toe")
ws = tictactoe.winfo_screenwidth() # width of the screen
hs = tictactoe.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
w = 300 # width of the screen
h = 170 # height of the screen
x = (ws/2) - (w/2) # position coordinates of the Tk window
y = (hs/2) - (h/2) # position coordinates of the Tk window
tictactoe.geometry('%dx%d+%d+%d' % (w, h, x, y))
tictactoe.configure(background='#F0F8FF')

pontuation = [[0,0,0],[0,0,0],[0,0,0]]
clicked = True

# Default values for the scores
x_score_text = tk.StringVar()
o_score_text = tk.StringVar()
draw_score_text = tk.StringVar()
x_score_text.set("0")
o_score_text.set("0")
draw_score_text.set("0")
x_score = 0
o_score = 0
draw_score = 0

def update_scores():
    global x_score, o_score, draw_score
    x_score_text.set(x_score)
    o_score_text.set(o_score)
    draw_score_text.set(draw_score)

def reset_scores():
    global x_score, o_score, draw_score, game_counts
    x_score_text.set(0)
    o_score_text.set(0)
    draw_score_text.set(0)
    game_counts = 0
    x_score = 0
    o_score = 0
    draw_score = 0

reset_scores()

tk.Label(tictactoe, text="X", font=("Tahoma", 10), background='#CFEAF3',fg='#005E7D').place(width=115, x=180, y=0)
x_score_label = tk.Label(tictactoe, textvariable=x_score_text, font=("Tahoma", 10), background='#DCF1F9',fg='#005E7D').place(width=115, x=180, y=26)

tk.Label(tictactoe, text="O", font=("Tahoma", 10), background='#DEF5C2',fg='#437D00').place(width=115, x=180, y=60)
o_score_label = tk.Label(tictactoe, textvariable=o_score_text, font=("Tahoma", 10), background='#E8F9D3',fg='#437D00').place(width=115, x=180, y=86)

tk.Label(tictactoe, text="Draw", font=("Tahoma", 10), background='#F4F5C2',fg='#7A7C00').place(width=115, x=180, y=120)
draw_score_label = tk.Label(tictactoe, textvariable=draw_score_text, font=("Tahoma", 10), background='#F9FAD6',fg='#7A7C00').place(width=115, x=180, y=146)


def game_score():
    global jogo
    jogo = [[0,0,0],[0,0,0],[0,0,0]]

def disable_buttons():
    bt1.configure(state=DISABLED)
    bt2.configure(state=DISABLED)
    bt3.configure(state=DISABLED)
    bt4.configure(state=DISABLED)
    bt5.configure(state=DISABLED)
    bt6.configure(state=DISABLED)
    bt7.configure(state=DISABLED)
    bt8.configure(state=DISABLED)
    bt9.configure(state=DISABLED)

# button clicked function
def botao(btn):
    global clicked, count
    if btn['text'] == " " and clicked:
        btn["text"] = "X"
        clicked = False
        count += 1
        jogada(btn)
        check_game()
    elif btn["text"] == " " and not clicked:
        btn["text"] = "O"
        clicked = True
        count += 1
        jogada(btn)
        check_game()
    else:
        messagebox.showerror("Error", "Choose other position!")


def jogada(btn):
    global jogo
    if count%2 == 0:
        if btn == bt1:
            jogo[0][0] = -1
        elif btn == bt2:
            jogo[0][1] = -1
        elif btn == bt3:
            jogo[0][2] = -1
        elif btn == bt4:
            jogo[1][0] = -1
        elif btn == bt5:
            jogo[1][1] = -1
        elif btn == bt6:
            jogo[1][2] = -1
        elif btn == bt7:
            jogo[2][0] = -1
        elif btn == bt8:
            jogo[2][1] = -1
        elif btn == bt9:
            jogo[2][2] = -1
    else:
        if btn == bt1:
            jogo[0][0] = 1
        elif btn == bt2:
            jogo[0][1] = 1
        elif btn == bt3:
            jogo[0][2] = 1
        elif btn == bt4:
            jogo[1][0] = 1
        elif btn == bt5:
            jogo[1][1] = 1
        elif btn == bt6:
            jogo[1][2] = 1
        elif btn == bt7:
            jogo[2][0] = 1
        elif btn == bt8:
            jogo[2][1] = 1
        elif btn == bt9:
            jogo[2][2] = 1


# Check if the game is over
def check_game():
    global winner, game_counts, x_score, o_score, draw_score
    # Checking the rows
    row1 = sum(jogo[0])
    row2 = sum(jogo[1])
    row3 = sum(jogo[2])
    col1 = jogo[0][0]+jogo[1][0]+jogo[2][0]
    col2 = jogo[0][1]+jogo[1][1]+jogo[2][1]
    col3 = jogo[0][2]+jogo[1][2]+jogo[2][2]
    diag1 = jogo[0][0]+jogo[1][1]+jogo[2][2]
    diag2 = jogo[0][2]+jogo[1][1]+jogo[2][0]
    if row1 == 3 or row2 == 3 or row3 == 3:
        if row1 == 3:
            bt1.config(bg = '#55C1E5', text = "X")
            bt2.config(bg = '#55C1E5', text = "X")
            bt3.config(bg = '#55C1E5', text = "X")
        elif row2 == 3:
            bt4.config(bg = '#55C1E5', text = "X")
            bt5.config(bg = '#55C1E5', text = "X")
            bt6.config(bg = '#55C1E5', text = "X")
        elif row3 == 3:
            bt7.config(bg = '#55C1E5', text = "X")
            bt8.config(bg = '#55C1E5', text = "X")
            bt9.config(bg = '#55C1E5', text = "X")
        messagebox.showinfo("Winner", "X Won!")
        disable_buttons()
        winner = True
        game_counts += 1
        x_score += 1
        update_scores()
    elif row1 == -3 or row2 == -3 or row3 == -3:
        if row1 == -3:
            bt1.config(bg = '#B0FF54', text = "O")
            bt2.config(bg = '#B0FF54', text = "O")
            bt3.config(bg = '#B0FF54', text = "O")
        elif row2 == -3:
            bt4.config(bg = '#B0FF54', text = "O")
            bt5.config(bg = '#B0FF54', text = "O")
            bt6.config(bg = '#B0FF54', text = "O")
        elif row3 == -3:
            bt7.config(bg = '#B0FF54', text = "O")
            bt8.config(bg = '#B0FF54', text = "O")
            bt9.config(bg = '#B0FF54', text = "O")
        messagebox.showinfo("Winner", "O Won!")
        disable_buttons()
        winner = True
        game_counts += 1
        o_score += 1
        update_scores()
    # Checking the columns
    elif col1 == 3 or col2 == 3 or col3 == 3:
        if col1 == 3:
            bt1.config(bg = "#55C1E5", text = "X")
            bt4.config(bg = "#55C1E5", text = "X")
            bt7.config(bg = "#55C1E5", text = "X")
        elif col2 == 3:
            bt2.config(bg = "#55C1E5", text = "X")
            bt5.config(bg = "#55C1E5", text = "X")
            bt8.config(bg = "#55C1E5", text = "X")
        elif col3 == 3:
            bt9.config(bg = "#55C1E5", text = "X")
            bt6.config(bg = "#55C1E5", text = "X")
            bt9.config(bg = "#55C1E5", text = "X")
        messagebox.showinfo("Winner", "X Won!")
        disable_buttons()
        winner = True
        game_counts += 1
        x_score += 1
        update_scores()        
    elif col1 == -3 or col2 == -3 or col3 == -3:
        if col1 == -3:
            bt1.config(bg = '#B0FF54', text = "O")
            bt4.config(bg = '#B0FF54', text = "O")
            bt7.config(bg = '#B0FF54', text = "O")
        elif col2 == -3:
            bt2.config(bg = '#B0FF54', text = "O")
            bt5.config(bg = '#B0FF54', text = "O")
            bt8.config(bg = '#B0FF54', text = "O")
        elif col3 == -3:
            bt9.config(bg = '#B0FF54', text = "O")
            bt6.config(bg = '#B0FF54', text = "O")
            bt9.config(bg = '#B0FF54', text = "O")
        messagebox.showinfo("Winner", "O Won!")
        disable_buttons()
        winner = True
        game_counts += 1
        o_score += 1
        update_scores()
    # Checking the diagonals
    elif diag1 == 3 or diag2 == 3:
        if diag1 == 3:
            bt1.config(bg = "#55C1E5", text = "X")
            bt5.config(bg = "#55C1E5", text = "X")
            bt9.config(bg = "#55C1E5", text = "X")
        elif diag2 == 3:
            bt3.config(bg = "#55C1E5", text = "X")
            bt5.config(bg = "#55C1E5", text = "X")
            bt7.config(bg = "#55C1E5", text = "X")
        messagebox.showinfo("Winner", "X Won!")
        disable_buttons()
        winner = True
        game_counts += 1
        x_score += 1
        update_scores()
    elif diag1 == -3 or diag2 == -3:
        if diag1 == -3:
            bt1.config(bg = "#B0FF54", text = "O")
            bt5.config(bg = "#B0FF54", text = "O")
            bt9.config(bg = "#B0FF54", text = "O")
        elif diag2 == -3:
            bt3.config(bg = "#B0FF54", text = "O")
            bt5.config(bg = "#B0FF54", text = "O")
            bt7.config(bg = "#B0FF54", text = "O")
        messagebox.showinfo("Winner", "O Won!")
        disable_buttons()
        winner = True
        game_counts += 1
        o_score += 1
        update_scores()
    if count == 9 and winner == False:
        bt1.config(bg = "#F9FAD6")
        bt2.config(bg = "#F9FAD6")
        bt3.config(bg = "#F9FAD6")
        bt4.config(bg = "#F9FAD6")
        bt5.config(bg = "#F9FAD6")
        bt6.config(bg = "#F9FAD6")
        bt7.config(bg = "#F9FAD6")
        bt8.config(bg = "#F9FAD6")
        bt9.config(bg = "#F9FAD6")     
        messagebox.showinfo("Draw", "Draw!")
        disable_buttons()
        game_counts += 1
        draw_score += 1
        update_scores()
        


# entrada de dados text
#vnome = Entry(tictactoe)
#vnome.place(x=100, y=70, width=300, height=30)
def reset_game():
    global bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9, clicked, count, winner
    clicked = True
    count = 0
    winner = False
    game_score()
    bt1 = Button(tictactoe, height = 3, width = 7, text=' ', command=(lambda: botao(bt1)))
    bt2 = Button(tictactoe, height = 3, width = 7, text=' ', command=(lambda: botao(bt2)))
    bt3 = Button(tictactoe, height = 3, width = 7, text=' ', command=(lambda: botao(bt3)))

    bt4 = Button(tictactoe, height = 3, width = 7, text=' ', command=(lambda: botao(bt4)))
    bt5 = Button(tictactoe, height = 3, width = 7, text=' ', command=(lambda: botao(bt5)))
    bt6 = Button(tictactoe, height = 3, width = 7, text=' ', command=(lambda: botao(bt6)))

    bt7 = Button(tictactoe, height = 3, width = 7, text=' ', command=(lambda: botao(bt7)))
    bt8 = Button(tictactoe, height = 3, width = 7, text=' ', command=(lambda: botao(bt8)))
    bt9 = Button(tictactoe, height = 3, width = 7, text=' ', command=(lambda: botao(bt9)))

    bt1.grid(row=1, column=0, padx= 0, pady=0)
    bt2.grid(row=1, column=1, padx= 0, pady=0)
    bt3.grid(row=1, column=2, padx= 0, pady=0)

    bt4.grid(row=2, column=0, padx= 0, pady=0)
    bt5.grid(row=2, column=1, padx= 0, pady=0)
    bt6.grid(row=2, column=2, padx= 0, pady=0)

    bt7.grid(row=3, column=0, padx= 0, pady=0)
    bt8.grid(row=3, column=1, padx= 0, pady=0)
    bt9.grid(row=3, column=2, padx= 0, pady=0)

# Creating a menu
menu = Menu(tictactoe)
tictactoe.config(menu=menu)

# Creating a submenu
submenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Options", menu=submenu)
submenu.add_command(label="New Game", command=reset_game)
submenu.add_command(label="Reset Scores", command=reset_scores)


reset_game()

tictactoe.mainloop()