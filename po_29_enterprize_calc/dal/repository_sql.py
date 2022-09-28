import pymssql
from pymssql._pymssql import Connection, Cursor
from .repository_base import RepositoryBase, datetime

class RepositorySql(RepositoryBase):

    def __init__(self, connection_string: str):
        params = connection_string.split(";")
        self.server = params[0]
        self.database = params[1]
        self.user = params[2]
        self.password = params[3]

    def add(self, x: int, y: int, result: int, operation: str, timestamp = datetime.now()):

        connection: Connection
        with pymssql.connect(
            server=self.server,
            database=self.database,
            user=self.user,
            password=self.password
        ) as connection:

            # Вообще-то это очень плохой стиль, уязвимость для sql injection
            sql = f"INSERT INTO calcs(x, y, result, author) VALUES({x}, {y}, {result}, 'YA')"

            cursor: Cursor
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
