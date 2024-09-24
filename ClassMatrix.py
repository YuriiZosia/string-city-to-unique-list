import pytest


class Matrix:
    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def get_diagonal(self) -> list:
        return [self.matrix[i][i] for i in range(len(self.matrix))]

    def get_counter_diagonal(self) -> list:
        return [self.matrix[i][len(self.matrix) - 1 - i] for i in range(len(self.matrix))]

    def rotate_rows(self, number: int) -> list:
        if not self.matrix:
            return []

        for _ in range(number % len(self.matrix)):
            self.matrix.append(self.matrix.pop(0))
        return self.matrix

    def rotate_columns(self, number: int) -> list:
        if not self.matrix:
            return []

        for _ in range(number % len(self.matrix)):
            for row in self.matrix:
                row.append(row.pop(0))
        return self.matrix


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


@pytest.mark.parametrize(
    "matrix",
    [
        [],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    ],
)
def test_matrix_init(matrix):
    mtrx = Matrix(matrix)
    assert mtrx.matrix == matrix, (
        f"Instance attribute 'matrix' should equal to {matrix} "
        f"when you create instance with 'Matrix({matrix})'"
    )


@pytest.mark.parametrize(
    "matrix,diagonal",
    [
        ([], []),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 5, 9]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [1, 6, 11, 16],
        ),
    ],
)
def test_matrix_get_diagonal(matrix, diagonal):
    mtrx = Matrix(matrix)
    assert mtrx.get_diagonal() == diagonal, (
        f"'mtrx.get_diagonal()' should equal to {diagonal}, "
        f"when 'mtrx' is created by 'Matrix({matrix})'"
    )


@pytest.mark.parametrize(
    "matrix,diagonal",
    [
        ([], []),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [3, 5, 7]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [4, 7, 10, 13],
        ),
    ],
)
def test_matrix_get_counter_diagonal(matrix, diagonal):
    mtrx = Matrix(matrix)
    assert mtrx.get_counter_diagonal() == diagonal, (
        f"'mtrx.get_counter_diagonal()' should equal to {diagonal}, "
        f"when 'mtrx' is created by 'Matrix({matrix})'"
    )


@pytest.mark.parametrize(
    "matrix,number,rotated",
    [
        ([], 5, []),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            1,
            [[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [1, 2, 3, 4]],
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            2,
            [[9, 10, 11, 12], [13, 14, 15, 16], [1, 2, 3, 4], [5, 6, 7, 8]],
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            41,
            [[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [1, 2, 3, 4]],
        ),
    ],
)
def test_matrix_rotate_rows(matrix, number, rotated):
    mtrx = Matrix(matrix)
    mtrx.rotate_rows(number)
    assert mtrx.matrix == rotated, (
        f"'mtrx = Matrix({matrix})' after 'mtrx.rotate_rows({number})' "
        f"'mtrx.matrix' should equal to {rotated}"
    )


@pytest.mark.parametrize(
    "matrix,number,rotated",
    [
        ([], 5, []),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            1,
            [[2, 3, 4, 1], [6, 7, 8, 5], [10, 11, 12, 9], [14, 15, 16, 13]],
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            2,
            [[3, 4, 1, 2], [7, 8, 5, 6], [11, 12, 9, 10], [15, 16, 13, 14]],
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            41,
            [[2, 3, 4, 1], [6, 7, 8, 5], [10, 11, 12, 9], [14, 15, 16, 13]],
        ),
    ],
)
def test_matrix_rotate_columns(matrix, number, rotated):
    mtrx = Matrix(matrix)
    mtrx.rotate_columns(number)
    assert mtrx.matrix == rotated, (
        f"'mtrx = Matrix({matrix})' after 'mtrx.rotate_columns({number})' "
        f"'mtrx.matrix' should equal to {rotated}"
    )
