from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QCheckBox, QGroupBox

class StartWidget(QWidget):
    def __init__(self, btn_exitClicked, btn_enterClicked, name):
        super().__init__()
        #widgets
        self.hello = QLabel(f"<center>Привет {name}</center>")
        self.question = QLabel("<center>Готовы ли вы пройти тест?</center>")
        self.btn_enter = QPushButton("Да")
        self.btn_exit = QPushButton("Выход")
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btn_enter)
        self.hbox.addWidget(self.btn_exit)
        #widgets settings
        self.question.setObjectName('LabelTestWindow')
        self.hello.setObjectName('LabelTestWindow')
        #handler events
        self.btn_exit.clicked.connect(btn_exitClicked)
        self.btn_enter.clicked.connect(btn_enterClicked)
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.hello)
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
        self.question = QLabel("<center>Кто правил в СССР?</center>")
        self.btn_next = QPushButton("Далее")
        self.btn_back = QPushButton("Назад")
        self.cb1 = QCheckBox("Ельцин")
        self.cb2 = QCheckBox("Хрущев")
        self.cb3 = QCheckBox("Сталин")
        #widget settings
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        self.btn_back.setObjectName("LabelQuestionTestWindow")
        self.question.setObjectName("LabelQuestionTestWindow")
        self.cb1.setObjectName('LabelTestWindow')
        self.cb2.setObjectName('LabelTestWindow')
        self.cb3.setObjectName('LabelTestWindow')
        #handler events
        self.btn_next.clicked.connect(btn_nextClicked)
        self.btn_back.clicked.connect(btn_backClicked)
        #layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.question)
        vbox.addWidget(self.cb1)
        vbox.addWidget(self.cb2)
        vbox.addWidget(self.cb3)
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
        self.res_list = res_list
        self.res = res
        self.txt = QLabel("<center>Тест пройден</center>")
        self.txt1 = QLabel(f"<center>Вы набрали {res} из 6 баллов</center>")
        self.btn = QPushButton("Записать результаты в файл")
        self.gb = QGroupBox("Смотреть результаты")
        self.gb_lbl1 = QLabel(f"Вопрос 1: {int(res_list[0]/50)} б.")
        self.gb_lbl2 = QLabel(f"Вопрос 2: {int(res_list[1]/50)} б.")
        self.gb_lbl3 = QLabel(f"Вопрос 3: {int(res_list[2]/50)} б.")
        #widget settings
        self.txt.setObjectName("LabelQuestionTestWindow")
        self.txt1.setObjectName("LabelQuestionTestWindow")
        self.btn.setObjectName("LabelQuestionTestWindow")
        self.gb.setObjectName('GroupTestWindow')
        self.gb_lbl1.setObjectName('GroupTestLbl')
        self.gb_lbl2.setObjectName('GroupTestLbl')
        self.gb_lbl3.setObjectName('GroupTestLbl')
        #layout
        vbox = QVBoxLayout()
        vbox_group = QVBoxLayout()
        vbox_group.addWidget(self.gb_lbl1)
        vbox_group.addWidget(self.gb_lbl2)
        vbox_group.addWidget(self.gb_lbl3)
        self.gb.setLayout(vbox_group)
        vbox.addWidget(self.txt)
        vbox.addWidget(self.txt1)
        vbox.addWidget(self.gb)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)
        self.btn.clicked.connect(self.write_res_clicked)
        with open('style.css') as style:
            self.setStyleSheet(style.read())

    def write_res_clicked(self):
        resultat = f"Результаты \n Вы набрали {self.res} из 6 баллов \n Вопрос 1: {int(self.res_list[0]/50)} \n Вопрос 2: {int(self.res_list[1]/50)} \n Вопрос 3: {int(self.res_list[2]/50)}"
        with open('results.txt', "w", encoding="utf-8") as f:
            f.write(resultat)
