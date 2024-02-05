import traceback
from typing import Callable

from kutilpy.kutil.urls.http_request import ContentType, BearerAuthorization
from kutilpy.kutil.urls.url import URL
from repobrowse.response import Repository
from repobrowse.storage import Storage, StorageJson


class Github:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.on_login = list[Callable[[], any]]()

    def try_login(self):
        is_login = self.storage.load().token != ""
        if not is_login:
            return False

        for task in self.on_login:
            # noinspection PyBroadException
            try:
                task()
            except Exception:
                traceback.print_exc()
        return True

    def login(self, token: str, user: str):
        current = self.storage.load()
        current.token = token
        current.user = user
        result = self.storage.save(current)
        self.try_login()
        return result

    def logout(self):
        self.storage.save(StorageJson("", ""))

    def repositories(self) -> list[Repository]:
        config = self.storage.load()
        return (
            URL.by_str(f"https://api.github.com/users/{config.user}/repos")
            .to_request()
            .accept(ContentType.GITHUB_JSON)
            .authorization(BearerAuthorization(config.token))
            .add_header("X-GitHub-Api-Version", "2022-11-28")
            .fetch()
            .to_json()
            .to_dataclass(list[Repository])
        )
