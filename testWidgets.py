from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton
from PyQt6.QtGui import QFont

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

class TestWidget1(QWidget):
    def __init__(self, btn_nextClicked):
        super().__init__()
        #widgets
        font = QFont("Open sans", pointSize=15)
        self.question = QLabel("<center>Вопрос 1</center>")
        self.btn_next = QPushButton("Далее")
        self.btn_next.setFont(font)
        self.question.setFont(font)
        self.rb1 = QRadioButton("Ответ 1")
        self.rb2 = QRadioButton("Ответ 2")
        self.rb3 = QRadioButton("Ответ 3")
        #handler events
        self.btn_next.clicked.connect(btn_nextClicked)
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.btn_next)
        self.setLayout(vbox)

class TestWidget2(QWidget):
    def __init__(self, btn_nextClicked):
        super().__init__()
        #widgets
        font = QFont("Open sans", pointSize=15)
        self.question = QLabel("<center>Вопрос 2</center>")
        self.btn_next = QPushButton("Далее")
        self.btn_next.setFont(font)
        self.question.setFont(font)
        self.rb1 = QRadioButton("Ответ 1")
        self.rb2 = QRadioButton("Ответ 2")
        self.rb3 = QRadioButton("Ответ 3")
        #handler events
        self.btn_next.clicked.connect(btn_nextClicked)
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.btn_next)
        self.setLayout(vbox)

class TestWidget3(QWidget):
    def __init__(self, btn_nextClicked):
        super().__init__()
        #widgets
        font = QFont("Open sans", pointSize=15)
        self.question = QLabel("<center>Вопрос 3</center>")
        self.btn_next = QPushButton("Далее")
        self.btn_next.setFont(font)
        self.question.setFont(font)
        self.rb1 = QRadioButton("Ответ 1")
        self.rb2 = QRadioButton("Ответ 2")
        self.rb3 = QRadioButton("Ответ 3")
        #handler events
        self.btn_next.clicked.connect(btn_nextClicked)
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
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