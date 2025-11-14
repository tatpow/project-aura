from app.ui.window import Window
from app.data import variables

import os
import sys

if getattr(sys, 'frozen', False):
    # Путь к исполняемому файлу
    app_path = os.path.dirname(sys.executable)
    internal_path = os.path.join(app_path, '_internal')
    
    # Добавляем в PATH
    os.environ['PATH'] = internal_path + os.pathsep + os.environ['PATH']

def run():
    application = Window() # Создание приложения из окна

    variables.console = application.consoleTextBox # запись консоли в глобальную переменную
    
    application.mainloop() # Его запуск

if __name__ == "__main__":
    run()
