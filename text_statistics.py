class Text_Stats:
"""class for evaluating the text based on multiple paramters
 and calculating the necesaary indices	"""
	def __init__( self, text ):
	"""There is a single argument a string of texts.
	The constructor initializes the instance variable self.text
	It also calls instance methods to generate the basic necessary text stat parameters"""
	self.text = text
	
	
	"""The necessary parameters are as listed below
	1.No of Lines
	2.No of Words
	3.No of Characters
	4.No of Syllables
	5.No of Complex Words
	
	The order for calculating the first three is as listed the 4th and 5th have to be calculated together
	
	Other calculatable values needed for The indices are as follows:
	