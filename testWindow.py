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
    def __init__(self, btn_nextClicked, btn_backClicked):
        super().__init__()
        #widgets
        self.question = QLabel("<center>Год крещения Руси</center>")
        self.btn_next = QPushButton("Далее")
        self.btn_back = QPushButton("Назад")
        self.rb1 = QRadioButton("988 г.")
        self.rb2 = QRadioButton("1127 г.")
        self.rb3 = QRadioButton("1456 г.")
        #handler events
        self.btn_next.clicked.connect(btn_nextClicked)
        self.btn_back.clicked.connect(btn_backClicked)
        #widget settings
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        self.btn_back.setObjectName("LabelQuestionTestWindow")
        self.question.setObjectName("LabelQuestionTestWindow")
        self.rb1.setObjectName('LabelTestWindow')
        self.rb2.setObjectName('LabelTestWindow')
        self.rb3.setObjectName('LabelTestWindow')
        #layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.question)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.btn_next)
        hbox.addWidget(self.btn_back)
        hbox.addWidget(self.btn_next)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        with open('style.css') as style:
            self.setStyleSheet(style.read())

class TestWidget2(QWidget):
    def __init__(self, btn_nextClicked, btn_backClicked):
        super().__init__()
        #widgets
        self.question = QLabel("<center>Кто правил в СССР первым</center>")
        self.btn_next = QPushButton("Далее")
        self.btn_back = QPushButton("Назад")
        self.rb1 = QRadioButton("Ельцин")
        self.rb2 = QRadioButton("Ленин")
        self.rb3 = QRadioButton("Сталин")
        #widget settings
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        self.btn_back.setObjectName("LabelQuestionTestWindow")
        self.question.setObjectName("LabelQuestionTestWindow")
        self.rb1.setObjectName('LabelTestWindow')
        self.rb2.setObjectName('LabelTestWindow')
        self.rb3.setObjectName('LabelTestWindow')
        #handler events
        self.btn_next.clicked.connect(btn_nextClicked)
        self.btn_back.clicked.connect(btn_backClicked)
        #layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.question)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.btn_next)
        hbox.addWidget(self.btn_back)
        hbox.addWidget(self.btn_next)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        with open('style.css') as style:
            self.setStyleSheet(style.read())

class TestWidget3(QWidget):
    def __init__(self, btn_nextClicked, btn_backClicked):
        super().__init__()
        #widgets
        self.question = QLabel("<center>Столица России</center>")
        self.btn_next = QPushButton("Далее")
        self.btn_back = QPushButton("Назад")
        self.rb1 = QRadioButton("Тбилиси")
        self.rb2 = QRadioButton("Воронеж")
        self.rb3 = QRadioButton("Москва")
        #handler events
        self.btn_next.clicked.connect(btn_nextClicked)
        self.btn_back.clicked.connect(btn_backClicked)
        #widget settings
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        self.btn_back.setObjectName("LabelQuestionTestWindow")
        self.question.setObjectName("LabelQuestionTestWindow")
        self.rb1.setObjectName('LabelTestWindow')
        self.rb2.setObjectName('LabelTestWindow')
        self.rb3.setObjectName('LabelTestWindow')
        #layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.question)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.btn_next)
        hbox.addWidget(self.btn_back)
        hbox.addWidget(self.btn_next)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        with open('style.css') as style:
            self.setStyleSheet(style.read())

class EndWidget(QWidget):
    def __init__(self, res, res_list):
        super().__init__()
        #widgets
        self.txt = QLabel("<center>Тест пройден</center>")
        self.txt = QLabel(f"<center>{res}</center>")
        #widget settings
        self.txt.setObjectName("LabelQuestionTestWindow")
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.txt)
        self.setLayout(vbox)
        with open('style.css') as style:
            self.setStyleSheet(style.read())
        result_txt_list = ("верно" if res_list[0] else "неверно", "верно" if res_list[1] else "неверно", "верно" if res_list[2] else "неверно")
        resultat = f"Результаты \n {res} \n Вопрос 1: {result_txt_list[0]} \n Вопрос 2: {result_txt_list[1]} \n Вопрос 3: {result_txt_list[2]}"
        with open('results.txt', "w", encoding="utf-8") as f:
            f.write(resultat)
