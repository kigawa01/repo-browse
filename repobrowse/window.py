from typing import override

from kutilpy.kutil.tk.element import WindowBase
from repobrowse.context import Context


class MainWindow(WindowBase):
    def __init__(self, context: Context):
        super().__init__(context.executor)
        self.frame().pack()
        if not context.github.is_login():
            self.child_window(LoginWindow(context))


class LoginWindow(WindowBase):
    def __init__(self, context: Context):
        super().__init__(context.executor)
        self.context = context
        self.button("ログイン").on_click(self.login).pack()
        self.input = self.entry().pack()
        self.is_force_focus(True)

    def login(self):
        value = self.input.value()
        self.parent.execute(self.login_task, value)

    def login_task(self, value: str):
        self.context.github.login(value)
        self.sync(self.destroy)

    @override
    def on_close(self):
        self.parent.destroy()
