from PyQt5.QtWidgets import QApplication, QMenu
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
import mouse
import keyboard

import sys
import time
import os
import threading
import traceback
import winreg

from modules.gamepad_functions import *
from ui.Tray import SystemTray
from ui.Settings import Ui_SettingsWindow
from modules.Configure import Configure
import modules.inputs as inputs
from modules.Logger import Logger

logger = Logger('log_records.csv') # Логирование

class Settings_UI(Ui_SettingsWindow):
	def setup(self):
		try:
			super().setup()
			self.mouseSpeedSpinBox.setValue(int(config.read('General', 'mouse_speed')))
			self.scrollSpeedSpinBox.setValue(int(config.read('General', 'scroll_speed')))
			self.deadzoneSpeedSpinBox.setValue(int(config.read('General', 'abs_deadzone')))

			self.checkBox.setChecked(bool(int(config.read('General', 'startup'))))

			hotkey = config.read('General', 'turn_on_off_hotkey')
			hotkey = hotkey.split('+')
			try:
				self.firstTurn_on_ofKeysComboBox.setCurrentText(list(self.gamepad_keys.keys())[list(self.gamepad_keys.values()).index(hotkey[0])])
				self.secondTurn_on_ofKeysComboBox.setCurrentText(list(self.gamepad_keys.keys())[list(self.gamepad_keys.values()).index(hotkey[1])])
			except IndexError:
				pass

		except Exception:
			logger.logging.error(traceback.format_exc().replace('"', '\''))
	
	def apply_general(self):
			# После нажатия кнопки "Apply" во вкладки General я сохраняю все данные из вкладки в конфиг файл
		try:
			startup = self.checkBox.isChecked()
			config.update('General', 'startup', str(int(startup)))

			file_path = str(os.path.dirname(os.path.abspath(__file__))) + '\\TS2GamepadControl.exe' # Получаю путь к файлу запуска приложения
			key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Run') # создаю ключ для автозапуска в реестре
			if startup:
				winreg.SetValueEx(key, 'TS2GamepadControl', 0, winreg.REG_SZ, file_path) # Добавляю приложение в автозапуск (в реестре)
			else:
				try:
					winreg.DeleteValue(key, 'TS2GamepadControl') # Удаляю приложение из автозапуска (В реестре)
				except FileNotFoundError:
					pass

			config.update('General', 'abs_deadzone', str(self.deadzoneSpeedSpinBox.value()))
			config.update('General', 'mouse_speed', str(self.mouseSpeedSpinBox.value()))
			config.update('General', 'scroll_speed', str(self.scrollSpeedSpinBox.value()))

			global config_mouse_speed
			config_mouse_speed = float(config.read('General', 'mouse_speed'))/10 # Скорость из конфига делю на 10

			global config_scroll_speed
			config_scroll_speed = float(config.read('General', 'scroll_speed'))/10 # Скорость из конфига делю на 10

			gamepad_functions.ABS_deadzone = int(config.read('General', 'ABS_deadzone'))

			hotkey = f'{self.gamepad_keys[self.firstTurn_on_ofKeysComboBox.currentText()]}+{self.gamepad_keys[self.secondTurn_on_ofKeysComboBox.currentText()]}'

			config.update('General', 'turn_on_off_hotkey', hotkey)

		except Exception:
			logger.logging.error(traceback.format_exc().replace('"', '\''))

	def apply_key(self):
		try:
			# После нажатия кнопки "Apply" во вкладки Key я сохраняю данные для выбранной кнопки геймпада в конфиг файл
			key = self.get_key_properties()

			config.update(key['key'], 'use_command', key['use_command'])
			config.update(key['key'], 'use_hotkey', key['use_hotkey'])
			config.update(key['key'], 'command', key['command'])
			config.update(key['key'], 'hotkey', key['hotkey'])

		except Exception:
			logger.logging.error(traceback.format_exc().replace('"', '\''))

	def set_key_properties(self):
		try:
			# После выбора кнопки геймпада из выпадающего списка устанавливается информация о кнопке из конфиг файла
			key = self.gamepad_keys[self.gamepadKeyComboBox.currentText()]

			hotkey = config.read(key, 'hotkey')
			hotkey = hotkey.split('+')

			self.firstKeyComboBox.setCurrentText('NO KEY')
			self.secondKeyComboBox.setCurrentText('NO KEY')
			self.thirdKeyComboBox.setCurrentText('NO KEY')

			try:
				self.firstKeyComboBox.setCurrentText(hotkey[0])
				self.secondKeyComboBox.setCurrentText(hotkey[1])
				self.thirdKeyComboBox.setCurrentText(hotkey[2])
			except IndexError:
				pass
			
			self.cmdLineEdit.setText(config.read(key, 'command'))
			
			if config.read(key, 'use_hotkey') == '1':
				self.useHotkeyRadioButton.setChecked(True)
			
			if config.read(key, 'use_command') == '1':
				self.useCmdRadioButton.setChecked(True)
			
			if config.read(key, 'use_hotkey') != '1' and config.read(key, 'use_command') != '1':
				self.dontUseRadioButton.setChecked(True)
		
		except Exception:
			logger.logging.error(traceback.format_exc().replace('"', '\''))

