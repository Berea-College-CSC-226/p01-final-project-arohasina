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
#chat GPT for: encoding='utf-8' which allows the letter like "é" and "è" to display properly
#chat GPT for the method:
# for widget in self.screen.winfo_children():
#        widget.destroy()
#winfo_children() is a method that returns a list of all the child widgets of a particular widget
#https://stackoverflow.com/questions/10158552/how-to-use-an-image-for-the-background-in-tkinter
#Photo by Tim Gouw on Unsplash
#################################################################################
import json
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage


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


class FlashcardApp:
    def __init__(self, screen, dictionary):
        self.screen = screen
        self.screen.title("French Flashcards")
        self.dictionary = dictionary
        self.current_index = 0
        self.word_keys = list(self.dictionary.flashcard_data.keys())


        self.show_homepage()

    def show_homepage(self):
        for widget in self.screen.winfo_children():
            widget.destroy()

        # Load background image
        self.background_image = PhotoImage(
            file=r"C:\Users\ravoahanginiainaa\PycharmProjects\p01-final-project-arohasina\bg_pic.gif")
        # Create a label with the background image
        self.background_label = tk.Label(self.screen, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Show the homepage
        self.homepage = Homepage(self.screen, self.start_flashcard)


    def start_flashcard(self):
        # Clear the frame but not the background canvas
        for widget in self.screen.winfo_children():
            widget.destroy()

        # Load background image
        self.background_image = PhotoImage(
            file=r"C:\Users\ravoahanginiainaa\PycharmProjects\p01-final-project-arohasina\bg_pic.gif")
        # Create a label with the background image
        self.background_label = tk.Label(self.screen, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Flashcard Display
        self.flashcard_frame = tk.Frame(self.screen)
        self.flashcard_frame.pack(pady=30, expand=True)

        self.word_label = tk.Label(self.flashcard_frame, text="", font=("Arial", 24))
        self.translation_label = tk.Label(self.flashcard_frame, text="", font=("Arial", 18), fg="blue")
        self.example_label = tk.Label(self.flashcard_frame, text="", font=("Arial", 16), wraplength=400, justify="center")
        self.word_label.pack()
        self.translation_label.pack()
        self.example_label.pack()

        # Navigation Buttons
        self.navigation_frame = tk.Frame(self.screen)
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
            self.translation_label.config(text="Translation: " + flashcard.translation)
            self.example_label.config(text="Example: " + flashcard.example_sentence)
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


class Homepage:
    def __init__(self, screen, start_flashcard):
        self.screen = screen
        self.start_flashcard= start_flashcard

        # Home Page Title
        title_label = tk.Label(self.screen, text="Welcome to Level Up Your French", font=("Arial", 24, "bold"))
        title_label.pack(pady=50)

        # Home Page Buttons
        start_button = tk.Button(self.screen, text="Start Flashcards", font=("Arial", 16), command=self.start_flashcard)
        start_button.pack(pady=30)

        exit_button = tk.Button(self.screen, text="Exit", font=("Arial", 16), command=self.screen.quit)
        exit_button.pack(pady=30)


