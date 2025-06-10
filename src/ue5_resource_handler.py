import subprocess
import os
import shutil

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
        """Небольшой парсер заголовков `.ucas`/`.utoc`."""
        if not os.path.exists(ucas_path):
            raise FileNotFoundError(".ucas файл не найден")
        if not os.path.exists(utoc_path):
            raise FileNotFoundError(".utoc файл не найден")

        with open(utoc_path, "rb") as f:
            magic = f.read(4)
            version_bytes = f.read(4)

        result = {
            "magic": magic,
            "version": int.from_bytes(version_bytes, "little") if version_bytes else None,
            "ucas_size": os.path.getsize(ucas_path),
        }

        print(f"UTOC magic: {result['magic']} version: {result['version']}")
        return result

    def extract_ubulk(self, ubulk_path, export_to):
        """Пример обработки .ubulk (копирование в каталог)."""
        if not os.path.exists(ubulk_path):
            raise FileNotFoundError(".ubulk файл не найден")
        if not os.path.exists(export_to):
            os.makedirs(export_to)

        dest = os.path.join(export_to, os.path.basename(ubulk_path))
        shutil.copyfile(ubulk_path, dest)
        print(f"UBULK скопирован в {dest}")
        return dest
