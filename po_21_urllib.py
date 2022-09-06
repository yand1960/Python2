# Получить курс доллара с визуальной страницы ЦБР

from urllib import request
from http import client


class CbrData:

    def __init__(self):
        self.url = "http://cbr.ru"

    def usd_rate(self):

        response: client.HTTPResponse = request.urlopen(self.url)
        # print(response)
        result = response.read().decode("utf-8")
        # print(result)

        pattern = '<div class="col-md-2 col-xs-9 _dollar">USD</div>'
        position = result.find(pattern)
        result = result[position: position + 200]

        pattern = '₽'
        position = result.find(pattern)
        result = result[position - 15: position ]

        pattern = '>'
        position = result.find(pattern)
        result = result[position + 1: ].strip(" ")

        return float(result.replace(",", "."))

if __name__ == "__main__":
 print(CbrData().usd_rate() * 2)