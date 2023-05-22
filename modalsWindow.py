from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QStackedLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QTimer
import random as rnd
import string
from testWindow import StartWidget, TestWidget1, TestWidget2, TestWidget3, EndWidget

class ModalLogin(QWidget):
    results = [0, 0, 0]
    def __init__(self, name):
        super().__init__()
        #window settings
        self.name = name
        self.setWindowTitle("Пройти тест")
        self.setFixedSize(400, 300)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        #add stacks
        self.stackLayout = QStackedLayout()
        self.add_layouts()
        self.setLayout(self.stackLayout)

    def add_layouts(self):
        self.startWidget = StartWidget(lambda: self.close(), lambda:  self.enter_clicked(), self.name)
        self.testWidget1 = TestWidget1(lambda: self.next_clicked1(), lambda: self.back_clicked1())
        self.testWidget2 = TestWidget2(lambda: self.next_clicked2(), lambda: self.back_clicked2())
        self.testWidget3 = TestWidget3(lambda: self.next_clicked3(), lambda: self.back_clicked3())
        self.stackLayout.addWidget(self.startWidget)
        self.stackLayout.addWidget(self.testWidget1)
        self.stackLayout.addWidget(self.testWidget2)
        self.stackLayout.addWidget(self.testWidget3)

    def next_clicked1(self):
        if self.testWidget1.rb1.isChecked():
            self.results[0] += 100
        self.stackLayout.setCurrentIndex(2)

    def next_clicked2(self):
        if self.testWidget2.cb1.isChecked():
            self.results[1] -= 50
        if self.testWidget2.cb2.isChecked():
            self.results[1] += 50
        if self.testWidget2.cb3.isChecked():
            self.results[1] += 50
        if self.results[1] < 0:
            self.results[1] = 0
        self.stackLayout.setCurrentIndex(3)

    def next_clicked3(self):
        if self.testWidget3.rb3.isChecked():
            self.results[2] += 100
        j = 0
        for i in self.results:
            if i == 100:
                j+=2
            elif i == 50:
                j+=1
        self.endWidget = EndWidget(str(j), self.results)
        self.stackLayout.addWidget(self.endWidget)
        self.stackLayout.setCurrentIndex(4)

    def back_clicked1(self):
        self.stackLayout.setCurrentIndex(0)

    def back_clicked2(self):
        self.stackLayout.setCurrentIndex(1)

    def back_clicked3(self):
        self.stackLayout.setCurrentIndex(2)

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
            if self.counter == 2:
                self.timer = 3
            elif self.counter == 3:
                self.timer = 5
            elif self.counter > 3:
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
        captcha_string = string.digits + string.ascii_lowercase
        cap_text_list = rnd.sample(captcha_string, 4)
        self.cap_text = ''.join(cap_text_list)
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
