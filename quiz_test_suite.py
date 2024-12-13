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
from inspect import getframeinfo, stack
from quiz import *


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


def quiz_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the quiz() class.

    :return: None
    """
    #dictionary of flashcard data
    flashcard_data = {
        "apple": {"french": "pomme"},
        "dog": {"french": "chien"},
        "cat": {"french": "chat"}
    }

   # flashcard and flashcard_app for testing
    class Flashcard:
        def __init__(self):
            self.flashcard_data = flashcard_data

    class MockFlashcardApp:
        def show_homepage(self):
            pass

    screen = tk.Tk()
    screen.geometry("600x400")

    flashcard_app = MockFlashcardApp()
    dictionary = Flashcard()

    quiz = Quiz(screen, dictionary, flashcard_app)

    # Test 1: Check initial score
    unittest(quiz.score == 0)

    # Test 2: Check total questions
    unittest(quiz.total_questions == len(flashcard_data))

    # Test 3: Check word_keys is correctly initialized
    unittest(quiz.word_keys == list(flashcard_data.keys()))

    # Test 4: Check generate_quiz method
    word_key, correct_answer, answer_choices = quiz.generate_quiz(0)
    unittest(word_key == "apple")
    unittest(correct_answer == "pomme")
    unittest(len(answer_choices) == 3)

    # Test 5: test when user submit correct answer
    quiz.answer_var.set("pomme")
    quiz.check_answer("pomme")
    unittest(quiz.score == 1)  # Score should increase after a correct answer

    # Test 6: test when user submit incorrect answer
    quiz.answer_var.set("chien")
    quiz.check_answer("pomme")
    unittest(quiz.score == 1)  # Score should remain the same after incorrect answer

    # Test 7: Check if the quiz progresses to the next question
    current_index_before = quiz.current_index
    quiz.next_question()
    unittest(quiz.current_index == current_index_before + 1)

    # Test 8: Test final score display
    quiz.current_index = quiz.total_questions - 1
    quiz.show_final_score()
    unittest(quiz.score == 1)

    print("All tests complete.")


def main():
    """
    start the quiz test suite
    :return: none
    """
    quiz_suite()

if __name__ == "__main__":
    main()
