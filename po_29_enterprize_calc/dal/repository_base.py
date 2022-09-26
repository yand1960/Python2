from datetime import datetime

class RepositoryBase:

    def add(self, x: int, y: int, result: int, operation: str, timestamp = datetime.now()):
        pass