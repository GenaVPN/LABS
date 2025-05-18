from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,  QLabel, QVBoxLayout
from  PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QMessageBox



class MAIN(QMainWindow):
    def Mesblock(self, s = None):

        self.mess = QMessageBox(self)
        self.mess.setMinimumSize(QSize(100,100))
        self.mess.setText("Хотите закрыть диалоговое окно?")
        self.mess.setWindowTitle("Диалог")
        self.mess.setStandardButtons(QMessageBox.Yes| QMessageBox.No)
        a = self.mess.exec()
        if a == QMessageBox.Yes:
            self.Label.setText("Yes")
        else:
            self.Label.setText("No")


    def __init__(self):
        super().__init__()
        lay = QVBoxLayout()

        self.Label = QLabel()

        self.but1 = QPushButton()
        self.button = QPushButton("Нажми")
        lay.addWidget(self.Label)
        lay.addWidget(self.button)
        self.button.setCheckable(True)
        self.Label.setFixedHeight(50)
        self.button.setFixedHeight(100)

        con = QWidget()
        con.setLayout(lay)
        self.setCentralWidget(con)
        self.button.clicked.connect(self.clickk)
        self.setGeometry(300, 300, 500, 400)

    def clickk(self):
        self.Mesblock()
        print("ИДИ В ПЕНЬ")




app = QApplication([])
win = MAIN()
win.show()

app.exec()