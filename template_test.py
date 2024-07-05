# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
# HEADERS ================================================================

from template_functions import *

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	separator("START")

	# get html of a site
	link_page = "https://dynasty-scans.com/doujins/bocchi_the_rock"
	print(link_page)
	write(content = get_html_urllib(link_page))
	write(get_html_request(link_page), "b.txt")


	# get img from link
	# link_image = "https://dynasty-scans.com/system/releases/000/039/165/03-04.webp"
	# download_img(link_image)

	separator("END")