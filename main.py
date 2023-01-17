from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import mouse
import keyboard

import sys
import time
import os
import multiprocessing

from modules.gamepad_functions import *
from modules.Tray import SystemTray
from modules.Configure import Configure
import modules.inputs as inputs

class Tray(SystemTray):
	def	exit(self):
		main_process.terminate()
		exit()

def	start_tray():
	app = QApplication(sys.argv)

	tray = Tray(QIcon('icon.png'), app)
	tray.show()

	sys.exit(app.exec_())

def mouse_move_control(x, y): # Управление мышкой (^ V < >)
	while True:
		if config.read('General', 'activate') == '1':
			if x.value != 0.0 or y.value != 0.0:
				mouse.move(x.value, y.value, False)
			time.sleep(0.005)

def mouse_scroll_control(speed): # Управление скролом
	while True:
		if config.read('General', 'activate') == '1':
			if speed.value != 0.0:
				mouse.wheel(speed.value)
			time.sleep(0.005)

class MainKeys(Keys):
	def check_dead_zone(func):
		def inner(self, state):
			if (state > 0 and state > self.ABS_deadzone*1000) or (state < 0 and state < self.ABS_deadzone*-1000):
				func(self, state)
			else:
				pass
				func(self, 0)
		
		inner.__name__ = func.__name__
		inner.__doc__ = func.__doc__

		return inner

	def btn_function(self, key, state):
		if config.read('General', 'activate') == '1':
			if config.read(key, 'use_command') == '1':
				if state == 1:
					global test_process
					try:
						test_process.terminate()
					except:
						pass
					test_process = multiprocessing.Process(target=os.system, args=(config.read(key, 'command'),))
					test_process.start()
				
			elif config.read(key, 'use_hotkey') == '1':
				mouse_keys = {
					'LBM':'left',
					'MBM':'middle',
					'RBM':'right'
				}
				hotkey = config.read(key, 'hoykey')

				mouse_ = ['RBM', 'LBM', 'MBM']
				notkeyboard = mouse_
				
				if hotkey not in notkeyboard: # Если это не действия с мышкой, то используются горячие клавишы клавиатуры
					if state == 1:
						keyboard.press(hotkey)
					else:
						keyboard.release(hotkey)
				elif hotkey in mouse_:
					if state == 1:
						mouse.press(mouse_keys[hotkey])
						time.sleep(0.01)
					else:
						mouse.release(mouse_keys[hotkey])

	@check_dead_zone
	def left_stick_x(self, state):
		global mouse_speed_x
		mouse_speed_x.value = state//2000

	@check_dead_zone
	def left_stick_y(self, state):
		global mouse_speed_y
		mouse_speed_y.value = state/-2000
	
	@check_dead_zone
	def right_stick_y(self, state):
		global scroll_speed
		scroll_speed.value = state/40000
	
gamepad_functions = MainKeys()

global config
config = Configure('./config.ini')

def main():
	global mouse_speed_x
	global mouse_speed_y
	mouse_speed_x = multiprocessing.Value('d', 0.0)	# Создаю переменные для скорости мыши и связываю их с процессом для мыши
	mouse_speed_y = multiprocessing.Value('d', 0.0)

	mouse_process = multiprocessing.Process(target=mouse_move_control, args=(mouse_speed_x, mouse_speed_y))
	mouse_process.start()

	global scroll_speed
	scroll_speed = multiprocessing.Value('d', 0.0)	# Создаю переменные для скорости скрола и связываю их с процессом для мыши

	scroll_process = multiprocessing.Process(target=mouse_scroll_control, args=(scroll_speed, ))
	scroll_process.start()

	next_action = 0
	while True:
		try:
			events = inputs.get_gamepad() # Ждёт ивента
			gamepad_functions.ABS_deadzone = int(config.read('General', 'ABS_deadzone'))

			for event in events:
				if event.ev_type != 'Sync':
					gamepad_functions.keys[event.code](event.state) # Вызываю нужную функцию
								
				hotkey_pressed = []
				for key in gamepad_functions.BTNs_status.keys():	# Добавляю в hotkey_pressed все нажатые клавишы
					if gamepad_functions.BTNs_status[key] == 1:
						hotkey_pressed.append(key)

				hotkey_pressed = sorted(hotkey_pressed) # Сортирую список нажатых клавиш

				turn_of_off_hotkey = sorted(config.read('General', 'turn_of_off_hotkey').split('+')) # Беру отсортированый список комбинации клавиш

				if turn_of_off_hotkey == hotkey_pressed:	# Если комбинация клавиш подходит, то когда она не будет подходить, сработает нужное действие
					next_action = 1
				else:
					if next_action == 1:
						next_action = 0
						if config.read('General', 'activate') == '1':
							config.update('General', 'activate', '0')
						else:
							config.update('General', 'activate', '1')


		except inputs.UnpluggedError as r:
			inputs.refresh_devices()
			os.system('cls')
			print(r)
			time.sleep(1.5)

if __name__ == '__main__':
	main_process = multiprocessing.Process(target=main)
	main_process.start()
	start_tray()