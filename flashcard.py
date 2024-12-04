#################################################################################
# Author: Arohasina Ravohanginiaina
# Username: Arohasina
#
# Assignment: p01
# Purpose: Interactive learning flashcards and quizzes for users to study French vocabulary.
#
# Google Doc Link: https://docs.google.com/document/d/1jGpdXDdU7qafmN9_lEAigKttqIAKwALNgQ69IkVdbLk/edit?tab=t.0
#
#################################################################################
# Acknowledgements:
#chat GPT for encoding='utf-8'
#chat GPT for the method for widget in self.root.winfo_children():
#        widget.destroy()
#################################################################################
import json
import tkinter as tk
from tkinter import messagebox


class Dictionary:
    def __init__(self, filename):
        try:
            self.file_content = open(filename, 'r', encoding='utf-8')
            self.flashcard_data = json.load(self.file_content)
        except Exception as e:
            self.flashcard_data = {}
            print(f"Error loading dictionary: {e}")
        finally:
            self.file_content.close()


class Flashcard:
    def __init__(self, word_key, dictionary):
        word_data = dictionary.flashcard_data.get(word_key, {})
        self.word = word_key
        self.translation = word_data.get("french", "Translation not available")
        self.example_sentence = word_data.get("sentence", "Example sentence not available")

    def display_flashcard(self):
        return ("Word: {}\n"
                "French Translation: {}\n"
                "Example Sentence: {}").format(self.word, self.translation, self.example_sentence)

# Flashcard Interface

class Homepage:
    def __init__(self, root, start_flashcard):
        self.root = root
        self.start_flashcard= start_flashcard

        # Home Page Title
        title_label = tk.Label(self.root, text="Welcome to Level Up Your French", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Home Page Buttons
        start_button = tk.Button(self.root, text="Start Flashcards", font=("Arial", 16), command=self.start_flashcard)
        start_button.pack(pady=10)

        exit_button = tk.Button(self.root, text="Exit", font=("Arial", 16), command=self.root.quit)
        exit_button.pack(pady=10)

class FlashcardApp:
    def __init__(self, root, dictionary):
        self.root = root
        self.root.title("French Flashcards")
        self.dictionary = dictionary
        self.current_index = 0
        self.word_keys = list(self.dictionary.flashcard_data.keys())

        self.show_homepage()

    def show_homepage(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Show the homepage
        self.homepage = Homepage(self.root, self.start_flashcard)

    def start_flashcard(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Flashcard Display
        self.flashcard_frame = tk.Frame(root)
        self.flashcard_frame.pack(pady=20)

        self.word_label = tk.Label(self.flashcard_frame, text="", font=("Arial", 24))
        self.translation_label = tk.Label(self.flashcard_frame, text="", font=("Arial", 18), fg="blue")
        self.example_label = tk.Label(self.flashcard_frame, text="", font=("Arial", 16), wraplength=400, justify="center")
        self.word_label.pack()
        self.translation_label.pack()
        self.example_label.pack()

        # Navigation Buttons
        self.navigation_frame = tk.Frame(root)
        self.navigation_frame.pack(pady=10)

        self.prev_button = tk.Button(self.navigation_frame, text="Previous", command=self.show_previous_card)
        self.next_button = tk.Button(self.navigation_frame, text="Next", command=self.show_next_card)
        self.prev_button.pack(side=tk.LEFT, padx=5)
        self.next_button.pack(side=tk.LEFT, padx=5)

        # Load the first flashcard
        self.show_flashcard(0)


    def show_flashcard(self, index):
        """Display the flashcard at the given index."""
        if 0 <= index < len(self.word_keys):  # Valid index check
            word_key = self.word_keys[index]
            flashcard = Flashcard(word_key, self.dictionary)
            self.word_label.config(text=flashcard.word)
            self.translation_label.config(text=f"Translation: {flashcard.translation}")
            self.example_label.config(text=f"Example: {flashcard.example_sentence}")
        else:
            messagebox.showinfo("Info", "No more flashcards!")

    def show_next_card(self):
        """Show the next flashcard."""
        if self.current_index < len(self.word_keys) - 1:
            self.current_index += 1
            self.show_flashcard(self.current_index)
        else:
            messagebox.showinfo("Info", "This is the last flashcard!")

    def show_previous_card(self):
        """Show the previous flashcard."""
        if self.current_index > 0:
            self.current_index -= 1
            self.show_flashcard(self.current_index)
        else:
            messagebox.showinfo("Info", "This is the first flashcard!")


# Load dictionary and start application
dictionary = Dictionary("files/chapter_1_words.json")

# Create the main Tkinter window
root = tk.Tk()
app = FlashcardApp(root, dictionary)
root.mainloop()