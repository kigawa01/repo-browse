from concurrent.futures import ThreadPoolExecutor

from repobrowse.context import Context
from repobrowse.github import Github
from repobrowse.storage import Storage


class Main:

    def __init__(self):
        with ThreadPoolExecutor() as executor:
            storage = Storage()
            github = Github(storage)
            from repobrowse.window import MainWindow
            MainWindow(Context(github, executor)).mainloop()


if __name__ == '__main__':
    main = Main()
