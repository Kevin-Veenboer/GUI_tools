import sys

from PySide6 import QtWidgets, QtGui
import time


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Adding central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # Adding Vertial layout
        self.vbox = QtWidgets.QVBoxLayout(central_widget)
        self.textBox = QtWidgets.QTextEdit()
        self.vbox.addWidget(self.textBox)

        # Horizontal box for buttons
        hbox = QtWidgets.QHBoxLayout()
        self.vbox.addLayout(hbox)
        self.start_button = QtWidgets.QPushButton("Start")
        self.clear_button = QtWidgets.QPushButton("Clear")
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.clear_button)

        # Test progress bar
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(4)

        # Connecting siganls
        self.clear_button.clicked.connect(self.textBox.clear)
        self.start_button.clicked.connect(self.working)

    def working(self):
        self.vbox.addWidget(self.progressBar)

        for val in range(0, 5):
            self.progressBar.setValue(val)
            self.textBox.append("Work is done")
            time.sleep(0.5)

    def external_func(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
