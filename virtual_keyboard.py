from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QGridLayout, QMessageBox
from PyQt6.QtCore import Qt
from pynput.keyboard import Key, KeyCode, Listener
from animated_button import AnimatedButton

import styles
import time

class VirtualKeyboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Key listener")
        self.setFixedSize(800, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.output_label = QLabel("Нажмите клавишу...")
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_label.setStyleSheet(styles.label_style)
        layout.addWidget(self.output_label)

        self.buttons = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", "\\"],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
        ]
        self.pressed_keys = set()
        self.key_to_button = {}
        self.create_keyboard()
        layout.addLayout(self.keyboard_layout)
        
        self.keyboard_listener = Listener(on_press=self.on_key_pressed, on_release=self.on_release)
        self.keyboard_listener.start()

    def create_keyboard(self):
        self.keyboard_layout = QGridLayout()
        self.keyboard_layout.setSpacing(5)

        for row_idx, row in enumerate(self.buttons):
            for col_idx, key in enumerate(row):
                btn = AnimatedButton(key)
                self.keyboard_layout.addWidget(btn, row_idx, col_idx)
                btn.clicked.connect(lambda checked, k=key: self.on_virtual_key_pressed(k))
                self.key_to_button[key.lower()] = btn

    def on_virtual_key_pressed(self, key):
        """Обработка нажатия виртуальной кнопки"""
        self.animate_button(key)
        self.update_output_label(key)

    def on_key_pressed(self, key):
        """Обработка физического нажатия клавиши"""
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key).split('.')[-1]

        self.pressed_keys.add(key_char)

        try:
            if key == Key.space:
                self.animate_button('Space')
                self.update_output_label('Space')
            elif key == Key.enter:
                self.animate_button('Enter')
                self.update_output_label('Enter')
            elif key == Key.backspace:
                self.animate_button('Backspace')
                self.update_output_label('Backspace')
            else:
                if hasattr(key, 'char') and key.char:
                    key_char = key.char.upper()
                    button_key = key_char.lower()
                    if button_key in self.key_to_button:
                        self.animate_button(button_key)
                        self.update_output_label(key_char)
                if {Key.ctrl_l, 'p'}.issubset(self.pressed_keys):
                    self.show_notification()
        except AttributeError:
            pass

    def on_release(self, key):
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key).split('.')[-1]
        
        if key_char in self.pressed_keys:
            self.pressed_keys.remove(key_char)

    def animate_button(self, key):
        """Анимация кнопки по её тексту"""
        button = self.key_to_button.get(key.lower())
        if button:
            button.animate_press()
            

    def update_output_label(self, key):
        """Обновление текста на экране"""
        if key == 'Space':
            self.output_label.setText('[SPACE]')
        elif key == 'Enter':
            self.output_label.setText('[ENTER]')
        elif key == 'Backspace':
            self.output_label.setText('[BACKSPACE]')
        else:
            self.output_label.setText(key)

    def closeEvent(self, event):
        """Остановка слушателя клавиатуры при закрытии окна"""
        self.keyboard_listener.stop()
        super().closeEvent(event)

    def show_notification(self):
        msg = QMessageBox()
        msg.setWindowTitle("Уведомление")
        msg.setText("Вы нажали комбинацию клавиш!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()