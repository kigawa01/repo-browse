from typing import override

from kutilpy.kutil.tk.element import WindowBase, FrameBase, SideType
from repobrowse.context import Context


class MainWindow(WindowBase):
    def __init__(self, context: Context):
        super().__init__(context.executor)
        self.context = context
        self.frame(RepositoryFrame).grid()
        if not context.github.try_login():
            self.child_window(LoginWindow(context))


class RepositoryFrame(
    FrameBase[MainWindow]
):
    def __init__(self, parent: MainWindow):
        super().__init__(parent)
        parent.context.github.on_login.append(self.fetch_repositories)

    def fetch_repositories(self):
        result = self.parent.context.github.repositories()
        print(result)


class LoginWindow(WindowBase):
    def __init__(self, context: Context):
        super().__init__(context.executor)
        self.context = context
        self.user = (
            self.labelEntry("ユーザー名")
            .label_width(15)
            .child_side(SideType.BOTTOM)
            .child_side(SideType.LEFT)
            .padx(20)
            .pady(20, 5))
        self.token = (
            self.labelEntry("トークン")
            .label_width(15)
            .child_side(SideType.LEFT)
            .padx(20)
            .pady(5))
        (self.button("ログイン")
         .on_click(self.login)
         .padx(20)
         .pady(5, 20))
        self.is_force_focus(True)

    def login(self):
        token = self.token.entry_.value()
        user = self.user.entry_.value()
        self.parent.execute(self.login_task, token, user)

    def login_task(self, token: str, user: str):
        self.context.github.login(token, user)
        self.sync(self.destroy)

    @override
    def on_close(self):
        self.parent.destroy()
