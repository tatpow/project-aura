from app.ui.window import Window
from app.data import variables

def run():
    application = Window() # Создание приложения из окна

    variables.console = application.consoleTextBox # запись консоли в глобальную переменную
    
    application.mainloop() # Его запуск

if __name__ == "__main__":
    run()
