from tkinter import *
import random


def next_turn(row, column):
    global player

    if matrix[row][column]['text'] == "" and winner_check() is False:

        if player == players[0]:

            matrix[row][column]['text'] = player

            if winner_check() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif winner_check() is True:
                label.config(text=(players[0] + " wins"))

            elif winner_check() == "Tie":
                label.config(text="Tie!")

        else:

            matrix[row][column]['text'] = player

            if winner_check() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif winner_check() is True:
                label.config(text=(players[1] + " wins"))

            elif winner_check() == "Tie":
                label.config(text="Tie!")


def winner_check():
    for row in range(3):
        if matrix[row][0]['text'] == matrix[row][1]['text'] == matrix[row][2]['text'] != "":
            matrix[row][0].config(bg="green")
            matrix[row][1].config(bg="green")
            matrix[row][2].config(bg="green")
            return True

    for column in range(3):
        if matrix[0][column]['text'] == matrix[1][column]['text'] == matrix[2][column]['text'] != "":
            matrix[0][column].config(bg="green")
            matrix[1][column].config(bg="green")
            matrix[2][column].config(bg="green")
            return True

    if matrix[0][0]['text'] == matrix[1][1]['text'] == matrix[2][2]['text'] != "":
        matrix[0][0].config(bg="green")
        matrix[1][1].config(bg="green")
        matrix[2][2].config(bg="green")
        return True

    elif matrix[0][2]['text'] == matrix[1][1]['text'] == matrix[2][0]['text'] != "":
        matrix[0][2].config(bg="green")
        matrix[1][1].config(bg="green")
        matrix[2][0].config(bg="green")
        return True

    elif space_check() is False:

        for row in range(3):
            for column in range(3):
                matrix[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def space_check():
    space = 9

    for row in range(3):
        for column in range(3):
            if matrix[row][column]['text'] != "":
                space -= 1

    if space == 0:
        return False
    else:
        return True


def next_game():
    global player

    player = random.choice(players)

    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            matrix[row][column].config(text="", bg="#F0F0F0")


window = Tk()
window.title("X-O-X GAME")
players = ["x", "o"]
player = random.choice(players)
matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

label = Label(text=player + " turns", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(window, text="reset", font=('consolas', 20), command=next_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        matrix[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                     command=lambda row=row, column=column: next_turn(row, column))
        matrix[row][column].grid(row=row, column=column)

window.mainloop()