# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: utils for general web scraping
# ========================================================================
# HEADERS
# ========================================================================

import os

import requests as req
from bs4 import BeautifulSoup as bs
	
# ========================================================================
# FUNCTIONS UTIL
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	print("-" * 50)
	print(section_name)
	print("-" * 50)

def write(content:str = "test", file_name:str = "temp.txt") -> None:
	try:
		if not os.path.exists(file_name):
			with open(file_name, "w", encoding="utf-8") as f:
				f.write("")

		# encoding='utf-8' to catch the error with sites that have characters the charmap cant handle
		with open(file_name, "w", encoding="utf-8") as f:
			f.write(str(content))
	except Exception as e:
		section(f"ERROR IN {'write':20}\n{e}")

def read(file_name:str = "temp.txt")->str:
	content = ""
	try:
		if not os.path.exists(file_name):
			with open(file_name, "w", encoding="utf-8") as f:
				f.write("")

		# encoding='utf-8' to catch the error with sites that have characters the charmap cant handle
		with open(file_name, "r", encoding="utf-8") as f:
			content:str = f.read()
	except Exception as e:
		content = ""
		section(f"ERROR IN {'read':20}\n{e}")
	return content

# ========================================================================

def get_soup(link:str = "https://example.com/")->bs:
	headers = {
		"User-Agent": (
			"Mozilla/5.0 (X11; Linux x86_64) "
			"AppleWebKit/537.36 (KHTML, like Gecko) "
			"Chrome/138.0.0.0 Safari/537.36"
		),
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language": "en-US,en;q=0.5",
	}

	try:
		response:req.Response = req.get(link, 
			timeout=2, 
			headers=headers, 
			allow_redirects=True
		)
	except Exception as e:
		section(f"ERROR IN {'request':20}\n{e}")

	soup = bs(response.content.decode("utf-8"), "html.parser")
	return soup