import tkinter as tk
from PIL import Image, ImageTk
from Game_with_AI import Game_with_AI
from Game_without_AI import Game_without_AI
from Random_AI import Random_AI_AI
def start_game_with_ai():
    root.destroy()
    Game_with_AI()

def start_game_without_ai():
    root.destroy()
    Game_without_AI()

def start_game_versus_random_AI():
    root.destroy()
    Random_AI_AI()

root = tk.Tk()
root.title("Selecteer Spelmodus")

window_size = 600
root.geometry(f"{window_size}x{window_size}")
root.configure(bg='white')

background_image = Image.open('Connect_4.webp')
original_width, original_height = background_image.size
new_width = window_size - 40
new_height = int((original_height / original_width) * new_width)

if new_height > window_size - 160:
    new_height = window_size - 160
    new_width = int((original_width / original_height) * new_height)

background_image = background_image.resize((new_width, new_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo, bg='white')
background_label.place(x=(window_size - new_width) // 2, y=60, width=new_width, height=new_height)

label = tk.Label(root, text="Kies of je tegen een AI wilt spelen of tegen elkaar", font=("Aptos", 18), bg='white', fg='black', pady=10)
label.pack(side='top', pady=10)

button_y = window_size - 60

button_style = {
    'font': ("Aptos", 14),
    'width': 15,
    'height': 2,
    'bg': 'lightgrey',
    'fg': 'black',
    'relief': 'raised',
    'borderwidth': 2
}

button_ai = tk.Button(root, text="Tegen AI", command=start_game_with_ai, **button_style)
button_ai.place(relx=0.15, y=button_y, anchor='center')

button_ai = tk.Button(root, text="Tegen random AI", command=start_game_with_ai, **button_style)
button_ai.place(relx=0.4, y=button_y, anchor='center')

button_ai = tk.Button(root, text="Ai tegen random AI", command=start_game_versus_random_AI, **button_style)
button_ai.place(relx=0.6, y=button_y, anchor='center')

button_pvp = tk.Button(root, text="Tegen elkaar", command=start_game_without_ai, **button_style)
button_pvp.place(relx=0.85, y=button_y, anchor='center')

root.mainloop()
