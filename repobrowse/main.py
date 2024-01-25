from concurrent.futures import ThreadPoolExecutor

from repobrowse.client import Client
from repobrowse.context import Context
from repobrowse.github import Github
from repobrowse.storage import Storage


class Main:

    def __init__(self):
        with ThreadPoolExecutor() as executor:
            storage = Storage()
            client = Client()
            github = Github(storage)
            from repobrowse.window import MainWindow
            MainWindow(Context(client, github, executor)).mainloop()


if __name__ == '__main__':
    main = Main()
