import csv
from os import path

class File:
    """Набор методов для парсинга,
    сохранения, изменения форматов файлов"""

    @staticmethod
    def create_csv_from_textfile(file_path: str):
        csv_file_path, _ = path.splitext(file_path)
        data = []
        with open(file_path, "r", encoding="latin-1") as file:
            start = False
            for line in file:
                if "Fin des courbes" in line:
                    break
                if start:
                    data.append(line.replace('"', "").split(","))
                if "Début des courbes" in line:
                    start = True
        for i in range(len(data[0])):
            data[0][i] = data[0][i] + ", " + data[1][i]
        data.pop(1)
        print(len(data[5]))
        with open(csv_file_path + ".csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(data)

        return data                


                

    @staticmethod
    def create_png():
        pass

if __name__=="__main__":
    file = "23-07-20 16-07.3R_Resultat"
    res = File.create_csv_from_textfile(file)
