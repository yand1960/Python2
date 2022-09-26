from unittest import TestCase
from po_29_enterprize_calc.dal.repository_csv import RepositoryCsv


class TestRepositoryCsv(TestCase):

    def test_add(self):
        path = "../../data/calcs.csv"

        with open(path, encoding="utf-8") as f:
                text = f.read();
        expected = len(text.split("\n")) + 1

        repository = RepositoryCsv(path)
        repository.add(1,2,3,"plus")

        with open(path, encoding="utf-8") as f:
            text = f.read();
        actual = len(text.split("\n"))

        self.assertEqual(expected, actual)

        line = text.split("\n")[-2]
        self.assertTrue(line.startswith("1;2;3;plus;"))
