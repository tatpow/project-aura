import copy
import json
import math
import librosa
from transformers import pipeline
import gc
import os
import torch

import app.ui.functions as func
import app.data.variables as variables

def get_device_and_dtype() -> dict:
    """
    Определяет, доступна ли CUDA, и возвращает информацию о вычислительном устройстве.

    Returns:
        dict: Содержит поля:
            - device (int): 0, если используется GPU (CUDA), или -1, если CPU.
            - dtype (torch.dtype): torch.float16 для GPU или torch.float32 для CPU.
    """
    try:
        cuda_available = torch.cuda.is_available()
    except Exception as e:
        func.consolePrint(f"Ошибка при проверке CUDA: {e}")
        cuda_available = False

    if cuda_available:
        device = 0
        dtype = torch.float16
        device_name = torch.cuda.get_device_name(0)
        func.consolePrint(f"CUDA доступна. Обнаружена видеокарта: {device_name}")
        func.consolePrint(f"Устройство: GPU (torch.float16)")
    else:
        device = -1
        dtype = torch.float32
        device_name = "CPU"
        func.consolePrint("CUDA недоступна — используется CPU.")
        func.consolePrint("Если у вас есть видеокарта NVIDIA, возможно, запущена CPU-версия сборки.")

    return device, dtype

def get_pipeline(device, dtype):
    """Возвращает готовый pipeline (создаёт один раз, переинициализирует при смене модели)."""
    model_name = variables.build["model"]

    if variables.asr_pipeline is not None and variables.current_model_name == model_name:
        return variables.asr_pipeline

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
        torch_dtype=dtype
    )
    variables.current_model_name = model_name
    func.consolePrint("Модель успешно загружена!")

    return variables.asr_pipeline

def transcribe():
    func.consolePrint("Запуск ASR...")

    if(variables.build["clear_export_folder"] == True):
        func.consolePrint("Очистка директории...")
        
        for filename in os.listdir(variables.EXPORT_PATH):
            file_path = os.path.join(variables.EXPORT_PATH, filename)
            if os.path.isfile(file_path): 
                 os.remove(file_path)
    
    func.consolePrint("Загрузка аудиофайла...")
    
    # Загружаем аудио через librosa 
    y, sr = librosa.load(variables.build["audio_path"], sr=16000, mono=True) 

    func.consolePrint("Деление аудиофайла...")

    total_samples = y.shape[0]
    chunk_size = int(variables.build["chunk_duration"]) * sr
    num_chunks = math.ceil(total_samples / chunk_size)

    func.consolePrint("Запуск pipeline...")

    # Создаем pipeline
    device, dtype = get_device_and_dtype()
    # asr = pipeline("automatic-speech-recognition", model=variables.build["model"], device=device)
    asr = get_pipeline(device, dtype)

    progress = {}

    if(variables.build["work_type"] == "new"):
        progress = copy.deepcopy(variables.BACKUP_PLACEHOLDER)
        func.consolePrint("Создание файла бекапа...")
    elif(variables.build["work_type"] == "continue"):
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
        try:
            text = asr(chunk)["text"]
        except Exception as e:
            func.consolePrint(f"Ошибка при обработке чанка {i+1}: {e}")
            text = ""

        progress["results"][str(i)] = text
        progress["last_processed_chunk"] = i
        
        if variables.build["create_backup_file"] == True:
            with open(os.path.join(variables.EXPORT_PATH, "backup.json"), "w", encoding="utf-8") as f:
                json.dump(progress, f, ensure_ascii=False, indent=2)
        
        func.consolePrint(f"Обработан чанк {i+1}/{num_chunks}")
        
    # Склеиваем текст
    final_text = " ".join(progress["results"][k] for k in sorted(progress["results"], key=lambda x: int(x)))
    with open(variables.EXPORT_PATH + "export.txt", "w", encoding="utf-8") as f:
        f.write(final_text)
        
    func.consolePrint("Успешно обработан текст!")
    return final_text
