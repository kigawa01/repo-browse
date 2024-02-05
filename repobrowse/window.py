import webbrowser
from typing import override

from kutilpy.kutil.tk.element import WindowBase, FrameBase, SideType, ElementContainer, AnchorType
from repobrowse.context import Context
from repobrowse.response import Repository


class MainWindow(WindowBase):
    def __init__(self, context: Context):
        super().__init__(context.executor)
        self.context = context
        # menu
        self.frame(SidebarFrame).side(SideType.LEFT).anchor(AnchorType.N)
        # list
        self.frame(RepositoryListFrame).side(SideType.LEFT).anchor(AnchorType.N)
        # login
        if not context.github.try_login():
            self.child_window(LoginWindow(context))

        self.min_size(200, 800)


class SidebarFrame(
    FrameBase[MainWindow]
):
    def __init__(self, parent: ElementContainer):
        super().__init__(parent)
        self.label("repo browse").pady(10).padx(20)
        self.button("logout").pady(5).padx(20).add_on_left_click(self.logout)

    def logout(self):
        self.window().context.github.logout()
        self.window().child_window(LoginWindow(self.window().context))


class RepositoryListFrame(
    FrameBase[MainWindow]
):
    def __init__(self, parent: ElementContainer):
        super().__init__(parent)
        self.window().context.github.on_login.append(self.fetch_repositories)

    def fetch_repositories(self):
        repo_list = self.window().context.github.repositories()
        self.parent.window().sync(self.fetched_task, repo_list)

    def fetched_task(self, repo_list: list[Repository]):
        for repo in repo_list:
            self.frame(RepositoryItemFrame, repo).pack()


class RepositoryItemFrame(
    FrameBase[RepositoryListFrame]
):
    def __init__(self, parent: RepositoryListFrame, repo: Repository):
        super().__init__(parent)
        self.repo = repo
        (self.label(repo.name)
         .bg("#ddd")
         .add_on_left_click(self.open_repo)
         .ipad(5)
         .side(SideType.LEFT)
         )
        (self.add_on_left_click(self.open_repo)
         .bg("#ddd")
         .size(200, 30)
         .pad(1)
         )

    def open_repo(self):
        print("repo item")
        webbrowser.open(self.repo.html_url)


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
         .add_on_left_click(self.login)
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
