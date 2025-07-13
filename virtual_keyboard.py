from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                            QLabel, QGridLayout, QMessageBox)
from PyQt6.QtCore import Qt, QTimer
from pynput.keyboard import Key, Listener
from animated_button import AnimatedButton
import styles

class VirtualKeyboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Virtual Keyboard")
        self.setFixedSize(1000, 600)
        
        # Настройка центрального виджета
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Лейбл для отображения нажатий
        self.output_label = QLabel("Нажмите любую клавишу...")
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_label.setStyleSheet(styles.label_style)
        layout.addWidget(self.output_label)
        
        # Создание виртуальной клавиатуры
        self.buttons_layout = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'Enter'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Space']
        ]
        
        self.key_to_button = {}
        self.pressed_keys = set()
        self.create_keyboard()
        layout.addLayout(self.keyboard_layout)
        
        # Таймер для проверки комбинаций
        self.combo_timer = QTimer()
        self.combo_timer.timeout.connect(self.check_combinations)
        self.combo_timer.start(100)  # Проверка каждые 100 мс
        
        # Запуск слушателя клавиатуры
        self.listener = Listener(on_press=self.on_key_press, on_release=self.on_key_release)
        self.listener.start()
    
    def create_keyboard(self):
        self.keyboard_layout = QGridLayout()
        self.keyboard_layout.setSpacing(10)
        
        for row_idx, row in enumerate(self.buttons_layout):
            for col_idx, key in enumerate(row):
                btn = AnimatedButton(key)
                
                # Специальные размеры для больших кнопок
                if key == 'Space':
                    self.keyboard_layout.addWidget(btn, row_idx, col_idx, 1, 3)
                    btn.setMinimumWidth(200)
                elif key in ['Backspace', 'Enter']:
                    self.keyboard_layout.addWidget(btn, row_idx, col_idx, 1, 2)
                    btn.setMinimumWidth(100)
                else:
                    self.keyboard_layout.addWidget(btn, row_idx, col_idx)
                
                btn.clicked.connect(lambda _, k=key: self.on_virtual_key_press(k))
                self.key_to_button[key.lower()] = btn
    
    def on_virtual_key_press(self, key):
        """Обработка нажатия виртуальной кнопки"""
        self.animate_button(key)
        self.update_output(key)
    
    def on_key_press(self, key):
        """Обработка физического нажатия клавиши"""
        try:
            if key == Key.space:
                key_str = 'Space'
            elif key == Key.enter:
                key_str = 'Enter'
            elif key == Key.backspace:
                key_str = 'Backspace'
            elif key == Key.ctrl_l or key == Key.ctrl_r:
                key_str = 'Ctrl'
            elif key == Key.alt_l or key == Key.alt_r:
                key_str = 'Alt'
            else:
                key_str = key.char.upper() if hasattr(key, 'char') else str(key).split('.')[-1]
            
            self.pressed_keys.add(key_str.lower())
            self.animate_button(key_str)
            self.update_output(key_str)
            print(f'Нажата кнопка {key_str}')
        except AttributeError:
            pass
    
    def on_key_release(self, key):
        """Обработка отпускания клавиши"""
        try:
            if key == Key.space:
                key_str = 'Space'
            elif key == Key.enter:
                key_str = 'Enter'
            elif key == Key.backspace:
                key_str = 'Backspace'
            elif key == Key.ctrl_l or key == Key.ctrl_r:
                key_str = 'Ctrl'
            elif key == Key.alt_l or key == Key.alt_r:
                key_str = 'Alt'
            else:
                key_str = key.char.lower() if hasattr(key, 'char') else str(key).split('.')[-1].lower()
            
            if key_str.lower() in self.pressed_keys:
                self.pressed_keys.remove(key_str.lower())
        except AttributeError:
            pass
    
    def check_combinations(self):
        """Проверка комбинаций клавиш"""
        if {'ctrl', 'alt', 'k'}.issubset(self.pressed_keys):
            self.show_notification("Комбинация Ctrl+Alt+K!")
            self.pressed_keys.clear()
    
    def animate_button(self, key):
        """Анимация нажатия кнопки"""
        button = self.key_to_button.get(key.lower())
        if button:
            button.animate_press()
    
    def update_output(self, key):
        """Обновление лейбла с нажатыми клавишами"""
        if key == 'Space':
            self.output_label.setText('[SPACE]')
        elif key == 'Enter':
            self.output_label.setText('[ENTER]')
        elif key == 'Backspace':
            self.output_label.setText('[BACKSPACE]')
        else:
            self.output_label.setText(key)
    
    def show_notification(self, message):
        """Показ уведомления"""
        msg = QMessageBox()
        msg.setWindowTitle("Уведомление")
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
    
    def closeEvent(self, event):
        """Остановка слушателей при закрытии"""
        self.listener.stop()
        self.combo_timer.stop()
        super().closeEvent(event)