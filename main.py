import inputs
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

import sys
import time
import os
import multiprocessing

from modules.gamepad_functions import *
from modules.Tray import SystemTray

class Tray(SystemTray):
	def	exit(self):
		tray_process.terminate()
		exit()

def	start_tray():
	app = QApplication(sys.argv)

	tray = Tray(QIcon('icon.png'), app)
	tray.show()

	sys.exit(app.exec_())

def get_device_list():
	return inputs.devices.gamepads

def main():
	while True:
		try:
			events = inputs.get_gamepad() # Ждёт ивента
			ABS_deadzone = 10

			for event in events:
				if event.ev_type != 'Sync':
					keys[event.code](event.state)

		except inputs.UnpluggedError as r:
			inputs.refresh_devices()
			os.system('cls')
			print(r)
			time.sleep(1.5)

if __name__ == '__main__':
	tray_process = multiprocessing.Process(target=main)
	tray_process.start()
	start_tray()