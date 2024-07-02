# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: A template class to 
# HEADERS ================================================================

from typing import List
from manga_class import *

from bs4 import BeautifulSoup as bs
import requests

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def separator(x:str = "SECTION") -> None:
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

# ========================================================================
# GLOBAL
# ========================================================================

DYNASTY_LINK:str = "https://dynasty-scans.com"

# ========================================================================
# CLASSES
# ========================================================================

class DynastyMangaChapter(MangaChapter):

	def get_pannel_links(self)->None:
		# getting html of the chapter
		response:requests = requests.get(self._chapter_link)
		soup:bs = bs(response.text , 'html.parser')

		# getting page links
		nav_div:bs = soup.find("div", class_= fr"pages-list")
		nav_a_list:List[bs] = nav_div.find_all("a", class_="page")

		# getting image prefix
		img_link_suffxies:List[str] = []
		for a in nav_a_list:
			img_link_suffxies.append(a.get_text())

		# getting image prefix
		images:List[bs] = soup.find_all('img')
		images_link:str = (images[1]).get('src')
		portions:List[str] = images_link.split("/")
		del portions[0]
		del portions[-1]

		img_link_prefix:str = DYNASTY_LINK + '/'
		for p in portions:
			img_link_prefix  = img_link_prefix + p + '/'

		# getting the image pannel links / mixing prefix and suffix
		for s in img_link_suffxies:
			self.add_pannel(f"{img_link_prefix}{s}.webp")

		separator("GOT PANNEL LINKS")

# ========================================================================
class DynastyMangaDetails(MangaDetails):
	def get_chapter_links()->None:
		pass

# ========================================================================
# MAIN
# ========================================================================

if __name__ == '__main__':
	separator("START")

	manga_link:str = "https://dynasty-scans.com/series/the_guy_she_was_interested_in_wasnt_a_guy_at_all"
	manga_title:str = "The Guy She Was Interested in Wasn't a Guy At All"
	manga: DynastyMangaDetails = DynastyMangaDetails(manga_link = manga_link, manga_title = manga_title)

	chapter_link = "https://dynasty-scans.com/chapters/the_guy_she_was_interested_in_wasnt_a_guy_at_all_ch00"
	chapter: DynastyMangaChapter = DynastyMangaChapter(chapter_link)

	chapter.create_folder()

	separator("END")