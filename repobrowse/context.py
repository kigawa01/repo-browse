from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from tkinter import ttk

from repobrowse.github import Github


@dataclass
class Context:
    github: Github
    executor: ThreadPoolExecutor

