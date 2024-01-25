import os
from dataclasses import dataclass, asdict
from json import JSONDecodeError

from kutilpy.kutil.file.file import File
from kutilpy.kutil.jsons.jsons import Json


@dataclass
class StorageJson:
    token: str = ""


class Storage:
    filedir = os.path.join(os.getenv('APPDATA'), "repo-browse")
    filename = os.path.join(filedir, "config.json")
    file = File(filename)

    def __init__(self):
        if not os.path.isdir(self.filedir):
            os.mkdir(self.filedir)
        if not self.file.is_file():
            self.file.write("{}")

    def load(self) -> StorageJson:
        try:
            return Json.by_str(self.file.read()).to_dataclass(StorageJson)
        except JSONDecodeError as e:
            print(self.filename)
            raise e

    def save(self, data: StorageJson):
        self.file.write(Json(asdict(data)).dumps())
