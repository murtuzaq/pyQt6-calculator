import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget, )

WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35


class pyQTCalWindow:
    def __init__(self):
        self.__window = QMainWindow()
        self.__window.setWindowTitle("QT Calculator")
        self.__window.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.__generalLayout = QVBoxLayout()

        centralWidget = QWidget()
        centralWidget.setLayout(self.__generalLayout)
        self.__window.setCentralWidget(centralWidget)

        self.__create_display()
        self.__create_button()

    def __create_display(self):
        self.__display = QLineEdit()
        self.__display.setFixedHeight(DISPLAY_HEIGHT)
        self.__display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.__display.setReadOnly(True)

        self.__generalLayout.addWidget(self.__display)

    def __create_button(self):
        list_buttons = []
        list_keyboard = [["7", "8", "9", "/", "C"],
                         ["4", "5", "6", "*", "("],
                         ["1", "2", "3", "-", ")"],
                         ["0", "00", ".", "+", "="]]

        button_layout = QGridLayout()

        row = 0
        col = 0

        for list_row in list_keyboard:
            for column in list_row:
                key_text = column
                key = QPushButton(key_text)
                button_layout.addWidget(key, row, col)
                list_buttons.append(key)

                col = col + 1
            row = row + 1
            col = 0
        self.__generalLayout.addLayout(button_layout)

    def show(self):
        self.__window.show()


def main():
    app = QApplication([])

    cal_window = pyQTCalWindow()
    cal_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
