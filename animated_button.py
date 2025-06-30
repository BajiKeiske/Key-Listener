from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QTimer, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor

class AnimatedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.default_style = """
            QPushButton {
                background-color: #404040;
                border: 2px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
                padding: 10px;
                min-width: 40px;
            }
            QPushButton:hover {
                background-color: #606060;
            }
        """
        self.pressed_style = """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 2px solid #45a049;
                border-radius: 5px;
                font-size: 16px;
                padding: 10px;
                min-width: 40px;
            }
        """
        self.setStyleSheet(self.default_style)
        
    def animate_press(self):
        # Анимация нажатия
        self.setStyleSheet(self.pressed_style)
        
        # Возвращаем обычный стиль через 200 мс
        QTimer.singleShot(200, lambda: self.setStyleSheet(self.default_style))
        
        # Дополнительная анимация (опционально)
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(100)
        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.anim.setStartValue(self.geometry())
        self.anim.setEndValue(self.geometry().adjusted(1, 1, -1, -1))
        self.anim.start()