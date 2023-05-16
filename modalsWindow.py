from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QStackedLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QPixmap
import functools
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
    isExit = False
    counter = 0
    acess = True
    def update_timer(self, timer): 
        self.attempt.setText(f"Ваша программа заблокирована на {self.total_seconds} секунд")
        if self.total_seconds == timer:
            self.attempt.setText("")
            self.timeq.stop()
            self.acess = True
        self.total_seconds -= 1

    def capthca_timer(self, timer):
        self.total_seconds = timer
        self.timeq = QTimer(self)
        self.timeq.setInterval(1000)
        self.timeq.timeout.connect(functools.partial(self.update_timer, 0))
        self.timeq.start()

    def captcha_clicked(self, captcha):
        if self.acess:
            self.timer = 0
            if captcha == "2vyk":
                self.isExit = True
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
                self.acess = False
                self.capthca_timer(self.timer)
    def closeEvent(self, e):
        if(not self.isExit):
            e.ignore()

    def __init__(self):
        super().__init__()
        #window settings
        self.setWindowTitle("Подтвердите, что вы не робот")
        self.setFixedSize(450, 250)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        #widgets
        self.captcha = QLabel()
        self.error = QLabel("<center>Введите текст с изображения</center>")
        self.captcha_edit = QLineEdit()
        self.attempt = QLabel("")
        self.btn = QPushButton("Ввести")
        #widget settings
        self.error.setObjectName("LabelModalWindow")
        self.captcha_edit.setObjectName("LabelModalWindow")
        self.attempt.setObjectName("LabelErrorModalWindow")
        self.captcha.setPixmap(QPixmap("./images/captcha.png"))
        #handler events
        self.btn.clicked.connect(lambda: self.captcha_clicked(self.captcha_edit.text()))
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