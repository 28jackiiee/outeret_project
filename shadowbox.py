import random
import tkinter as tk
from tkinter import messagebox
import time

def shadowboxing():
    wins = [0]
    turn = [0]

    def ai_turn():
        aichoice = random.randint(1, 4)
        if aichoice == 1:
            direction = 'Left'
        elif aichoice == 2:
            direction = 'Right'
        elif aichoice == 3:
            direction = 'Up'
        elif aichoice == 4:
            direction = 'Down'
        ai_label.config(text=f"AI's Turn: {direction}")

        if turn[0] == 0:
            if wins[0] == 1:
                messagebox.showinfo("You Lost", "You lost!")
                root.destroy()
            else:
                wins[0] += 1
        else:
            turn[0] -= 1

    def player_turn():
        direction = direction_var.get()
        timer_label.config(text="Times up")

        if direction == ai_label.cget("text").split()[-1]:
            if turn[0] == 0:
                ai_label.config(text="The AI has guessed your direction. It now has one more try to guess, otherwise you lose.")
                wins[0] += 1
            else:
                ai_label.config(text="You guessed the AI's direction. If you guess again, you win.")
        else:
            if turn[0] == 0:
                ai_label.config(text="It is now your turn")
                turn[0] += 1
            else:
                ai_turn()
        if wins[0] == 1 and turn[0] == 1:
            messagebox.showinfo("You Win!", "You win!")
            root.destroy()

    def start_timer(count):
        timer_label.config(text=str(count))
        if count > 0:
            root.after(1000, start_timer, count - 1)
        else:
            timer_label.config(text="Times up")
            player_turn()

    root = tk.Tk()
    root.title("Shadowboxing Game")

    welcome_label = tk.Label(root, text="Welcome to shadowboxing. The rules are simple. All you have to do is guess a random direction and the AI will also choose a random direction. If the AI guesses wrong, it becomes your turn. If the AI guesses correctly, it goes again. If he guesses right again, you lose.")
    welcome_label.pack(pady=10)

    ai_label = tk.Label(root, text="It is now the AI's turn")
    ai_label.pack(pady=10)

    direction_var = tk.StringVar()
    direction_var.set("Left")
    direction_label = tk.Label(root, text="Please input a direction:")
    direction_label.pack(pady=5)
    direction_entry = tk.Entry(root, textvariable=direction_var)
    direction_entry.pack(pady=5)

    timer_label = tk.Label(root, text="")
    timer_label.pack()

    player_button = tk.Button(root, text="Submit", command=lambda: start_timer(5))
    player_button.pack(pady=10)

    # Adding the canvas for the animated head
    head_image = tk.PhotoImage(file="head.png")
    head_position = [50, 50]

    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack()

    head = canvas.create_image(head_position[0], head_position[1], image=head_image)

    def animate_head():
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        canvas.move(head, dx, dy)

        canvas.after(100, animate_head)

    animate_head()

    root.mainloop()

shadowboxing()
