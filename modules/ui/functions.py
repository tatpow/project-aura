import modules.data as data
from tkinter import filedialog
import os

console = None

def consolePrint(message): 
    if message and console is not None:
        console.configure(state="normal")
        console.insert("end", message + "\n")
        console.configure(state="disabled")
        console.see("end")
        
        print(message)

def select_model(model):
    data.settings["build"]["model"] = model
    consolePrint(f"Модель равна {model}.")

def select_work_type(type, button):
    data.settings["build"]["work_type"] = type
    if(type == "continue"):
        button.configure(state="normal")
    else:
        button.configure(state="disabled")
    consolePrint(f"Тип работы установлен на {type}")

def load_audio_file():
    path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3")])
    if path:
        data.settings["build"]["audio_path"] = path
        consolePrint(f"Загружен аудио: {os.path.basename(path)}.")
        consolePrint(f"Путь: {path}")

def load_backup_file():
    path = filedialog.askopenfilename(filetypes=[("Backup JSON File", "*.json")])
    if path:
        data.settings["build"]["backup_path"] = path
        consolePrint(f"Загружен файл-бекап: {os.path.basename(path)}.")
        consolePrint(f"Путь: {path}")     

def change_state_time_time_entry(time_entry_ui, time_entry_var):
    if time_entry_ui:
        if data.time_entry_state == True:
            if time_entry_var.get().isdigit():
                data.settings["build"]["chunk_duration"] = int(time_entry_var.get())
                time_entry_ui.configure(state="disabled", fg_color="gray10")
                consolePrint(f"Время выставлено: {time_entry_var.get()}. Поле заблокировано.")
                data.time_entry_state = False
            else:
                consolePrint("Пожалуйста, введите корректное число.")
        else:
            data.settings["build"]["chunk_duration"] = ""
            time_entry_ui.configure(state="normal", fg_color="gray20")
            consolePrint(f"Поле раблокировано.")
            data.time_entry_state = True

def change_checkbox_value(param, value):
    if param and (value is not None):
        if(data.settings["build"].get(param) is not None):
            data.settings["build"][param] = bool(value)
            consolePrint(f"{param} равен {bool(value)}")
