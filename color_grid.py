from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QScrollArea,
    QGridLayout,
    QMainWindow,
    QInputDialog,
    QPushButton
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor

class ColorCard(QPushButton):
    color_clicked = Signal(str)
    def __init__(self, color: str):
        super().__init__()
        self.setText(color)
        self.color = color

       

        self.setupUi()

    def setupUi(self):
        self.setStyleSheet(f'background-color:{self.color};font-size:30px;')
        #self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.clicked.connect(lambda: self.color_clicked.emit(self.color))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        while (True) :
            text, ok = QInputDialog.getText(self, "Syöte", "Row Amount:")
            if ok and int(text) : break
            if not ok :exit()
        
        self.COLORS_PER_ROW = int(text)
        self.setupUi()

    def setupUi(self):
        layout = QGridLayout()
        for index, color in enumerate(QColor.colorNames()):
            row = index // self.COLORS_PER_ROW
            column = index % self.COLORS_PER_ROW
            widget = ColorCard(color)
            widget.color_clicked.connect(lambda color: print(color))
            layout.addWidget(widget,row,column)
            
        
        widget = QWidget()
        widget.setLayout(layout)

        scrollarea = QScrollArea()
        scrollarea.setWidget(widget)

        self.setCentralWidget(scrollarea)
        self.resize(widget.width()+16,600)

        

app = QApplication()
window = MainWindow()
window.show()
app.exec()