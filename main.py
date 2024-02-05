from concurrent.futures import ThreadPoolExecutor

from repobrowse.context import Context
from repobrowse.github import Github
from repobrowse.storage import Storage


class Main:

    def __init__(self):
        with ThreadPoolExecutor() as executor:
            # config 関係
            storage = Storage()
            # web api関係
            github = Github(storage)
            from repobrowse.window import MainWindow
            # window関係
            MainWindow(Context(github, executor)).mainloop()


if __name__ == '__main__':
    main = Main()
