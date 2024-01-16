from tkinter import messagebox
from urllib.error import HTTPError

from kutilpy.kutil.urls.http_request import ContentType
from kutilpy.kutil.urls.url import URL
from repobrowse.response import LoginDeviceCode


class Client:
    def is_login(self):
        return False

    def login(self):
        print("login")
        url = (
            URL
            .by_str("https://github.com/login/device/code")
            .join_query({"client_id": "0ecd67b374795cf3f544"})
        )
        req = (
            url
            .to_request()
            .set_method("POST")
            .accept(ContentType.JSON)
        )
        try:
            res = req.fetch()
        except HTTPError as e:
            messagebox.showerror(title="login error", message=f"{e.code}: {e.reason}")
            return

        json = (
            res
            .to_json()
            .to_dataclass(LoginDeviceCode)
        )
        print(json)
