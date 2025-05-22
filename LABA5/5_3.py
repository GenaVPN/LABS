from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QRadioButton, QSlider
from  PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtWidgets import QCheckBox


class MAIN(QMainWindow):
    def __init__(self):
        super().__init__()

        checkbox = QCheckBox("ТЫКНИ")
        radio = QRadioButton("JOPA")
        slider = QSlider()
        layout = QVBoxLayout()
        layout.addWidget(checkbox)
        layout.addWidget(radio)
        layout.addWidget(slider)
        con = QWidget()
        con.setLayout(layout)
        self.setCentralWidget(con)
        self.setGeometry(300, 300, 500, 400)







app = QApplication([])
win = MAIN()
win.show()

app.exec()