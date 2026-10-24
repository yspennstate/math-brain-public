from collections import Counter
from fractions import Fraction


def compress(n, M, coord):
    M = set(M)
    out = set(M)
    bit = 1 << coord
    for x in sorted(M):
        if x & bit:
            y = x ^ bit
            if y not in M:
                out.discard(x)
                out.add(y)
    return out


def boundary(n, M):
    M = set(M)
    return sum(1 for x in M for i in range(n) if (x ^ (1 << i)) not in M)


def bool_walsh(n, M):
    M = set(M)
    N = 1 << n
    vals = []
    for S in range(N):
        if S == 0:
            vals.append(N - 2 * len(M))
        else:
            sm = sum(-1 if ((S & x).bit_count() & 1) else 1 for x in M)
            vals.append(-2 * sm)
    return vals


def exact_entropy_if_dyadic(n, M):
    N = 1 << n
    H = Fraction(0, 1)
    for v in bool_walsh(n, M):
        if v == 0:
            continue
        p = Fraction(v * v, N * N)
        assert p.numerator == 1
        d = p.denominator
        assert d & (d - 1) == 0
        k = d.bit_length() - 1
        H += p * k
    return H


def record(n, M):
    vals = bool_walsh(n, M)
    return {
        "B": boundary(n, M),
        "I": Fraction(boundary(n, M), 1 << (n - 1)),
        "H": exact_entropy_if_dyadic(n, M),
        "abs_walsh": Counter(abs(v) for v in vals),
    }


# Counterexample A: one-coordinate compression decreases G_C = C I - H
# for every C>0.
n = 3
M = {1, 2}
Mc = compress(n, M, 0)
assert Mc == {0, 2}
a = record(n, M)
ac = record(n, Mc)
assert a["B"] == 6 and ac["B"] == 4
assert a["I"] == Fraction(3, 2) and ac["I"] == Fraction(1, 1)
assert a["H"] == ac["H"] == Fraction(2, 1)
assert a["abs_walsh"] == ac["abs_walsh"] == Counter({4: 4, 0: 4})
# Hence (G_C after - G_C before) = -C/2 < 0 for every C>0.

# Counterexample B: one-coordinate compression increases the same G_C by
# exactly 1 for every C.
n = 4
M = {8, 3, 5, 6}
Mc = compress(n, M, 3)
assert Mc == {0, 3, 5, 6}
b = record(n, M)
bc = record(n, Mc)
assert b["B"] == bc["B"] == 16
assert b["I"] == bc["I"] == Fraction(2, 1)
assert b["H"] == Fraction(3, 1) and bc["H"] == Fraction(2, 1)
assert b["abs_walsh"] == Counter({4: 8, 0: 6, 8: 2})
assert bc["abs_walsh"] == Counter({0: 12, 8: 4})
# Hence (G_C after - G_C before) = +1.

print("N3_BEFORE", a)
print("N3_AFTER", ac)
print("N3_GAP_DELTA=-C/2_FOR_ALL_C>0")
print("N4_BEFORE", b)
print("N4_AFTER", bc)
print("N4_GAP_DELTA=+1")
print("P03-COMPRESSION-MONOTONICITY-ROUTE-KILL=PASS")
