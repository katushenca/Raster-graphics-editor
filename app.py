from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv) # всегда только один экземпляр

window = QWidget() # widget qt окно
window.show() # по умолчанию окно скрыто

app.exec() # запускаем цикл событий

# пока из цикла не выйдем (из приложения) сюда не доберемся

