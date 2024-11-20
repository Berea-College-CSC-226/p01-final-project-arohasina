#################################################################################
# Author: Arohasina Ravoahanginiaina
# Username: aro
#
# Assignment: HW05
# Purpose: Test suite to test the ask_question function in chapter_6_1_6_5_function.py
# Google Doc Link: https://docs.google.com/document/d/1xaYR5Rd44RI8u7r9cWetyFPGFR50NzTNq2Mo8KA2wO4/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
from inspect import getframeinfo, stack
from chapter_6_1_6_5_function import ask_question


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


def chapter_6_1_6_5_function_suite():
    """
    this function test the ask_question() function.
    :return: none
    """
    unittest(ask_question("B") == True) #test the right answer
    unittest(ask_question("A") == False) #test the wrong answer
    unittest(ask_question("C") == False) #test the wrong answer
    unittest(ask_question("D") == False) #test the wrong answer

    unittest(ask_question("E")== False) #right type of data, but not a possible answer
    unittest(ask_question("F") == False) #right type of data, but not a possible answer

    unittest(ask_question("0.1") == False)  # test wrong type of data
    unittest(ask_question("888") == False)  # test wrong type of data





