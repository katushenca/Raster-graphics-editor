from PyQt6.QtWidgets import QApplication
from windows.main_window import MainWindow
from Entities.userData import User

app = QApplication([])
user = User()
window = MainWindow(user)
user.main_window = window
window.show()
app.exec()
