import modules.data as data
import modules.ui.functions as func
from models import asr
def start():
    if data.settings["build"]["model"] == "":
        func.consolePrint("Не выбрана нейросеть для распознавания речи")
        return 0
    
    if int(data.settings["build"]["chunk_duration"]) <= 0:
        func.consolePrint("Невозможное время для чанка")
        return 0
    
    if data.settings["build"]["work_type"] == "":
        func.consolePrint("Не выбран формат работы")
        return 0
    
    if data.settings["build"]["audio_path"] == "":
        func.consolePrint("Не выбран файл audio.mp3")
        return 0

    if data.settings["build"]["work_type"] == "continue" and data.settings["build"]["backup_path"] == "":
        func.consolePrint("Не выбран файл backup.json")
        return 0
    
    func.consolePrint("Инициализация прошла успешно.")
    
    asr.transcribe()
