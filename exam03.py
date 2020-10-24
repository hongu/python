import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("안녕하세요")

        menu = self.menuBar()
        menu_file = menu.addMenu('File')
        menu_file = menu.addMenu('Edit')

        self.resize(450,400)
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())
