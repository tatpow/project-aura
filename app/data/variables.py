import os
import copy

from app.data.utils import load_json, resource_path

# === Глобальные переменные приложения ===
console = None
time_entry_state = True
is_asr_running = False
asr_pipeline = None
current_model_name = None

# === Пути ===
UTILS_PATH = resource_path(os.path.join('app', 'json', 'utils.json'))
UTILS = load_json(UTILS_PATH)

MODELS_DICT_PATH = resource_path(os.path.join('app', 'json', 'models.json'))
MODELS = load_json(MODELS_DICT_PATH)

BUILD_PLACEHOLDER_PATH = resource_path(os.path.join('app', 'json', 'build_placeholder.json'))
BUILD_PLACEHOLDER = load_json(BUILD_PLACEHOLDER_PATH)

BACKUP_PLACEHOLDER_PATH = resource_path(os.path.join('app', 'json', 'backup_placeholder.json'))
BACKUP_PLACEHOLDER = load_json(BACKUP_PLACEHOLDER_PATH)

EXPORT_PATH = "export/"

# === Рабочие переменные (могут изменяться во время выполнения) ===
build = copy.deepcopy(BUILD_PLACEHOLDER)
