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
	def __init__(self,word):
		self.word = word
		del(word)
		self.letter_count = len(self.word)
		self.syllable_count = syllable_counter(self.word)
	
	
		
class Sentence:
	"""
	Sentence class-
	> words - tuple of Word objects
	> length - len(words)
	> complex_words 
	
	!get_words -  generates a list of Word objects from the sentence and sets the length
	!count_complex_words - counts the no of words with syllable_count greater than 2"""
	
	def __init__(self,sentence):
		self.words= None
		self.get_words(sentence)
		del(sentence)
		self.word_count = len(self.words)
		self.complex_words = self.count_complex_words()
	
	def get_words(self, sentence):
		words_raw = nltk.tokenize.word_tokenize(sentence)
		self.words = []
		for word in words_raw:
			self.words.append(Word(word))
		
	
	def count_complex_words(self):
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
	
	def __init__(self, text):
		self.text = text
		del(text)
		self.sentences = None
		self.get_sentences(self.text)
		self.sentence_count = len(self.sentences)
		self.word_count = 0
		self.calculate_word_count()
		self.letter_count =  0 
		self.calculate_letter_count()
		"""
		self.syllable_count = self.get_syllable_count()
		self.complex_words = self.get_complex_words()
		self.indices = dict()
		self.generate_indices()"""
	
	def get_sentences(self,text):
		self.sentences = []
		sentences_raw = nltk.tokenize.sent_tokenize(text)
		for sentence in sentences_raw:
			self.sentences.append(Sentence(sentence))	
		del(sentence)
		del(sentences_raw)
		
	def calculate_word_count(self):
		for sentence in self.sentences:
			self.word_count += sentence.word_count
		del(sentence)
		
	def calculate_letter_count(self):
		for sentence in self.sentences:
			for word in sentence.words:
				self.letter_count += word.letter_count
		del(word)
		del(sentence)
	
	def get_syllable_count(self):
		pass
	
	def get_complex_words(self):
		pass
	def generate_indices(self):
		pass
		
if __name__ == "__main__":
	text = Text(open(os.sys.argv[1],"r").read())
	print text.sentence_count
	print text.word_count
	print text.letter_count
	