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

from inspect import getframeinfo, stack
from flashcard import *


def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def flashcard_suite():
    """
    The test_suite function utilizes the unittest() function,
    and is designed to test the Flashcard, Dictionary, and FlashcardApp classes.

    :return: None
    """

    # Test 1: Testing the Dictionary class loading and content
    print("Test 1: Testing the Dictionary class loading")
    try:
        dictionary = Dictionary("files/chapter_1_words.json")
        unittest(dictionary.flashcard_data)  # Check if data was loaded
    except Exception as e:
        unittest(False)  # If error occurs, the test fails

    # Test 2: Testing the Flashcard class initialization
    print("Test 2: Testing the Flashcard class")
    try:
        dictionary = Dictionary("files/chapter_1_words.json")

        #testing word and its translation
        flashcard = Flashcard("my name is", dictionary)
        unittest(flashcard.word == "my name is" and flashcard.translation == "je m'appelle")

        flashcard = Flashcard("i am from", dictionary) #updating flashcard object
        unittest(flashcard.word == "i am from" and flashcard.translation == "je suis de")

        flashcard = Flashcard("computer science", dictionary) #updating flashcard object
        unittest(flashcard.word == "computer science" and flashcard.translation == "l'informatique")


        # testing word and its example sentence
        flashcard = Flashcard("my name is", dictionary) #updating flashcard object
        unittest(flashcard.word == "my name is" and flashcard.example_sentence == "je m'appelle John")

        flashcard = Flashcard("i am from", dictionary)  # updating flashcard object
        unittest(flashcard.word == "i am from" and flashcard.example_sentence == "je suis de Madagascar")

        flashcard = Flashcard("computer science", dictionary)  # updating flashcard object
        unittest(flashcard.word == "computer science" and flashcard.example_sentence == "J'étudie l'informatique à l'université.")




    except Exception as e:
        unittest(False)  # If error occurs, the test fails


    # Test 3: Testing FlashcardApp's start_flashcard method
    print("Test 4: Testing the start_flashcard() method in FlashcardApp")
    try:
        dictionary = Dictionary("files/chapter_1_words.json")
        screen = tk.Tk()
        app = FlashcardApp(screen, dictionary)
        app.start_flashcard()  # Test if this method works without errors
        unittest(True)  # If no errors occur, the test passes
    except Exception as e:
        unittest(False)  # If error occurs, the test fails


def main():
    """
    start the flashcard test suite
    :return: none
    """
    flashcard_suite()

if __name__ == "__main__":
    main()
