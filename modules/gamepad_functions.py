class Keys:
	def check_dead_zone(func):
		def inner(state):
			if (state > 0 and state > ABS_deadzone*1000) or (state < 0 and state < ABS_deadzone*-1000):
				func(state)
			else:
				pass
				func(0)
		
		inner.__name__ = func.__name__
		inner.__doc__ = func.__doc__

		return inner

	@check_dead_zone
	def left_stick_x(state):
		print(f'left_stick_x - {state}')

	@check_dead_zone
	def left_stick_y(state):
		print(f'left_stick_y - {state}')

	@check_dead_zone
	def right_stick_x(state):
		print(f'right_stick_x - {state}')

	@check_dead_zone
	def right_stick_y(state):
		print(f'right_stick_y - {state}')

	def D_pad_x(state):
		print(f'D_pad_x - {state}')

	def D_pad_y(state):
		print(f'D_pad_y - {state}')

	def btn_a(state):
		print(f'A - {state}')

	def btn_x(state):
		print(f'X - {state}')

	def btn_b(state):
		print(f'B - {state}')

	def btn_y(state):
		print(f'Y - {state}')

	def btn_start(state):
		print(f'Start - {state}')

	def btn_back(state):
		print(f'Back - {state}')

	def left_button(state):
		print(f'left_button - {state}')

	def right_button(state):
		print(f'right_button - {state}')

	def left_trigger(state):
		print(f'left_trigger - {state}')

	def right_trigger(state):
		print(f'right_trigger - {state}')

	def btn_left_stick(state):
		print(f'btn_left_stick - {state}')

	def btn_right_stick(state):
		print(f'btn_right_stick - {state}')


keys = {
	'ABS_X': Keys.left_stick_x,
	'ABS_Y': Keys.left_stick_y,
	'ABS_RX': Keys.right_stick_x,
	'ABS_RY': Keys.right_stick_y,
	'ABS_HAT0X': Keys.D_pad_x,
	'ABS_HAT0Y': Keys.D_pad_y,
	'BTN_SOUTH': Keys.btn_a,
	'BTN_WEST': Keys.btn_x,
	'BTN_EAST': Keys.btn_b,
	'BTN_NORTH': Keys.btn_y,
	'BTN_SELECT': Keys.btn_start,
	'BTN_START': Keys.btn_back,
	'BTN_TL': Keys.left_button,
	'BTN_TR': Keys.right_button,
	'ABS_RZ': Keys.right_trigger,
	'ABS_Z': Keys.left_trigger,
	'BTN_THUMBL': Keys.btn_left_stick,
	'BTN_THUMBR': Keys.btn_right_stick
}

ABS_deadzone = 10