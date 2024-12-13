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
#background Photo by Tim Gouw on Unsplash.com
#Some French vocabulary and phrases were sourced from the book at:
# https://www.laits.utexas.edu/fi/
#################################################################################
import json
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from quiz import*


class Dictionary:
    """
    Loads the dictionary data from a JSON file.
    """
    def __init__(self, filename):
        """
        Initializes the dictionary by loading data from a JSON file.

        :param filename: The path to the JSON file containing flashcard data.
        """
        try:
            self.file_content = open(filename, 'r', encoding='utf-8')
            self.flashcard_data = json.load(self.file_content)
        except Exception as e:
            self.flashcard_data = {}
            print("Error loading dictionary: {}".format(e))
        finally:
            self.file_content.close()



class Flashcard:
    """
    Create a flashcard with a word, its translation, and example sentence.
    """
    def __init__(self, word_key, dictionary):
        """
        Initializes the flashcard with word data from the dictionary.

        :param word_key: The key representing the word in the dictionary.
        :param dictionary: The dictionary object containing the flashcard data.
        """
        word_data = dictionary.flashcard_data.get(word_key, {})
        self.word = word_key
        self.translation = word_data.get("french", "Translation not available")
        self.example_sentence = word_data.get("sentence", "Example sentence not available")



class FlashcardApp:
    """
    Main application for displaying flashcards and navigating between them.
    """
    def __init__(self, screen, dictionary):
        """
        Initializes the flashcard application.

        :param screen: The Tkinter window where the flashcards will be displayed.
        :param dictionary: The dictionary object containing flashcard data.
        """
        self.screen = screen
        self.screen.title("Level Up Your French")
        self.screen.resizable(False, False)  # Disable window resizing
        self.dictionary = dictionary
        self.current_index = 0
        self.word_keys = list(self.dictionary.flashcard_data.keys())
        self.quiz_page = QuizPage(self.screen, self)
        self.start_quiz_instance = Quiz(self.screen, self.dictionary, self)

        self.show_homepage()


    def show_homepage(self):
        """
        Displays the homepage with the option to start learning or take a quiz.
        """
        # Clear the frame
        for widget in self.screen.winfo_children():
            widget.destroy()

        # Load background image
        self.background_image = PhotoImage(
            file="image/bg_pic.gif")
        # Create a label with the background image
        self.background_label = tk.Label(self.screen, image=self.background_image)
        self.background_label.place(x=0, y=0)

        # Show the homepage
        self.homepage = Homepage(self.screen, self.start_flashcard, self.start_quiz)


    def start_flashcard(self):
        """
        Starts the flashcard mode and displays the first flashcard.
        """
        # Reset the flashcard index
        self.current_index = 0

        # Clear the frame
        for widget in self.screen.winfo_children():
            widget.destroy()

        # Load background image
        self.background_image = PhotoImage(
            file="image/bg_pic.gif")

        # Create a label with the background image
        self.background_label = tk.Label(self.screen, image=self.background_image)
        self.background_label.place(x=0, y=0)

        # Flashcard Display
        self.flashcard_frame = tk.Frame(self.screen, bg="light yellow")
        self.flashcard_frame.place(x=200, y=100)

        self.word_label = tk.Label(self.flashcard_frame, text="", font=("Helvetica", 26), bg="light yellow", fg="coral2")
        self.translation_label = tk.Label(self.flashcard_frame, text="", font=("Helvetica", 18), bg="light yellow")
        self.example_label = tk.Label(self.flashcard_frame, text="", font=("Helvetica", 18), bg="light yellow",
                                      wraplength=400, justify="center")

        #pack flashcard info inside the flashcard frame
        self.word_label.pack()
        self.translation_label.pack()
        self.example_label.pack()

        #place navigation buttons
        self.prev_button = tk.Button(self.screen, text="Previous",bg="IndianRed1",fg="white",
                                     font=("Helvetica", 14), command=self.show_previous_card)
        self.next_button = tk.Button(self.screen, text="    Next    ", bg="IndianRed1",fg="white",
                                     font=("Helvetica", 14), command=self.show_next_card)
        self.prev_button.place(x=270, y=350)
        self.next_button.place(x=370, y=350)

        # Load the first flashcard
        self.show_flashcard(self.current_index)


    def show_flashcard(self, index):
        """
        Displays the flashcard at the given index.

        :param index: The index of the flashcard to display.
        """
        if 0 <= index < len(self.word_keys):  # Valid index check
            word_key = self.word_keys[index]
            flashcard = Flashcard(word_key, self.dictionary)
            self.word_label.config(text="\n"+flashcard.word)
            self.translation_label.config(text="  \nIn French: " + flashcard.translation+"  ")
            self.example_label.config(text="  Example: " + flashcard.example_sentence+"  \n"+"\n")

            # button to go to the quiz directly
            quiz_button = tk.Button(self.screen, text="Take the Quiz", bg="dark sea green",fg="white", font=("Helvetica", 13),
                                    command=self.start_quiz)
            quiz_button.place(x=580, y=450)

            # button to go to the homepage directly
            go_homepage_button = tk.Button(self.screen, text="Back to Homepage", bg="dark sea green",fg="white", font=("Helvetica", 13),
                                           command=self.show_homepage)
            go_homepage_button.place(x=10, y=450)
        else:
            self.show_quizPage() #when all the flashcards have been shown


    def show_next_card(self):
        """
        Show the next flashcard.
        """
        if self.current_index < len(self.word_keys) - 1:
            self.current_index += 1
            self.show_flashcard(self.current_index)
        else:
            self.show_quizPage() #when all the flashcards have been shown


    def show_previous_card(self):
        """
        Show the previous flashcard.
        """
        if self.current_index > 0:
            self.current_index -= 1
            self.show_flashcard(self.current_index)
        else:
            messagebox.showinfo("Info", "This is the first flashcard!")


    def start_quiz(self):
        """
        This method is called when the start quiz button is clicked.
        """
        self.start_quiz_instance.start_quiz()


    def show_quizPage(self):
        """
        Displays the quiz page.
        """
        self.quiz_page.show_quizPage()