class Tray(SystemTray):
	def set_menu(self):
		try:
			menu = QMenu()

			# Устанавливаю кнопки для меню в трее
			call_settings_action = menu.addAction('Settings') # Делаю текст пункту
			call_settings_action.triggered.connect(self.call_settings)	# Добавляю действие при нажании на пункт

			exit_action = menu.addAction('Exit')
			exit_action.triggered.connect(self.exit)

			self.setContextMenu(menu)

		except Exception:
			logger.logging.error(traceback.format_exc().replace('"', '\''))
		
	def	exit(self):
		try:
			app.setQuitOnLastWindowClosed(True)
			
			try:
				Settings.close()
			except NameError:
				pass

		except Exception:
			logger.logging.error(traceback.format_exc().replace('"', '\''))
			
		sys.exit(0)

	def call_settings(self):
		try:
			global Settings
			SettingsWindow = QtWidgets.QMainWindow()

			Settings = Settings_UI(SettingsWindow, 'icon.png')
			Settings.show()

		except Exception:
			logger.logging.error(traceback.format_exc().replace('"', '\''))

def	start_tray():
	try:
		global app
		app = QApplication(sys.argv)
		app.setQuitOnLastWindowClosed(False)

		global tray
		tray = Tray(QIcon('icon.png'), app, 'TS2 Gamepad Control')
		tray.show()

		sys.exit(app.exec_())
	except Exception:
			logger.logging.error(traceback.format_exc().replace('"', '\''))

def mouse_move_control(): # Управление мышкой (^ V < >)
	try:
		global mouse_speed_x
		global mouse_speed_y
		global activate
		global config_mouse_speed
		while True:
			if (mouse_speed_x != 0.0 or mouse_speed_y != 0.0) and activate:
				mouse.move(mouse_speed_x*config_mouse_speed, mouse_speed_y*config_mouse_speed, False) # Двигаю мышь относительно текущей позиции
			time.sleep(0.005)

	except Exception:
			logger.logging.error(traceback.format_exc().replace('"', '\''))

def mouse_scroll_control(): # Управление скролом
	try:
		global scroll_speed
		global activate
		global config_scroll_speed
		while True:
			if scroll_speed != 0.0 and activate:
				mouse.wheel(scroll_speed*config_scroll_speed)
			time.sleep(0.005)

	except Exception:
			logger.logging.error(traceback.format_exc().replace('"', '\''))

