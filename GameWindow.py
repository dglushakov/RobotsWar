import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QAction, qApp, QGridLayout, QHBoxLayout, \
    QVBoxLayout

from Arena import Arena


class GameWindow(QMainWindow):

    def __init__(self, arena=None):
        super().__init__()
        self.arena = arena
        self.initUI()
        self.arena.reset()
        self.draw_arena()

    def initUI(self):
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(qApp.quit)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(exitAction)

        self.arena_grid = QGridLayout()
        self.update()
        # for robot in self.arena.get_robots():
        #     button = QPushButton()
        #     button.setFixedSize(40, 40)
        #     button.setStyleSheet(f"background: {robot.color};")
        #     self.arena_grid.addWidget(button, robot.corY, robot.corX)

        main_layout = QHBoxLayout()
        main_layout.addLayout(self.arena_grid)

        self.right_layout = QVBoxLayout()
        main_layout.addLayout(self.right_layout)

        button1 = QPushButton('New game')
        button1.clicked.connect(self.new_game)
        self.right_layout.addWidget(button1)

        btn_make_turn = QPushButton('Make turn')
        btn_make_turn.clicked.connect(self.make_turn)
        self.right_layout.addWidget(btn_make_turn)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        self.setGeometry(0, 0, 600, 300)

    def new_game(self):
        self.arena.reset()
        self.draw_arena()

    def draw_arena(self):
        for i in range(1, self.arena.ArenaWidth + 1):
            for j in range(1, self.arena.ArenaHeight + 1):
                button = QPushButton()
                button.setFixedSize(40, 40)
                button.setStyleSheet(f"background: white;")
                for robot in self.arena.get_robots():
                    if robot.corY == i and robot.corX == j:
                        button.setStyleSheet(f"background: {robot.color};")
                        button.setText(str(robot.id))
                self.arena_grid.addWidget(button, i, j)

        # if self.arena_grid.itemAtPosition(2, 3):
        #     btn = self.arena_grid.itemAtPosition(2, 3).widget()
        #     btn.setStyleSheet(f"background: yellow;")

        # btn = self.arena_grid.takeAt(2)
        # btn_widget = btn.widget()
        # btn_widget.deleteLater()

    def make_turn(self):
        self.arena.make_turn()
        self.draw_arena()

        # self.arena.make_turn()


if __name__ == '__main__':
    arena = Arena()
    arena.reset()
    app = QApplication(sys.argv)
    ex = GameWindow(arena)
    ex.show()
    sys.exit(app.exec_())
