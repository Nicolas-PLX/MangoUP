from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QTextEdit, QDialog
)
from PySide6.QtCore import Qt
import sys
from Launcher.model import Model
from Launcher.redirectText import RedirectText
from Launcher.customMenus import addDialog
from Save.configjson import test

class Launcher(QMainWindow):
    def __init__(self, qApp):
        super().__init__()
        
        self.qApp = qApp
        self.setWindowTitle("MangoUP")

        window_width = 1200
        window_height = 800
        self.resize(window_width, window_height)
        self.setFixedSize(window_width, window_height)

        self.model = Model()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Top Controls
        top_controls_layout = QHBoxLayout()

        add_manga_button = QPushButton("Ajouter")
        add_manga_button.setStyleSheet("background-color: green; width: 10em;")
        add_manga_button.clicked.connect(self.addMenu)
        top_controls_layout.addWidget(add_manga_button)

        rm_manga_button = QPushButton("Supprimer")
        rm_manga_button.setStyleSheet("background-color: red; width: 10em;")
        top_controls_layout.addWidget(rm_manga_button)


        # Main Frame
        middle_layout = QHBoxLayout()

        # List Manga Frame
        list_manga_layout = QVBoxLayout()
        self.list_manga_text = QListWidget()
        self.list_manga_text.setFixedSize(350, 750)
        list_manga_layout.addLayout(top_controls_layout)
        list_manga_layout.addWidget(self.list_manga_text)
        middle_layout.addLayout(list_manga_layout)

        # Log Control Frame
        log_control_layout = QVBoxLayout()
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setFixedSize(825, 660)
        log_control_layout.addWidget(self.log_text)
        middle_layout.addLayout(log_control_layout)

        main_layout.addLayout(middle_layout)

        # Bottom Controls
        bottom_controls_layout = QHBoxLayout()

        save_button = QPushButton("Sauvegarder")
        save_button.clicked.connect(self.model.save)
        bottom_controls_layout.addWidget(save_button)

        load_button = QPushButton("Charger")
        load_button.clicked.connect(self.model.load)
        bottom_controls_layout.addWidget(load_button)

        check_update_button = QPushButton("Check Update !")
        check_update_button.setStyleSheet("width: 60em;")
        bottom_controls_layout.addWidget(check_update_button)

        log_control_layout.addLayout(bottom_controls_layout)

        sys.stdout = RedirectText(self.log_text, self.qApp)


    def addMenu(self):
        dialog = addDialog()
        if dialog.exec_() == QDialog.Accepted:  # Attend que le dialogue soit fermé
            # Récupérer les valeurs des champs
            title = dialog.title_input.text()
            url = dialog.url_input.text()
            site = dialog.dropdown.currentText()
            number = float(dialog.number_input.text())

            new_title = self.model.add(title,site,url,number)

            if new_title != None:
                self.list_manga_text.addItem(new_title)

            #self.list_manga_text.addItem(f"{title} | {url} | {number}")
