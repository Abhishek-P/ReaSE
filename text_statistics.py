class Text_Stats:
"""class for evaluating the text based on multiple paramters
 and calculating the necesaary indices	"""
	def __init__( self, text ):
	"""There is a single argument a string of texts.
	The constructor initializes the instance variable self.text
	It also calls instance methods to generate the basic necessary text stat parameters"""
	self.text = text
	