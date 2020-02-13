import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui_file import Ui_MainWindow
from ui_mapfile import Ui_Form


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openfunction)

    def openfunction(self):
        self.second_form = SecondWindow()
        self.second_form.show()




class SecondWindow(QMainWindow, Ui_Form):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
