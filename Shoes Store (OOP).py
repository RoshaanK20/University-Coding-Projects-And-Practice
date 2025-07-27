import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QFont, QIntValidator
from PyQt6.QtCore import Qt

class Product:
    def __init__(self, name, price, image_filename):
        self.name = name
        self.price = price
        self.image_filename = image_filename


class ProductWidget(QGroupBox):
    def __init__(self, product, image_path):
        super().__init__(f"{product.name} ----> Rs.{product.price}")
        self.setFont(QFont("Arial", 14))
        self.product = product
        self.image_path = image_path
        self.quantity_input = QLineEdit()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        image_label = QLabel(self)
        pixmap = QPixmap(f"{self.image_path}/{self.product.image_filename}")
        pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.quantity_input.setPlaceholderText(f"Enter quantity")
        self.quantity_input.setValidator(QIntValidator(0, 999))
        self.quantity_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.quantity_input.setFont(QFont("Arial", 12))
        self.quantity_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 3px solid #191970;
                border-radius: 12px;
                background-color: #f2f2f2;
                color: #333;
                font-size: 14px;
                font-weight: bold;
                text-align: center;
            }
            QLineEdit:focus {
                border: 2px solid #3e8e41;
            }
        """)
        layout.addWidget(self.quantity_input, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setStyleSheet("""
            QGroupBox {
                background-color: #e6f7ff;
                border: 2px solid #577fa1;
                border-radius: 10px;
                padding: 10px;
                margin-top: 10px;
            }
        """)

        self.setLayout(layout)

    def get_quantity(self):
        try:
            return int(self.quantity_input.text() or 0)
        except ValueError:
            return 0


class CheckoutApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check N Pay")
        self.setGeometry(100, 100, 1000, 700)

        self.tax_rate = 0.13
        self.discount_rate = 0.15
        self.image_path = r"C:\Roshaan's Work\Programming Fundamental Projects\image"
        self.products = self.create_products()
        self.init_ui()

    def create_products(self):
        return [
            Product("Nike Mercurial", 2500, "nike_mercurial.png"),
            Product("Nike Phantom", 2200, "nike_phantom.png"),
            Product("Nike Tiempo", 1900, "nike_tiempo.png"),
            Product("Puma Future", 2050, "puma_future.png"),
            Product("Puma King", 2020, "puma_king.png"),
            Product("Adidas Nemeziz", 2810, "adidas_nemeziz.png"),
            Product("Adidas F50", 2750, "adidas_f50.png"),
            Product("Adidas Predator", 2890, "adidas_predator.png"),
        ]

    def init_ui(self):
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)

        main_widget.setStyleSheet("background-color: #f0f5f9;")

        title_label = QLabel("MHR Soccer Cleats Store", self)
        title_label.setFont(QFont("Stencil Std", 28))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: white; background-color: #395A75; padding: 10px;")
        layout.addWidget(title_label)

        self.product_widgets = []
        products_layout = QVBoxLayout()

        for product in self.products:
            product_widget = ProductWidget(product, self.image_path)
            products_layout.addWidget(product_widget)
            self.product_widgets.append(product_widget)

        layout.addLayout(products_layout)

        # New Labels for Subtotal, Tax, Discount, and Final Total
        self.subtotal_label = QLabel("Subtotal: Rs. 0", self)
        self.subtotal_label.setFont(QFont("Arial", 18))
        layout.addWidget(self.subtotal_label)

        self.discount_label = QLabel("Discount: Rs. 0", self)
        self.discount_label.setFont(QFont("Arial", 18))
        layout.addWidget(self.discount_label)

        self.tax_label = QLabel("Tax: Rs. 0", self)
        self.tax_label.setFont(QFont("Arial", 18))
        layout.addWidget(self.tax_label)

        self.total_label = QLabel("Total Amount: Rs. 0", self)
        self.total_label.setFont(QFont("Arial", 18))
        layout.addWidget(self.total_label)

        self.calculate_button = QPushButton("Calculate Total", self)
        self.calculate_button.clicked.connect(self.calculate_total)
        self.calculate_button.setStyleSheet("background-color: lightgreen; font-size: 16px; padding: 10px;")
        layout.addWidget(self.calculate_button)

        self.reset_button = QPushButton("Reset", self)
        self.reset_button.clicked.connect(self.reset_fields)
        self.reset_button.setStyleSheet("background-color: lightcoral; font-size: 16px; padding: 10px;")
        layout.addWidget(self.reset_button)

        self.thanks_label = QLabel("")
        self.thanks_label.setFont(QFont("Arial", 24))
        self.thanks_label.setStyleSheet("color: black;")
        self.thanks_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.thanks_label)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QScrollArea.Shape.NoFrame)

        scroll_content = QWidget()
        scroll_content.setLayout(layout)

        scroll_area.setWidget(scroll_content)
        self.setCentralWidget(scroll_area)

    def calculate_total(self):
        subtotal = sum(widget.get_quantity() * widget.product.price for widget in self.product_widgets)
        if subtotal == 0:
            QMessageBox.warning(self, "Warning", "Please enter quantities for at least one product.")
            return

        discount = subtotal * self.discount_rate if subtotal > 4000 else 0
        tax = subtotal * self.tax_rate
        total_amount = subtotal - discount + tax

        self.update_labels(subtotal, discount, tax, total_amount)

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Total Amount")
        msg_box.setText(f"Your total amount is Rs. {total_amount:.2f}")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def update_labels(self, subtotal, discount, tax, total):
        self.subtotal_label.setText(f"Subtotal: Rs. {subtotal:.2f}")
        self.discount_label.setText(f"Discount: Rs. {discount:.2f}")
        self.tax_label.setText(f"Tax: Rs. {tax:.2f}")
        self.total_label.setText(f"Total Amount: Rs. {total:.2f}")
        self.thanks_label.setText("Thanks for shopping!")

    def reset_fields(self):
        reply = QMessageBox.question(self, 'Reset Confirmation', 
                                     'Are you sure you want to reset the fields?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            for widget in self.product_widgets:
                widget.quantity_input.clear()
            self.update_labels(0, 0, 0, 0)
            self.thanks_label.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CheckoutApp()
    window.show()
    sys.exit(app.exec())