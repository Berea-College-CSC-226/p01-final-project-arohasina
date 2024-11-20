#################################################################################
# Author: Arohasina Ravohanginiaina
# Username: Arohasina
#
# Assignment: p01
# Purpose: Flashcards project with an interactive learning and quizzes for users to study French vocabulary.
#
# Google Doc Link: https://docs.google.com/document/d/1jGpdXDdU7qafmN9_lEAigKttqIAKwALNgQ69IkVdbLk/edit?tab=t.0
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

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

class Quiz:
    def __init__(self, word, translation,question):
        self.word_translation= Flashcard(word,translation)
        self.question=