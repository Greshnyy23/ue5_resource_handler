# UE5 Resource Handler

Этот проект предоставляет инструменты для обработки ресурсов Unreal Engine 5, таких как `.pak`, `.ucas`, `.utoc`, и `.ubulk` файлы.

## Возможности

- Экстракция `.pak` файлов.
- Разбор `.ucas` и `.utoc` файлов.
- Обработка `.ubulk` файлов (чтение и экспорт).

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/Greshnyy23/ue5_resource_handler.git
   cd ue5_resource_handler
   ```

2. Установите зависимости (если потребуется):
   ```bash
   pip install -r requirements.txt
   ```

## Использование

### Программный интерфейс

```python
from src.ue5_resource_handler import UE5ResourceHandler

# Пример использования
unrealpak_path = "/path/to/UnrealPak.exe"
handler = UE5ResourceHandler(unrealpak_path)

# Экстракция PAK-файла
handler.extract_pak("example.pak", "./extracted")
```

### Графический интерфейс (GUI)

Запустите графический интерфейс командой:
```bash
python ue5_resource_handler_gui.py
```

### Командная строка (CLI)

После установки пакета доступна команда `ue5-handler`.
Доступные подкоманды:
* `extract-pak` – извлечение PAK-файла;
* `parse-ucas` – разбор файлов UCAS/UTOC (ограниченный);
* `extract-ubulk` – копирование UBULK в каталог.

## Тестирование

Запустите тесты с помощью `pytest`:
```bash
pytest tests/
```

## Вклад

Добро пожаловать к участию в проекте! Открывайте issues и создавайте pull requests.