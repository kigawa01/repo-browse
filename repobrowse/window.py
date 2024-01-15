from kutilpy.kutil.tk.element import WindowBase
from repobrowse import main
from repobrowse.client import Client


class MainWindow(WindowBase):
    def __init__(self):
        super().__init__()
        self.frame().pack()
        self.client = Client()

    def on_focus(self, event):
        window = main.force_window
        if len(window) != 0:
            window[-1].focus_force()

    def on_mainloop(self):
        window = main.force_window
        if len(window) != 0:
            window[-1].focus_force()


class LoginWindow(WindowBase):
    def __init__(self, client: Client):
        super().__init__()
        self.client = client
        self.button().pack()
        main.force_window.append(self)

    def on_destroy(self):
        main.force_window.remove(self)
