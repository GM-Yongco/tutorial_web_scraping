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
	link_page = "https://housekinokunimanga.com/manga/houseki-no-kuni-chapter-15/"
	write(get_html(link_page))


	# get img from link
	link_image = "https:/xfs-n18.xfspp.com/comic/5003/962/628073bbfe272d6dc98e8269/15928920_1444_2048_1035819.jpeg"
	download_img(link_image)

	separator("END")