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
	link_page = "https://dynasty-scans.com/chapters/the_guy_she_was_interested_in_wasnt_a_guy_at_all_ch00#2"
	print(link_page)
	write(get_html(link_page))
	write(get_html_old(link_page), "b.txt")


	# get img from link
	# link_image = "https://dynasty-scans.com/system/releases/000/039/165/03-04.webp"
	# download_img(link_image)

	separator("END")