from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QMainWindow,
    QLabel
)
from PySide6.QtCore import Qt
class CustomWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):

        widget = QWidget()
        layout = QVBoxLayout(widget)
        label = QLabel('Press the button to do something', alignment=Qt.AlignmentFlag.AlignCenter)
        button = QPushButton('Press me')
        button.clicked.connect(lambda: print('Button has been pressed'))
                               
        layout.addWidget(label)
        layout.addWidget(button)
        self.setCentralWidget(widget)

        self.show()

app = QApplication()
window = CustomWindow()
app.exec()