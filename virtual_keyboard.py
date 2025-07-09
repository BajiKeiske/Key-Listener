from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QGridLayout
from PyQt6.QtCore import Qt
from animated_button import AnimatedButton
from pynput.keyboard import Key, KeyCode, Controller, Listener

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
        self.output_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                border: 2px solid #aaa;
                border-radius: 5px;
                padding: 10px;
                background-color: #404040;
                min-height: 40px;
            }
        """)
        layout.addWidget(self.output_label)

        self.buttons = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", "\\"],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'],
            ['Space', 'Backspace', 'Enter']
        ]
        self.create_keyboard()
        layout.addLayout(self.keyboard_layout)
        keyboard_listener = Listener(on_press=self.on_key_pressed)
        keyboard_listener.start()

    def create_keyboard(self):
        self.keyboard_layout = QGridLayout()
        self.keyboard_layout.setSpacing(5)

        special_sizes = {
            'Space': (3, 10),
            'Backspace': (2, 10),
            'Enter': (2, 10)
        }

        for row_idx, row in enumerate(self.buttons):
            for col_idx, key in enumerate(row):
                btn = AnimatedButton(key)
                
                if key in special_sizes:
                    span, width = special_sizes[key]
                    btn.setMinimumWidth(width)
                    self.keyboard_layout.addWidget(btn, row_idx, col_idx, 1, span)
                else:
                    self.keyboard_layout.addWidget(btn, row_idx, col_idx)
                
                btn.clicked.connect(self.on_key_pressed)

    def on_key_pressed(self, key: KeyCode):
        '''print(key.__str__().upper())
        v_key = ''
        if (key.__str__().upper() in self.buttons):
            v_key = key
        #sender = self.sender()  # Получаем кнопку, которая была нажата
        
        
        # Анимируем нажатие
        #sender.animate_press()'''
        
        current_text = self.output_label.text()
        
        '''if key == Key.space:
            new_text = current_text + '[SPACE]'
        elif key == Key.backspace:
            new_text = current_text + '[BACKSPACE]'
        elif key == "ENTER":
            new_text = current_text + "\n"
        else:
            new_text = current_text + v_key'''

        self.output_label.clear()
        self.output_label.setText(key.__str__().upper())