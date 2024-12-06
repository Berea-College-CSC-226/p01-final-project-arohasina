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
from quiz import *


class MainProgram:
    def __init__(self, dictionary):
        """
        MainProgram class for handling the program logic.

        :param dictionary: The Dictionary object containing the French vocabulary data.
        """
        self.dictionary = dictionary

        self.screen = tk.Tk()
        self.screen.geometry("700x500")

        self.app = FlashcardApp(self.screen, self.dictionary)


    def run(self):
        """
        Runs the Tkinter main loop.
        """
        self.screen.mainloop()

def main():
    """
    Starts the Level Up Your French program.
    """
    dictionary = Dictionary("files/chapter_1_words.json")
    program= MainProgram(dictionary)
    program.run()


if __name__ == "__main__":
    main()