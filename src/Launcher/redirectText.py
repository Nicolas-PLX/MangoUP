from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QTextEdit
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor
class RedirectText:
    def __init__(self, widget, qApp):
        self.widget = widget
        self.qApp = qApp

    def write(self, text):
        cursor = self.widget.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.widget.setTextCursor(cursor)
        self.widget.ensureCursorVisible()
        self.qApp.processEvents()

    def flush(self):
        pass
