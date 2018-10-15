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

		# tap video
		TEXT_LAYER1_X = SCREEN_WIDTH / 2
		TEXT_LAYER1_Y = SCREEN_LENGTH / 3 + 10
		TEXT_LAYER1 = (TEXT_LAYER1_X, TEXT_LAYER1_Y)
		print("tap video: ", TEXT_LAYER1)
		adb.tap_screen(TEXT_LAYER1)
		time.sleep(60)

		# # swipe screen
		# print("swipe screen: ", times, "times")
		# for i in range(1):
			# print("time", i)
			# SWIPE_START_AREA_X = SCREEN_WIDTH / 2
			# SWIPE_START_AREA_Y = SCREEN_LENGTH * 2 / 3
			# SWIPE_START_AREA = (SWIPE_START_AREA_X, SWIPE_START_AREA_Y)

			# SWIPE_END_AREA_X = SCREEN_WIDTH / 2
			# SWIPE_END_AREA_Y = SCREEN_LENGTH * 1 / 3
			
			# SWIPE_END_AREA = (SWIPE_END_AREA_X, SWIPE_END_AREA_Y)
			# adb.swipe_screen(SWIPE_START_AREA, SWIPE_END_AREA)
			# time.sleep(3)
		
		# back
		# BACK_BUTTON_X = random.randint(0 + DIFF, 100 - DIFF)
		# BACK_BUTTON_Y = random.randint(50 + DIFF, 150 - DIFF)
		# BACK_BUTTON = (BACK_BUTTON_X, BACK_BUTTON_Y )
		# adb.tap_screen(BACK_BUTTON)
		# time.sleep(1)
		

if __name__ == "__main__":
	main()
