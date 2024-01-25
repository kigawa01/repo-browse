from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

from repobrowse.client import Client
from repobrowse.github import Github


@dataclass
class Context:
    client: Client
    github: Github
    executor: ThreadPoolExecutor
