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

from typing import Callable, List
from utils import section, read, write

from fetch_data_manga_xbato import fetch_data_sitting_next_to_me, fetch_data_our_sunny_days
from fetch_data_manga_mangadex import fetch_data_tgswiiwagaa

# ========================================================================
# CLASS
# ========================================================================

class DetectorDataUpdates():
	def __init__(
			self, TOKEN:str = "", 
			LOG_CHANNEL_ID:str = ""
		) -> None:
		self.fetch_data_function_list:List[Callable] = []

	def is_new_record(
			self,
			fetch_data:Callable
		) -> bool:
		
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

	# ====================================================================
	
	def fetch_data(self)->None:
		for fetch_data_function in self.fetch_data_function_list:
			try:
				if self.is_new_record(fetch_data_function):
					print(f"YEA BABY, NEW CHAPTER in {fetch_data_function.__name__}")
				else:
					print(f"no new chapter :((( in {fetch_data_function.__name__}")
			except Exception as e:
				section(f"ERROR PROCESSING {f'{fetch_data_function.__name__}':20}\n{e}")
		

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")

	detector:DetectorDataUpdates = DetectorDataUpdates()
	detector.fetch_data_function_list.append(fetch_data_sitting_next_to_me)
	detector.fetch_data_function_list.append(fetch_data_our_sunny_days)
	detector.fetch_data_function_list.append(fetch_data_tgswiiwagaa)
	detector.fetch_data()

	section("END")