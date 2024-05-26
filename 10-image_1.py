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
		req.urlretrieve(url, path)
	except Exception as e:
		separator(f"error: {e}")



# ========================================================================
# MAIN 
# ========================================================================

def main():
	link1 = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4b-cPrsYmAOwBz_-P7YRn5xx_YZm2ZOEdVWqse-HXqoOcCVvS0mw0E9U7YZq7Y_mxPlDs1dLsp_96HowTspXqzhz69CpJdkABCYYq1zNOEX9cIAKGLrdsxWpYta3uQsV60NWufVcFjUMEXKvLeVwWjTxwoojXUQmpTgHxDb8qISPjFiok41v_Zr456w/s1600/03.jpg"
	download_img(link1)

# ========================================================================

if __name__ == '__main__':
	separator("START")
	main()
	separator("END")