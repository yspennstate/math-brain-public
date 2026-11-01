"""Exact integer Walsh check of the prescribed-coordinate FEI proxy witness."""

from fractions import Fraction


def parity(z: int) -> int:
    return z.bit_count() & 1


def check(m: int) -> tuple[Fraction, Fraction, Fraction]:
    assert m % 2 == 0 and m >= 2
    n = 1 << m
    g = []
    for x in range(n):
        q = sum(((x >> (2 * j)) & 1) * ((x >> (2 * j + 1)) & 1)
                for j in range(m // 2))
        g.append(1 if q % 2 == 0 else -1)
    assert g[0] == 1
    walsh = [sum(g[x] * (1 if parity(x & s) == 0 else -1)
                 for x in range(n)) for s in range(n)]
    assert all(abs(w) ** 2 == n for w in walsh)
    lhs = Fraction(sum(abs((w - 2) ** 2 - w ** 2) for w in walsh), n ** 2)
    rhs = Fraction(sum(4 for _ in walsh), n ** 2)
    # Avoid floating point in the actual assertion.
    root = 1 << (m // 2)
    assert lhs == Fraction(4 * (n - 1), n * root)
    assert rhs == Fraction(4, n)
    assert lhs / rhs == Fraction(n - 1, root)
    return lhs, rhs, lhs / rhs


if __name__ == "__main__":
    for bits in (2, 4, 6, 8):
        left, right, ratio = check(bits)
        print(f"m={bits} N={1 << bits} LHS={left} RHS={right} ratio={ratio}")
