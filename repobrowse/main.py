from kutilpy.kutil.tk.element import WindowBase


class Main:

    def __init__(self):
        from repobrowse.window import MainWindow
        self.main_window = MainWindow()

        if len(force_window) != 0:
            force_window[-1].most_front(True).most_front(False).mainloop()
        else:
            self.main_window.mainloop()


force_window: list[WindowBase] = []

if __name__ == '__main__':
    main = Main()
