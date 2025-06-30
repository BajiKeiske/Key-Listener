from PyQt6.QtWidgets import QApplication

from virtual_keyboard import VirtualKeyboard

app = QApplication([])

window = VirtualKeyboard()
window.show()

app.exec()