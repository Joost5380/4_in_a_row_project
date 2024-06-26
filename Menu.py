import tkinter as tk
from PIL import Image, ImageTk
from Game_with_AI import Game_with_AI
from Game_without_AI import Game_without_AI
from Random_AI import Random_AI_AI
from AI_Tegen_RandomAI import Ai_Tegen_RandomAI
from MINIMAX_tegen_MINIMAX import MINIMAX_tegen_MINIMAX
from MINIMAX_Pruning_tegen_MINIMAX import MINIMAX_tegen_MINIMAXPRUNING

def start_game_with_ai():
    root.destroy()
    Game_with_AI()

def start_game_without_ai():
    root.destroy()
    Game_without_AI()

def start_game_versus_random_AI():
    root.destroy()
    Random_AI_AI()

def start_Ai_Tegen_RandomAI():
    root.destroy()
    Ai_Tegen_RandomAI()

def start_MINIMAX_tegen_MINIMAX():
    root.destroy()
    MINIMAX_tegen_MINIMAX()

def start_MINIMAX_tegen_MINIMAXPRUNING():
    root.destroy()
    MINIMAX_tegen_MINIMAXPRUNING()

root = tk.Tk()
root.title("Selecteer Spelmodus")

# Venstergrootte vergroot
window_size = 900
root.geometry(f"{window_size}x{window_size}")
root.configure(bg='white')

# Laad en pas de achtergrondafbeelding aan
background_image = Image.open('Connect_4.webp')
original_width, original_height = background_image.size
new_width = window_size - 40
new_height = int((original_height / original_width) * new_width)

if new_height > window_size - 350:
    new_height = window_size - 350
    new_width = int((original_width / original_height) * new_height)

background_image = background_image.resize((new_width, new_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo, bg='white')
background_label.place(x=(window_size - new_width) // 2, y=60, width=new_width, height=new_height)

label = tk.Label(root, text="Kies of je tegen een AI wilt spelen of tegen elkaar", font=("Aptos", 26), bg='white', fg='black', pady=10)
label.pack(side='top', pady=20)

button_y1 = window_size - 240
button_y2 = window_size - 140

button_style = {
    'font': ("Aptos", 18),
    'width': 22,
    'height': 2,
    'bg': 'lightgrey',
    'fg': 'black',
    'relief': 'raised',
    'borderwidth': 3
}

button_pvp = tk.Button(root, text="Tegen elkaar", command=start_game_without_ai, **button_style)
button_pvp.place(relx=0.15, y=button_y1, anchor='center')

button_minimax = tk.Button(root, text="Tegen AI", command=start_game_with_ai, **button_style)
button_minimax.place(relx=0.5, y=button_y1, anchor='center')

button_random_ai = tk.Button(root, text="Tegen random AI", command=start_game_versus_random_AI, **button_style)
button_random_ai.place(relx=0.85, y=button_y1, anchor='center')

button_ai = tk.Button(root, text="MINIMAX tegne MINIMAX AI", command=start_MINIMAX_tegen_MINIMAX, **button_style)
button_ai.place(relx=0.15, y=button_y2, anchor='center')

button_ai_vs_random = tk.Button(root, text="Ai tegen random AI", command=start_Ai_Tegen_RandomAI, **button_style)
button_ai_vs_random.place(relx=0.5, y=button_y2, anchor='center')

button_minimax_pruning = tk.Button(root, text="MINIMAX Pruning tegen MINIMAX", command=start_MINIMAX_tegen_MINIMAXPRUNING, **button_style)
button_minimax_pruning.place(relx=0.85, y=button_y2, anchor='center')

root.mainloop()
