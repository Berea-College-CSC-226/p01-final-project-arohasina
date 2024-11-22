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
import json

class Dictionary:
    def __init__(self, filename):
        try:
            self.file_content = open(filename, 'r')
            self.flashcard_data = json.load(self.file_content)
            print(self.flashcard_data)
        finally:
            self.file_content.close()


class Audio:
    pass

class Flashcard:
    def __init__(self, word_key, dictionary):
        word_data = dictionary.flashcard_data.get(word_key, {})
        self.word = word_key
        self.translation = word_data.get("french", "Translation not available")
        self.example_sentence = word_data.get("sentence", "Example sentence not available")

    def display_word(self):
        return self.word

    def display_translation(self):
        return self.translation

    def display_example_sentence(self):
        return self.example_sentence

    def display(self):
        pass



d= Dictionary("files/chapter_1_words.json")
print(d.flashcard_data['my name is...']['french'])



