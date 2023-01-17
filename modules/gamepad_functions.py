class Keys:
	def __init__(self):
		self.keys = {
		'ABS_X': self.left_stick_x,
		'ABS_Y': self.left_stick_y,
		'ABS_RX': self.right_stick_x,
		'ABS_RY': self.right_stick_y,
		'ABS_HAT0X': self.D_pad_x,
		'ABS_HAT0Y': self.D_pad_y,
		'BTN_SOUTH': self.btn_a,
		'BTN_WEST': self.btn_x,
		'BTN_EAST': self.btn_b,
		'BTN_NORTH': self.btn_y,
		'BTN_SELECT': self.btn_start,
		'BTN_START': self.btn_back,
		'BTN_TL': self.left_button,
		'BTN_TR': self.right_button,
		'ABS_RZ': self.right_trigger,
		'ABS_Z': self.left_trigger,
		'BTN_THUMBL': self.btn_left_stick,
		'BTN_THUMBR': self.btn_right_stick
		}

		self.BTNs_status = {
		'Left_Stick': 0,
		'Right_Stick': 0,
		'D_Pad_up': 0,
		'D_Pad_left': 0,
		'D_Pad_right': 0,
		'D_Pad_down': 0,
		'A': 0,
		'B': 0,
		'X': 0,
		'Y': 0,
		'Back': 0,
		'Start': 0,
		'RB': 0,
		'RT': 0,
		'LB': 0,
		'LT': 0,
		}

		self.ABS_deadzone = 6

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
		pass

	@check_dead_zone
	def left_stick_x(self, state):
		pass

	@check_dead_zone
	def left_stick_y(self, state):
		pass

	@check_dead_zone
	def right_stick_x(self, state):
		pass

	@check_dead_zone
	def right_stick_y(self, state):
		pass

	def D_pad_x(self, state):
		if state == -1:
			self.BTNs_status['D_Pad_left'] = 1
			self.btn_function('D_Pad_left', 1)
		elif state == 1:
			self.BTNs_status['D_Pad_right'] = 1
			self.btn_function('D_Pad_right', 1)
		elif state == 0:
			self.BTNs_status['D_Pad_left'] = 0
			self.BTNs_status['D_Pad_right'] = 0
			self.btn_function('D_Pad_left', 0)
			self.btn_function('D_Pad_right', 0)

	def D_pad_y(self, state):
		if state == -1:
			self.BTNs_status['D_Pad_up'] = 1
			self.btn_function('D_Pad_up', 1)
		elif state == 1:
			self.BTNs_status['D_Pad_down'] = 1
			self.btn_function('D_Pad_down', 1)
		elif state == 0:
			self.BTNs_status['D_Pad_up'] = 0
			self.BTNs_status['D_Pad_down'] = 0
			self.btn_function('D_Pad_up', 0)
			self.btn_function('D_Pad_down', 0)

	def btn_a(self, state):
		if state == 1:
			self.BTNs_status['A'] = 1
			self.btn_function('A', 1)
		else:
			self.BTNs_status['A'] = 0
			self.btn_function('A', 0)

	def btn_x(self, state):
		if state == 1:
			self.BTNs_status['X'] = 1
			self.btn_function('X', 1)
		else:
			self.BTNs_status['X'] = 0
			self.btn_function('X', 0)

	def btn_b(self, state):
		if state == 1:
			self.BTNs_status['B'] = 1
			self.btn_function('B', 1)
		else:
			self.BTNs_status['B'] = 0
			self.btn_function('B', 0)

	def btn_y(self, state):
		if state == 1:
			self.BTNs_status['Y'] = 1
			self.btn_function('Y', 1)
		else:
			self.BTNs_status['Y'] = 0
			self.btn_function('Y', 0)

	def btn_start(self, state):
		if state == 1:
			self.BTNs_status['Start'] = 1
			self.btn_function('Start', 1)
		else:
			self.BTNs_status['Start'] = 0
			self.btn_function('Start', 0)

	def btn_back(self, state):
		if state == 1:
			self.BTNs_status['Back'] = 1
			self.btn_function('Back', 1)
		else:
			self.BTNs_status['Back'] = 0
			self.btn_function('Back', 0)

	def left_button(self, state):
		if state == 1:
			self.BTNs_status['LB'] = 1
			self.btn_function('LB', 1)
		else:
			self.BTNs_status['LB'] = 0
			self.btn_function('LB', 0)

	def right_button(self, state):
		if state == 1:
			self.BTNs_status['RB'] = 1
			self.btn_function('RB', 1)
		else:
			self.BTNs_status['RB'] = 0
			self.btn_function('RB', 0)

	def left_trigger(self, state):
		if state > 1:
			self.BTNs_status['LT'] = 1
			self.btn_function('LT', 1)
		else:
			self.BTNs_status['LT'] = 0
			self.btn_function('LT', 0)

	def right_trigger(self, state):
		if state > 1:
			self.BTNs_status['RT'] = 1
			self.btn_function('RT', 1)
		else:
			self.BTNs_status['RT'] = 0
			self.btn_function('RT', 0)

	def btn_left_stick(self, state):
		if state == 1:
			self.BTNs_status['Left_Stick'] = 1
			self.btn_function('Left_Stick', 1)
		else:
			self.BTNs_status['Left_Stick'] = 0
			self.btn_function('Left_Stick', 0)

	def btn_right_stick(self, state):
		if state == 1:
			self.BTNs_status['Right_Stick'] = 1
			self.btn_function('Right_Stick', 1)
		else:
			self.BTNs_status['Right_Stick'] = 0
			self.btn_function('Right_Stick', 0)