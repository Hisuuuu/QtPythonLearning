import sys
from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__() #Constructor
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press me!")

        self.setCentralWidget(button)