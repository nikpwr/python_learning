from PySide6.QtWidgets import (
    QApplication, 
    QWidget, 
    QVBoxLayout,
    QPushButton,
    QSpinBox, 
    QFormLayout,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    )

app = QApplication()
window = QWidget()
window.show()

# layout = QVBoxLayout()
# layout.addWidget(QPushButton('Yksi'))
# layout.addWidget(QPushButton('Toinen'))
# layout.addWidget(QPushButton('Kolmas'))

# layout = QGridLayout()
# layout.addWidget(QPushButton('Yksi'))
# layout.addWidget(QPushButton('Toinen'))
# layout.addWidget(QPushButton('Kolmas'))

# layout = QFormLayout()

# layout.addRow('Nimi: ',QLineEdit())
# layout.addRow('Sähköposti: ',QLineEdit())

main_layout = QHBoxLayout()
left_layout = QVBoxLayout()
left_layout.addWidget(QPushButton('Yksi'))
left_layout.addWidget(QPushButton('Toinen'))

right_layout = QVBoxLayout()
right_layout.addWidget(QLineEdit())

layout = QFormLayout()

layout.addRow('Nimi: ',QLineEdit())
layout.addRow('Sähköposti: ',QLineEdit())

main_layout.addLayout(left_layout)
main_layout.addLayout(right_layout)
main_layout.addLayout(layout)

window.setLayout(main_layout)

app.exec()