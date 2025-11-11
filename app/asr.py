import copy
import json
import math
import librosa
from transformers import pipeline
import os
import torch
import gc

import app.ui.functions as func
import app.data.variables as variables

def get_pipeline(device):
    """Возвращает готовый pipeline (создаёт один раз, переинициализирует при смене модели)."""
    model_name = variables.build["model"]

    # Проверяем, не изменилась ли модель
    if variables.asr_pipeline is not None and variables.current_model_name == model_name:
        return variables.asr_pipeline

    # Если модель поменялась — освобождаем память
    if variables.asr_pipeline is not None:
        func.consolePrint("Освобождаю память от предыдущей модели...")
        del variables.asr_pipeline
        variables.asr_pipeline = None
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    func.consolePrint(f"Загрузка модели: {model_name} (может занять некоторое время)...")
    variables.asr_pipeline = pipeline(
        "automatic-speech-recognition",
        model=model_name,
        device=device,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    variables.current_model_name = model_name
    func.consolePrint("Модель успешно загружена!")

    return variables.asr_pipeline

def transcribe():
    func.consolePrint("Запуск ASR...")

    if(variables.build["clear_export_folder"] == True):
        func.consolePrint("Очистка дериктории...")
        
        for filename in os.listdir(variables.EXPORT_PATH):
            file_path = os.path.join(variables.EXPORT_PATH, filename)
            if os.path.isfile(file_path):  # проверяем, что это файл, а не папка
                 os.remove(file_path)
    
    func.consolePrint("Загрузка аудиофайла...")
    
    # Загружаем аудио через librosa
    y, sr = librosa.load(variables.build["audio_path"], sr=16000, mono=True)  # сразу моно и 16 kHz data.settings

    func.consolePrint("Деление аудиофайла...")

    total_samples = y.shape[0]
    chunk_size = int(variables.build["chunk_duration"]) * sr
    num_chunks = math.ceil(total_samples / chunk_size)

    func.consolePrint("Запуск pipeline...")

    # Создаем pipeline
    device = 0 if torch.cuda.is_available() else -1
    # asr = pipeline("automatic-speech-recognition", model=variables.build["model"], device=device)
    asr = get_pipeline(device)

    progress = {}

    if(variables.build["work_type"] == "new"):
        progress = copy.deepcopy(variables.BACKUP_PLACEHOLDER)
        func.consolePrint("Создание файла бекапа...")
    elif(variables.build["work_type"] == "continue"):
        os.makedirs(variables.EXPORT_PATH, exist_ok=True)
        if(os.path.exists(variables.build["backup_path"])):
            with open(variables.build["backup_path"], "r", encoding="utf-8") as f:
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
        
        if variables.build["create_backup_file"] == True:
            with open(variables.EXPORT_PATH + "backup.json", "w", encoding="utf-8") as f:
                json.dump(progress, f, ensure_ascii=False, indent=2)
        
        func.consolePrint(f"Обработан чанк {i+1}/{num_chunks}")
        
    # Склеиваем текст
    final_text = " ".join(progress["results"][k] for k in sorted(progress["results"], key=lambda x: int(x)))
    with open(variables.EXPORT_PATH + "export.txt", "w", encoding="utf-8") as f:
        f.write(final_text)
        
    func.consolePrint("Успешно обработан текст!")
    return final_text
