from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QTimer, QPropertyAnimation, QEasingCurve

import styles

class AnimatedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumSize(60, 60)
        self.setStyleSheet(styles.btn_default_style)
    
    def animate_press(self):
        """Анимация нажатия кнопки"""
        self.setStyleSheet(styles.btn_pressed_style)
        
        QTimer.singleShot(200, self.reset_style)
    
    def reset_style(self):
        """Возврат к исходному стилю"""
        self.setStyleSheet(styles.btn_default_style)