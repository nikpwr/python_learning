from PySide6.QtWidgets import QHBoxLayout, QFormLayout, QApplication, QLineEdit, QWidget, QLabel

app = QApplication()
window = QWidget()

layout = QHBoxLayout()

label = QLabel('The text')
label.setPalette
textInput = QLineEdit(placeholderText='Enter Text')

textInput.textChanged.connect(label.setText)

layout.addWidget(label)
layout.addWidget(textInput)
window.setLayout(layout)

window.show()
app.exec()