class MainKeys(Keys):
	def check_dead_zone(func): 
		# Проверка на Dead Zone у стиков (Если он меньше, то в функцию идёт 0)
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
		try:
			global activate
			if activate:
				if config.read(key, 'use_command') == '1': # Если нужно выполнить команду, то создаёт процесс и запускает в нёи эту команду
					if state == 1:
						global test_process
						test_process = threading.Thread(target=os.system, args=(config.read(key, 'command'),))
						test_process.start()
					
				elif config.read(key, 'use_hotkey') == '1': # Если используется комбинация клавишь
					mouse_keys = {
						'LMB':'left',
						'MMB':'middle',
						'RMB':'right'
					}

					hotkeys = config.read(key, 'hotkey')

					mouse_ = ['RMB', 'LMB', 'MMB']
					notkeyboard = mouse_
					
					for hotkey in list(map(str, hotkeys.split('+'))):
						hotkey = Settings_UI.keyboard_keys[hotkey]

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

		except Exception:
			logger.logging.error(traceback.format_exc().replace('"', '\''))

	@check_dead_zone
	def left_stick_x(self, state):
		global mouse_speed_x
		mouse_speed_x = state//2000

	@check_dead_zone
	def left_stick_y(self, state):
		global mouse_speed_y
		mouse_speed_y = state/-2000
	
	@check_dead_zone
	def right_stick_y(self, state):
		global scroll_speed
		scroll_speed = state/40000
	
gamepad_functions = MainKeys()

global config
config = Configure('./config.ini')

def main():
	next_action = 0
	while True:
		try:
			events = inputs.get_gamepad() # Ждёт ивента

			for event in events:
				if event.ev_type != 'Sync':
					gamepad_functions.keys[event.code](event.state) # Вызываю нужную функцию
								
				hotkey_pressed = []
				for key in gamepad_functions.BTNs_status.keys():	# Добавляю в hotkey_pressed все нажатые клавишы
					if gamepad_functions.BTNs_status[key] == 1:
						hotkey_pressed.append(key)

				hotkey_pressed = sorted(hotkey_pressed) # Сортирую список нажатых клавиш

				turn_on_off_hotkey = config.read('General', 'turn_on_off_hotkey') # Беру отсортированый список комбинации клавиш
				turn_on_off_hotkey = sorted(turn_on_off_hotkey.split('+'))

				if turn_on_off_hotkey == hotkey_pressed:	# Если комбинация клавиш подходит, то когда она не будет подходить, сработает нужное действие
					next_action = 1
				else:
					if next_action == 1:
						next_action = 0
						global activate
						if config.read('General', 'activate') == '1':
							config.update('General', 'activate', '0')
							activate = False
						else:
							config.update('General', 'activate', '1')
							activate = True

		except AttributeError:
			logger.logging.error(traceback.format_exc().replace('"', '\''))

		except inputs.UnpluggedError as r:
			inputs.refresh_devices()
			os.system('cls')
			print(r)
			time.sleep(1.5)
		
		except Exception:
			logger.logging.error(traceback.format_exc().replace('"', '\''))

if __name__ == '__main__':
	try:
		global activate
		activate = config.read('General', 'activate')
		if activate == '1':
			activate = True
		else:
			activate = False

		global config_mouse_speed
		config_mouse_speed = float(config.read('General', 'mouse_speed'))/10 # Скорость из конфига делю на 10

		global config_scroll_speed
		config_scroll_speed = float(config.read('General', 'scroll_speed'))/10 # Скорость из конфига делю на 10

		gamepad_functions.ABS_deadzone = int(config.read('General', 'ABS_deadzone'))

		global mouse_speed_x
		global mouse_speed_y
		mouse_speed_x = 0.0	# Создаю переменные для скорости мыши и связываю их с процессом для мыши
		mouse_speed_y = 0.0

		mouse_process = threading.Thread(target=mouse_move_control, daemon=True)
		mouse_process.start()

		global scroll_speed
		scroll_speed = 0.0	# Создаю переменные для скорости скрола и связываю их с процессом для мыши

		scroll_process = threading.Thread(target=mouse_scroll_control, daemon=True)
		scroll_process.start()

		main_process = threading.Thread(target=main, daemon=True)
		main_process.start()

		start_tray()

	except Exception:
		logger.logging.error(traceback.format_exc().replace('"', '\''))