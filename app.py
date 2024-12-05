from PyQt6.QtWidgets import QApplication
from windows.main_window import MainWindow
from Entities.userData import User

app = QApplication([])
user = User()
window = MainWindow(user)
window.show()
app.exec()
print(user.Canvas.qtColor, user.Canvas.width, user.Canvas.height)
