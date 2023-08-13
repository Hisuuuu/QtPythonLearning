import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from button_holder import ButtonHolder

'''
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__() #Constructor
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press me!")

        self.setCentralWidget(button)
'''
app = QApplication(sys.argv)

window = ButtonHolder()

window.show()
app.exec()

