"""Exact, bounded checks of the C0029 collision and sparse-bridge claims."""
from fractions import Fraction
from itertools import product
from math import comb


def stirling_signed(n):
    row = [1]
    for k in range(1, n + 1):
        nxt = [0] * (k + 1)
        for j, v in enumerate(row):
            nxt[j] -= (k - 1) * v
            nxt[j + 1] += v
        row = nxt
    return row


def partitions(seq):
    if not seq:
        yield ()
        return
    first, *rest = seq
    for tail in partitions(rest):
        yield ((first,),) + tail
        for k in range(len(tail)):
            yield tail[:k] + ((first,) + tail[k],) + tail[k + 1 :]


def normalized(bits, n):
    d = [[0] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            d[i][j] = bits[(i - 1) * (n - 1) + j - 1]
    return d


def constant_on_partition_rectangles(d, pi, tau):
    return all(
        len({d[i][j] for i in rs for j in cs}) == 1
        for rs in pi for cs in tau
    )


def collision(d):
    n = len(d)
    rows = [tuple(r) for r in d]
    cols = [tuple(d[i][j] for i in range(n)) for j in range(n)]
    return len(set(rows)) != n or len(set(cols)) != n


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    m, n = len(a), len(a[0])
    pivot = 0
    for j in range(n):
        k = next((i for i in range(pivot, m) if a[i][j]), None)
        if k is None:
            continue
        a[pivot], a[k] = a[k], a[pivot]
        q = a[pivot][j]
        a[pivot] = [x / q for x in a[pivot]]
        for i in range(m):
            if i != pivot and a[i][j]:
                q = a[i][j]
                a[i] = [x - q * y for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == m:
            break
    return pivot


def check_collision_formulas():
    for n in range(1, 5):
        states = [normalized(bits, n) for bits in product((0, 1), repeat=(n - 1) ** 2)]
        pp = list(partitions(tuple(range(n))))
        for pi in pp:
            for tau in pp:
                actual = sum(constant_on_partition_rectangles(d, pi, tau) for d in states)
                expected = 2 ** ((len(pi) - 1) * (len(tau) - 1))
                assert actual == expected, (n, pi, tau, actual, expected)
        sn = stirling_signed(n)
        formula_no_collision = Fraction(
            sum(sn[a] * sn[b] * 2 ** ((a - 1) * (b - 1))
                for a in range(1, n + 1) for b in range(1, n + 1)),
            2 ** ((n - 1) ** 2),
        )
        actual_no_collision = Fraction(sum(not collision(d) for d in states), len(states))
        assert actual_no_collision == formula_no_collision, (n, actual_no_collision, formula_no_collision)
        print(f"n={n}: states={len(states)}, partition_pairs={len(pp)**2}, P(E)={1-actual_no_collision}")


def check_four_support():
    t = [[1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
    for n in (5, 6, 7):
        d = [[0] * (n - 1) for _ in range(n - 1)]
        for i in range(4):
            d[i][:4] = t[i]
        for i in range(4, n - 1):
            d[i][i] = 1
        b = [[1] * n for _ in range(n)]
        for i in range(1, n):
            for j in range(1, n):
                b[i][j] -= 2 * d[i - 1][j - 1]
        v = [0, 1, -1, -1, 1] + [0] * (n - 5)
        assert rank(b) == n - 1
        assert all(sum(x * y for x, y in zip(row, v)) == 0 for row in b)
        assert len(set(tuple(r) for r in d)) == n - 1
        assert len(set(tuple(d[i][j] for i in range(n - 1)) for j in range(n - 1))) == n - 1
        print(f"four-support n={n}: rank={rank(b)}, kernel support={sum(x!=0 for x in v)}")


def check_flat_atom():
    a = [[1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]]
    assert rank(a) == 3
    assert all(sum(r) == 0 for r in a)
    zero = sum(sum(x) == 0 for x in product((-1, 1), repeat=4))
    assert zero == comb(4, 2)
    print(f"flat atom n=4: P(distance=0)={Fraction(zero,16)}")


if __name__ == "__main__":
    check_collision_formulas()
    check_four_support()
    check_flat_atom()
