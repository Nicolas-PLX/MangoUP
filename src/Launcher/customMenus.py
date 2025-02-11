from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QPushButton, QDialog,
    QLineEdit, QLabel, QMessageBox, QComboBox
)
 


class addDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ajouter un Manga")
        self.setFixedSize(400, 350)

        # Create layout
        layout = QVBoxLayout()

        # Title input
        self.title_label = QLabel("Titre:")
        self.title_input = QLineEdit()
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_input)

        # URL input
        self.url_label = QLabel("URL:")
        self.url_input = QLineEdit()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)

        # Number input
        self.number_label = QLabel("Numéro (Double):")
        self.number_input = QLineEdit()
        self.number_input.setPlaceholderText("Exemple: 3.14")
        layout.addWidget(self.number_label)
        layout.addWidget(self.number_input)

        # Dropdown for selection
        self.dropdown_label = QLabel("Choisir une catégorie:")
        self.dropdown = QComboBox()
        self.dropdown.addItems(["Manganato"])
        layout.addWidget(self.dropdown_label)
        layout.addWidget(self.dropdown)

        # Buttons
        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Annuler")
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        # Connect signals
        self.ok_button.clicked.connect(self.validate_inputs)
        self.cancel_button.clicked.connect(self.reject)

        self.setLayout(layout)

    def validate_inputs(self):
        title = self.title_input.text().strip()
        url = self.url_input.text().strip()
        number_text = self.number_input.text().strip()

        # Validate title
        if not title:
            self.show_error("Le titre ne peut pas être vide.")
            return

        # Validate URL (basic check)
        if not url.startswith("http://") and not url.startswith("https://"):
            self.show_error("L'URL doit commencer par http:// ou https://.")
            return

        # Validate number
        try:
            number = float(number_text)
        except ValueError:
            self.show_error("Le numéro doit être un nombre décimal valide.")
            return

        # If all inputs are valid, accept the dialog
        self.accept()

    def show_error(self, message):
        QMessageBox.critical(self, "Erreur", message)