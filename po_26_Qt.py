from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedWidth(300)
        self.setFixedHeight(200)

        # Сменить заголовок окна на Демо (21:06)
        self.setWindowTitle("Демо")

        self.button = QPushButton(parent=self)
        self.button.setText("Click me")
        self.button.setGeometry(10, 10, 280, 180)
        self.button.clicked.connect(self.button_click)

        self.show()

    def button_click(self):
        # print("Hello, world!")
        # Написать код, который выведет надпись на саму кнопку (21:29)
        self.button.setText("Hello, world!")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    app.exec()