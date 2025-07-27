import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QFont, QIntValidator
from PyQt6.QtCore import Qt
from functools import partial

# Encapsulation: Protects user data by making attributes private and providing methods to access them.
class User:
    users_db = {}  # Temporary dictionary to store user credentials

    def __init__(self, username, password):
        self.__username = username  # Private variable for username
        self.__password = password  # Private variable for password

    def save_user(self):
        User.users_db[self.__username] = self.__password

    @staticmethod
    def authenticate(username, password):
        return User.users_db.get(username) == password

# --Product Class--
# Encapsulation:
class Product:
    def __init__(self, name, price, image_filename):
        self.__name = name  # Private variable for product name
        self.__price = price  # Private variable for product price
        self.__image_filename = image_filename  # Private variable for product image filename

    def get_name(self):
        return self.__name  # Getter for product name

    def get_price(self):
        return self.__price  # Getter for product price

    def get_image_filename(self):
        return self.__image_filename  # Getter for product image filename

# --ProductWidget Class--
# Inheritance: Inheriting from QGroupBox to create a custom product widget
class ProductWidget(QGroupBox):
    def __init__(self, product, image_path):
        super().__init__(f"{product.get_name()} ----> Rs.{product.get_price()}")
        self.product = product
        self.image_path = image_path
        self.quantity_input = QLineEdit()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Product Image
        image_label = QLabel(self)
        image_file = f"{self.image_path}/{self.product.get_image_filename()}"
        
        # Ensure the image file exists and is valid
        pixmap = QPixmap(image_file)
        if pixmap.isNull():
            pixmap = QPixmap("default_image.png")  # Provide a default image if the file is not found
        pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Quantity Input
        self.quantity_input.setPlaceholderText("Enter quantity")
        self.quantity_input.setValidator(QIntValidator(0, 999))
        self.quantity_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.quantity_input.setFont(QFont("Arial", 12))
        self.quantity_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 3px solid #191970;
                border-radius: 12px;
                background-color: #f2f2f3;
                color: #333;
                font-size: 14px;
                font-weight: bold;
                text-align: center;
            }
            QLineEdit:focus {
                border: 2px solid #3e8e41;
            }
        """)
        layout.addWidget(self.quantity_input)
        self.setLayout(layout)

    def get_quantity(self):
        return int(self.quantity_input.text() or 0)

# --Receipt Class--
# Abstraction: Provides a high-level interface to generate receipt text without exposing the details.
class Receipt:
    def __init__(self, username, items, total_amount):
        self.username = username
        self.items = items
        self.total_amount = total_amount

    def generate_receipt_text(self):
        receipt = f"Receipt for: {self.username}\n\n"
        for item, quantity in self.items.items():
            receipt += f"{item} x {quantity}\n"
        receipt += f"\nTotal Amount: Rs. {self.total_amount:.2f}"
        return receipt

# --SignIn Window--
class SignInWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MHR TECH")
        self.setGeometry(200, 200, 500, 450)
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1a1a2e;
            }
            QLabel {
                color: white;
                font-size: 16px;
                margin-bottom: 10px;
            }
            QLineEdit {
                padding: 10px;
                border: 2px solid #1f4068;
                border-radius: 10px;
                font-size: 14px;
                color: #eaeaea;
                background-color: #162447;
            }
            QLineEdit:focus {
                border: 2px solid #e43f5a;
            }
            QPushButton {
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 10px;
                color: white;
            }
            QPushButton#login {
                background-color: #0f3460;
            }
            QPushButton#login:hover {
                background-color: #e43f5a;
            }
            QPushButton#signup {
                background-color: #e43f5a;
            }
            QPushButton#signup:hover {
                background-color: #0f3460;
            }
        """)

        layout = QVBoxLayout()

        title_label = QLabel("Welcome To Our E-Store!")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title_label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.setObjectName("login")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setObjectName("signup")
        self.signup_button.clicked.connect(self.open_signup_window)
        layout.addWidget(self.signup_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if User.authenticate(username, password):
            QMessageBox.information(self, "Success", "Login Successful!")
            self.main_window = CheckoutApp(username)
            self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials!")

    def open_signup_window(self):
        self.signup_window = SignUpWindow()
        self.signup_window.show()
        self.close()


class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Up")
        self.setGeometry(100, 100, 400, 300)
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1a1a2e;
            }
            QLabel {
                color: white;
                font-size: 16px;
                margin-bottom: 10px;
            }
            QLineEdit {
                padding: 10px;
                border: 2px solid #1f4068;
                border-radius: 10px;
                font-size: 14px;
                color: #eaeaea;
                background-color: #162447;
            }
            QLineEdit:focus {
                border: 2px solid #e43f5a;
            }
            QPushButton {
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 10px;
                color: white;
            }
            QPushButton#register {
                background-color: #e43f5a;
            }
            QPushButton#register:hover {
                background-color: #0f3460;
            }
            QPushButton#back {
                background-color: #0f3460;
            }
            QPushButton#back:hover {
                background-color: #e43f5a;
            }
        """)

        layout = QVBoxLayout()

        title_label = QLabel("Register Your Account!")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title_label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Choose a username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Choose a password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.register_button = QPushButton("Register")
        self.register_button.setObjectName("register")
        self.register_button.clicked.connect(self.register)
        layout.addWidget(self.register_button)

        self.back_button = QPushButton("Back to Login")
        self.back_button.setObjectName("back")
        self.back_button.clicked.connect(self.open_login_window)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username and password:
            User(username, password).save_user()
            QMessageBox.information(self, "Success", "User Registered Successfully!")
            self.open_login_window()
        else:
            QMessageBox.warning(self, "Error", "Please enter valid credentials!")

    def open_login_window(self):
        self.login_window = SignInWindow()
        self.login_window.show()
        self.close()

# --Main Checkout Window--
# Polymorphism: Overriding the `update_labels` function allows flexibility in updating the values.
class CheckoutApp(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle("Check N Pay")
        self.setGeometry(100, 100, 1000, 700)
        self.products = self.create_products()
        self.image_path = r"C:\Roshaan's Work\Programming Fundamental Projects\image"
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
     main_layout = QVBoxLayout(main_widget)

    # Add a stylish header
     header_label = QLabel("Welcome to MHR Soccer Cleats Store", self)
     header_label.setFont(QFont("Stencil Std", 28))
     header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
     header_label.setStyleSheet("""
        background-color: #2C3E50;
        color: white;
        padding: 20px;
        border-radius: 8px;
    """)
     main_layout.addWidget(header_label)

    # Product Grid
     grid_layout = QGridLayout()
     grid_layout.setSpacing(20)

    # Initialize product_widgets list
     self.product_widgets = []

     for row, product in enumerate(self.products):
        product_widget = ProductWidget(product, self.image_path)
        product_widget.setStyleSheet("""
            QGroupBox {
                background-color: #e6f7ff;
                border: 2px solid #ddd;
                border-radius: 10px;
                padding: 10px;
            }
            QLabel {
                color: #333;
            }
        """)
        grid_layout.addWidget(product_widget, row // 2, row % 2)
        self.product_widgets.append(product_widget)

     scroll_area = QScrollArea()
     scroll_area.setWidgetResizable(True)
     scroll_content = QWidget()
     scroll_content.setLayout(grid_layout)
     scroll_area.setWidget(scroll_content)

     main_layout.addWidget(scroll_area)

    # Stylish Checkout Area
     checkout_area = QWidget()
     checkout_layout = QVBoxLayout(checkout_area)
     checkout_area.setStyleSheet("""
        background-color: #f0f5f9 ;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
    """)

     self.subtotal_label = QLabel("Subtotal: Rs. 0", self)
     self.subtotal_label.setFont(QFont("Arial", 16))
     checkout_layout.addWidget(self.subtotal_label)

     self.discount_label = QLabel("Discount: Rs. 0", self)
     self.discount_label.setFont(QFont("Arial", 16))
     checkout_layout.addWidget(self.discount_label)

     self.tax_label = QLabel("Tax: Rs. 0", self)
     self.tax_label.setFont(QFont("Arial", 16))
     checkout_layout.addWidget(self.tax_label)

     self.total_label = QLabel("Total Amount: Rs. 0", self)
     self.total_label.setFont(QFont("Arial", 18))
     self.total_label.setStyleSheet("color: #3f51b5;")
     checkout_layout.addWidget(self.total_label)

     button_layout = QHBoxLayout()
     self.calculate_button = QPushButton("Checkout")
     self.calculate_button.setStyleSheet("""
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
    """)
     self.calculate_button.clicked.connect(self.checkout)
     button_layout.addWidget(self.calculate_button)

     self.reset_button = QPushButton("Reset")
     self.reset_button.setStyleSheet("""
        background-color: #f44336;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
    """)
     self.reset_button.clicked.connect(self.reset_fields)
     button_layout.addWidget(self.reset_button)

     checkout_layout.addLayout(button_layout)
     main_layout.addWidget(checkout_area)

     self.setCentralWidget(main_widget)

    def checkout(self):
        items = {}
        subtotal = 0
        discount = 0.10  # 10% discount
        tax_rate = 0.18  # 18% tax

        for widget in self.product_widgets:
            quantity = widget.get_quantity()
            if quantity > 0:
                items[widget.product.get_name()] = quantity
                subtotal += quantity * widget.product.get_price()

        if not items:
            QMessageBox.warning(self, "Warning", "No items selected!")
            return

        # Apply discount
        discount_amount = subtotal * discount
        # Apply tax
        tax_amount = subtotal * tax_rate
        total_amount = subtotal - discount_amount + tax_amount

        # Update the labels
        self.update_labels(subtotal, discount_amount, tax_amount, total_amount)

        # Generate Receipt
        receipt = Receipt(self.username, items, total_amount)
        QMessageBox.information(self, "Receipt", receipt.generate_receipt_text())

    def reset_fields(self):
        reply = QMessageBox.question(self, 'Reset Confirmation', 
                                     'Are you sure you want to reset the fields?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            for widget in self.product_widgets:
                widget.quantity_input.clear()
            self.update_labels(0, 0, 0, 0)

    def update_labels(self, subtotal, discount, tax, total):
        self.subtotal_label.setText(f"Subtotal: Rs. {subtotal:.2f}")
        self.discount_label.setText(f"Discount: Rs. {discount:.2f}")
        self.tax_label.setText(f"Tax: Rs. {tax:.2f}")
        self.total_label.setText(f"Total Amount: Rs. {total:.2f}")


# --Main Execution--
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = SignInWindow()
    login_window.show()
    sys.exit(app.exec())
