from kore import App

from src import MainWindow

if __name__ == "__main__":
    app = App()
    window = MainWindow(app)
    app.run()
