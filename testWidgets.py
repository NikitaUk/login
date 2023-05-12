from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QRadioButton, QButtonGroup
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QPixmap

class StartWidget(QWidget):
    def __init__(self, btn_exitClicked, btn_enterClicked):
        super().__init__()
        #widgets
        font = QFont("Open sans", pointSize=15)
        self.error = QLabel("<center>Готовы ли вы пройти тест?</center>")
        self.btn_enter = QPushButton("Да")
        self.btn_exit = QPushButton("Выход")
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btn_enter)
        self.hbox.addWidget(self.btn_exit)
        self.error.setFont(font)
        #handler events
        self.btn_exit.clicked.connect(btn_exitClicked)
        self.btn_enter.clicked.connect(btn_enterClicked)
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.error)
        vbox.addLayout(self.hbox)
        self.setLayout(vbox)

class TestWidget(QWidget):
    rb_list = []
    def __init__(self, btn_nextClicked, questionName, answers):
        super().__init__()
        #widgets
        font = QFont("Open sans", pointSize=15)
        self.question = QLabel(f"<center>{questionName}</center>")
        self.btn_next = QPushButton("Далее")
        self.btn_next.setFont(font)
        self.question.setFont(font)
        #handler events
        self.btn_next.clicked.connect(btn_nextClicked)
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        for i in answers:
            rb = QRadioButton(i)
            vbox.addWidget(rb)
            self.rb_list.append(rb)
        vbox.addWidget(self.btn_next)
        self.setLayout(vbox)

class EndWidget(QWidget):
    def __init__(self):
        super().__init__()
        #widgets
        font = QFont("Open sans", pointSize=15)
        self.txt = QLabel("<center>Тест пройден</center>")
        self.txt.setFont(font)
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.txt)
        self.setLayout(vbox)