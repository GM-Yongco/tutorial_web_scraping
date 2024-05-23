# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
# HEADERS ================================================================

import os
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen, urlretrieve

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def separator(x:str = "SECTION") -> None:
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

def write(content:str = "test", file_name:str = "a.txt") -> None:
	path = "00_REFERENCES/" + file_name

	# checking anc creation
	if(os.path.exists(path) == False):
		the_file = open(path, "x")
		the_file.close

	# writing
	the_file = open(path, "w")
	the_file.write(str(content))
	the_file.close

# ========================================================================
# FUNCTIONS SCRAPE
# ========================================================================

def get_html(url:str = "https://chihuahuaspin.com/"):
	request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
	page = urlopen(request_site)

	html = (page.read().decode(("utf-8")))
	html = str(html.encode('utf-8'))

	return html

# ========================================================================
# MAIN 
# ========================================================================

def main():
	# getting the raw html ===============================================
	DYNASTY = "https://dynasty-scans.com"
	title = "the_guy_she_was_interested_in_wasnt_a_guy_at_all"
	link = DYNASTY + "/series/" + title

	html = get_html(link)
	# write(html)

	# filter for chapter links ===========================================
	chapter_links:list = []
	
	for element in bs(html, "html.parser").find_all("dd"):
		chapter_links.append(DYNASTY + element.find("a").get("href"))
	
	# write_links = ""
	# for link in chapter_links:
	# 	write_links = write_links + link + "\n"
	# write(write_links)

	# filter for image links from every chapter link =====================
	html = get_html(chapter_links[0])
	write(html)
		



if __name__ == '__main__':
	separator("START")
	main()
	separator("END")