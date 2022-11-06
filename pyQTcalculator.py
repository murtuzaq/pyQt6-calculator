import sys
from PyQt6.QtWidgets import (
    QApplication,
    # QGridLayout,
    # QLineEdit,
    QMainWindow,
    # QPushButton,
    # QVBoxLayout,
    QWidget, )

WINDOW_SIZE = 235


class pyQTCalWindow:
    def __init__(self):
        self.__window = QMainWindow()
        self.__window.setWindowTitle("QT Calculator")
        self.__window.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)

        centralWidget = QWidget()
        self.__window.setCentralWidget(centralWidget)

    def show(self):
        self.__window.show()


def main():
    app = QApplication([])

    cal_window = pyQTCalWindow()
    cal_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