class Homepage:
    """
    Displays the homepage with buttons to start flashcards or take a quiz.
    """
    def __init__(self, screen, start_flashcard,start_quiz):
        """
        Initializes the homepage with buttons for flashcards and quizzes.

        :param screen: The Tkinter window for displaying the homepage.
        :param start_flashcard: The method to start flashcards when clicked.
        :param start_quiz: The method to start the quiz when clicked.
        """
        self.screen = screen
        self.start_flashcard= start_flashcard
        self.start_quiz = start_quiz

        # Home Page Title
        title_label = tk.Label(self.screen, text="  Welcome to\nLevel Up Your French!  ", bg="light yellow",fg="dark sea green",
                               font=("Helvetica", 30, "italic"), wraplength=500, justify="center")
        title_label.place(x=150, y=140)

        # Home Page Buttons
        start_button = tk.Button(self.screen, text="  Start Learning  ", bg="dark sea green",fg="white",
                                 font=("Helvetica", 16), command=self.start_flashcard)
        start_button.place(x=265, y=260)

        # button to start the quiz directly
        quiz_button = tk.Button(self.screen, text="  Take the Quiz  ", bg="dark sea green",fg="white", font=("Helvetica", 16),
                                command=self.start_quiz)
        quiz_button.place(x=265, y=320)



class QuizPage:
    """
    Displays the quiz page and manages quiz interactions.
    """
    def __init__(self, screen,flashcard_app):
        """
        Initializes the quiz page with the flashcard app.

        :param screen: The Tkinter window to display the quiz page.
        :param flashcard_app: The main flashcard application instance.
        """
        self.flashcard_app = flashcard_app
        self.screen= screen
        self.dictionary = flashcard_app.dictionary


    def show_quizPage(self):
        """
        Displays the quiz page.
        """
        for widget in self.screen.winfo_children():
            widget.destroy()

        # Load background image
        self.background_image = PhotoImage(
            file="image/quiz_page_bg.gif")

        # Create a label with the background image
        self.background_label = tk.Label(self.screen, image=self.background_image)
        self.background_label.place(x=0, y=0)

        # quiz Page Title
        title_label = tk.Label(self.screen, text="You have learned all the words\nfor this chapter",
                               bg="light coral", fg="white",
                               font=("Helvetica", 24, "italic", "bold"))
        title_label.place(x=100, y=150)

        # start quizz button for quiz page
        start_quiz_button = tk.Button(self.screen, text="Take the quiz", bg="dark sea green",fg="white",
                                      font=("Helvetica", 16), command=self.start_quiz)
        start_quiz_button.place(x=280, y=250)

        # Back to Homepage button
        back_button = tk.Button(self.screen, text="Back to Homepage", font=("Helvetica", 16), command=self.show_homepage)
        back_button.place(x=253, y=300)


    def show_homepage(self):
        """
        Navigates back to the homepage when clicked
        """
        self.flashcard_app.show_homepage()


    def start_quiz(self):
        """
        Starts the quiz when clicked.
        """
        self.flashcard_app.start_quiz()





