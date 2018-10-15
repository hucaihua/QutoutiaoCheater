import random
import time
from screen_class import *

	
def main():
	adb = AndroidDubugBrideCmd()
	while True:
    
        # refresh screen
		print("refresh screen: ")
		for i in range(1):
			SWIPE_START_AREA_X = SCREEN_WIDTH / 2
			SWIPE_START_AREA_Y = SCREEN_LENGTH * 1 / 3
			SWIPE_START_AREA = (SWIPE_START_AREA_X, SWIPE_START_AREA_Y)

			SWIPE_END_AREA_X = SCREEN_WIDTH / 2
			SWIPE_END_AREA_Y = SCREEN_LENGTH * 2 / 3
			
			SWIPE_END_AREA = (SWIPE_END_AREA_X, SWIPE_END_AREA_Y)
			adb.swipe_screen(SWIPE_START_AREA, SWIPE_END_AREA)
			time.sleep(5)

		# tap first news
		titleHeight = SCREEN_LENGTH / 5
		TEXT_LAYER1_X = SCREEN_WIDTH / 2
		TEXT_LAYER1_Y = titleHeight
		TEXT_LAYER1 = (TEXT_LAYER1_X, TEXT_LAYER1_Y)
		print("tap news: ", TEXT_LAYER1)
		adb.tap_screen(TEXT_LAYER1)
		time.sleep(5)

		# swipe screen
		# print("swipe screen: ", 10, "times")
		# for i in range(10):
			# print("-->time", i)
			# SWIPE_START_AREA_X = SCREEN_WIDTH / 2
			# SWIPE_START_AREA_Y = SCREEN_LENGTH * 2 / 3
			# SWIPE_START_AREA = (SWIPE_START_AREA_X, SWIPE_START_AREA_Y)

			# SWIPE_END_AREA_X = SCREEN_WIDTH / 2
			# SWIPE_END_AREA_Y = SWIPE_START_AREA_Y - 140
			
			# SWIPE_END_AREA = (SWIPE_END_AREA_X, SWIPE_END_AREA_Y)
			# adb.swipe_screen(SWIPE_START_AREA, SWIPE_END_AREA)
			# time.sleep(3)
			
        # swipe screen
		print("swipe screen: ", 10, "times")
		for i in range(10):
			print("-->time", i)
			SWIPE_START_AREA_X = random.uniform(SCREEN_WIDTH * 3 / 8, SCREEN_WIDTH * 5 / 8)
			SWIPE_START_AREA_Y = random.uniform(SCREEN_LENGTH * 5 / 8, SCREEN_LENGTH * 6 / 8)
			SWIPE_START_AREA = (SWIPE_START_AREA_X, SWIPE_START_AREA_Y)
			SWIPE_END_AREA_X = random.uniform(SCREEN_WIDTH * 3 / 8, SCREEN_WIDTH * 5 / 8)
			SWIPE_END_AREA_Y = random.uniform(SCREEN_LENGTH * 2 / 8, SCREEN_LENGTH * 3 / 8)
			SWIPE_END_AREA = (SWIPE_END_AREA_X, SWIPE_END_AREA_Y)
			adb.swipe_screen(SWIPE_START_AREA, SWIPE_END_AREA ,100)
			time.sleep(3)
		
		# back
		adb.back()
		time.sleep(2)
		

if __name__ == "__main__":
	main()
