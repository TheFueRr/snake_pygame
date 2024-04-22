from PyQt6 import QtWidgets, QtGui, QtCore
import random

from game_over import Ui_Form
from main_gui import Ui_MainWindow


class Food:
    def __init__(self, width, height) -> None:
        self.bag = []

        self.width = width
        self.height = height
        self.image = QtGui.QImage('food/apple.png')

    def generate_food(self, count: int, snake):
        while count > 0:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if not ([x, y] in snake.body):
                self.bag.append([x, y])
                count -= 1


class Snake:
    def __init__(self, width, height) -> None:
        self.body = [[5, 5], [5, 6]]
        self.head = [5, 5]

        self.direction = 'left'
        self.height = height
        self.width = width
        self.grow = False

        self.left_image = QtGui.QImage('food/head_left.png')
        self.right_image = QtGui.QImage('food/head_right.png')
        self.up_image = QtGui.QImage('food/head_up.png')
        self.down_image = QtGui.QImage('food/head_down.png')

        self.image = self.left_image

    def move(self):
        if self.direction == 'left':
            self.image = self.left_image
            self.head = [self.head[0] - 1, self.head[1]]
            if self.head[0] == -1:
                self.head[0] = self.width - 1
        elif self.direction == 'right':
            self.image = self.right_image
            self.head = [self.head[0] + 1, self.head[1]]
            if self.head[0] == self.width:
                self.head[0] = 0
        elif self.direction == 'up':
            self.image = self.up_image
            self.head = [self.head[0], self.head[1] - 1]
            if self.head[1] == -1:
                self.head[1] = self.height - 1
        elif self.direction == 'down':
            self.image = self.down_image
            self.head = [self.head[0], self.head[1] + 1]
            if self.head[1] == self.height:
                self.head[1] = 0

        self.body.insert(0, self.head)
        if self.grow == False:
            self.body.pop()
        else:
            self.grow = False

    def is_dead(self):
        pass


