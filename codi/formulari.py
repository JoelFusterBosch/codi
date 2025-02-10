from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QHeaderView
from database import Database
import os
class Formulari(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestió d'Usuaris")
        self.setGeometry(100, 100, 600, 500)
        self.db = Database(db_name=os.path.join(os.path.dirname(__file__), 'users.db'))

    # Widget principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.layout = QVBoxLayout()
        main_widget.setLayout(self.layout)

        # Formulari (afegit directament a la finestra)
        self.name_input = QLineEdit()
        self.password_input = QLineEdit() 
        self.role_input = QLineEdit() 

        self.layout.addWidget(QLabel("Nom:"))
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(QLabel("Contrasenya:"))  
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(QLabel("Rol (Admin, Usuari, Convidat):")) 
        self.layout.addWidget(self.role_input)
    


