from ..dal.repository_csv import RepositoryCsv

class Calculations:

    def __init__(self, connectionString: str):
        self.repository = RepositoryCsv(connectionString)

    def plus(self, x, y):
        result = x + y
        self.repository.add(x,y,result,"plus")
        return result

    def minus(self, x, y):
        result = x - y
        self.repository.add(x, y, result, "minus")
        return result