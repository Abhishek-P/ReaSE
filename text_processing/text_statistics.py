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
import os
def syllable_counter(word):
	pass
	
class Word:
	"""
	Word class - 
	> word - string of the word
	> letter_count
	> syllable_count"""
	def __init__(this,word):
		this.word = word
		this.letter_count = len(word)
		this.syllable_count = syllable_counter(word)

class Sentence:
	"""
	Sentence class-
	> words - tuple of Word objects
	> length - len(words)
	> complex_words 
	
	!get_words -  generates a list of Word objects from the sentence and sets the length
	!count_complex_words - counts the no of words with syllable_count greater than 2"""
	
	def __init__(this,sentence):
		this.sentence = this.get_words(sentence)
		this.length = len(sentence)
		this.complex_words = this.count_complex_words()
	
	def get_words(this, sentence):
		pass
	
	def count_complex_words(this):
		pass

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
	! get_word_count
	! get_letter_count
	! get_syllable_count
	! get_complex_words
	! generate_indices"""
	
	def __init__(this, text):
		this.text = text
		this.sentences = this.get_sentences()
		"""this.sentence_count = len(this.sentences)
		this.word_count = this.get_word_count()
		this.letter_count = this.get_letter_count()
		this.syllable_count = this.get_syllable_count()
		this.complex_words = this.get_complex_words()
		this.indices = dict()
		this.generate_indices()"""
	
	def get_sentences(this,text):
		sentences = nltk.tokenize.sent_tokenize(text)
		print sentences
		
	def get_word_count(this):
		pass
		
	def get_letter_count(this):
		pass
	
	def get_syllable_count(this):
		pass
	
	def get_complex_words(this):
		pass
	def generate_indices(this):
		pass
		
if __name__ == "__main__":
	text = Text(open(os.sys.argv[0],"r").read())