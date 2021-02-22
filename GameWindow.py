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
        self.setGeometry(0, 0, 800, 400)

    def new_game(self):
        self.arena.reset()
        self.draw_arena()

    def draw_arena(self):
        for i in range(1, self.arena.ArenaWidth + 1):
            for j in range(1, self.arena.ArenaHeight + 1):
                button = QPushButton()
                button.setFixedSize(60, 60)
                button.setStyleSheet(f"background: white;")
                for robot in self.arena.get_robots():
                    if robot.corY == i and robot.corX == j:
                        button.setStyleSheet(f"background: {robot.color};")

                        w = ''
                        for weapon_slot in range(robot.weapon_slots):
                            w += str(robot.weapon_equipped[weapon_slot])
                        button_text = str(robot.id) + 'hp' + str(robot.health_points) + ' s' + str(robot.movement_speed) \
                                      + '\nw: ' + w + ' \nb' + str(robot.body)
                        button.setText(button_text)
                self.arena_grid.addWidget(button, i, j)

    def make_turn(self):
        self.arena.make_turn()
        self.draw_arena()


if __name__ == '__main__':
    arena = Arena()
    arena.reset()
    app = QApplication(sys.argv)
    ex = GameWindow(arena)
    ex.show()
    sys.exit(app.exec_())
