# TS2 Gamepad Control
## Оглавление
- [TS2 Gamepad Control](#ts2-gamepad-control)
	- [Оглавление](#оглавление)
	- [Введение](#введение)
	- [Как скачать?](#как-скачать)
	- [Как пользоваться?](#как-пользоваться)
		- [Клавиши по умолчанию](#клавиши-по-умолчанию)
		- [Трей](#трей)
		- [Настройки](#настройки)
				- [General](#general)
				- [Keys](#keys)

## Введение
TS2 Gamepad Control - Приложение для управления ПК с помощью геймпада. ([Референс](http://controllercompanion.com/))

Были использованы следующие сторонние библиотеки:
- [inputs](https://pypi.org/project/inputs/) Но я редактировал её код (Изменённая версия находится в "modules")
- [PyQt5](https://pypi.org/project/PyQt5/)
- [mouse](https://pypi.org/project/mouse/)
- [keyboard](https://pypi.org/project/keyboard/)
- [pywin32](https://pypi.org/project/pywin32/)

## Как скачать?

- Перейдите в [релизы](https://github.com/Shoker2/TS2_Gamepad_Control/releases)
- Раскройте выпадающий список "Assets"
- Нажмите на TS2GamepadControl.zip и он скачается

## Как пользоваться?

### Клавиши по умолчанию

![image](https://user-images.githubusercontent.com/66993983/213866826-c1567142-03bb-46e4-8119-065be892962f.png)

- Левый джостик - управление мышью
- Правый джостик - прокручивание (вверх/вниз)
- A - Левая кнопка мыши
- B - Правая кнопка мыши
- X - Esc
- Y - Backspace (Стереть)
- Left Stick - Средняя кнопка мыши
- Right Stick - Enter
- RB - CTRL+V
- LB - открыть [Simple Keyboard](https://github.com/Shoker2/TS2-Simple-Keyboard)
- D-pad - стрелки
- Back + Start - Включить/выключить управления ПК

### Трей

![image](https://user-images.githubusercontent.com/66993983/213255450-c3e54c8d-7937-480a-a12e-cbc6520345fe.png)

Нажмите по значку приложения в трее, чтобы открыть меню. В это мены вы можете выбрать:
- Exit - Выйти из приложения
- Settings - Открыть настройки

### Настройки

##### General

![image](https://user-images.githubusercontent.com/66993983/213396103-5badec0a-25a4-4a41-916d-05696f586613.png)

- Mouse Speed - Скорость движения мыши (1 - 100)
- Scroll Speed - Скорость прокрутки (1 - 100)
- Dead Zone - Зона нечувствительности джойстиков геймпада (1 - 40)
- Turn off/on hotkey - Сочетание клавиш геймпада для включения/выключения управления ПК
- Add to startup - Запуск приложения вместе с ПК

##### Keys

Вкладка для настройки кнопок геймпада

![image](https://user-images.githubusercontent.com/66993983/213396358-b82952f1-db3a-476e-a0a0-96688fef2b55.png)

- Key - Кнопка геймпада
- Don't use - Не использовать
- Use hotkey - Использовать кнопки клавиатуры и мышь (ниже 3 списка с кнопками клавиатуры и мышки)
- Use cmd command - Использовать командную строку (ниже нужно вписать команду)

[:arrow_up: К оглавлению](#оглавление)