# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: detecting a change in the web 
# 		its also persistent
# 		is abstracted for editing convenience
# 		
# ========================================================================
# HEADERS
# ========================================================================

import os

from typing import Callable
from bs4 import BeautifulSoup as bs

from utils import section, read, write, get_soup

# ========================================================================
# FETCH RELEVANT DATA
# ========================================================================

def fetch_data_sitting_next_to_me()->str:
	ret_val:str = ""

	try:
		soup:bs = get_soup(link="https://mto.to/chapter/3041986")
		soup:bs = soup.select("optgroup option")[-1]

		ret_val += f"Title: {soup.get_text().strip()}"
		ret_val += "\n"
		ret_val += f"Link: https://mto.to/chapter/{soup.get('value').strip()}"
	except Exception as e:
		section(f"ERROR IN {'fetch_data':20}\n{e}")
	
	return ret_val

# ========================================================================

def detector(fetch_data:Callable = fetch_data_sitting_next_to_me) -> bool:
	ret_val:bool = False
	file_name:str = "temp_" + fetch_data.__name__ + ".txt"
	

	old_record:str = read(file_name)
	new_record:str = fetch_data()

	# is true when old doesnt coencide with new
	if new_record == "":
		# this is an error check
		pass
	elif  old_record == new_record:
		pass
	else:
		ret_val = True
		write(content=new_record, file_name=file_name)
	
	return ret_val

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")

	if detector():
		print("YEA BABY, NEW CHAPTER")
	else:
		print("no new chapter :(((")
	section("END")