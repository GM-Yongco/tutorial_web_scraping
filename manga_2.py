# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to 
# HEADERS ================================================================

from manga_class import *

import requests
from bs4 import BeautifulSoup as bs

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def separator(x:str = "SECTION") -> None:
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

# ========================================================================
# GLOBAL
# ========================================================================

DYNASTY_LINK:str = "https://dynasty-scans.com/"

# ========================================================================
# CLASSES
# ========================================================================

class DynastyMangaChapter(MangaChapter):

	def get_pannel_links(self)->None:
		response: requests.Response = requests.get(self._chapter_link)
		soup: bs = bs(response.text, 'html.parser')

		img_src = DYNASTY_LINK + soup.find_all('img')[1].get('src')
		self.add_pannel(img_src)
		
		separator("GOT PANNEL LINKS")

	def download_pannels(self)->None:
		for pannels in self._pannels:
			pannels.download_pannel()
		
		separator("CHAPTER DOWNLOADED")		

# ========================================================================
# MAIN
# ========================================================================

if __name__ == '__main__':
	separator("START")

	chapter_link = "https://dynasty-scans.com/chapters/the_guy_she_was_interested_in_wasnt_a_guy_at_all_ch01"
	chapter: DynastyMangaChapter = DynastyMangaChapter(chapter_link)

	chapter.get_pannel_links()
	chapter.download_pannels()

	separator("END")