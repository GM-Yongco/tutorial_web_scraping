# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: to test if I can download images
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

def download_img(url:str = "https://dynasty-scans.com/system/releases/000/041/912/05.webp", file_name:str = "a.png") -> None:
	# check if scraped folder exists
	path = "00_Scraped/"
	if(os.path.exists(path) == False):
		os.makedirs(path)

	path = "00_Scraped/" + file_name
	try:
		req.urlretrieve(url, path)
	except Exception as e:
		separator(f"error: {e}")



# ========================================================================
# MAIN 
# ========================================================================

def main():
	link1 = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiayevwGfXu1HJ8TU-5l5r0u0LVQDxKeoNEWZAMmXohT-_oxazsk8pSYPQPczzUk5BIrd-vaE1jMdquWununVHUuxSKr8f7WBM94tr2ZP6gVXGu9_euMWuTwzlCJ194gErnPKgcBYbcVjZqMbFWE9eFMFkNY1qsfktvoC6Tl5qrmwHJcPJeJU4VBSFn/s2992/002.jpg"
	link1 = "https://1.bp.blogspot.com/-8gQaRr2nkYQ/Xc4AOKHElSI/AAAAAAAABLw/z42BtMu88AYvsdgl5LlyL5EAStnExMrpACLcBGAsYHQ/s1600/013.jpg"
	download_img(link1)

# ========================================================================

if __name__ == '__main__':
	separator("START")
	main()
	separator("END")