import json
import os
import sys

def load_json(path: str) -> dict:
    """
    *Параметры*:\n
    - Вход: path (формат str) - путь до файла\n
    - Выход: dict - JSON файл в формате dict

    *Описание*:\n
    Возвращает JSON файл, найденный по пути.\n 
    В случае отсутствия файла или ошибки чтения вернёт пустой массив.
    """
    if not os.path.exists(path):
        print(f"Не найден JSON: {path}")
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON ({path}): {e}")
        return {}

def resource_path(relative_path: str) -> str:
    """Возвращает корректный путь к ресурсам (учитывает PyInstaller). ПОЗЖЕ ДОПИШУ"""
    try:
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    except Exception as e:
        print(f"Ошибка вычисления пути ресурса: {e}")
        return relative_path
