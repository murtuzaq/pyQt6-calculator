import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

WINDOW_SIZE = 235


def main():
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("QT Calculator")
    window.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
