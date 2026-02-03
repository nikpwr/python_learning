from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QMessageBox,
    QPushButton,
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        button = QPushButton('Press me')
        button.clicked.connect(self.open_dialog)
        self.setCentralWidget(button)

    def open_dialog(self):
        result = QMessageBox.warning(self,'Hello','Hello',buttons=QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel)
        #dialog.setStandardButtons(QMessageBox.StandardButton.Save |QMessageBox.StandardButton.Discard)
        #dialog.setIcon(QMessageBox.Icon.Question)
        print(repr(result))

app = QApplication()
window = MainWindow()
window.show()

app.exec()
