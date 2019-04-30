
def create_matrix(m, n):
    a = []
    for i in range(m):
        a.append([])
        for j in range(n):
            a[i].append(None)
    return a


def split_to_integer(s):
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = int(s[i])
    return s


def split_to_float(s):
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = float(s[i])
    return s


def read_matrix(m, n):
    a = create_matrix(m, n)
    for i in range(m):
        a[i] = split_to_integer(input())
    return a


def print_matrix(a, m, n):
    for i in range(m):
        s = ''
        for j in range(n):
            if s == '':
                s = str(a[i][j])
            else:
                s += " " + str(a[i][j])
        print(s)


def sum(a, b, m, n):
    for i in range(m):
        for j in range(n):
            a[i][j] += b[i][j]
    return a


def multiply_by_scalar(alpha, a, m, n):
    for i in range(m):
        for j in range(n):
            a[i][j] *= alpha
    return a


def product(a, b, m, p, n):
    c = create_matrix(m, n)
    for i in range(m):
        for j in range(n):
            c[i][j] = 0
            for k in range(p):
                c[i][j] += a[i][k] * b[k][j]
    return c


def transpose(a, m, n):
    at = create_matrix(n, m)
    for i in range(m):
        for j in range(n):
            at[j][i] = a[i][j]
    return at


def main():
    operation = int(input())
    if operation == 0:
        v = split_to_integer(input())
        m = v[0]
        n = v[1]
        a = read_matrix(m, n)
        b = read_matrix(m, n)
        c = sum(a, b, m, n)
        print_matrix(c, m, n)
    elif operation == 1:
        v = split_to_integer(input())
        m = v[0]
        n = v[1]
        alpha = float(input())
        a = read_matrix(m, n)
        alpha_a = multiply_by_scalar(alpha, a, m, n)
        print_matrix(alpha_a, m, n)
    elif operation == 2:
        v = split_to_integer(input())
        m = v[0]
        p = v[1]
        n = v[2]
        a = read_matrix(m, p)
        b = read_matrix(p, n)
        c = product(a, b, m, n, p)
        print_matrix(c, m, n)
    elif operation == 3:
        v = split_to_integer(input())
        m = v[0]
        n = v[1]
        a = read_matrix(m, n)
        at = transpose(a, m, n)
        print_matrix(at, n, m)


if __name__ == "__main__":
    main()
