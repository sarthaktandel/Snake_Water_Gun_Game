import tkinter as tk
import random

def play(choice):
    # Game logic
    computer = random.choice([-1, 0, 1])
    youDict = {'🐍': 1, '💧': -1, '🔫': 0}
    reverseDict = {1: "🐍 Snake", -1: "💧 Water", 0: "🔫 Gun"}
    
    you = youDict[choice]
    
    result_text = f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}\n"
    
    if computer == you:
        result_text += "It's a draw 🤝"
    elif (computer == -1 and you == 1):
        result_text += "You win! 🎉"
    elif (computer == -1 and you == 0):
        result_text += "You lose! 😢"
    elif (computer == 1 and you == -1):
        result_text += "You lose! 😢"
    elif (computer == 1 and you == 0):
        result_text += "You win! 🎉"
    elif (computer == 0 and you == -1):
        result_text += "You win! 🎉"
    elif (computer == 0 and you == 1):
        result_text += "You lose! 😢"
    else:
        result_text += "Something went wrong!"
    
    result_label.config(text=result_text)

# Set up the main window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

# Create styled buttons for the user's choices
snake_button = tk.Button(button_frame, text="🐍", font=("Helvetica", 24), command=lambda: play('🐍'), bg="#ffcccb", fg="#333", bd=0, activebackground="#ff9999")
snake_button.grid(row=0, column=0, padx=10, pady=10)

water_button = tk.Button(button_frame, text="💧", font=("Helvetica", 24), command=lambda: play('💧'), bg="#b3e6ff", fg="#333", bd=0, activebackground="#80d4ff")
water_button.grid(row=0, column=1, padx=10, pady=10)

gun_button = tk.Button(button_frame, text="🔫", font=("Helvetica", 24), command=lambda: play('🔫'), bg="#d9b3ff", fg="#333", bd=0, activebackground="#c480ff")
gun_button.grid(row=0, column=2, padx=10, pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0")
result_label.pack(pady=20)

# Run the application
root.mainloop()