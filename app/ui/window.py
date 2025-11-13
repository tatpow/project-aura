import customtkinter as ctk

import app.ui.functions as func
from app.run import start
import app.data.variables as variables

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # ===== Главное окно =====
        self.title("Проект АУРА")
        self.geometry("1100x750")
        
        # ===== Основная колонка =====
        frame_main = ctk.CTkFrame(self, corner_radius=10)
        frame_main.pack(side="left", fill="both", expand=True, padx=10, pady=10, anchor="center")

        ctk.CTkLabel(frame_main, text="Настройки", font=ctk.CTkFont(size=16, weight="bold"), padx=10, pady=10).pack(padx=10)
        
        # Консоль
        console = ctk.CTkFrame(frame_main, corner_radius=10)
        console.pack(side="bottom", pady=10, padx=10, fill="x", anchor="center")

        ctk.CTkLabel(console, text="Консоль:").pack(fill="x", expand=True, side="top", pady=5)

        self.consoleTextBox = ctk.CTkTextbox(console, state="disabled", height=200)
        self.consoleTextBox.pack(fill="x", expand=True, side="bottom")
        
        # Выбор нейросети
        ctk.CTkLabel(frame_main, text="--- Нейросеть для автоматического распознавания речи | ASR ---", 
                    font=ctk.CTkFont(size=12, weight="bold"), padx=10, pady=10).pack(padx=10)

        asr_model_option = ctk.CTkFrame(frame_main, corner_radius=10)
        asr_model_option.pack(pady=10, padx=10, fill="x")

        inner_asr_model_option = ctk.CTkFrame(asr_model_option, fg_color="transparent")
        inner_asr_model_option.pack(anchor="center")

        ctk.CTkLabel(inner_asr_model_option, text="Модель:").grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkOptionMenu(inner_asr_model_option, variable=ctk.StringVar(value=""), 
                          values=list(variables.MODELS.keys()), 
                          command=lambda choice:func.select_model(variables.MODELS[choice])).grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkButton(inner_asr_model_option, 
                      text="Проверка", command=lambda:func.consolePrint(variables.build["model"])).grid(row=0, column=2, padx=5, pady=5)
        
        # Дополнительные настройки
        ctk.CTkLabel(frame_main, text="--- Параметры ---", font=ctk.CTkFont(size=12, weight="bold"), padx=5, pady=5).pack(padx=5)

        main_options = ctk.CTkFrame(frame_main, corner_radius=10)
        main_options.pack(pady=5, padx=5, fill="x")
        
        inner_main_options = ctk.CTkFrame(main_options, fg_color="transparent")
        inner_main_options.pack(anchor="center")
        
        ctk.CTkLabel(inner_main_options, 
                     text="Файл (mp3):"
                     ).grid(row=0, column=0, padx=5, pady=15)
        ctk.CTkButton(inner_main_options, 
                      text="Загрузить файл",
                      command=lambda: func.load_audio_file()
                      ).grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(inner_main_options, 
                     text="Время чанка:"
                     ).grid(row=0, column=2, padx=5, pady=5)
        timeEntry = ctk.StringVar(value="-1")
        time_entry_ui = ctk.CTkEntry(inner_main_options, 
                                     textvariable=timeEntry,
                                     placeholder_text="сек", width=60)
        time_entry_ui.grid(row=0, column=3, padx=5, pady=5)
        ctk.CTkButton(inner_main_options, 
                      text="Зафиксировать время", 
                      command=lambda:func.change_state_time_time_entry(time_entry_ui, timeEntry)
                      ).grid(row=0, column=4, padx=5, pady=5)
        
        ctk.CTkLabel(inner_main_options, text="Формат:").grid(row=1, column=0, padx=5, pady=5)

        backup_file_btn = ctk.CTkButton(inner_main_options, 
                      text="Выбрать", 
                      command=lambda:func.load_backup_file(),
                      state="disabled")
        backup_file_btn.grid(row=1, column=3, padx=5, pady=5)
        
        ctk.CTkOptionMenu(inner_main_options, 
                        variable=ctk.StringVar(value=""), 
                        values=list(variables.UTILS["work_type"].keys()), 
                        command=lambda choice:func.select_work_type(variables.UTILS["work_type"][choice], backup_file_btn)
                        ).grid(row=1, column=1, padx=5, pady=5)
        ctk.CTkLabel(inner_main_options, 
                     text="Файл backup.json:"
                     ).grid(row=1, column=2, padx=5, pady=5)
        
        check_clear_export = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(inner_main_options, 
                        text="Очистить папку Export",
                        command = lambda: func.change_checkbox_value("clear_export_folder", check_clear_export.get()),
                        variable=check_clear_export,
                        ).grid(row=2, column=0, padx=5, pady=5)
        check_backup = ctk.BooleanVar(value=True)
        ctk.CTkCheckBox(inner_main_options, 
                        text="Создавать файл backup.json",
                        command = lambda: func.change_checkbox_value("create_backup_file", check_backup.get()),
                        variable=check_backup,
                        ).grid(row=2, column=1, padx=5, pady=5)
        
        frame_start = ctk.CTkFrame(frame_main, corner_radius=10)
        frame_start.pack(pady=5, padx=5, fill="x", anchor="center")
    
        ctk.CTkButton(frame_start, 
                      text="Запустить", 
                      command=lambda: start()
                      ).pack(padx=5, pady=5)
