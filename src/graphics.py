import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog

from .file_processing import File


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Графики из файла")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.open_button = QPushButton("Открыть файл")
        self.open_button.clicked.connect(self.open_file)
        self.layout.addWidget(self.open_button)

    def open_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Выберите текстовый файл")
        self.create_graph(file_path)

    def create_graph(self, file_path):
        data = File.create_csv_from_textfile(file_path)
        print(data)
