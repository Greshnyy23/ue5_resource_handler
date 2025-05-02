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

GUI будет добавлено в будущих версиях.

### Командная строка (CLI)

CLI будет добавлено в будущих версиях.

## Тестирование

Запустите тесты с помощью `pytest`:
```bash
pytest tests/
```

## Вклад

Добро пожаловать к участию в проекте! Открывайте issues и создавайте pull requests.