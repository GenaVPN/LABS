from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout
from  PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget



class MAIN(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(QSize(800,500))
        self.setMinimumSize(500,400)
        lay = QVBoxLayout()

        self.Label = QLabel()
        self.line = QLineEdit()
        self.button = QPushButton("Нажми")
        lay.addWidget(self.line)
        lay.addWidget(self.Label)
        lay.addWidget(self.button)
        self.button.setFixedSize(200,200)
        con = QWidget()
        con.setLayout(lay)
        self.setCentralWidget(con)

        # self.setCentralWidget(LAbel)
        # self.setCentralWidget(line)




app = QApplication([])
win = MAIN()
win.show()

app.exec()