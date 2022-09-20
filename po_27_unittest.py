from unittest import TestCase
# from po_07_functions import plus, plus_minus
from po_23_xml_repository import ProductRepositoryXml, Product

# class TestPo07(TestCase):
#
#     def test_plus(self):
#         x = [1, 2, 8]
#         y = [5, 6, 3]
#         tax =[0, 0.1, 0.3]
#         expected = [6, 7.2, 7.7]
#         for i in range(0, len(x)):
#             result = plus(x[i], y[i], tax[i])
#             # self.assertEqual(expected, result)
#             self.assertAlmostEqual(expected[i], result, 6)


class TestProductRepositoryXml(TestCase):

    def setUp(self):
        self.repository = ProductRepositoryXml("data/ProductsTesting.xml")

    def test_products(self):
        products = self.repository.products
        self.assertEqual(254, len(products))
        p = products[123]
        self.assertEqual(869, p.id)
        self.assertEqual("Women's Mountain Shorts, L", p.name)
        self.assertEqual("SH-W890-L", p.code)
        self.assertEqual(83.36, p.price)

    def test_getbyid(self):
        p = self.repository.getbyid(869)
        self.assertEqual("Women's Mountain Shorts, L", p.name)
        self.assertEqual("SH-W890-L", p.code)
        self.assertEqual(83.36, p.price)

    def test_getbyfirstletters(self):
        products = self.repository.getbyfirstletters("re")
        self.assertEqual(2, len(products))
        p = products[1]
        self.assertEqual(907, p.id)
        self.assertEqual("Rear Brakes", p.name)
        self.assertEqual("RB-9231", p.code)
        self.assertEqual(126.84, p.price)