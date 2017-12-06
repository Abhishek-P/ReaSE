"""
@author: Abhishek P
text_statistics:
input -  text
generates : all the necessary text statistics
    * Sentence Count
    * Word Count
    * Letter Count
    * Syllable Count
    * Complex words

    Average Sentence Length = Word Count/Sentence Count
    Average Word Length = Letter Count/ Word Count
    Average Syllables per word =  Total Syallable Count
    Complex Words = Syllables Count > 3


Steps:
1. Sentence Tokenization -  Sentence Count
2. Word Tokenization -  Word Count
3. Syllable Count -  Complex Words

Hierarchy:
Text:
    List of Sentences

Sentences:
    List of Words

Word:
    List of letters
    > Syllable Count
    """
import nltk
import time
import sylco
import scores
import os

punctuations = {".", "!", "\"", "\'", ",", ":", ";"}


class Word(str):
    """
    Word class -
    > word - string of the word
    > letter_count
    > syllable_count"""

    def __init__(self, word, sentence_index, word_index):
        super(Word, self).__init__(word)
        self.word = word
        del word
        del sentence_index
        del word_index
        self.letter_count = len(self.word)
        self.syllable_count = sylco.get_syllable_count(self.word)



class Sentence:
    """
    Sentence class-
    > words - tuple of Word objects
    > length - len(words)
    > complex_words

    !get_words -  generates a list of Word objects from the sentence and sets the length
    !count_complex_words - counts the no of words with syllable_count greater than 2"""

    def __init__(self, sentence):
        self.value = sentence
        self.words = None
        self.letter_count = 0
        self.complex_words = 0
        self.syllable_count = 0
        self.word_count = 0
        self.get_words()

    def get_words(self):
        pass

    def process_raw(self, words_raw):
        for word_raw in words_raw:
            if word_raw in punctuations:
                continue
            self.process_word(word_raw)

    def process_word(self, word_raw):
        word = Word(word_raw, )
        self.words.append(word)
        self.process_stats(self, word)

    def process_stats(self,word):
        self.complex_words += (1 * (word.syllable_count >= 3))
        self.syllable_count += word.syllable_count
        self.letter_count += len(word)
        self.word_count += 1


    def substitute_word(self, word_no, new_word_raw):
        old_word = self.words[word_no]
        self.complex_words -= (1 * (old_word.syllable_count >= 3))
        self.syllable_count -= old_word.syllable_count
        self.letter_count -= len(old_word)
        self.word_count -= 1
        new_word = Word(new_word_raw)
        self.words[word_no] = new_word
        self.process_stats(new_word)







class Text:
    """
    Text class -
    > sentences - Tuple of sentence objects
    > sentence_count
    > word_count
    > letter_count
    > syllable count
    > complex_words
    >indices - dictionary of indices

    ! get_sentences - returns a tuple of sentence objects
    ! generate_indices"""

    def __init__(self, text):
        self.text = text
        del (text)
        self.sentences = None
        self.sentence_count = 0
        self.word_count = 0
        self.letter_count = 0
        self.complex_words = 0
        self.syllable_count = 0
        self.get_sentences(self.text)
        self.stats = dict()
        self.populate_stats()

    def get_sentences(self, text):
        self.sentences = []
        sentences_raw = nltk.tokenize.sent_tokenize(text)
        for sentence_raw in sentences_raw:
            sentence = Sentence(sentence_raw, self.sentence_count)
            self.sentences.append(sentence)
            self.sentence_count += 1
            self.process_new_sentence_stats(sentence)

    def process_new_sentence_stats(self, sentence):
        self.word_count += sentence.word_count
        self.letter_count += sentence.letter_count
        self.complex_words += sentence.complex_words
        self.syllable_count += sentence.syllable_count

    def populate_stats(self):
        self.stats["letter_count"] = self.letter_count
        self.stats["word_count"] = self.word_count
        self.stats["syllable_count"] = self.syllable_count
        self.stats["complex_words"] = self.complex_words
        self.stats["sentence_count"] = self.sentence_count
        self.stats["words_per_sentence"] = self.word_count / self.sentence_count
        self.stats["syllables_per_word"] = self.syllable_count / self.word_count
        self.stats["fk_index"] = scores.flesch_kincaid_score()
        self.stats["dc_index"] = scores.dale_chall_score(self.stats)
        self.stats["gf_index"] = scores.gunning_fog_score(self.stats)
        self.stats["cl_index"] = scores.coleman_liau_score(self.stats)
        self.stats["as_index"] = scores.automated_score(self.stats)

    def substitute_word(self, sentence_no, word_no, new_word_raw):
        sentence = self.sentences[sentence_no]
        self.word_count -= sentence.word_count
        self.letter_count -= sentence.letter_count
        self.complex_words -= sentence.complex_words
        self.syllable_count -= sentence.syllable_count
        sentence.substitute_word(word_no, new_word_raw)







if __name__ == "__main__":
    text_sample = """Perhaps the greatest faculty our minds possess is the ability to cope with pain.\
     Classic thinking teaches us of the four doors of the mind, which everyone moves through according\
     to their need.First is the door of sleep. Sleep offers us a retreat from the world and all its pain.\
     Sleep marks passing time, giving us distance from the things that have hurt us.\
     When a person is wounded they will often fall unconscious.\
     Similarly, someone who hears traumatic news will often swoon or faint.\
     This is the mind's way of protecting itself from pain by stepping through the first door.\
     Second is the door of forgetting. Some wounds are too deep to heal, or too deep to heal quickly.\
     In addition, many memories are simply painful, and there is no healing to be done.\
     The saying "time heals all wounds" is false. Time heals most wounds. The rest are hidden behind this door.\
     Third is the door of madness. There are times when the mind is dealt such a blow it hides itself in insanity.\
     While this may not seem beneficial, it is. There are times when reality is nothing but pain,\
     and to escape that pain the mind must leave reality behind.\
     Last is the door of death. The final resort. Nothing can hurt us after we are dead, or so we have been told."""
    text = Text(text_sample)
    print text.sentence_count
    print text.word_count
    print text.letter_count
    print text.word_count
    print text.sentence_count
    print text.complex_words
    print text.syllable_count