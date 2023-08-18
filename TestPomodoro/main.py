import sys
from PySide6.QtWidgets import (
    QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QWidget, QLineEdit
)
from PySide6.QtCore import QTimer, Slot

class Pomodoro(QWidget):

    def __init__(self):
        super().__init__()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        
        # Session length variable
        self.session_length = 25*60
        self.pomodoro_counter = 0
        
        self.label = QLabel('25:00')
        self.pomodoro_label = QLabel("Pomodoro: 0")
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_timer)
        self.reset_button = QPushButton('Reset')
        self.reset_button.clicked.connect(self.reset_timer)
        self.custom_length_input = QLineEdit()
        self.custom_length_button = QPushButton("Set Custom Session Length")
        self.custom_length_button.clicked.connect(self.set_custom_session_length)
        self.custom_break_input = QLineEdit()
        self.custom_break_button = QPushButton("Set Custom Break Length")
        self.custom_break_button.clicked.connect(self.set_custom_break_length)
        
        # Session length button
        self.length_button = QPushButton('Short Session')
        self.length_button.clicked.connect(self.switch_session_length)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pomodoro_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.length_button)
        self.setLayout(layout)

        # Layout for custom session length
        custom_length_layout = QHBoxLayout()
        custom_length_layout.addWidget(self.custom_length_input)
        custom_length_layout.addWidget(self.custom_length_button)
        layout.addLayout(custom_length_layout)

        custom_break_layout = QHBoxLayout()
        custom_break_layout.addWidget(self.custom_break_input)
        custom_break_layout.addWidget(self.custom_break_button)
        layout.addLayout(custom_break_layout)

        self.show()

    def start_timer(self):
        if self.start_button.text() == "Pause":
            self.timer.stop()
            self.start_button.setText('Resume')
        else:
            if hasattr(self, 'time'):  # Check if 'time' attribute exists
                self.timer.start(1000)
                self.start_button.setText('Pause')
            else:
                self.time = self.session_length
                self.timer.start(1000)
                self.start_button.setText('Pause')
            # Rest of start_timer

        
    def switch_session_length(self):
        if self.session_length == 25*60:
            self.session_length = 60*60
            self.length_button.setText('Long Session')
        else:
            self.session_length = 25*60
            self.length_button.setText('Short Session')
            
        self.reset_timer()
        self.update_timer()
        
    def reset_timer(self):
        self.time = self.session_length
        self.update_timer()
        self.timer.stop()
        self.start_button.setText("Start")
        # Rest of reset_timer

    def update_timer(self):
        if self.time > 0:
            minutes, seconds = divmod(self.time, 60)
            timeformat = '{:02d}:{:02d}'.format(minutes, seconds)
            self.label.setText(timeformat)
            self.time -= 1
            if self.time == 0:
                self.pomodoro_counter += 1
                self.pomodoro_label.setText(f"Pomodoro: {self.pomodoro_counter}")

    def set_custom_session_length(self):
        custom_length_text = self.custom_length_input.text()
        try:
            custom_length_minutes = int(custom_length_text)
            if custom_length_minutes > 0:
                self.time = custom_length_minutes * 60
                self.update_timer()
        except ValueError:
            pass

    def set_custom_break_length(self):   
        custom_break_text = self.custom_break_input.text()
        try:
            custom_break_minutes = int(custom_break_text)
            if custom_break_minutes > 0:
                self.time = custom_break_minutes * 60
                self.update_timer()
        except ValueError:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Pomodoro()
    sys.exit(app.exec())