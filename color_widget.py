from PySide6.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout

from PySide6.QtGui import QColor, QPalette

class ColorWidget(QWidget):
    def __init__(self, color: str):
        super().__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window,QColor(color))
        self.setPalette(palette)

        self.show()



app = QApplication()
window = QWidget()

layout = QHBoxLayout(window)

col1 = QVBoxLayout()
col2 = QVBoxLayout()
col3 = QVBoxLayout()

col1.addWidget(ColorWidget('red'))
col1.addWidget(ColorWidget('green'))
col1.addWidget(ColorWidget('blue'))

col2.addWidget(ColorWidget('yellow'))

col3.addWidget(ColorWidget('pink'))
col3.addWidget(ColorWidget('purple'))

layout.addLayout(col1)
layout.addLayout(col2)
layout.addLayout(col3)

# layout = QHBoxLayout(window)
# layout.addWidget(ColorWidget('red'))
# layout.addWidget(ColorWidget('green'))
window.show()
window.setMinimumSize(500,500)
app.exec()