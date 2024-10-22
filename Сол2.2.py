import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QTabWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QListWidget, QComboBox, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class PizzaOrderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Заказ пиццы")
        self.setGeometry(100, 100, 800, 600)
        self.cart = []

        self.setupUI()
        self.show()

    def setupUI(self):
        tab_widget = QTabWidget()

        tab_widget.addTab(self.createPizzaSelectionTab(), "Выбор пиццы")
        tab_widget.addTab(self.createCustomPizzaTab(), "Собрать пиццу")
        tab_widget.addTab(self.createCartTab(), "Корзина")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)

        style_sheet = """
        QWidget{background-color: #FFA54F;}
        QLabel{background-color: #ffffff; border-radius: 5px; padding: 5px;}
        QPushButton{background-color: #FF0000; color: white; border-radius: 5px; padding: 10px;}
        QPushButton:pressed{background-color: #0056b3;}
        QListWidget{background-color: #ffffff; border-radius: 5px;}
        QComboBox{background-color: #ffffff; border-radius: 5px;}
        """
        self.setStyleSheet(style_sheet)

    def createPizzaSelectionTab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        pizzas = [
            ("С ветчиной и грибими", "1.png"),
            ("Пепперони", "3.jpg"),
            ("Овощная", "2.png")
        ]

        for name, image_path in pizzas:
            pizza_layout = QHBoxLayout()
            pizza_image = QLabel()
            pixmap = QPixmap(image_path).scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
            pizza_image.setPixmap(pixmap)
            
            pizza_name = QLabel(name)
            add_button = QPushButton("Добавить в корзину")
            add_button.clicked.connect(lambda checked, n=name: self.addToCart(n))
            
            pizza_layout.addWidget(pizza_image)
            pizza_layout.addWidget(pizza_name)
            pizza_layout.addWidget(add_button)
            layout.addLayout(pizza_layout)

        widget.setLayout(layout)
        return widget

    def createCustomPizzaTab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        dough_label = QLabel("Выберите тесто:")
        self.dough_combo = QComboBox()
        self.dough_combo.addItems(["Тонкое", "Толстое", "С сыром"])

        ingredients_label = QLabel("Выберите ингредиенты:")
        self.ingredients_list = QListWidget()
        self.ingredients_list.addItems(["Сыр", "Грибы", "Ветчина", "Ананас", "Пепперони"])

        add_button = QPushButton("Добавить в корзину")
        add_button.clicked.connect(self.addCustomPizzaToCart)

        layout.addWidget(dough_label)
        layout.addWidget(self.dough_combo)
        layout.addWidget(ingredients_label)
        layout.addWidget(self.ingredients_list)
        layout.addWidget(add_button)

        widget.setLayout(layout)
        return widget

    def createCartTab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.cart_list = QListWidget()

        checkout_button = QPushButton("Оформить заказ")
        checkout_button.clicked.connect(self.checkout)

        layout.addWidget(self.cart_list)
        layout.addWidget(checkout_button)

        widget.setLayout(layout)
        return widget

    def addToCart(self, pizza_name):
        self.cart.append(pizza_name)
        self.updateCart()

    def addCustomPizzaToCart(self):
        dough = self.dough_combo.currentText()
        ingredients = [item.text() for item in self.ingredients_list.selectedItems()]
        custom_pizza = f"Пицца на {dough} тесте с {', '.join(ingredients)}"
        self.cart.append(custom_pizza)
        self.updateCart()

    def updateCart(self):
        self.cart_list.clear()
        self.cart_list.addItems(self.cart)

    def checkout(self):
        QMessageBox.information(self, "Заказ оформлен", f"Вы заказали {len(self.cart)} пицц(ы). Спасибо!")
        self.cart.clear()
        self.updateCart()

app = QApplication(sys.argv)
window = PizzaOrderApp()
sys.exit(app.exec())
