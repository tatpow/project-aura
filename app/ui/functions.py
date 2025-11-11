from tkinter import filedialog
import datetime
import os

import app.data.variables as variables

# === Отправка в консоль ===
def consolePrint(message, level="INFO"):
    """Безопасно выводит сообщение в UI и консоль."""
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    text = f"[{timestamp}] [{level}] {message}"
    
    print(text)  # вывод в терминал для отладки
    
    if variables.console and variables.console.winfo_exists():
        try:
            variables.console.after(0, lambda: _safe_insert(text))
        except Exception:
            pass
def _safe_insert(text):
    """Безопасное добавление текста в текстбокс"""
    if not variables.console or not variables.console.winfo_exists():
        return
    variables.console.configure(state="normal")
    variables.console.insert("end", text + "\n")
    variables.console.configure(state="disabled")
    variables.console.see("end")

# === Выбор модели ===
def select_model(model):
    variables.build["model"] = model
    consolePrint(f"Выбрана модель: {model}.")

# === Тип работы (новая/продолжить) ===
def select_work_type(type, button):
    variables.build["work_type"] = type
    if(type == "continue"):
        button.configure(state="normal")
    else:
        button.configure(state="disabled")
    consolePrint(f"Тип работы: {type}")

# === Загрузка аудиофайла ===
def load_audio_file():
    path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3")])
    if not path:
        return
    if not os.path.exists(path):
        consolePrint("Указанный файл не найден.", level="ERROR")
        return
    
    variables.build["audio_path"] = path
    consolePrint(f"Загружен аудио: {os.path.basename(path)}")
    consolePrint(f"Путь: {path}")

# === Загрузка backup ===
def load_backup_file():
    path = filedialog.askopenfilename(filetypes=[("Backup JSON File", "*.json")])
    if not path:
        return
    if not os.path.exists(path):
        consolePrint("Указанный файл не найден.", level="ERROR")
        return
    
    variables.build["backup_path"] = path
    consolePrint(f"Загружен backup: {os.path.basename(path)}")
    consolePrint(f"Путь: {path}")   

# === Работа с entry времени чанка ===
def change_state_time_time_entry(entry_widget, var):
    if not entry_widget:
        return
    
    if variables.time_entry_state:
        try:
            val = int(var.get())
            if val <= 0:
                raise ValueError
            
            variables.build["chunk_duration"] = val
            entry_widget.configure(state="disabled", fg_color="gray10")
            consolePrint(f"Время чанка зафиксировано: {val} сек.")
            variables.time_entry_state = False
        except ValueError:
            consolePrint("Введите корректное число секунд.", level="ERROR")
    else:
        variables.build["chunk_duration"] = ""
        entry_widget.configure(state="normal", fg_color="gray20")
        consolePrint(f"Поле раблокировано.")
        variables.time_entry_state = True

# === Чекбоксы ===
def change_checkbox_value(param, value):
    if param and (value is not None):
        if(variables.build.get(param) is not None):
            variables.build[param] = bool(value)
            consolePrint(f"{param}: {bool(value)}")
