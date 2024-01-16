from kutilpy.kutil.tk.element import WindowBase
from repobrowse.client import Client


class MainWindow(WindowBase):
    def __init__(self):
        super().__init__()
        self.client = Client()
        self.frame().pack()
        if not self.client.is_login():
            self.child_window(LoginWindow(self.client))


class LoginWindow(WindowBase):
    def __init__(self, client: Client):
        super().__init__()
        self.client = client
        self.button("ログイン").on_click(client.login).pack()
        self.is_force_focus(True)
