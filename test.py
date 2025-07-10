import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt, QTimer
from pynput import keyboard

class KeyTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Key Tracker")
        self.setGeometry(100, 100, 400, 200)
        
        self.pressed_keys = set()
        self.combination = {'ctrl', 'alt', 'k'}
        
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        self.label = QLabel("Нажмите любые клавиши...")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        self.check_timer = QTimer()
        self.check_timer.timeout.connect(self.check_combination)
        self.check_timer.start(100)  # Проверяем каждые 100 мс
        
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        self.listener.start()
        
    def on_press(self, key):
        try:
            key_char = key.char.lower()
        except AttributeError:
            key_char = str(key).split('.')[-1].lower()
        
        self.pressed_keys.add(key_char)
        self.update_label()
    
    def on_release(self, key):
        try:
            key_char = key.char.lower()
        except AttributeError:
            key_char = str(key).split('.')[-1].lower()
        
        if key_char in self.pressed_keys:
            self.pressed_keys.remove(key_char)
        self.update_label()
    
    def check_combination(self):
        if self.combination.issubset(self.pressed_keys):
            self.show_notification()
            self.pressed_keys.clear()
            self.update_label()
    
    def update_label(self):
        keys_text = " + ".join(sorted(self.pressed_keys))
        self.label.setText(f"Нажатые клавиши: {keys_text}")
    
    def show_notification(self):
        msg = QMessageBox()
        msg.setWindowTitle("Уведомление")
        msg.setText("Комбинация Ctrl+Alt+K сработала!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
    
    def closeEvent(self, event):
        self.listener.stop()
        self.check_timer.stop()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyTracker()
    window.show()
    sys.exit(app.exec())