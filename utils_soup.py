# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: utils for general web scraping
# ========================================================================
# HEADERS
# ========================================================================

import requests as req
from bs4 import BeautifulSoup as bs

from utils import section

# ========================================================================
# FUNCTIONS UTIL
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