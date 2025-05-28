import tkinter as tk
import random


flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Who killed Itachi Uchiha?", "answer": "No one they all are already in his genjutsu"},
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What color do you get by mixing red and white?", "answer": "Pink"},
    {"question": "What is the opposite of 'cold'?", "answer": "Hot"},
    {"question": "Who's not made a move yet in one peice?", "answer": "Dragon. You swear to a God please made a move bro"},
    {"question": "What do bees make?", "answer": "Honey"},
    {"question": "What is 10 x 2?", "answer": "20"},
    {"question": "How many legs does a spider have?", "answer": "8"},
    {"question": "Which animal is the king of the jungle?", "answer": "Lion"},
    {"question": "What do you drink to stay hydrated?", "answer": "Water"},
    {"question": "Which day comes after Friday?", "answer": "Saturday"},
    {"question": "How many letters are there in the English alphabet?", "answer": "26"},
    {"question": "Which shape has 3 sides?", "answer": "Triangle"},
    {"question": "Which color is a banana?", "answer": "Yellow"},
    {"question": "How many hours are in a day?", "answer": "24"}
]

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flashcard App")
        self.current_card = {}
        self.is_answer = False

        
        self.text = tk.Label(master, text="", font=("Arial", 18), wraplength=300, width=35, height=4, bg="white", relief="solid", bd=1)
        self.text.pack(pady=20)

        self.flip_button = tk.Button(master, text="Flip", command=self.flip)
        self.flip_button.pack(pady=5)

        self.next_button = tk.Button(master, text="Next Card", command=self.next_card)
        self.next_button.pack(pady=5)

      
        self.next_card()

    def next_card(self):
        self.current_card = random.choice(flashcards)
        self.is_answer = False
        self.text.config(text=self.current_card["question"])

    def flip(self):
        if self.is_answer:
            self.text.config(text=self.current_card["question"])
            self.is_answer = False
        else:
            self.text.config(text=self.current_card["answer"])
            self.is_answer = True


if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
