
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setMinimumSize(700, 700)
        self.setWindowTitle("6.1 - GUI заказа еды")
        self.setUpMainWindow()
        self.show()

        style_sheet = """
        QWidget{background-color: #C92108;}
        QWidget#Tabs{background-color: #FCEBCD; border-radius: 4px}
        QWidget#ImageBorder{background-color: #FCF9F3; border-width: 2px; border-style: solid; border-radius: 4px; border-color: #FABB4C}
        QWidget#Side{background-color: #EFD096; border-radius: 4px}
        QLabel{background-color: #EFD096; border-width: 2px; border-style: solid; border-radius: 4px; border-color: #EFD096}
        QLabel#Header{background-color: #EFD096; border-width: 2px; border-style: solid; border-radius: 4px; border-color: #EFD096; padding-left: 10px; color: #961A07}
        QLabel#ImageInfo{background-color: #FCF9F3; border-radius: 4px;}
        QPushButton{background-color: #C92108; border-radius: 4px; padding: 6px; color: #FFFFFF}
        QPushButton:pressed{background-color: #C86354; border-radius: 4px; padding: 6px; color: #DFD8D7}
        """
        self.setStyleSheet(style_sheet)
        
    def setUpMainWindow(self):
        self.tab_bar = QTabWidget()
        self.pizza_tab = QWidget()
        self.pizza_tab.setObjectName("Tabs")
        self.wings_tab = QWidget()
        self.wings_tab.setObjectName("Tabs")
        self.tab_bar.addTab(self.pizza_tab, "Пицца")
        self.tab_bar.addTab(self.wings_tab, "Крылышки")

        self.pizzaTab()
        self.wingsTab()
        self.side_widget = QWidget()

        self.side_widget.setObjectName("Tabs")
        order_label = QLabel("ВАШ ЗАКАЗ")
        order_label.setObjectName("Header")

        items_box = QWidget()
        items_box.setObjectName("Side")
        pizza_label = QLabel("Тип пиццы: ")
        self.display_pizza_label = QLabel("")
        toppings_label = QLabel("Начинки: ")
        self.display_toppings_label = QLabel("")
        extra_label = QLabel("Дополнительно: ")
        self.display_wings_label = QLabel("")

        items_grid = QGridLayout()
        items_grid.addWidget(pizza_label, 0, 0, Qt.AlignmentFlag.AlignRight)
        items_grid.addWidget(self.display_pizza_label, 0, 1)
        items_grid.addWidget(toppings_label, 1, 0, Qt.AlignmentFlag.AlignRight)
        items_grid.addWidget(self.display_toppings_label, 1, 1)
        items_grid.addWidget(extra_label, 2, 0, Qt.AlignmentFlag.AlignRight)
        items_grid.addWidget(self.display_wings_label, 2, 1)
        items_box.setLayout(items_grid)

        side_v_box = QVBoxLayout()
        side_v_box.addWidget(order_label)
        side_v_box.addWidget(items_box)
        side_v_box.addStretch()
        self.side_widget.setLayout(side_v_box)

        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.tab_bar, 1)
        main_h_box.addWidget(self.side_widget)
        self.setLayout(main_h_box)

    def pizzaTab(self):
        tab_pizza_label = QLabel("СОЗДАЙТЕ СВОЮ СОБСТВЕННУЮ ПИЦЦУ")
        tab_pizza_label.setObjectName("Header")
        description_box = QWidget()
        description_box.setObjectName("ImageBorder")
        pizza_image_path = "images/pizza.png"  # Убедитесь, что путь к изображению корректен
        pizza_image = self.loadImage(pizza_image_path)
        pizza_desc = QLabel()
        pizza_desc.setObjectName("ImageInfo")
        pizza_desc.setText("""<p>Создаем для вас пиццу на заказ. Начните с вашего любимого коржа и добавьте любые начинки, а также идеальное количество сыра и соуса.</p>""")
        
       
        pizza_layout = QVBoxLayout()
        pizza_layout.addWidget(tab_pizza_label)
        pizza_layout.addWidget(pizza_image)
        pizza_layout.addWidget(pizza_desc)
        self.pizza_tab.setLayout(pizza_layout)

    def wingsTab(self):
        tab_wings_label = QLabel("ВЫБЕРИТЕ СВОИ КРЫЛЫШКИ")
        tab_wings_label.setObjectName("Header")

        wings_layout = QVBoxLayout()
        wings_layout.addWidget(tab_wings_label)
        self.wings_tab.setLayout(wings_layout)

    def loadImage(self, image_path):
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        image_label.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
        return image_label

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())


