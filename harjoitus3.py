from PySide6.QtWidgets import QWidget, QApplication, QLabel, QComboBox, QHBoxLayout
from PySide6.QtGui import QColor, QPalette

app = QApplication()
window = QWidget()

layout = QHBoxLayout()
label = QLabel('Color Selector')
combo = QComboBox()

combo.addItems(QColor.colorNames())

# def setColor(color):
#     label.setAutoFillBackground(True)
#     labelpalette = label.palette()
#     labelpalette.setColor(QPalette.ColorRole.Window,QColor(color))
#     label.setPalette(labelpalette)

# combo.currentTextChanged.connect(setColor)
combo.currentTextChanged.connect(lambda color: label.setStyleSheet(f"background-color:{color};"))
combo.currentTextChanged.connect(label.setText)

layout.addWidget(label)
layout.addWidget(combo)

window.setLayout(layout)

window.show()
app.exec()