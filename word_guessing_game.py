import tkinter as tk
from tkinter import messagebox
import random


word_bank = ['love', 'happiness', 'friendship', 'kindness', 'joyful', 'compassion', 'grace', 'serenity', 'bliss', 'affection']
word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 10

def check_guess():
    global attempts
    guess = entry_guess.get().lower().strip()
    entry_guess.delete(0, tk.END)

    if not guess or len(guess) != 1:
        messagebox.showinfo("💌 Oops!", "Please enter a single letter, cutie 💕")
        return

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        label_message.config(text="🌸 Excellent Guess, Babes!")
    else:
        attempts -= 1
        label_message.config(text=f"💔 Wrong Guess! Attempts Left: {attempts}")

    # Update displayed word
    label_word.config(text=" ".join(guessedWord))

    # Check win/lose
    if "_" not in guessedWord:
        messagebox.showinfo("🎀 Yay!", f"Congratulations Babes!! You guessed the word: {word} 💖")
        reset_game()
    elif attempts == 0:
        messagebox.showinfo("💀 Oh no!", f"Game Over! The word was: {word}")
        reset_game()

def reset_game():
    global word, guessedWord, attempts
    word = random.choice(word_bank)
    guessedWord = ['_'] * len(word)
    attempts = 10
    label_word.config(text=" ".join(guessedWord))
    label_message.config(text="💞 New game started! Guess a letter, babes!")

# GUI Setup
root = tk.Tk()
root.title("💖 Word Guess Game ")
root.geometry("420x360")
root.resizable(False, False)
root.configure(bg="#ffe6f2")  # soft pastel pink background

# Title
title_label = tk.Label(
    root,
    text="💋 Word Guess Game 💋",
    font=("Comic Sans MS", 20, "bold"),
    bg="#ffe6f2",
    fg="#ff66b3"
)
title_label.pack(pady=10)

# Cute subtitle
subtitle = tk.Label(
    root,
    text="✨ Guess the secret word before you run out of hearts! ✨",
    font=("Comic Sans MS", 10),
    bg="#ffe6f2",
    fg="#b56576"
)
subtitle.pack()

# Current word display
label_word = tk.Label(
    root,
    text=" ".join(guessedWord),
    font=("Courier", 26, "bold"),
    bg="#ffe6f2",
    fg="#ff3385"
)
label_word.pack(pady=15)

# Entry field
entry_guess = tk.Entry(
    root,
    font=("Comic Sans MS", 16),
    width=4,
    justify='center',
    bg="#fff0f5",
    fg="#ff1493",
    relief="flat",
    highlightbackground="#ffb6c1",
    highlightthickness=2
)
entry_guess.pack(pady=8)

# Guess button
btn_guess = tk.Button(
    root,
    text="💌 Guess!",
    font=("Comic Sans MS", 12, "bold"),
    bg="#ffb6c1",
    fg="white",
    relief="flat",
    width=10,
    command=check_guess,
    activebackground="#ff69b4"
)
btn_guess.pack(pady=5)

# Message area
label_message = tk.Label(
    root,
    text="💞 Guess a letter to start the magic 💞",
    font=("Comic Sans MS", 11),
    bg="#ffe6f2",
    fg="#b56576"
)
label_message.pack(pady=10)

# Reset button
btn_reset = tk.Button(
    root,
    text="🔄 New Game",
    font=("Comic Sans MS", 10, "bold"),
    bg="#ffccd5",
    fg="#5e1742",
    relief="flat",
    command=reset_game,
    activebackground="#f48fb1"
)
btn_reset.pack(pady=5)

# Footer
footer = tk.Label(
    root,
    text="made with 💖 by Fatima",
    font=("Comic Sans MS", 8),
    bg="#ffe6f2",
    fg="#a05278"
)
footer.pack(side="bottom", pady=8)

root.mainloop()
