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
from flashcard import *
import random
import tkinter as tk
from tkinter import messagebox


class Quiz:
    def __init__(self,screen, dictionary, flashcard_app):
        """
        Initializes a Quiz instance.

        :param screen: The tkinter screen on which the quiz will be displayed.
        :param dictionary: The flashcard data dictionary containing words and their French translations.
        :param flashcard_app: The parent flashcard application instance for navigation.
        """
        self.screen = screen
        self.dictionary = dictionary
        self.flashcard_app = flashcard_app
        self.word_keys = list(self.dictionary.flashcard_data.keys())
        self.total_questions = len(self.word_keys)
        self.current_index = 0
        self.score = 0
        self.answer_var = tk.StringVar()  # Variable to hold selected answer


    def start_quiz(self):
        """
        Starts the quiz by displaying the first question.
        """
        self.display(self.current_index)


    def display(self, index):
        """
        Display the question and multiple-choice options.

        :param index: The index of the current question to be displayed.
        """
        #clear the screen
        for widget in self.screen.winfo_children():
            widget.destroy()

        # Load background image
        self.background_image = PhotoImage(file="image/bg_pic.gif")
        # Create a label with the background image
        self.background_label = tk.Label(self.screen, image=self.background_image)
        self.background_label.place(x=0, y=0)

        # Generate the quiz question, correct answer, and possible answer choices
        word_key, correct_answer, answer_choices = self.generate_quiz(index)

        # Display the question
        question_text = "In French, how do we say: '{}'?".format(word_key)
        question_label = tk.Label(self.screen, text=question_text, font=("Helvetica", 20), fg="firebrick4")
        question_label.place(x=70, y=150)

        # Reset the answer variable
        self.answer_var.set(None)

        # Base position for the answer choices
        base_x = 100
        base_y = 200
        y_gap = 40  # Vertical gap between each choice

        # Display answer choices as radio buttons
        index = 0  #index counter
        for choice in answer_choices:
            choice_button = tk.Radiobutton(
                self.screen,
                text=choice,
                variable=self.answer_var,
                value=choice,
                font=("Helvetica", 20),
            )
            choice_button.place(x=base_x, y=base_y + index * y_gap)
            index += 1  # Increment index

        #function for the submit button
        def submit_answer():
            self.check_answer(correct_answer)

        # Submit button
        submit_button = tk.Button(
            self.screen, text="Submit", font=("Helvetica", 16), bg="dark sea green",
            command=submit_answer
        )
        submit_button.place(x=base_x, y=base_y +12 + index * y_gap)

        # back to Homepage button
        homepage_button= tk.Button(self.screen, text="Back to Homepage", font=("Helvetica", 16),command=self.go_to_Homepage)
        homepage_button.place(x=base_x, y=base_y + 70 + index * y_gap)


    def generate_quiz(self, index):
        """
        Generate a question with multiple-choice answers.

        :param index: The index of the current question.
        :return: A tuple containing the word_key, correct_answer, and answer_choices.
        """
        if 0 <= index < len(self.word_keys): # Valid index check
            word_key = self.word_keys[index]
            word_data = self.dictionary.flashcard_data.get(word_key, {})

            # Get the correct answer (French translation)
            correct_answer = word_data.get("french", "")

            # Generate a list of answer choices
            answer_choices = [correct_answer]

            # get other random French words
            for key in self.word_keys:
                word_data = self.dictionary.flashcard_data.get(key, {})
                french_translation = word_data.get("french", "")

                # Add to answer choices if it's not the correct answer
                if french_translation != correct_answer:
                    answer_choices.append(french_translation)

            # Limit the answer choices to 3 options
            random.shuffle(answer_choices)
            answer_choices = answer_choices[:3]  # 3 random choices

            # Ensure the correct answer is in the choices
            if correct_answer not in answer_choices:
                answer_choices.append(correct_answer)
                random.shuffle(answer_choices)

            return word_key, correct_answer, answer_choices


    def check_answer(self, correct_answer):
        """
        Compares the user’s answer to the correct answer, returning True if correct, otherwise False.

        :param correct_answer: The correct French translation for the word being asked.
        """
        user_answer = self.answer_var.get()

        if user_answer == correct_answer:
            self.score += 1  # Increase score if correct
            messagebox.showinfo("Correct", "Well done! Your answer is correct.")
        else:
            messagebox.showinfo("Incorrect", "Oops! That's not correct. The right answer is: {}".format(correct_answer))

        # Move to next question or finish quiz
        self.next_question()


    def next_question(self):
        """
        Move to the next question in the quiz
        """
        self.current_index += 1
        if self.current_index < self.total_questions:
            self.display(self.current_index)  # Show the next question
        else:
            self.show_final_score()


    def show_final_score(self):
        """
        Display the final score directly on the screen.
        """
        # Clear the screen for the final score
        for widget in self.screen.winfo_children():
            widget.destroy()

        # Load background image
        self.background_image = PhotoImage(
            file="image/quiz_page_bg.gif")
        # Create a label with the background image
        self.background_label = tk.Label(self.screen, image=self.background_image)
        self.background_label.place(x=0, y=0)

        # Display the final score message
        final_score_text = "Your score is {} out of {}".format(self.score, self.total_questions)
        final_score_label = tk.Label(self.screen, text=final_score_text, font=("Helvetica", 24), bg="IndianRed1",fg="white")
        final_score_label.place(x=100, y=150)  # You can adjust x and y for positioning

        #buttons for retaking the quiz
        retake_button = tk.Button(self.screen, text="Retake Quiz", font=("Helvetica", 14),bg="dark sea green",fg="white",
                                   command=self.retake_quiz)
        retake_button.place(x=100, y=200)

        #button for going back to Homepage
        homepage_button = tk.Button(self.screen, text="Back to Homepage", font=("Helvetica", 14),
                                    bg="dark sea green",fg="white", command=self.go_to_Homepage)
        homepage_button.place(x=250, y=200)


    def retake_quiz(self):
        """
        Reset the quiz and start again.
        """
        self.word_keys = list(self.dictionary.flashcard_data.keys())  # Refresh keys
        self.current_index = 0
        self.score = 0
        self.display(self.current_index)  # Start from the first question


    def go_to_Homepage(self):
        """
        Go back to the Homepage.
        """
        self.word_keys = list(self.dictionary.flashcard_data.keys())  # Refresh keys
        self.current_index = 0
        self.score = 0
        self.flashcard_app.show_homepage()