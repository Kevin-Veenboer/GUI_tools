import sys

from PySide6 import QtWidgets
import time


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Adding central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # Adding Vertial layout
        vbox = QtWidgets.QVBoxLayout(central_widget)
        self.textBox = QtWidgets.QTextEdit()
        vbox.addWidget(self.textBox)

        # Horizontal box for buttons
        hbox = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox)
        self.start_button = QtWidgets.QPushButton("Start")
        self.clear_button = QtWidgets.QPushButton("Clear")
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.clear_button)

        # Connecting siganls
        self.clear_button.clicked.connect(self.textBox.clear)
        self.start_button.clicked.connect(self.working)

    def working(self):
        self.textBox.append("Work is done")


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
