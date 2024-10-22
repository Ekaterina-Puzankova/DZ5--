import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt6.QtGui import QPixmap

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setGeometry(100, 100, 300, 200)

        # Установка цветовой схемы
        self.setStyleSheet("background-color: #AB82FF;")

        
        self.username_label = QLabel("Имя пользователя:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.check_login)

        
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

    def check_login(self):
        # Простая проверка логина и пароля
        if self.username_input.text() == "user" and self.password_input.text() == "password":
            self.profile_window = ProfileWindow()
            self.profile_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверное имя пользователя или пароль")



class ProfileWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Личный профиль")
        self.setGeometry(100, 100, 400, 300)

        # Установка цветовой схемы
        self.setStyleSheet("background-color: #7FFFD4;")

        # Фотография профиля
        self.profile_pic = QLabel(self)
        pixmap = QPixmap("фото1.jpg")
        self.profile_pic.setPixmap(pixmap.scaled(150, 150))
        
        self.profile_pic1 = QLabel(self)
        pixmap1 = QPixmap("фото2.jpg")
        self.profile_pic1.setPixmap(pixmap1.scaled(150, 150))

        # Личные данные
        self.name_label = QLabel("Имя: Бакуля Пузанков")
        self.email_label = QLabel("Email: bucky@krasauchik.com")
        self.status_label = QLabel("Статус: Курочка ван лав")

        
        # Используем QHBoxLayout для размещения фото рядом
        layout = QHBoxLayout()  
        layout.addWidget(self.profile_pic)
        layout.addWidget(self.profile_pic1)

        # Используем QVBoxLayout для размещения личных данных под фото
        data_layout = QVBoxLayout()
        data_layout.addWidget(self.name_label)
        data_layout.addWidget(self.email_label)
        data_layout.addWidget(self.status_label)

        # Объединяем макеты фото и личных данных
        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)  # Добавляем фото
        main_layout.addLayout(data_layout)  # Добавляем личные данные
        self.setLayout(main_layout)

app = QApplication(sys.argv)
login_window = LoginWindow()
login_window.show()
sys.exit(app.exec())
