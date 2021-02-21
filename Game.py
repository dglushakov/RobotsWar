import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QGridLayout, QWidget, QPushButton, QAction, qApp, \
    QHBoxLayout


from Arena import Arena
from GameWindow import GameWindow

arena = Arena()
arena.reset()

app = QApplication(sys.argv)
ex = GameWindow(arena)
ex.show()
sys.exit(app.exec_())

