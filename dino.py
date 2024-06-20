import tkinter as tk
import random
import time

# Function to determine the winner
def determine_winner(player_choice, dino_choice):
    if player_choice == dino_choice:
        return "Tie"
    elif (player_choice == "Rock" and dino_choice == "Scissors") or \
         (player_choice == "Paper" and dino_choice == "Rock") or \
         (player_choice == "Scissors" and dino_choice == "Paper"):
        return "Player wins!"
    else:
        return "Dino wins!"

# Function to handle the player's choice
def play(player_choice):
    result_label.config(text="Dino is thinking...")
    root.update()
    time.sleep(2)  # Simulate the dino thinking

    dino_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(player_choice, dino_choice)
    
    result_label.config(text=f"Player chose: {player_choice}\nDino chose: {dino_choice}\nResult: {result}")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Create and place widgets
tk.Label(root, text="Choose Rock, Paper, or Scissors").pack()

buttons_frame = tk.Frame(root)
buttons_frame.pack()

tk.Button(buttons_frame, text="Rock", command=lambda: play("Rock")).pack(side=tk.LEFT)
tk.Button(buttons_frame, text="Paper", command=lambda: play("Paper")).pack(side=tk.LEFT)
tk.Button(buttons_frame, text="Scissors", command=lambda: play("Scissors")).pack(side=tk.LEFT)

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
