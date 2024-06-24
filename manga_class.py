# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class for manga downlaoding
# HEADERS ================================================================
import os
import requests
from typing import List

# ========================================================================
# CLASSES
# ========================================================================

class MangaPannel:
	def __init__(self, pannel_link: str) -> None:
		self._pannel_link: str = pannel_link
		self._downloaded: bool = False
	
	def __str__(self)->None:
		return f"status: {self._downloaded}\t{self._pannel_link}"
	
	def download_pannel(
		self,
		file_name:str = "manga_pannel.png",
		file_path:str = ""
		)->None:

		file_path = f"00_Scraped/{file_path}{file_name}"

		try:
			response = requests.get(self._pannel_link, timeout = 60)
			open(file_path, 'wb').write(response.content)
		except Exception as e:
			print(e)
		else:
			print("download success")
			self._downloaded = True
	
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

	def __str__(self)->None:
		retval:str = f"{self._chapter_title}:{self._chapter_link}"
		retval = retval + ("-"*50)
		for elements in self._pannels:
			retval = retval + str(elements)
		retval = retval + ("-"*50)

		return retval
	
	# Core Functions -----------------------------------------------------

	def create_folder(self, manga_title:str = "manga_title")->None:
		try:
			path = fr"00_Scraped/{manga_title}/{self._chapter_title}"
			if os.path.exists(path) == False:
				os.makedirs(path)
		except Exception as e:
			print(e)
		else:
			self._chapter_folder_created = True
	
	def add_pannel(self, pannel_link:str)->None:
		self._pannels.append(MangaPannel(pannel_link))

	def get_pannel_links()->None:
		pass
		
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

	def __str__(self)->None:
		retval:str = f"{self._manga_title}:{self._manga_link}"
		retval = retval + ("="*50)

		for elements in self._chapters:
			retval = retval + str(elements)

		retval = retval + ("="*50)

		return retval

	# Core Functions -----------------------------------------------------
	
	def create_folder(self)->None:
		try:
			path = fr"00_Scraped/{self._manga_title}"
			if os.path.exists(path) == False:
				os.makedirs(path)
		except Exception as e:
			print(e)
		else:
			self._manga_folder_created = True

	def add_chapter(self, chapter_link, chapter_title)->None:
		self._chapters.append(MangaChapter(chapter_link, chapter_title))
	
	def get_chapter_links()->None:
		pass

	