# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to 
# HEADERS ================================================================
import os
import urllib.request as req
from typing import List

# ========================================================================
# CLASSES
# ========================================================================

class MangaPannel:
	def __init__(self, pannel_link: str) -> None:
		self._pannel_link: str = pannel_link
		self._downloaded: bool = False

	def download(
		self,
		file_name:str = "manga_pannel.png",
		file_path:str = "00_Scraped/"
		)->None:

		try:
			req.urlretrieve(self._pannel_link, f"{file_path}{file_name}")
		except Exception as e:
			print(e)
		else:
			self._downloaded = True
	
	def __str__(self):
		return f"status: {self._downloaded}\t{self._pannel_link}"


# ========================================================================
class MangaChapter:
	def __init__(self, 
		chapter_link:str = "0",
		chapter_title:str = "chapter_title"
		)-> None:

		self._chapter_link:str = chapter_link
		self._chapter_title:str = chapter_title
		self._chapter_folder_created:bool = False
		self._pannels:List[MangaPannel] = []

	def add_pannel(self, pannel_link:str):
		self._pannels.append(MangaPannel(pannel_link))
	
	def create_folder(self, manga_title:str = "manga_title"):
		try:
			path = fr"00_Scraped/{manga_title}/{self._chapter_title}"
			if os.path.exists(path) == False:
				os.makedirs(path)
		except Exception as e:
			print(e)
		else:
			self._chapter_folder_created = True
		
	def __str__(self):
		retval:str = f"{self._chapter_title}:{self._chapter_link}"
		retval = retval + ("-"*50)

		for elements in self._pannels:
			retval = retval + str(elements)

		retval = retval + ("-"*50)

		return retval

# ========================================================================
class MangaDetails:
	def __init__(self, 
		manga_link:str = "0",
		manga_title:str = "manga_title"
		)-> None:

		self._manga_link:str = manga_link
		self._manga_title:str = manga_title
		self._manga_folder_created:bool = False
		self._chapters:List[MangaChapter] = []

	def add_chapter(self, chapter_link, chapter_title):
		self._manga_chapters.append(MangaChapter(chapter_link, chapter_title))

	def create_folder(self):
		try:
			path = fr"00_Scraped/{self._manga_title}"
			if os.path.exists(path) == False:
				os.makedirs(path)
		except Exception as e:
			print(e)
		else:
			self._manga_folder_created = True

	def __str__(self):
		retval:str = f"{self._manga_title}:{self._manga_link}"
		retval = retval + ("="*50)

		for elements in self._chapters:
			retval = retval + str(elements)

		retval = retval + ("="*50)

		return retval