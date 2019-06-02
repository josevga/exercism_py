class Matrix(object):
    def __init__(self, matrix_string):
        rows = matrix_string.splitlines()
        self.matrix = [[int(x) for x in row.split()] for row in rows]
        print(self.matrix)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [x[index - 1] for x in self.matrix]
