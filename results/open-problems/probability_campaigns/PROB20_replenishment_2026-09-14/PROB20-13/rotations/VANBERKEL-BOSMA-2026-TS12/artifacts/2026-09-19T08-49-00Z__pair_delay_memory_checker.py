#!/usr/bin/env python3
"""Exact pair-delay records for VANBERKEL-BOSMA-2026-TS12, S_(4,6,17).

The generator implements the strict greedy 3-sumfree rule with Python integer
bitsets. S marks accepted values; P marks sums of two distinct accepted values;
T marks sums of three distinct accepted values. On accepting x, every old pair
sum p gives the new strict triple sum p+x, then every old accepted y gives the
new distinct pair sum y+x. All arithmetic is exact.

For selected excluded n we compute
    mu(n) = min {a+b : a,b,c are pairwise-distinct members of S,
                         a+b+c=n}.
The returned minimum p=a+b is always < n/2, so c=n-p>p>a,b and distinctness
from c is automatic. The scan is in increasing p, hence the reported minima are
exact, not heuristic search values.
"""

from bisect import bisect_left

F0, G0, H0 = 4, 6, 17
LIMIT = 720_000
EXPECTED = {
    757: (139, 618, (37, 102)),
    1776: (828, 948, (38, 790)),
    5212: (2523, 2689, (6, 2517)),
    10242: (5044, 5198, (4, 5040)),
    53405: (12442, 40963, (37, 12405)),
    81275: (20644, 60631, (37, 20607)),
    100943: (40312, 60631, (37, 40275)),
    285423: (96771, 188652, (4, 96767)),
    377150: (188498, 188652, (4, 188494)),
    718521: (196691, 521830, (6, 196685)),
}

MASK = (1 << (LIMIT + 1)) - 1
S = (1 << F0) | (1 << G0) | (1 << H0)
P = (1 << (F0 + G0)) | (1 << (F0 + H0)) | (1 << (G0 + H0))
T = 1 << (F0 + G0 + H0)
values = [F0, G0, H0]

for x in range(H0 + 1, LIMIT + 1):
    if ((T >> x) & 1) == 0:
        T |= (P << x) & MASK
        P |= (S << x) & MASK
        S |= 1 << x
        values.append(x)

value_set = set(values)


def min_pair_delay(n: int):
    """Return the exact least (p,c), p=a+b, for the selected excluded n."""
    i = bisect_left(values, n)
    # c descending is p=n-c ascending. Stop when p>=c. Once a witness is found
    # before that point, every smaller possible p has already been tested.
    for c in reversed(values[:i]):
        p = n - c
        if p >= c:
            break
        if (P >> p) & 1:
            return p, c
    raise AssertionError(f"no pair-delay witness below n/2 for n={n}")


def pair_witness(p: int, c: int):
    """Recover one exact a<b with a+b=p and a,b,c distinct."""
    for a in values:
        if 2 * a >= p:
            break
        b = p - a
        if b in value_set and b != c and a != c:
            return a, b
    raise AssertionError(f"no strict pair witness for p={p}, c={c}")


print(f"seed=({F0},{G0},{H0}) limit={LIMIT} accepted_count={len(values)}")
last_mu = -1
for n, expected in EXPECTED.items():
    assert ((S >> n) & 1) == 0, f"target {n} unexpectedly accepted"
    p, c = min_pair_delay(n)
    a, b = pair_witness(p, c)
    assert (p, c) == expected[:2], (n, p, c, expected)
    assert (a, b) == expected[2], (n, a, b, expected)
    assert a < b < c < n
    assert a + b == p and p + c == n
    assert a in value_set and b in value_set and c in value_set
    print(f"n={n} mu={p} witness={a}+{b}+{c}")
    assert p > last_mu
    last_mu = p

print("ALL_EXACT_CHECKS_PASS")
