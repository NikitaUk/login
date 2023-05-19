from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton

class StartWidget(QWidget):
    def __init__(self, btn_exitClicked, btn_enterClicked):
        super().__init__()
        #widgets
        self.question = QLabel("<center>Готовы ли вы пройти тест?</center>")
        self.btn_enter = QPushButton("Да")
        self.btn_exit = QPushButton("Выход")
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btn_enter)
        self.hbox.addWidget(self.btn_exit)
        #widgets settings
        self.question.setObjectName('LabelTestWindow')

        #handler events
        self.btn_exit.clicked.connect(btn_exitClicked)
        self.btn_enter.clicked.connect(btn_enterClicked)
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        vbox.addLayout(self.hbox)
        self.setLayout(vbox)
        with open('style.css') as style:
            self.setStyleSheet(style.read())

class TestWidget1(QWidget):
    def __init__(self, btn_nextClicked):
        super().__init__()
        #widgets
        self.question = QLabel("<center>Вопрос 1</center>")
        self.btn_next = QPushButton("Далее")
        self.rb1 = QRadioButton("Ответ 1")
        self.rb2 = QRadioButton("Ответ 2")
        self.rb3 = QRadioButton("Ответ 3")
        #handler events
        self.btn_next.clicked.connect(btn_nextClicked)
        #widget settings
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        self.question.setObjectName("LabelQuestionTestWindow")
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.btn_next)
        self.setLayout(vbox)
        with open('style.css') as style:
            self.setStyleSheet(style.read())

class TestWidget2(QWidget):
    def __init__(self, btn_nextClicked):
        super().__init__()
        #widgets
        self.question = QLabel("<center>Вопрос 2</center>")
        self.btn_next = QPushButton("Далее")
        self.rb1 = QRadioButton("Ответ 1")
        self.rb2 = QRadioButton("Ответ 2")
        self.rb3 = QRadioButton("Ответ 3")
        #widget settings
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        self.question.setObjectName("LabelQuestionTestWindow")
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
        with open('style.css') as style:
            self.setStyleSheet(style.read())

class TestWidget3(QWidget):
    def __init__(self, btn_nextClicked):
        super().__init__()
        #widgets
        self.question = QLabel("<center>Вопрос 3</center>")
        self.btn_next = QPushButton("Далее")
        self.rb1 = QRadioButton("Ответ 1")
        self.rb2 = QRadioButton("Ответ 2")
        self.rb3 = QRadioButton("Ответ 3")
        #handler events
        self.btn_next.clicked.connect(btn_nextClicked)
        #widget settings
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        self.question.setObjectName("LabelQuestionTestWindow")
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.btn_next)
        self.setLayout(vbox)
        with open('style.css') as style:
            self.setStyleSheet(style.read())

class EndWidget(QWidget):
    def __init__(self):
        super().__init__()
        #widgets
        self.txt = QLabel("<center>Тест пройден</center>")
        #widget settings
        self.txt.setObjectName("LabelQuestionTestWindow")
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.txt)
        self.setLayout(vbox)
        with open('style.css') as style:
            self.setStyleSheet(style.read())
