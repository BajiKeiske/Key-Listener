from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QTimer, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor

import styles

class AnimatedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.default_style = styles.btn_default_style
        self.pressed_style = styles.btn_pressed_style
        self.setStyleSheet(self.default_style)
        
        self.original_geometry = self.geometry()
        
    def animate_press(self):
        self.setStyleSheet(self.pressed_style)
        
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(100)
        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.anim.setStartValue(self.original_geometry)
        self.anim.setEndValue(self.original_geometry.adjusted(2, 2, -2, -2))
        self.anim.start()
        
        QTimer.singleShot(200, self.reset_state)
        
    def reset_state(self):
        self.setStyleSheet(self.default_style)
        
        self.return_anim = QPropertyAnimation(self, b"geometry")
        self.return_anim.setDuration(100)
        self.return_anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.return_anim.setStartValue(self.geometry())
        self.return_anim.setEndValue(self.original_geometry)
        self.return_anim.start()