import asyncio

from repobrowse.window.main import MainWindow


class Main:
    def __init__(self):
        self.main_window = MainWindow()
        self.main_window.mainloop()


if __name__ == '__main__':
    main = Main()
