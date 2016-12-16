from PyQt4 import QtGui, QtCore



class Window(QtGui.QWidget):
    def __init__(self):

        QtGui.QWidget.__init__(self)
        self.setWindowTitle('Control Panel')

        self.setFixedSize(600, 300)
        self.warp1_slider = QtGui.QSlider(1, self)
        self.warp1_slider.setFixedSize(500, 60)
        self.warp1_slider.sliderMoved.connect(self.calc_slider1)
        self.warp1_slider.setStyleSheet(self.stylesheet())
        self.setStyleSheet("background-color: black;")

        self.button = QtGui.QPushButton("OK", self)
        self.button.setStyleSheet(self.buttonstyle())
        self.button.setFixedSize(100, 80)
        self.button.move(280, 50)

        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(self.button)
        vbox.addWidget(self.warp1_slider)
        self.setLayout(vbox)
        self.setGeometry(100,100,200,200)
        self.show()

    def calc_slider1(self, event):
        print self.warp1_slider.value()


    def stylesheet(self):
        return """
                QSlider::groove:horizontal {
                    height: 50px;

                    border: 0px solid #abc;
                    }

                QSlider::sub-page:horizontal {
                    background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
                        stop: 0 #333, stop: 1 #aaa);
                    background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
                        stop: 0 #333, stop: 1 #aaa);
                    height: 40px;
                }

                QSlider::add-page:horizontal {
                    background: #222;
                    border: 2px solid gray;
                    height: 40px;
                }

                QSlider::handle:horizontal {
                    background: #000;
                    width: 35px;
                    border: 2px solid white;
                    margin-top: 0px;
                    margin-bottom: 0px;
                    border-radius: 0px;
                }
            """
    def buttonstyle(self):
        return """
                QPushButton {
                    background-color: rgb(50, 50, 50);
                    border-style: outset;
                    border-width: 2px;
                    border-radius: 5px;
                    border-color: white;
                    font: bold 14px;
                    padding: 6px;
                }
                QPushButton::pressed {
                    background-color: rgb(200, 200, 200);
                    border-style: inset;
                }
            """
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
