# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
# HEADERS ================================================================

import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen, urlretrieve

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def separator(x:str = "SECTION") -> None:
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

def decorator_start_end(func):
	def wrapper():
		separator(f"START\t: {func.__name__}")
		func()
		separator(f"END\t: {func.__name__}")
	return wrapper

# ========================================================================
# FUNCTIONS TEST
# ========================================================================

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
# FUNCTIONS SCRAPE IMG
# ========================================================================

@decorator_start_end
def download_img(
		url:str = "https://xfs-n18.xfspp.com/comic/5003/962/628073bbfe272d6dc98e8269/15928920_1444_2048_1035819.jpeg", 
		file_name:str = "a.png"
	) -> None:
	# check if scraped folder exists
	path = "00_Scraped/"
	if(os.path.exists(path) == False):
		os.makedirs(path)

	path = "00_Scraped/" + file_name
	try:
		urlretrieve(url, path)
	except Exception as e:
		print(e)

# ========================================================================
# FUNCTIONS SCRAPE HTML
# ========================================================================

@decorator_start_end
def get_html_urllib(url:str = "https://chihuahuaspin.com/")->str:
	request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
	page = urlopen(request_site)

	html = (page.read().decode(("utf-8")))
	html = str(html.encode('utf-8'))

	return html

@decorator_start_end
def get_html_request(url:str = "https://chihuahuaspin.com/")->bs:
	response:requests = requests.get(url)
	soup:bs = bs(response.text, 'html.parser')
	return soup

@decorator_start_end
def get_html_selenium(THE_URL):
	driver = webdriver.Chrome()
	driver.get(THE_URL)
	wait_seconds:int = 30
	driver.implicitly_wait(wait_seconds)
	page_source = driver.page_source
	driver.quit()

	soup:bs = bs(page_source, "html.parser")

	return soup