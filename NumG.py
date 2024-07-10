import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        self.master.geometry("1366x768")  # Set to average laptop screen size
        self.master.configure(bg='#FFFACD')  # Yellowish background color

        self.max_attempts = 10
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        self.title_label = tk.Label(self.master, text="Welcome to Guess the Number Game!", 
                                    font=('Helvetica', 28, 'bold'), bg='#FFFACD')
        self.title_label.pack(pady=20)

        self.label = tk.Label(self.master, text="Guess a number between 1 and 100:", 
                              font=('Helvetica', 22), bg='#FFFACD')
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.master, font=('Helvetica', 20))
        self.entry.pack(pady=20)

        self.guess_button = tk.Button(self.master, text="Guess", font=('Helvetica', 20), 
                                      bg='blue', fg='white', command=self.check_guess, 
                                      width=12, height=2)
        self.guess_button.pack(pady=20)

        self.result_label = tk.Label(self.master, text="", font=('Helvetica', 20), bg='#FFFACD')
        self.result_label.pack(pady=20)

        self.reset_button = tk.Button(self.master, text="Reset", font=('Helvetica', 20), 
                                      bg='green', fg='white', command=self.reset_game, 
                                      width=12, height=2)
        self.reset_button.pack(pady=20)

        self.attempts_label = tk.Label(self.master, text="", font=('Helvetica', 20), bg='#FFFACD')
        self.attempts_label.pack(pady=20)

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.number_of_attempts = 0
        self.result_label.config(text="")
        self.attempts_label.config(text=f"Attempts left: {self.max_attempts}")
        self.entry.delete(0, tk.END)
        self.entry.focus()
        print(f"Debug: The number to guess is {self.number_to_guess}")  # Debug print for development

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
            return

        self.number_of_attempts += 1
        attempts_left = self.max_attempts - self.number_of_attempts

        if user_guess < self.number_to_guess:
            self.result_label.config(text="Too low! Try again.")
        elif user_guess > self.number_to_guess:
            self.result_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number in {self.number_of_attempts} attempts!")
            self.reset_game()
            return

        if attempts_left > 0:
            self.attempts_label.config(text=f"Attempts left: {attempts_left}")
        else:
            messagebox.showinfo("Game Over", f"You're out of attempts! The number was {self.number_to_guess}.")
            self.reset_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()
