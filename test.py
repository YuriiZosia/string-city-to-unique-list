class Matrix:
    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def get_diagonal(self) -> list:
        return [self.matrix[i][i] for i in range(len(self.matrix))]

    def get_counter_diagonal(self) -> list:
        return [self.matrix[i][len(self.matrix) - 1 - i] for i in range(len(self.matrix))]

    def rotate_rows(self, number: int) -> list:
        return self.matrix[number % len(self.matrix):] + self.matrix[:number % len(self.matrix)]

    def rotate_columns(self, number: int) -> list:
        number = number % len(self.matrix)
        if number == 0:
            return self.matrix

        for _ in range(number):
            for row in self.matrix:
                row.append(row.pop(0))
        return self.matrix
        # return [row[number % len(self.matrix):] + row[:number % len(self.matrix)] for row in self.matrix]


# matrix_inst = Matrix([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
matrix_inst = Matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
print(matrix_inst.get_diagonal())
print(matrix_inst.get_counter_diagonal())
print(matrix_inst.rotate_rows(1))
print(matrix_inst.rotate_columns(41))


