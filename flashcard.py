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
class Dictionary:
    def __init__(self, word, translation, example_sentence):
        pass

class Audio:
    pass

class Flashcard:
    def __init__(self, word, translation, example_sentence=""):
        self.word=word
        self.translation= translation
        self.example_sentence= example_sentence

    def display_word(self):
        return self.word

    def display_translation(self):
        return self.translation

    def display_example_sentence(self):
        return self.example_sentence

    def display(self):
        pass


