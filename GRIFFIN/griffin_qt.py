from PyQt5.QtWidgets import QApplication, QLabel


def rungui():
    app = QApplication([])
    label = QLabel('AHello World!')
    label.show()
    app.exec_()


if __name__ == "__main__":
    rungui()
