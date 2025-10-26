import json
import os
import sys

def resource_path(relative_path: str) -> str:
    """Возвращает абсолютный путь к ресурсу.
    Работает и при обычном запуске, и внутри exe (PyInstaller)."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

SETTINGS_FILE = resource_path(os.path.join("json", "settings.json"))
BACKUP_FILE   = resource_path(os.path.join("json", "backup_example.json"))

def loadJson(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Не найден файл {file}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON ({file}): {e}")
        return {}

settings = loadJson(SETTINGS_FILE)
backup_example = loadJson(BACKUP_FILE)

time_entry_state = True
