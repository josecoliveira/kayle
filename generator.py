from random import randint
from typing import List, Union
from copy import deepcopy
import answer

Num = Union[int, float]

MIN_COLUMNS = 2
MAX_COLUMNS = 100

SUM_CASES = 10
MULTIPLY_CASES = 10
PRODUCT_CASES = 10
TRANSPOSE_CASES = 10

INT_MIN = 0
INT_MAX = 10


def create_random_matrix(num_lines: int, num_columns: int) -> List[List[int]]:
    matrix = []
    for i in range(num_lines):
        line = []
        for j in range(num_columns):
            random = randint(INT_MIN, INT_MAX)
            line += [random]
        matrix += [line]
    return matrix


def save_file(name: str, string: str) -> None:
    with open(name, "w") as file:
        file.write(string)


def get_intervals(num_cases: int) -> List[List[int]]:
    if num_cases == 1:
        return [[MIN_COLUMNS, MAX_COLUMNS]]
    else:
        step = int((MAX_COLUMNS - MIN_COLUMNS) / SUM_CASES)
        steps = list(range(MIN_COLUMNS, MAX_COLUMNS, step))
        intervals = []
        for i in range(0, len(steps) - 1):
            intervals += [[steps[i], steps[i + 1]]]
        return intervals


def to_string_matrix(matrix: List[List[int]]) -> str:
    matrix = deepcopy(matrix)
    num_lines = len(matrix)
    num_columns = len(matrix[0])
    string = ""
    for i in range(num_lines):
        for j in range(num_columns):
            matrix[i][j] = str(matrix[i][j])
        string += ' '.join(matrix[i])
        if i < num_lines - 1:
            string += '\n'
    return string


def get_sum_input(num_lines: int, num_columns: int, a: List[List[int]], b: List[List[int]]) -> str:
    return '0\n{0} {1}\n{2}\n{3}\n'.format(num_lines, num_columns, to_string_matrix(a), to_string_matrix(b))


def get_sum_output(a: List[List[int]]) -> str:
    return '{0}\n'.format(to_string_matrix(a))


def generate_sum_cases() -> None:
    intervals = get_intervals(SUM_CASES)
    for i, interval in enumerate(intervals):
        m = randint(interval[0], interval[1])
        n = randint(interval[0], interval[1])
        a = create_random_matrix(m, n)
        b = create_random_matrix(m, n)
        c = answer.sum(a, b, m, n)
        save_file('inputs/sum{0}.txt'.format(i), get_sum_input(m, n, a, b))
        save_file('outputs/sum{0}.txt'.format(i), get_sum_output(c))


def get_multiply_input(num_lines: int, num_columns: int, alpha: int, a: List[List[int]]) -> str:
    return '1\n{0} {1}\n{2}\n{3}\n'.format(num_lines, num_columns, alpha, to_string_matrix(a))


def get_multiply_output(a: List[List[int]]) -> str:
    return '{0}\n'.format(to_string_matrix(a))


def generate_multiply_cases():
    intervals = get_intervals(MULTIPLY_CASES)
    for i, interval in enumerate(intervals):
        num_lines = randint(interval[0], interval[1])
        num_columns = randint(interval[0], interval[1])
        alpha = randint(INT_MIN, INT_MAX)
        a = create_random_matrix(num_lines, num_columns)
        alpha_a = answer.multiply_by_scalar(alpha, a, num_lines, num_columns)
        save_file('inputs/multiply{0}.txt'.format(i), get_multiply_input(num_lines, num_columns, alpha, a))
        save_file('outputs/multiply{0}.txt'.format(i), get_multiply_output(alpha_a))


def get_product_input(m, p, n, a, b):
    return '2\n{0} {1} {2}\n{3}\n{4}\n'.format(m, p, n, to_string_matrix(a), to_string_matrix(b))


def get_product_output(a):
    return '{0}\n'.format(to_string_matrix(a))


def generate_product_cases():
    intervals = get_intervals(PRODUCT_CASES)
    for i, interval in enumerate(intervals):
        m = randint(interval[0], interval[1])
        p = randint(interval[0], interval[1])
        n = randint(interval[0], interval[1])
        a = create_random_matrix(m, p)
        b = create_random_matrix(p, n)
        c = answer.product(a, b, m, p, n)
        save_file('inputs/product{0}.txt'.format(i), get_product_input(m, p, n, a, b))
        save_file('outputs/product{0}.txt'.format(i), get_product_output(c))


def get_transpose_input(m, n, a):
    return '3\n{0} {1}\n{2}\n'.format(m, n, to_string_matrix(a))


def get_transpose_output(at):
    return '{0}\n'.format(to_string_matrix(at))


def generate_transpose_cases():
    intervals = get_intervals(TRANSPOSE_CASES)
    for i, interval in enumerate(intervals):
        num_lines = randint(interval[0], interval[1])
        num_columns = randint(interval[0], interval[1])
        a = create_random_matrix(num_lines, num_columns)
        at = answer.transpose(a, num_lines, num_columns)
        save_file('inputs/transpose{0}.txt'.format(i), get_transpose_input(num_lines, num_columns, a))
        save_file('outputs/transpose{0}.txt'.format(i), get_product_output(at))


def main():
    generate_sum_cases()
    generate_multiply_cases()
    generate_product_cases()
    generate_transpose_cases()


if __name__ == "__main__":
    main()
