from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QStackedLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QTimer
import random as rnd
from testWindow import StartWidget, TestWidget1, TestWidget2, TestWidget3, EndWidget

class ModalLogin(QWidget):
    def __init__(self):
        super().__init__()
        #window settings
        self.setWindowTitle("Пройти тест")
        self.setFixedSize(400, 200)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        #add stacks
        self.stackLayout = QStackedLayout()
        self.add_layouts()
        self.setLayout(self.stackLayout)

    def add_layouts(self):
        self.startWidget = StartWidget(lambda: self.close(), lambda:  self.enter_clicked())
        self.testWidget1 = TestWidget1(lambda: self.next_clicked1())
        self.testWidget2 = TestWidget2(lambda: self.next_clicked2())
        self.testWidget3 = TestWidget3(lambda: self.next_clicked3())
        self.endWidget = EndWidget()
        self.stackLayout.addWidget(self.startWidget)
        self.stackLayout.addWidget(self.testWidget1)
        self.stackLayout.addWidget(self.testWidget2)
        self.stackLayout.addWidget(self.testWidget3)
        self.stackLayout.addWidget(self.endWidget)

    def next_clicked1(self):
        if self.testWidget1.rb1.isChecked():
            self.stackLayout.setCurrentIndex(2)

    def next_clicked2(self):
        if self.testWidget2.rb2.isChecked():
            self.stackLayout.setCurrentIndex(3)

    def next_clicked3(self):
        if self.testWidget3.rb3.isChecked():
            self.stackLayout.setCurrentIndex(4)

    def enter_clicked(self):
        self.stackLayout.setCurrentIndex(1)

class CaptchaLogin(QWidget):
    counter = 0
    timer = 0
    def update_timer(self): 
        self.attempt.setText(f"Ваша программа заблокирована на {self.total_seconds} секунд")
        if self.total_seconds == 0:
            self.attempt.setText("")
            self.timeq.stop()
            self.btn.setEnabled(True)
        self.total_seconds -= 1

    def start_timer(self):
        self.btn.setEnabled(False)
        self.total_seconds = self.timer
        self.timeq.start()

    def capthca_timer(self):
        self.timeq = QTimer()
        self.timeq.setInterval(1000)
        self.timeq.timeout.connect(self.update_timer)
        self.start_timer()

    def captcha_clicked(self):
        if self.captcha_edit.text() == self.cap_text:
            self.timer = 0
            self.close()
        else:
            self.counter += 1
            if  self.counter == 2:
                self.timer = 3
            elif  self.counter == 3:
                self.timer = 5
            elif  self.counter > 3:
                self.timer = 10
        if self.timer > 0:
            self.capthca_timer()

    def __init__(self):
        super().__init__()
        #window settings
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Подтвердите, что вы не робот")
        self.setFixedSize(450, 250)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        #widgets
        self.cap_text = str(rnd.randint(1000, 9999))
        self.captcha = QLabel(f"<center>{self.cap_text}</center>")
        self.error = QLabel("<center>Введите текст с изображения</center>")
        self.captcha_edit = QLineEdit()
        self.attempt = QLabel("")
        self.btn = QPushButton("Ввести")
        #widget settings
        self.captcha.setObjectName("LabelCaptcha")
        self.error.setObjectName("LabelModalWindow")
        self.captcha_edit.setObjectName("LabelModalWindow")
        self.attempt.setObjectName("LabelErrorModalWindow")
        #handler events
        self.btn.clicked.connect(self.captcha_clicked)
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.captcha)
        vbox.addWidget(self.error)
        vbox.addWidget(self.captcha_edit)
        vbox.addWidget(self.attempt)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)
        with open('style.css') as style:
            self.setStyleSheet(style.read())
