from PyQt5.QtWidgets import QApplication, QMenu
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
import mouse
import keyboard

import sys
import time
import os
import multiprocessing
import winreg

from modules.gamepad_functions import *
from ui.Tray import SystemTray
from ui.Settings import Ui_SettingsWindow
from modules.Configure import Configure
import modules.inputs as inputs

class Settings_UI(Ui_SettingsWindow):
	def setup(self):
		super().setup()
		self.mouseSpeedSpinBox.setValue(int(config.read('General', 'mouse_speed')))
		self.scrollSpeedSpinBox.setValue(int(config.read('General', 'scroll_speed')))
		self.deadzoneSpeedSpinBox.setValue(int(config.read('General', 'abs_deadzone')))

		self.checkBox.setChecked(bool(int(config.read('General', 'startup'))))

		hotkey = config.read('General', 'turn_of_off_hotkey').split('+')
		try:
			self.firstTurn_on_ofKeysComboBox.setCurrentText(hotkey[0].replace('_', ' '))
			self.secondTurn_on_ofKeysComboBox.setCurrentText(hotkey[1].replace('_', ' '))
		except IndexError:
			pass
	
	def apply_general(self):
		# После нажатия кнопки "Apply" во вкладки General я сохраняю все данные из вкладки в конфиг файл
		startup = self.checkBox.isChecked()
		config.update('General', 'startup', str(int(startup)))

		file_path = str(os.path.abspath(os.getcwd())) + '.exe' # Получаю путь к файлу запуска приложения
		key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Run') # создаю ключ для автозапуска в реестре
		if startup:
			winreg.SetValueEx(key, 'TS2GamepadControl', 0, winreg.REG_SZ, {file_path}) # Добавляю приложение в автозапуск (в реестре)
		else:
			try:
				winreg.DeleteValue(key, 'TS2GamepadControl') # Удаляю приложение из автозапуска (В реестре)
			except FileNotFoundError:
				pass

		config.update('General', 'abs_deadzone', str(self.deadzoneSpeedSpinBox.value()))
		config.update('General', 'mouse_speed', str(self.mouseSpeedSpinBox.value()))
		config.update('General', 'scroll_speed', str(self.scrollSpeedSpinBox.value()))

		hotkey = f'{self.firstTurn_on_ofKeysComboBox.currentText()}+{self.secondTurn_on_ofKeysComboBox.currentText()}'

		config.update('General', 'turn_of_off_hotkey', hotkey.replace(' ', '_'))

	def apply_key(self):
		# После нажатия кнопки "Apply" во вкладки Key я сохраняю данные для выбранной кнопки геймпада в конфиг файл
		key = self.get_key_properties()

		config.update(key['key'], 'use_command', key['use_command'])
		config.update(key['key'], 'use_hotkey', key['use_hotkey'])
		config.update(key['key'], 'command', key['command'])
		config.update(key['key'], 'hoykey', key['hotkey'])

	def set_key_properties(self):
		# После выбора кнопки геймпада из выпадающего списка устанавливается информация о кнопке из конфиг файла
		key = self.gamepadKeyComboBox.currentText().replace(' ', '_')

		self.useHotkeyRadioButton.setChecked(bool(int(config.read(key, 'use_hotkey'))))
		hotkey = config.read(key, 'hoykey').split('+')

		try:
			self.firstKeyComboBox.setCurrentText(hotkey[0])
			self.secondKeyComboBox.setCurrentText(hotkey[1])
			self.thirdKeyComboBox.setCurrentText(hotkey[2])
		except IndexError:
			pass
		
		self.useCmdRadioButton.setChecked(bool(int(config.read(key, 'use_command'))))
		self.cmdLineEdit.setText(config.read(key, 'command'))

		if config.read(key, 'use_hotkey') != '1' and config.read(key, 'use_command') != '1':
			self.dontUseRadioButton.setChecked(True)

class Tray(SystemTray):
	def set_menu(self):
		menu = QMenu()

		# Устанавливаю кнопки для меню в трее
		call_settings_action = menu.addAction('Settings') # Делаю текст пункту
		call_settings_action.triggered.connect(self.call_settings)	# Добавляю действие при нажании на пункт

		exit_action = menu.addAction('Exit')
		exit_action.triggered.connect(self.exit)

		self.setContextMenu(menu)
		
	def	exit(self):
		main_process.terminate() # Выключаю процесс для управление геймпадом
		Settings.close()
		quit()

	def call_settings(self):
		global Settings
		SettingsWindow = QtWidgets.QMainWindow()

		Settings = Settings_UI(SettingsWindow, 'icon.png')
		Settings.show()

def	start_tray():
	global app
	app = QApplication(sys.argv)
	app.setQuitOnLastWindowClosed(False)

	global tray
	tray = Tray(QIcon('icon.png'), app, 'TS2 Gamepad Control')
	tray.show()

	sys.exit(app.exec_())

def mouse_move_control(x, y): # Управление мышкой (^ V < >)
	while True:
		if config.read('General', 'activate') == '1':
			if x.value != 0.0 or y.value != 0.0:
				config_mouse_speed = float(config.read('General', 'mouse_speed'))/10 # Скорость из конфига делю на 10
				mouse.move(x.value*config_mouse_speed, y.value*config_mouse_speed, False) # Двигаю мышь относительно текущей позиции
			time.sleep(0.005)

def mouse_scroll_control(speed): # Управление скролом
	while True:
		if config.read('General', 'activate') == '1':
			if speed.value != 0.0:
				config_scroll_speed = float(config.read('General', 'scroll_speed'))/10 # Скорость из конфига делю на 10
				mouse.wheel(speed.value*config_scroll_speed)
			time.sleep(0.005)

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
		if config.read('General', 'activate') == '1':

			if config.read(key, 'use_command') == '1': # Если нужно выполнить команду, то создаёь процесс и запускает в нёи эту команду
				if state == 1:
					global test_process
					try:
						test_process.terminate()
					except:
						pass
					test_process = multiprocessing.Process(target=os.system, args=(config.read(key, 'command'),))
					test_process.start()
				
			elif config.read(key, 'use_hotkey') == '1': # Если используется комбинация клавишь
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