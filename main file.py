import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui_file import Ui_MainWindow
from ui_mapfile import Ui_Form
from test2 import get_coordinates, get_ll_span
from mapapi import show_map

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openfunction)

    def openfunction(self):
        self.second_form = SecondWindow()
        self.second_form.show()
        toponym_to_find = " ".join(sys.argv[1:])

        if toponym_to_find:
            # Показываем карту с фиксированным масштабом.
            lat, lon = get_coordinates(toponym_to_find)
            ll_spn = "ll={0},{1}&spn=0.005,0.005".format(lat, lon)
            show_map(ll_spn, "map")

            # Показываем карту с масштабом, подобранным по заданному объекту.
            ll, spn = get_ll_span(toponym_to_find)
            ll_spn = "ll={ll}&spn={spn}".format(**locals())
            show_map(ll_spn, "map")

            # Добавляем исходную точку на карту.
            point_param = "pt={ll}".format(**locals())

            show_map(ll_spn, "map", add_params=point_param)
        else:
            print('No data')




class SecondWindow(QMainWindow, Ui_Form):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
