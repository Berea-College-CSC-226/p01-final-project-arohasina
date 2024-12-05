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
    def __init__(self, dictionary):
        """
        MainProgram class for handling the program logic.
        """
        # Load dictionary and start application
        self.dictionary = dictionary

        # Create the main Tkinter window
        self.screen = tk.Tk()
        self.screen.geometry("700x500")
        self.app = FlashcardApp(self.screen, self.dictionary)


    def run(self):
        self.screen.mainloop()

def main():
    """
    Starts the Level Up Your French program.

    :return: None
    """
    dictionary = Dictionary("files/chapter_1_words.json")
    print(type(dictionary))  # Check the type of dictionary
    print(dictionary.flashcard_data)

    program= MainProgram(dictionary)
    program.run()


if __name__ == "__main__":
    main()