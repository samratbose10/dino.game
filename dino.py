import tkinter as tk
import random
import time
from PIL import Image, ImageTk

def determine_winner(player_choice, dino_choice):
    if player_choice == dino_choice:
        return "Tie"
    elif (player_choice == "Rock" and dino_choice == "Scissors") or \
         (player_choice == "Paper" and dino_choice == "Rock") or \
         (player_choice == "Scissors" and dino_choice == "Paper"):
        return "Player wins!"
    else:
        return "Dino wins!"

def play(player_choice):
    result_label.config(text="Dino is thinking...", fg="blue")
    root.update()
    time.sleep(2) 

    dino_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(player_choice, dino_choice)
    
    result_label.config(text=f"Player chose: {player_choice}\nDino chose: {dino_choice}\nResult: {result}", fg="green")
    
    new_game_button.pack(pady=10)

def new_game():
    result_label.config(text="")
    new_game_button.pack_forget()

def create_button(text, command):
    return tk.Button(buttons_frame, text=text, command=command, font=("Helvetica", 14), 
                     bg="#add8e6", fg="black", activebackground="#87CEEB", relief="raised", bd=5)

root = tk.Tk()
root.title("Rock Paper Scissors Game")

root.geometry("500x500")
root.configure(bg="#ffe5b4")

image_path = "C:/Users/Lenovo/Desktop/dino/dino.game/dino.png"  
dino_img = Image.open(image_path)
dino_img = dino_img.resize((100, 100), Image.LANCZOS)
dino_photo = ImageTk.PhotoImage(dino_img)
tk.Label(root, image=dino_photo, bg="#ffe5b4").pack(pady=20)

tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 16), bg="#ffe5b4").pack(pady=10)

buttons_frame = tk.Frame(root, bg="#ffe5b4")
buttons_frame.pack(pady=10)

create_button("Rock", lambda: play("Rock")).pack(side=tk.LEFT, padx=15)
create_button("Paper", lambda: play("Paper")).pack(side=tk.LEFT, padx=15)
create_button("Scissors", lambda: play("Scissors")).pack(side=tk.LEFT, padx=15)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#ffe5b4")
result_label.pack(pady=20)

new_game_button = tk.Button(root, text="New Game", command=new_game, font=("Helvetica", 14), 
                            bg="#4CAF50", fg="white", activebackground="#45a049", relief="raised", bd=5)

root.mainloop()
