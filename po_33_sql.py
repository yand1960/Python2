import pymssql


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