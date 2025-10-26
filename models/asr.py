import modules.data as data
import modules.ui.functions as func
import json
import math
import librosa
from transformers import pipeline
import os

def transcribe():
    func.consolePrint("Запуск ASR...")

    if(data.settings["build"]["clear_export_folder"] == True):
        func.consolePrint("Очистка дериктории...")
        
        for filename in os.listdir(data.settings["export_path"]):
            file_path = os.path.join(data.settings["export_path"], filename)
            if os.path.isfile(file_path):  # проверяем, что это файл, а не папка
                 os.remove(file_path)
    
    func.consolePrint("Загрузка аудиофайла...")
    
    # Загружаем аудио через librosa
    y, sr = librosa.load(data.settings["build"]["audio_path"], sr=16000, mono=True)  # сразу моно и 16 kHz data.settings

    func.consolePrint("Деление аудиофайла...")

    total_samples = y.shape[0]
    chunk_size = int(data.settings["build"]["chunk_duration"]) * sr
    num_chunks = math.ceil(total_samples / chunk_size)

    func.consolePrint("Запуск pipeline...")

    # Создаем pipeline
    asr = pipeline("automatic-speech-recognition", model=data.settings["build"]["model"], device=0)

    progress = {}

    if(data.settings["build"]["work_type"] == "new"):
        progress = data.backup_example
        func.consolePrint("Создание файла бекапа...")
    elif(data.settings["build"]["work_type"] == "continue"):
        if(os.path.exists(data.settings["build"]["backup_path"])):
            with open(data.settings["build"]["backup_path"], "r", encoding="utf-8") as f:
                progress = json.load(f)
            func.consolePrint("Открытие файла бекапа...")
        else:
            func.consolePrint("Файл бекапа не найден!")

    func.consolePrint("Обработка чанков")

    # Обработка чанков
    for i in range(progress["last_processed_chunk"] + 1, num_chunks):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, total_samples)
        chunk = y[start:end]

        text = asr(chunk)["text"]

        progress["results"][str(i)] = text
        progress["last_processed_chunk"] = i
        
        if data.settings["build"]["create_backup_file"] == True:
            with open(data.settings["export_path"] + "backup.json", "w", encoding="utf-8") as f:
                json.dump(progress, f, ensure_ascii=False, indent=2)
        
        func.consolePrint(f"Обработан чанк {i+1}/{num_chunks}")
        
    # Склеиваем текст
    final_text = " ".join(progress["results"][k] for k in sorted(progress["results"], key=lambda x: int(x)))
    with open(data.settings["export_path"] + "export.txt", "w", encoding="utf-8") as f:
        f.write(final_text)
        
    func.consolePrint("Успешно обработан текст!")

    return final_text
