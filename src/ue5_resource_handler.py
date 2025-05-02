import subprocess
import os

class UE5ResourceHandler:
    def __init__(self, unrealpak_path=""):
        self.unrealpak_path = unrealpak_path

    def extract_pak(self, pak_path, extract_to):
        """Извлечение .pak-файла"""
        if not self.unrealpak_path or not os.path.exists(self.unrealpak_path):
            raise FileNotFoundError("UnrealPak.exe не найден")
        if not os.path.exists(pak_path):
            raise FileNotFoundError(".pak файл не найден")
        if not os.path.exists(extract_to):
            os.makedirs(extract_to)
        subprocess.run([self.unrealpak_path, pak_path, "-Extract", extract_to], check=True)

    def parse_ucas(self, ucas_path, utoc_path):
        """Заготовка для парсинга .ucas и .utoc"""
        # TODO: Реализовать разбор
        print(f"Парсинг {ucas_path} и {utoc_path} (заглушка)")

    def extract_ubulk(self, ubulk_path, export_to):
        """Заготовка для обработки .ubulk"""
        # TODO: Реализовать обработку
        print(f"Обработка {ubulk_path} и экспорт в {export_to} (заглушка)")