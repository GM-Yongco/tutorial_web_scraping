# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to 
# HEADERS ================================================================
from typing import List

# ========================================================================
# CLASSES
# ========================================================================

class MangaChapterDetails:
	def __init__(self, chapter_link:str = "0"):
		self.chapter_num:float = -1
		self.chapter_link:str = chapter_link
		self.pannel_links:List[str] = []
	
	# getters and setters

	def set_chapter_num(self, chapter_num:int):
		self.chapter_num = chapter_num
	def get_chapter_num(self):
		return self.chapter_num

	def set_chapter_link(self, chapter_link:str):
		self.chapter_link = chapter_link
	def get_chapter_link(self):
		return self.chapter_link

	# core functions

	def add_pannel_link(self, new_pannel_link):
		self.pannel_links.append(new_pannel_link)
	
	def print_attributes(self):
		print(self.chapter_link)
		for elements in self.add_pannel_link:
			print(f"\t{elements}")

# ========================================================================
class MangaDetails:
	def __init__(self, manga_link:str = "0"):
		self.manga_link:str = manga_link
		self.manga_chapters:List[MangaChapterDetails] = []

	# getters and setters

	def set_manga_link(self, manga_link):
		self.manga_link = manga_link
	def get_manga_link(self):
		return self.manga_link

	# core functions

	def add_chapter(self, manga_chapter:MangaChapterDetails):
		self.manga_chapters.append(manga_chapter)

	def print_attributes(self):
		print(self.manga_link)
		for elements in self.manga_chapters:
			print(f"Chapter: {elements.get_chapter_num}")
			elements.print_attributes()