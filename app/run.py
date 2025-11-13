import threading
import os

import app.ui.functions as func
import app.data.variables as variables
import app.asr as asr

def start():
    if variables.is_asr_running:
        func.consolePrint("ASR уже запущен. Подожди завершения текущей расшифровки.")
        return
    
    if not validate_before_start():
        return
    
    variables.is_asr_running = True
    func.consolePrint("Инициализация прошла успешно. Запускаю фоновую расшифровку...")

    thread = threading.Thread(target=run_asr, daemon=True)
    thread.start()

def validate_before_start():
    if not variables.build["model"]:
        func.consolePrint("Не выбрана нейросеть для распознавания речи", level="ERROR")
        return 0
    
    if int(variables.build["chunk_duration"]) <= 0:
        func.consolePrint("Невозможное время для чанка", level="ERROR")
        return 0
    
    if not variables.build["work_type"]:
        func.consolePrint("Не выбран формат работы", level="ERROR")
        return 0
    
    if not variables.build["audio_path"]:
        func.consolePrint("Не выбран файл audio.mp3", level="ERROR")
        return 0

    if variables.build["work_type"] == "continue" and not variables.build["backup_path"]:
        func.consolePrint("Не выбран файл backup.json", level="ERROR")
        return 0

    if not os.path.exists(variables.EXPORT_PATH):
        os.makedirs(variables.EXPORT_PATH, exist_ok=True)
        func.consolePrint(f"Создана директория экспорта: {variables.EXPORT_PATH}")

    return True

def run_asr():
    try:
        asr.transcribe()
        func.consolePrint("Расшифровка завершена.")
    except Exception as e:
        func.consolePrint(f"Ошибка при выполнении ASR: {e}")
    finally:
        variables.is_asr_running = False
