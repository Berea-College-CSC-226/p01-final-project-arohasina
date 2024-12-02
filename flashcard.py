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
#
#
#################################################################################
import json
import pygame
import tkinter as tk
from tkinter import messagebox
#from pygame.examples.audiocapture import audio

# Initialize pygame mixer
#pygame.mixer.init()

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


# class Audio:
#     def __init__(self, audio_file=""):
#         """Single audio file for the whole chapter"""
#         self.audio_file = audio_file
#
#     def play(self):
#         """Plays the entire audio file"""
#         try:
#             pygame.mixer.music.load(self.audio_file)
#             pygame.mixer.music.play()
#             # Wait until the audio is finished playing
#             while pygame.mixer.music.get_busy():
#                 pygame.time.Clock().tick(10)  # Wait for the music to finish playing
#         except Exception as e:
#             print(f"Error playing audio: {e}")

class Flashcard:
    def __init__(self, word_key, dictionary):
        word_data = dictionary.flashcard_data.get(word_key, {})
        self.word = word_key
        self.translation = word_data.get("french", "Translation not available")
        self.example_sentence = word_data.get("sentence", "Example sentence not available")

    def display_word(self):
        return self.word

    def display_translation(self):
        return self.translation

    def display_example_sentence(self):
        return self.example_sentence

    def display_flashcard(self):
        return ("Word: {}\n"
                "French Translation: {}\n"
                "Example Sentence: {}").format(self.word, self.translation, self.example_sentence)

# Flashcard Interface
class FlashcardApp:
    def __init__(self, root, dictionary):
        self.root = root
        self.root.title("French Flashcards")
        self.dictionary = dictionary
        # self.audio = audio
        self.current_index = 0
        self.word_keys = list(self.dictionary.flashcard_data.keys())
        # Audio Buttons
        # self.audio_frame = tk.Frame(root)
        # self.audio_frame.pack(pady=10)
        # self.play_button = tk.Button(self.audio_frame, text="Play Audio", command=self.audio.play)
        # self.stop_button = tk.Button(self.audio_frame, text="Stop Audio", command=self.audio.stop)
        # self.play_button.pack(side=tk.LEFT, padx=5)
        # self.stop_button.pack(side=tk.LEFT, padx=5)

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
        if 0 <= index < len(self.word_keys):
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

dictionary = Dictionary("files/chapter_1_words.json")
#chapter_audio = Audio("audio/chapter0.mp3")

# Create the main Tkinter window
root = tk.Tk()
app = FlashcardApp(root, dictionary)
root.mainloop()

#d= Dictionary("files/chapter_1_words.json")
# print(d.flashcard_data['my name is...']['french'])

# d= Dictionary("files/chapter_1_words.json")
# f= Flashcard("my name is...", d)
# print(f.display_flashcard())

# chapterzero= Audio("audio/chapter0.mp3")
# chapterzero.play()
