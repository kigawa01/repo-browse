from repobrowse.response import Repository
from repobrowse.storage import Storage


class Github:

    def __init__(self, storage: Storage):
        self.storage = storage

    def is_login(self):
        return self.storage.load().token != ""

    def login(self, token: str):
        current = self.storage.load()
        current.token = token
        return self.storage.save(current)

    def repositories(self, username: str) -> list[Repository]:
        pass
