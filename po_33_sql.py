import pymssql
from pymssql import Connection, Cursor


connection: Connection
with pymssql.connect(
    server="yand.dyndns.org",
    database="AdventureWorks",
    user="northwind",
    password="northwind"
) as connection:

    # 1. Вывести названия товаров вместе с ценами
    sql = f"SELECT Name, ListPrice, ProductID FROM Production.Product"

    cursor: Cursor
    with connection.cursor() as cursor:
        cursor.execute(sql)
        products = cursor.fetchall()

    # for p in products:
    #     print(f"{p[0]}\t-\t{p[1]}")

        # 2. Посчитать, у скольких товаров не заполнена колонка ProductSubcategoryID
        sql = """
            SELECT COUNT(*) 
            FROM Production.Product 
            WHERE ProductSubcategoryID IS NULL
        """

        cursor: Cursor
        with connection.cursor() as cursor:
            cursor.execute(sql)
            # categories = cursor.fetchall()
            result = cursor.fetchone()

        print(result[0])

        # print(len(list(filter(lambda c: c[0] is None, categories))))
        # print(len(categories))


