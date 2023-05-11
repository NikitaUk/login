from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QPixmap
import functools

class ModalLogin(QWidget):
    def __init__(self):
        super().__init__()
        #window settings
        self.setWindowTitle("Вы вошли")
        self.setFixedSize(400, 200)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        #widgets
        font = QFont("Open sans", pointSize=15)
        self.error = QLabel("<center>Верный пароль</center>")
        self.error.setFont(font)
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.error)
        self.setLayout(vbox)

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
        font = QFont("Open sans", pointSize=15)
        font_error = QFont("Open sans", pointSize=10)
        self.error.setFont(font)
        self.captcha_edit.setFont(font)
        self.attempt.setFont(font_error)
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