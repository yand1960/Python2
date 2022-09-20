# Реализовать репозиторий для товаров, хранящихся в xml файле

import xml.etree.ElementTree as ET
from typing import List


class Product:

    def __init__(self, id: int, name: str, code: str, price: float):
        self.id = id
        self.name = name
        self.code = code
        self.price = price


class ProductRepositoryXml:

    def __init__(self, datafile: str):
        with open(datafile, encoding="utf-8") as f:
            text = f.read()
        products_tree = ET.fromstring(text)

        self.products = []
        for p in products_tree.findall("Product"):
            id = int(p.find("ProductID").text)
            name = p.find("Name").text
            code = p.find("ProductNumber").text
            price = float(p.find("ListPrice").text)
            self.products.append(Product(id, name, code, price))

    def getbyid(self, id: int) -> Product:
        # в одну строку реализуйте  (20:30)
        return list(filter(lambda p: p.id == id, self.products))[0]

    def getbyfirstletters(self, letters: str) -> List[Product]:
        # в одну строку реализуйте  (20:46)
        return list(filter(lambda p: p.name.upper().startswith(letters.upper()), self.products))


if __name__ == "__main__":

    repository = ProductRepositoryXml("data/Products.xml")
    # products = repository.products
    products = repository.getbyfirstletters("a")
    for p in products:
        print(f"{p.name}\t{p.price}")
    # print(repository.getbyid(342).name)