class File:
    """Набор методов для парсинга,
    сохранения, изменения форматов файлов"""

    @staticmethod
    def create_csv_from_textfile(file_path: str):
        # здесь прописать основную логику парсинга файла
        data = []
        with open(file_path, "r") as file:
            flag = False
            for line in file:
                if flag:
                    data.append(line)
                if "des courbes" in line:
                    flag = True
                if "Fin des courbes" in line:
                    flag = False

    @staticmethod
    def create_png():
        pass
