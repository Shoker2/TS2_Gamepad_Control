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
				'mouse_speed': '7',
				'scroll_speed': '7',
				'turn_on_off_hotkey': 'Start+Back'
			}
			self.config['Left_Stick'] = {
				'use_command': '0',
				'use_hotkey': '1',
				'command': '',
				'hotkey': 'MIDDLE MOUSE BUTTON'
			}
			self.config['Right_Stick'] = {
				'use_command': '0',
				'use_hotkey': '1',
				'command': '',
				'hotkey': 'ENTER'
			}
			self.config['D_Pad_up'] = {
				'use_command': '0',
				'use_hotkey': '1',
				'command': '',
				'hotkey': 'UP ARROW'
			}
			self.config['D_Pad_left'] = {
				'use_command': '0',
				'use_hotkey': '1',
				'command': '',
				'hotkey': 'LEFT ARROW'
			}
			self.config['D_Pad_right'] = {
				'use_command': '0',
				'use_hotkey': '1',
				'command': '',
				'hotkey': 'RIGHT ARROW'
			}
			self.config['D_Pad_down'] = {
				'use_command': '0',
				'use_hotkey': '1',
				'command': '',
				'hotkey': 'DOWN ARROW'
			}
			self.config['A'] = {
				'use_command': '0',
				'use_hotkey': '1',
				'command': '',
				'hotkey': 'LEFT MOUSE BUTTON'
			}
			self.config['B'] = {
				'use_command': '0',
				'use_hotkey': '1',
				'command': '',
				'hotkey': 'RIGHT MOUSE BUTTON'
			}
			self.config['X'] = {
				'use_command': '0',
				'use_hotkey': '1',
				'command': '',
				'hotkey': 'BACKSPACE'
			}
			self.config['Y'] = {
				'use_command': '0',
				'use_hotkey': '1',
				'command': '',
				'hotkey': 'ESC'
			}
			self.config['Back'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': '',
				'hotkey': 'No Key'
			}
			self.config['Start'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': '',
				'hotkey': 'No Key'
			}
			self.config['RB'] = {
				'use_command': '0',
				'use_hotkey': '1',
				'command': '',
				'hotkey': 'CTRL+V'
			}
			self.config['RT'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': '',
				'hotkey': 'No Key'
			}
			self.config['LB'] = {
				'use_command': '0',
				'use_hotkey': '1',
				'command': '',
				'hotkey': 'SIMPLE KEYBOARD'
			}
			self.config['LT'] = {
				'use_command': '0',
				'use_hotkey': '0',
				'command': '',
				'hotkey': 'No Key'
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