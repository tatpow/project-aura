import modules.ui.main as main
import modules.ui.functions as func

if __name__ == "__main__":
    app = main.App()
    func.console = app.consoleTextBox
    
    app.mainloop()
