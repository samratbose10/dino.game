import tkinter as tk
import random
import time
from PIL import Image, ImageTk
import pygame

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
    result_label.config(text="Rock Paper Scissor...", fg="blue")
    root.update()
    time.sleep(2)  

    dino_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(player_choice, dino_choice)
    
    result_label.config(text=f"Player chose: {player_choice}\nDino chose: {dino_choice}\nResult: {result}", fg="green")
    
    if dino_choice == "Rock":
        dino_img = Image.open(rock_image_path)
    elif dino_choice == "Paper":
        dino_img = Image.open(paper_image_path)
    elif dino_choice == "Scissors":
        dino_img = Image.open(scissors_image_path)
    else:
        dino_img = Image.open(default_image_path)
    
    dino_img = dino_img.resize((100, 100), Image.LANCZOS)
    dino_photo = ImageTk.PhotoImage(dino_img)
    dino_label.config(image=dino_photo)
    dino_label.image = dino_photo

    if result == "Player wins!":
        root.configure(bg="lightgreen")
    elif result == "Dino wins!":
        root.configure(bg="lightcoral")
    else:
        root.configure(bg="lightyellow")

    
    new_game_button.pack(pady=10)

def new_game():
    result_label.config(text="")
    root.configure(bg="#ffe5b4")  
    new_game_button.pack_forget()
    dino_img = Image.open(default_image_path)
    dino_img = dino_img.resize((100, 100), Image.LANCZOS)
    dino_photo = ImageTk.PhotoImage(dino_img)
    dino_label.config(image=dino_photo)
    dino_label.image = dino_photo

def create_button(text, command):
    return tk.Button(buttons_frame, text=text, command=command, font=("Helvetica", 14), 
                     bg="#add8e6", fg="black", activebackground="#87CEEB", relief="raised", bd=5)

def init_music():
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/Lenovo/Desktop/dino/dino.game/background.mp3")  
    pygame.mixer.music.play(-1)  


root = tk.Tk()
root.title("Rock Paper Scissors Game")


root.geometry("500x500")
root.configure(bg="#ffe5b4")


default_image_path = "C:/Users/Lenovo/Desktop/dino/dino.game/dino.png" 
rock_image_path = "C:/Users/Lenovo/Desktop/dino/dino.game/rock-dino.png"  
paper_image_path = "C:/Users/Lenovo/Desktop/dino/dino.game/paper-dino.png" 
scissors_image_path = "C:/Users/Lenovo/Desktop/dino/dino.game/scissors-dino.png" 


dino_img = Image.open(default_image_path)
dino_img = dino_img.resize((100, 100), Image.LANCZOS)
dino_photo = ImageTk.PhotoImage(dino_img)
dino_label = tk.Label(root, image=dino_photo, bg="#ffe5b4")
dino_label.pack(pady=20)

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

init_music()

root.mainloop()
