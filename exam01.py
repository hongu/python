import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton('눌러주세요', self)
        btn.resize(btn.sizeHint())
        btn.setToolTip('툴팁입니다.')
        btn.move(20, 30)

        self.setGeometry(300,300,400,500)   
        self.setWindowTitle("첫 수업 입니다.")
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())