class Board(QtWidgets.QFrame):
    AMOUNT_OF_FRUITS = 1
    SPEED = 80
    HEIGHTINBLOCKS = 20
    WIDTHINBLOCKS = 30

    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)

        self.timer = QtCore.QBasicTimer()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.hide_ui()

        self.snake = Snake(self.WIDTHINBLOCKS, self.HEIGHTINBLOCKS)
        self.food = Food(self.WIDTHINBLOCKS, self.HEIGHTINBLOCKS)

        self.ui.restart_pushButton.clicked.connect(self.restart_game)
        self.ui.save_pushButton.clicked.connect(self.read_name)
        self.ui.input_pushButton.clicked.connect(self.save_result)

    def save_result(self):
        name = self.ui.lineEdit.text()
        res = (len(self.snake.body) - 1)
        f = open("score.txt", 'r')
        text = f.read().split()
        new_text = []
        for i in range(0, len(text), 2):
            new_text.append([int(text[i + 1]), text[i]])
        new_text.append([res, name + ":"])
        new_text.sort()
        new_text = new_text[::-1]
        f.close()
        f = open("score.txt", 'w')
        for i in new_text:
            f.write(i[1] + " " + str(i[0]) + "\n")
        f.close()

    def hide_ui(self):
        self.ui.label.hide()
        self.ui.label_2.hide()
        self.ui.restart_pushButton.hide()
        self.ui.menu_pushButton.hide()
        self.ui.save_pushButton.hide()
        self.ui.lineEdit.hide()
        self.ui.input_pushButton.hide()

    def show_ui(self):
        self.ui.label.show()
        self.ui.label_2.show()
        self.ui.restart_pushButton.show()
        self.ui.menu_pushButton.show()
        self.ui.save_pushButton.show()

    def timerEvent(self, a0: QtCore.QTimerEvent) -> None:
        if a0.timerId() == self.timer.timerId():
            self.drop_food()
            self.snake.move()
            self.is_dead()
            self.colision()
            self.update()

    def block_width(self):
        return int(self.frameGeometry().width() / self.WIDTHINBLOCKS)

    def block_height(self):
        return int(self.frameGeometry().height() / self.HEIGHTINBLOCKS)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:

        painter = QtGui.QPainter(self)

        rect = self.contentsRect()

        boardtop = rect.bottom() - self.frameGeometry().height()
        self.drawimage(painter, rect.left() + self.snake.head[0] * self.block_width(),
                       boardtop + self.snake.head[1] * self.block_height(), self.snake.image)

        for cord in self.snake.body[1:]:
            self.drawrectangle(painter, rect.left() + cord[0] * self.block_width(),
                               boardtop + cord[1] * self.block_height())

        for cord in self.food.bag:
            self.drawimage(painter, rect.left() + cord[0] * self.block_width(),
                           boardtop + cord[1] * self.block_height(), self.food.image)

    def drawrectangle(self, painter: QtGui.QPainter, x, y):
        rect = QtCore.QRect(x, y, self.block_width(), self.block_height())
        painter.setBrush(QtGui.QColor(255, 0, 0, 0))
        painter.drawRect(rect)

    def drawimage(self, painter, x, y, image):
        rect = QtCore.QRect(x, y, self.block_width(), self.block_height())
        painter.drawImage(rect, image)

    def start(self):
        self.timer.start(self.SPEED, self)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        key = a0.key()

        if key == QtCore.Qt.Key.Key_Left:
            if self.snake.direction != 'right':
                self.snake.direction = 'left'
        elif key == QtCore.Qt.Key.Key_Right:
            if self.snake.direction != 'left':
                self.snake.direction = 'right'
        elif key == QtCore.Qt.Key.Key_Up:
            if self.snake.direction != 'down':
                self.snake.direction = 'up'
        elif key == QtCore.Qt.Key.Key_Down:
            if self.snake.direction != 'up':
                self.snake.direction = 'down'

    def drop_food(self):
        if len(self.food.bag) < self.AMOUNT_OF_FRUITS:
            self.food.generate_food(self.AMOUNT_OF_FRUITS - len(self.food.bag), self.snake)

    def colision(self):
        for i, cord in enumerate(self.food.bag):
            if cord == self.snake.head:
                self.snake.grow = True
                self.food.bag.pop(i)
                break

    def is_dead(self):
        for snake_part in self.snake.body[1:]:
            if snake_part == self.snake.head:
                self.show_ui()
                self.ui.label.setText(f'Your Score: {len(self.snake.body) - 1}')
                self.timer.stop()

    def restart_game(self):
        self.snake = Snake(self.WIDTHINBLOCKS, self.HEIGHTINBLOCKS)
        self.food = Food(self.WIDTHINBLOCKS, self.HEIGHTINBLOCKS)
        self.timer = QtCore.QBasicTimer()
        self.hide_ui()
        self.start()

    def read_name(self):
        self.ui.lineEdit.show()
        self.ui.input_pushButton.show()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.board = Board(self)
        self.ui.stackedWidget.addWidget(self.board)

        self.ui.start_pushButton.clicked.connect(self.start_game)
        self.ui.settings_pushButton.clicked.connect(self.open_settings)
        self.ui.score_pushButton.clicked.connect(self.open_score)

        self.ui.back_pushButton.clicked.connect(self.open_menu)
        self.ui.back_pushButton_1.clicked.connect(self.open_menu)

        self.board.ui.menu_pushButton.clicked.connect(self.open_menu)
        self.ui.radioButton_fast.clicked.connect(lambda x: self.speed('f'))
        self.ui.radioButton_medium.clicked.connect(lambda x: self.speed('m'))
        self.ui.radioButton_slow.clicked.connect(lambda x: self.speed('s'))
        self.ui.Amount_of_fruits.valueChanged.connect(self.amount_of_fruits)
        self.ui.Height_size.valueChanged.connect(self.change_height)
        self.ui.Width_size.valueChanged.connect(self.change_width)

        self.show()

    def change_width(self, cnt):
        self.board.WIDTHINBLOCKS = cnt

    def change_height(self, cnt):
        self.board.HEIGHTINBLOCKS = cnt

    def amount_of_fruits(self, cnt):
        self.board.AMOUNT_OF_FRUITS = cnt

    def speed(self, option: str):
        if option == 's':
            self.board.SPEED = 120
        if option == 'm':
            self.board.SPEED = 80
        if option == 'f':
            self.board.SPEED = 50

    def start_game(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.board.start()

    def open_menu(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def open_settings(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def open_score(self):
        f = open('score.txt', 'r')
        text = f.read()
        self.ui.textBrowser.setPlainText(text)
        self.ui.textBrowser.selectAll()
        self.ui.textBrowser.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ui.stackedWidget.setCurrentIndex(1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
