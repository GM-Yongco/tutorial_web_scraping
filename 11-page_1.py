# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: to tetst if I can download a page with just get_html
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
	# check if references folder exists
	path = "00_REFERENCES/"
	if(os.path.exists(path) == False):
		os.makedirs(path)

	# checking and creation of text file
	path = path + file_name
	if(os.path.exists(path) == False):
		the_file = open(path, "x")
		the_file.close

	# writing in the text file
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
	link1 = "https://housekinokunimanga.com/manga/houseki-no-kuni-chapter-15/"
	
	html:str = get_html(link1)
	write(html)

if __name__ == '__main__':
	separator("START")
	main()
	separator("END")