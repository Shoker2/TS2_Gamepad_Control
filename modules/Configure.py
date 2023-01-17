import configparser
import os

class Configure:
	def __init__(self, config_path):
		self.config_path = config_path
		self.config = configparser.ConfigParser()

		if not os.path.isfile(self.config_path):
			self.config['General'] = {
				'activate': '1',
				'startup': '0',
				'ABS_deadzone': '8',
				'mouse_speed': '10',
				'scroll_speed': '10',
				'turn_of_off_hotkey': 'Start+Back'
			}
			self.config['Left_Stick'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['Right_Stick'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['D_Pad_up'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['D_Pad_left'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['D_Pad_right'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['D_Pad_down'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['A'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['B'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['X'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['Y'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['Back'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['Start'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['RB'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['RT'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['LB'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			self.config['LT'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': 'osk',
				'hoykey': 'esc'
			}
			
			self.write()
			
		self.config.read(self.config_path, encoding='utf-8')
		
	def read(self, section, key):
		self.config.read(self.config_path, encoding='utf-8')
		return self.config[section][key]
	
	def	update(self, section, key, arg):
		self.config[section][key] = arg
		self.write()

	def write(self):
		with open(self.config_path, 'w+', encoding='utf-8') as configfile:
			self.config.write(configfile)

if __name__ == '__main__':
	config = Configure('./config.ini')