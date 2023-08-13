'''
from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked():
    print("You clicked the button, didn't you!")

app = QApplication()
button = QPushButton("Press me")

button.clicked.connect(button_clicked)

button.show()
app.exec() 
'''

from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QApplication, QSlider

def respond_to_slider(data):
    print("slider moved to: ", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
