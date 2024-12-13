#################################################################################
# Author: Cody Bandy
# Username: bandyc
#
# Assignment: HW05
# Purpose: Ask the user a multiple choice question about functions and provide feedback based on the answer.
# Google Doc Link: https://docs.google.com/document/d/1xaYR5Rd44RI8u7r9cWetyFPGFR50NzTNq2Mo8KA2wO4/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


def ask_question(test_input=None):
    """
    Function that asks a multiple choice question and allows the user to input an answer. Provides a print statement based on the user's input and returns True or False.
    :param test_input: Optional parameter for test input instead of user input.
    :return: True or False
    """
    if test_input is None:     #if this is a non-test environment, run the function as normal, asking for user input
        print("\nWhich of the following functions is NOT a fruitful function?")     # the multiple choice question, with answers on separate lines
        print("A) A function that returns the length of a string.")
        print("B) A function that prints a welcome message to the user.")
        print("C) A function that returns a new string with vowels removed.")
        print("D) A function that returns the square of a number.")
        answer = input("\nPlease pick an answer (A, B, C, D).\n").upper()     # asks the user for an input, converts it to uppercase automatically
    else:     # otherwise, this is a test environment
        answer = test_input.upper()  # use test_input when running tests

    if answer == "B":      # if input is B returns True, also if it was user input return a print message saying correct answer
        if test_input is None:
            print("Correct! This function does not return a value, it just prints a message.")
        return True
    elif answer == "A" or answer == "C" or answer == "D":     # if input is A, C, or D returns False, also if it was user input return a print message saying incorrect answer
        if test_input is None:
            print("Incorrect. This function returns a value.")
        return False
    else:      # if input is something unexpected returns False, also if it was user input return a print message explaining the answer is invalid
        if test_input is None:
            print("Invalid. Please choose A, B, C, or D.")
        return False

def main():
    """
    Calls the function that asks the multiple choice question.
    :return: None
    """
    ask_question()     # call to the function to ask the question

if __name__ == "__main__":      # ensures it only runs when the program is run, and not in the test suite
    main()