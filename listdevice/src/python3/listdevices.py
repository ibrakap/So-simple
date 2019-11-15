#!/usr/bin/python3
import os
import getpass
import time
def main():
	try:
		while True:
			devices  = os.listdir("/media/{}".format(getpass.getuser()))
			wait_time = 2
			if len(devices) > 0:
				print("Device name:")
				for device in devices:
					print(device)
				print("***********************\n"+str(len(devices)),"devices connected!")
				print("{} second then will refresh".format(wait_time))
				time.sleep(wait_time)
				os.system("clear")
			else:
				print("Not connected any devices")
				print("{} second then will refresh".format(wait_time))
				time.sleep(wait_time)
				os.system("clear")

	except KeyboardInterrupt:
			print("Program terminated")
	except:
		print("Unknown error")
if __name__ == "__main__":
	main()