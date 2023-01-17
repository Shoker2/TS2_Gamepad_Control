# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Shoker2/Desktop/TS2_Gamepad_Control/ui/Settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_SettingsWindow(QMainWindow):
	resized = QtCore.pyqtSignal()

	keyboard_keys = [
		'No Key',
		'Esc',
		'A',
		'B',
		'C',
		'D',
		'E',
		'F',
		'G',
		'H',
		'I',
		'J',
		'K',
		'L',
		'M',
		'N',
		'O',
		'P',
		'Q',
		'R',
		'S',
		'T',
		'U',
		'V',
		'W',
		'X',
		'Y',
		'Z',
		'Space',
		'Ctrl',
		'Alt',
		'Enter',
		'0',
		'1',
		'2',
		'3',
		'4',
		'5',
		'6',
		'7',
		'8',
		'9',
		'F0',
		'F1',
		'F2',
		'F3',
		'F4',
		'F5',
		'F6',
		'F7',
		'F8',
		'F9',
		'LBM',
		'RBM',
		'MBM',
		'left',
		'right',
		'up',
		'down',
	]
	
	gamepad_keys = [
		'A',
		'B',
		'X',
		'Y',
		'D Pad up',
		'D Pad left',
		'D Pad right',
		'D Pad down',
		'Back',
		'Start',
		'Left Stick',
		'Right Stick',
		'RB',
		'RT',
		'LB',
		'LT',
	]

	def __init__(self, SettingsWindow, icon_path = ''):
		super(Ui_SettingsWindow, self).__init__()
		self.SettingsWindow = SettingsWindow

		if icon_path != '':
			self.setWindowIcon(QtGui.QIcon(icon_path))

		self.setObjectName("SettingsWindow")
		self.resize(701, 752)
		self.setMinimumSize(347, 213)
		self.centralwidget = QtWidgets.QWidget(self.SettingsWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		self.tabWidget.setGeometry(QtCore.QRect(0, 0, 501, 491))
		self.tabWidget.setObjectName("tabWidget")
		self.General_page = QtWidgets.QWidget()
		self.General_page.setObjectName("General_page")
		self.GeneralScrollArea = QtWidgets.QScrollArea(self.General_page)
		self.GeneralScrollArea.setGeometry(QtCore.QRect(0, 0, 481, 411))
		self.GeneralScrollArea.setWidgetResizable(True)
		self.GeneralScrollArea.setObjectName("GeneralScrollArea")
		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 479, 409))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.mouseSpeedLlabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.mouseSpeedLlabel.setFont(font)
		self.mouseSpeedLlabel.setObjectName("mouseSpeedLlabel")
		self.horizontalLayout_3.addWidget(self.mouseSpeedLlabel)
		self.mouseSpeedSpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.mouseSpeedSpinBox.setFont(font)
		self.mouseSpeedSpinBox.setMinimum(1)
		self.mouseSpeedSpinBox.setMaximum(100)
		self.mouseSpeedSpinBox.setProperty("value", 1)
		self.mouseSpeedSpinBox.setDisplayIntegerBase(10)
		self.mouseSpeedSpinBox.setObjectName("mouseSpeedSpinBox")
		self.horizontalLayout_3.addWidget(self.mouseSpeedSpinBox)
		self.verticalLayout.addLayout(self.horizontalLayout_3)
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		self.scrollSpeedLlabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.scrollSpeedLlabel.setFont(font)
		self.scrollSpeedLlabel.setObjectName("scrollSpeedLlabel")
		self.horizontalLayout_5.addWidget(self.scrollSpeedLlabel)
		self.scrollSpeedSpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.scrollSpeedSpinBox.setFont(font)
		self.scrollSpeedSpinBox.setMinimum(1)
		self.scrollSpeedSpinBox.setMaximum(100)
		self.scrollSpeedSpinBox.setProperty("value", 1)
		self.scrollSpeedSpinBox.setDisplayIntegerBase(10)
		self.scrollSpeedSpinBox.setObjectName("scrollSpeedSpinBox")
		self.horizontalLayout_5.addWidget(self.scrollSpeedSpinBox)
		self.verticalLayout.addLayout(self.horizontalLayout_5)
		self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_8.setObjectName("horizontalLayout_8")
		self.deadzoneSpeedLlabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.deadzoneSpeedLlabel.setFont(font)
		self.deadzoneSpeedLlabel.setObjectName("deadzoneSpeedLlabel")
		self.horizontalLayout_8.addWidget(self.deadzoneSpeedLlabel)
		self.deadzoneSpeedSpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.deadzoneSpeedSpinBox.setFont(font)
		self.deadzoneSpeedSpinBox.setMinimum(1)
		self.deadzoneSpeedSpinBox.setMaximum(40)
		self.deadzoneSpeedSpinBox.setProperty("value", 1)
		self.deadzoneSpeedSpinBox.setDisplayIntegerBase(10)
		self.deadzoneSpeedSpinBox.setObjectName("deadzoneSpeedSpinBox")
		self.horizontalLayout_8.addWidget(self.deadzoneSpeedSpinBox)
		self.verticalLayout.addLayout(self.horizontalLayout_8)
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.turn_on_ofLlabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.turn_on_ofLlabel.setFont(font)
		self.turn_on_ofLlabel.setObjectName("turn_on_ofLlabel")
		self.horizontalLayout_4.addWidget(self.turn_on_ofLlabel)
		self.firstTurn_on_ofKeysComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.firstTurn_on_ofKeysComboBox.setFont(font)
		self.firstTurn_on_ofKeysComboBox.setObjectName("firstTurn_on_ofKeysComboBox")
		self.horizontalLayout_4.addWidget(self.firstTurn_on_ofKeysComboBox)
		self.secondTurn_on_ofKeysComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.secondTurn_on_ofKeysComboBox.setFont(font)
		self.secondTurn_on_ofKeysComboBox.setObjectName("secondTurn_on_ofKeysComboBox")
		self.horizontalLayout_4.addWidget(self.secondTurn_on_ofKeysComboBox)
		self.verticalLayout.addLayout(self.horizontalLayout_4)
		self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.checkBox.setFont(font)
		self.checkBox.setObjectName("checkBox")
		self.verticalLayout.addWidget(self.checkBox)
		self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_6.setObjectName("horizontalLayout_6")
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_6.addItem(spacerItem)
		self.ApplyPushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.ApplyPushButton.setFont(font)
		self.ApplyPushButton.setObjectName("ApplyPushButton")
		self.horizontalLayout_6.addWidget(self.ApplyPushButton)
		self.verticalLayout.addLayout(self.horizontalLayout_6)
		self.GeneralScrollArea.setWidget(self.scrollAreaWidgetContents)
		self.tabWidget.addTab(self.General_page, "")
		self.Keys_page = QtWidgets.QWidget()
		self.Keys_page.setObjectName("Keys_page")
		self.KeysScrollArea = QtWidgets.QScrollArea(self.Keys_page)
		self.KeysScrollArea.setGeometry(QtCore.QRect(0, 0, 471, 331))
		self.KeysScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.KeysScrollArea.setWidgetResizable(True)
		self.KeysScrollArea.setObjectName("KeysScrollArea")
		self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
		self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 469, 329))
		self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.gamepadKeyLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.gamepadKeyLabel.sizePolicy().hasHeightForWidth())
		self.gamepadKeyLabel.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.gamepadKeyLabel.setFont(font)
		self.gamepadKeyLabel.setObjectName("gamepadKeyLabel")
		self.horizontalLayout_2.addWidget(self.gamepadKeyLabel)
		self.gamepadKeyComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.gamepadKeyComboBox.sizePolicy().hasHeightForWidth())
		self.gamepadKeyComboBox.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.gamepadKeyComboBox.setFont(font)
		self.gamepadKeyComboBox.setObjectName("gamepadKeyComboBox")
		self.horizontalLayout_2.addWidget(self.gamepadKeyComboBox)
		self.verticalLayout_2.addLayout(self.horizontalLayout_2)
		self.dontUseRadioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.dontUseRadioButton.setFont(font)
		self.dontUseRadioButton.setChecked(True)
		self.dontUseRadioButton.setObjectName("dontUseRadioButton")
		self.verticalLayout_2.addWidget(self.dontUseRadioButton)
		self.useHotkeyRadioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.useHotkeyRadioButton.setFont(font)
		self.useHotkeyRadioButton.setObjectName("useHotkeyRadioButton")
		self.verticalLayout_2.addWidget(self.useHotkeyRadioButton)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.firstKeyComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
		self.firstKeyComboBox.setFont(font)
		self.firstKeyComboBox.setObjectName("firstKeyComboBox")
		self.horizontalLayout.addWidget(self.firstKeyComboBox)
		self.secondKeyComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
		self.secondKeyComboBox.setFont(font)
		self.secondKeyComboBox.setObjectName("secondKeyComboBox")
		self.horizontalLayout.addWidget(self.secondKeyComboBox)
		self.thirdKeyComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
		self.thirdKeyComboBox.setFont(font)
		self.thirdKeyComboBox.setObjectName("thirdKeyComboBox")
		self.horizontalLayout.addWidget(self.thirdKeyComboBox)
		self.verticalLayout_2.addLayout(self.horizontalLayout)
		self.useCmdRadioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.useCmdRadioButton.setFont(font)
		self.useCmdRadioButton.setObjectName("useCmdRadioButton")
		self.verticalLayout_2.addWidget(self.useCmdRadioButton)
		self.cmdLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
		self.cmdLineEdit.setObjectName("cmdLineEdit")
		self.verticalLayout_2.addWidget(self.cmdLineEdit)
		self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_7.setObjectName("horizontalLayout_7")
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_7.addItem(spacerItem1)
		self.ApplyKeyPushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.ApplyKeyPushButton.setFont(font)
		self.ApplyKeyPushButton.setObjectName("ApplyKeyPushButton")
		self.horizontalLayout_7.addWidget(self.ApplyKeyPushButton)
		self.verticalLayout_2.addLayout(self.horizontalLayout_7)
		self.KeysScrollArea.setWidget(self.scrollAreaWidgetContents_2)
		self.tabWidget.addTab(self.Keys_page, "")
		self.setCentralWidget(self.centralwidget)

		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(self.SettingsWindow)

		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("SettingsWindow", "Settings"))
		self.mouseSpeedLlabel.setText(_translate("SettingsWindow", "Mouse Speed"))
		self.scrollSpeedLlabel.setText(_translate("SettingsWindow", "Scroll Speed"))
		self.deadzoneSpeedLlabel.setText(_translate("SettingsWindow", "Dead Zone"))
		self.turn_on_ofLlabel.setText(_translate("SettingsWindow", "Turn off/on hotkey"))
		self.checkBox.setText(_translate("SettingsWindow", "Add to startup"))
		self.ApplyPushButton.setText(_translate("SettingsWindow", "Apply"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.General_page), _translate("SettingsWindow", "General"))
		self.gamepadKeyLabel.setText(_translate("SettingsWindow", "Key"))
		self.dontUseRadioButton.setText(_translate("SettingsWindow", "Don\'t use"))
		self.useHotkeyRadioButton.setText(_translate("SettingsWindow", "Use hotkey"))
		self.useCmdRadioButton.setText(_translate("SettingsWindow", "Use cmd command"))
		self.ApplyKeyPushButton.setText(_translate("SettingsWindow", "Apply key"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.Keys_page), _translate("SettingsWindow", "Keys"))

		self.resized.connect(self.auto_resize) # Делаю ивент на изменение размера окна
		self.ApplyKeyPushButton.clicked.connect(lambda: self.apply_key())
		self.ApplyPushButton.clicked.connect(lambda: self.apply_general())
		self.gamepadKeyComboBox.currentTextChanged.connect(lambda: self.set_key_properties())

		self.resize(500, 350)
		self.setup()
	
	def resizeEvent(self, event):
		self.resized.emit()
		return super(Ui_SettingsWindow, self).resizeEvent(event)
	
	def apply_general(self):
		pass
	
	def apply_key(self):
		pass
	
	def setup(self):
		for key in self.keyboard_keys:
			self.firstKeyComboBox.addItem(key)
			self.secondKeyComboBox.addItem(key)
			self.thirdKeyComboBox.addItem(key)
		
		for btn in self.gamepad_keys:
			self.gamepadKeyComboBox.addItem(btn)
			self.firstTurn_on_ofKeysComboBox.addItem(btn)
			self.secondTurn_on_ofKeysComboBox.addItem(btn)

	def set_key_properties(self):
		pass

	def get_key_properties(self):
		key = {}
		key['key'] = self.gamepadKeyComboBox.currentText().replace(' ', '_')
		key['use_hotkey'] = str(int(self.useHotkeyRadioButton.isChecked()))
		key['hotkey'] = f'{self.firstKeyComboBox.currentText()}+{self.secondKeyComboBox.currentText()}+{self.thirdKeyComboBox.currentText()}'
		key['hotkey'] = key['hotkey'].replace('No Key', '').strip('+')
		key['use_command'] = str(int(self.useCmdRadioButton.isChecked()))
		key['command'] = self.cmdLineEdit.text()

		return key
	
	def auto_resize(self):
		self.tabWidget.setGeometry(0, 0, self.size().width(), self.size().height())
		self.GeneralScrollArea.setGeometry(0, 0, self.tabWidget.size().width(), self.tabWidget.size().height())
		self.KeysScrollArea.setGeometry(0, 0, self.tabWidget.size().width(), self.tabWidget.size().height())

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	global Settings
	SettingsWindow = QtWidgets.QMainWindow()

	Settings = Ui_SettingsWindow(SettingsWindow)
	Settings.show()
	sys.exit(app.exec_())