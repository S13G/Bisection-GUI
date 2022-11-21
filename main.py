from ui_interface import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Remove title bar
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # Set main background transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Shadow effect style
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))

        # apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # Set windows title
        self.setWindowTitle('Bisection Function')

        # Window size grip
        QSizeGrip(self.ui.resizer)

        # Start calculation
        self.ui.start_button.clicked.connect(
            lambda: self.bisection(a=float(self.ui.first_value.text()), b=float(self.ui.second_value.text())))

        # reset the values
        self.ui.pushButton_5.clicked.connect(lambda: self.new())

        self.show()

    def new(self):
        self.ui.first_value.clear()
        self.ui.second_value.clear()
        self.ui.result.clear()

    def func(self, x):
        return x * x * x - x * x + 2

    def bisection(self, a, b):
        if self.ui.first_value.text():
            self.ui.result.setText('Not empty')
        else:
            self.ui.result.setText("Empty")
        if self.func(a) * self.func(b) >= 0:
            self.ui.result.setText("You have not assumed a and b")
            return

        c = a
        while (b - a) >= 0.01:

            # Find middle point
            c = (a + b) / 2

            # Check if middle point is root
            if self.func(c) == 0.0:
                break

            # Decide the side to repeat the steps
            if self.func(c) * self.func(a) < 0:
                b = c
            else:
                a = c
        self.ui.result.setText("The value of the root is %.4f" % c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())