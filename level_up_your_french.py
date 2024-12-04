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
from flashcard import *
from quiz import *

class MainProgram:
    def __init__(self):
        """
        MainProgram class for handling the program logic.
        """
        # Load dictionary and start application
        self.dictionary = Dictionary("files/chapter_1_words.json")

        # Create the main Tkinter window
        self.root = tk.Tk()
        self.app = FlashcardApp(self.root, self.dictionary)

    def run(self):
        self.root.mainloop()

def main():
    """
    Starts the Level Up Your French program.

    :return: None
    """
    program= MainProgram()
    program.run()


if __name__ == "__main__":
    main()