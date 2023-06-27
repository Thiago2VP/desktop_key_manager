import connection
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QGridLayout,
    QWidget,
)
from PyQt5.QtGui import QPalette, QColor

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Word Admin")

        layout1 = QGridLayout()

        self.search = QPushButton("Buscar")
        self.update = QPushButton("Mudar")
        self.delete = QPushButton("Deletar")
        self.insert = QPushButton("Adicionar")

        self.search.setStyleSheet('QPushButton {background-color: #181926; color: #b7bdf8;}')
        self.update.setStyleSheet('QPushButton {background-color: #181926; color: #b7bdf8;}')
        self.delete.setStyleSheet('QPushButton {background-color: #181926; color: #b7bdf8;}')
        self.insert.setStyleSheet('QPushButton {background-color: #181926; color: #b7bdf8;}')

        self.search.clicked.connect(self.search_data)
        self.update.clicked.connect(self.update_data)
        self.delete.clicked.connect(self.delete_data)
        self.insert.clicked.connect(self.insert_data)

        layout1.addWidget(self.search, 0, 0)
        layout1.addWidget(self.update, 0, 1)
        layout1.addWidget(self.delete, 0, 2)
        layout1.addWidget(self.insert, 0, 3)

        layout2 = QGridLayout()

        wordIdLabel = QLabel("Id:")
        self.wordId = QLineEdit()
        nameLabel = QLabel("Name:")
        self.name = QLineEdit()
        loginLabel = QLabel("Login:")
        self.login = QLineEdit()
        keyPassLabel = QLabel("KeyPass:")
        self.keyPass = QLineEdit()
        descriptionLabel = QLabel("Description:")
        self.description = QLineEdit()
        resultLabel = QLabel("Resultado:")
        self.result = QLineEdit()

        self.wordId.setStyleSheet('QLineEdit {background-color: #181926; color: #b7bdf8;}')
        self.name.setStyleSheet('QLineEdit {background-color: #181926; color: #b7bdf8;}')
        self.login.setStyleSheet('QLineEdit {background-color: #181926; color: #b7bdf8;}')
        self.keyPass.setStyleSheet('QLineEdit {background-color: #181926; color: #b7bdf8;}')
        self.description.setStyleSheet('QLineEdit {background-color: #181926; color: #b7bdf8;}')
        self.result.setStyleSheet('QLineEdit {background-color: #181926; color: #a6da95;}')

        layout2.addWidget(wordIdLabel, 0, 0)
        layout2.addWidget(self.wordId, 0, 1)
        layout2.addWidget(nameLabel, 1, 0)
        layout2.addWidget(self.name, 1, 1)
        layout2.addWidget(loginLabel, 2, 0)
        layout2.addWidget(self.login, 2, 1)
        layout2.addWidget(keyPassLabel, 3, 0)
        layout2.addWidget(self.keyPass, 3, 1)
        layout2.addWidget(descriptionLabel, 4, 0)
        layout2.addWidget(self.description, 4, 1)
        layout2.addWidget(resultLabel, 5, 0)
        layout2.addWidget(self.result, 5, 1)

        layout = QGridLayout()
        layout.addLayout(layout1, 0, 0)
        layout.addLayout(layout2, 1, 0)

        widget = QWidget()
        widget.setLayout(layout)

        self.setFixedSize(QSize(700, 400))

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('#24273a'))
        palette.setColor(QPalette.WindowText, QColor('#cad3f5'))
        self.setPalette(palette)

    def search_data(self):
        words = connection.slectData()
        for i in words:
            if (i[1] == self.name.text()):
                self.wordId.setText(str(i[0]))
                self.name.setText(i[1])
                self.login.setText(i[2])
                self.keyPass.setText(i[3])
                self.description.setText(i[4])

        self.result.setText("Busca Realizada")

    def update_data(self):
        words = connection.slectData()
        resp = ""
        for i in words:
            if (i[0] == int(self.wordId.text())):
                resp = connection.updateData(int(self.wordId.text()), self.name.text(), self.login.text(), self.keyPass.text(), self.description.text())

        self.result.setText(str(resp))

    def delete_data(self):
        words = connection.slectData()
        resp = ""
        for i in words:
            if (i[0] == int(self.wordId.text())):
                resp = connection.deleteData(int(self.wordId.text()))

        self.result.setText(str(resp))

    def insert_data(self):
        resp = connection.insertData(self.name.text(), self.login.text(), self.keyPass.text(), self.description.text())

        self.result.setText(str(resp))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
