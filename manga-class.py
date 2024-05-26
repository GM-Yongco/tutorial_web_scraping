class MangaChapter:
	def __init__(self, chapter_link:str, pannel_links:list):
		"""Initializer (Constructor) method."""
		self.attribute1:str
		self.attribute2:list = []
	
	def add_pannel_link(self):
		"""A simple instance method."""
		return f"Attribute 1 is {self.attribute1}"
	
	def method2(self, value):
		"""Another instance method that modifies an attribute."""
		self.attribute2 = value
		return f"Attribute 2 is now {self.attribute2}"