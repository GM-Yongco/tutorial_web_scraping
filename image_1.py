# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
# HEADERS ================================================================
import os
import urllib.request as req

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def separator(x:str = "SECTION") -> None:
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

# ========================================================================
# FUNCTIONS SCRAPE
# ========================================================================

def download_img(url:str = "https://i.imgur.com/R10MS0w.png", file_name:str = "a.png") -> None:
	# check if scraped folder exists
	path = "00_Scraped/"
	if(os.path.exists(path) == False):
		os.makedirs(path)

	path = "00_Scraped/" + file_name
	req.urlretrieve(url, path)

# ========================================================================
# MAIN 
# ========================================================================

def main():
	link1 = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiayevwGfXu1HJ8TU-5l5r0u0LVQDxKeoNEWZAMmXohT-_oxazsk8pSYPQPczzUk5BIrd-vaE1jMdquWununVHUuxSKr8f7WBM94tr2ZP6gVXGu9_euMWuTwzlCJ194gErnPKgcBYbcVjZqMbFWE9eFMFkNY1qsfktvoC6Tl5qrmwHJcPJeJU4VBSFn/s2992/002.jpg"
	download_img(link1)

if __name__ == '__main__':
	separator("START")
	main()
	separator("END")