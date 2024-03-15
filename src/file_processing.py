import csv
from os import path
import pandas as pd
from enum import Enum
import matplotlib
import matplotlib.pyplot as plt



class Color(Enum):
    pass



class FileData:
    def __init__(self):
        self.data = []

    def import_data(self, file_path: str):
        self.data = []
        # открытие и обработка файла
        with open(file_path, "r", encoding="latin-1") as file:
            start = False
            for line in file:
                if "Fin des courbes" in line:
                    break
                if start:
                    data = line.split('","')
                    data = [item.replace('"', "") for item in data]
                    data = [item.replace('\n', "") for item in data]
                    self.data.append(data)
                if "Début des courbes" in line:
                    start = True
        # изменение названий полей
        for i in range(len(self.data[0])):
            self.data[0][i] = self.data[0][i] + ", " + self.data[1][i]
        self.data.pop(1)
        # преобразование в удобную структуру
        self.data = pd.DataFrame(self.data[1:], columns=self.data[0])

    def import_from_csv(self, csv_file_path: str):
        self.data = pd.read_csv(csv_file_path, index=False)

    def export_to_csv(self, csv_file_path: str):
        if type(self.data) != type([]):
            self.data.to_csv(csv_file_path, sep=';')
        else:
            print('no data')

    def plot(self, x_label: str, y_label: str, title: str):
        x = self.data[x_label]
        y = self.data[y_label]
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)
        ax.grid()
        formatter_x = matplotlib.ticker.FormatStrFormatter('%.1f')
        ax.xaxis.set_major_formatter(formatter_x)
        formatter_y = matplotlib.ticker.FormatStrFormatter('%2.1f')
        ax.yaxis.set_major_formatter(formatter_y)
        return fig


    def create_png(self, fig, picture_path: str):
        fig.savefig(picture_path)

    def __repr__(self):
        return f"{self.data}"



if __name__=="__main__":
    input_file = "23-07-20 16-07.3R_Resultat"
    filename, _ = path.splitext(input_file)
    csv_file_path = filename + ".csv"

    file_obj = FileData()
    file_obj.import_data(input_file)

    file_obj.export_to_csv(csv_file_path)

    x = ["Elongation XHead, mm", "Position XHead, mm"]
    y = ["Force, kN", "Strength, MPa"]
    title = ["№1 Зависимость нагрузки от удлинения", "№2 Зависимость напряжения от относительной деформации"]
    figs = []
    for i in range(len(title)):
        figs.append(file_obj.plot(x[i], y[i], title[i]))
    

    file_obj.create_png(figs[0], filename + "_1.png")
    file_obj.create_png(figs[1], filename + "_2.png")


