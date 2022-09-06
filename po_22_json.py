# Получать курсы валют от веб службы ЦБР (путем десериализации json)

from urllib import request
from http import client
import json
from po_21_urllib import CbrData


class CbrDataExtended(CbrData):

    def __init__(self):
        self.url_ws = "https://www.cbr-xml-daily.ru/daily_json.js"
        super().__init__()

    def rate(self, currency):

        response: client.HTTPResponse = request.urlopen(self.url_ws)
        # print(response)
        result = response.read().decode("utf-8")
        # print(result)

        rates = json.loads(result)
        try:
            return rates['Valute'][currency]['Value']
        except KeyError:
            raise KeyError(f"Данные о валюте {currency} отсутствуют")


if __name__ == "__main__":
    # print(rate("USD"), rate("AZN"))
    cbr = CbrDataExtended()
    print(cbr.usd_rate(), cbr.rate("USD"), cbr.rate("AZN"))