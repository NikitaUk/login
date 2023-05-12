from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtGui import QFont
import sys
from modalsWindow import ModalLogin, CaptchaLogin

class LoginWindow(QWidget):
    def enterClicked(self, login, password):
            if login == "a" and password == "b":
                self.modal = ModalLogin()
                self.modal.show()
                self.close()
            else:
                self.captchaModal = CaptchaLogin()
                self.captchaModal.show()

    
    def __init__(self):
        super().__init__()
        #window settings
        self.setWindowTitle("Вход")
        self.setFixedSize(300, 400)
        #widgets
        self.login_lbl = QLabel("Введите логин:")
        self.password_lbl = QLabel("Введите пароль:")
        self.login_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.enter_btn = QPushButton("Вход")
        #widgets settings
        font = QFont("Open sans", pointSize=25)
        font_btn = QFont("Open sans", pointSize=20)
        self.login_lbl.setFont(font)
        self.login_edit.setFont(font)
        self.password_lbl.setFont(font)
        self.password_edit.setFont(font)
        self.enter_btn.setFont(font_btn)
        self.login_edit.setPlaceholderText("Логин")
        self.password_edit.setPlaceholderText("Пароль")
        #handler events
        self.enter_btn.clicked.connect(lambda: self.enterClicked(self.login_edit.text(), self.password_edit.text()))
        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.login_lbl)
        vbox.addWidget(self.login_edit)
        vbox.addWidget(self.password_lbl)
        vbox.addWidget(self.password_edit)
        vbox.addWidget(self.enter_btn)
        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    app.exec()