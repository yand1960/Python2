from .repository_base import RepositoryBase, datetime


class RepositoryCsv(RepositoryBase):

    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def add(self, x: int, y: int, result: int, operation: str, timestamp = datetime.now()):
        with open(self.connection_string, "a", encoding="utf-8") as f:
            f.write(f"{x};{y};{result};{operation};{timestamp}\n")