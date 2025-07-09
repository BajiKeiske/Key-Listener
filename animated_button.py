from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QTimer, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor


class AnimatedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.default_style = """
            QPushButton {
                position: relative;
                border: none;
                background: transparent;
                padding: 0;
                outline: none;
                cursor: pointer;
                font-family: sans-serif;
            }

            QPushButton.shadow {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.25);
                border-radius: 8px;
                transform: translateY(2px);
                transition: transform 600ms cubic-bezier(0.3, 0.7, 0.4, 1);
            }

            QPushButton.edge {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                border-radius: 8px;
                background: linear-gradient(
                    to left,
                    hsl(217, 33%, 16%) 0%,
                    hsl(217, 33%, 32%) 8%,
                    hsl(217, 33%, 32%) 92%,
                    hsl(217, 33%, 16%) 100%
                );
            }

            QPushButton.front {
                position: relative;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 12px 28px;
                font-size: 1.25rem;
                color: white;
                background: hsl(217, 33%, 17%);
                border-radius: 8px;
                transform: translateY(-4px);
                transition: transform 600ms cubic-bezier(0.3, 0.7, 0.4, 1);
            }

            QPushButton:hover.shadow {
                transform: translateY(4px);
                transition: transform 250ms cubic-bezier(0.3, 0.7, 0.4, 1.5);
            }

            QPushButton:hover.front {
                transform: translateY(-6px);
                transition: transform 250ms cubic-bezier(0.3, 0.7, 0.4, 1.5);
            }

            QPushButton:active.shadow {
                transform: translateY(1px);
                transition: transform 34ms;
            }

            QPushButton:active.front {
                transform: translateY(-2px);
                transition: transform 34ms;
            }

            .QPushButton.front span {
                user-select: none;
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
        self.setStyleSheet(self.pressed_style)
        
        QTimer.singleShot(200, lambda: self.setStyleSheet(self.default_style))
        
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(100)
        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.anim.setStartValue(self.geometry())
        self.anim.setEndValue(self.geometry().adjusted(1, 1, -1, -1))
        self.anim.start()