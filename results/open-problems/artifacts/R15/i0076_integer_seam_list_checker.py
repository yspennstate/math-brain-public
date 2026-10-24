#!/usr/bin/env python3
from fractions import Fraction

print("I0076 R15 list-decoding seam obstruction self-check")

# 1. Exact offset/copy check for many finite source-compatible tuples.
count = 0
for c in range(2, 15):
    for a in range(-c + 1, 0):
        for b in range(1, c):
            for S in range(a + 1, b):
                for d in range(1, 9):
                    # Source copy: left index a-d+j carries the same bit
                    # as right index b+1+j.
                    U = tuple((j % 2) * 2 - 1 for j in range(d))
                    V = {}
                    for j, u in enumerate(U):
                        V[b + 1 + j] = u
                        V[a - d + j] = u

                    # Future raw increments A_k=V_{S+k} contain U at
                    # offset i=b+1-S.
                    i = b + 1 - S
                    assert 1 <= i <= 2 * c
                    Afuture = tuple(V[S + k] for k in range(i, i + d))
                    assert Afuture == U

                    # Past raw increments B_k=V_{S-1-k} contain reverse(U)
                    # at offset j0=S-a.
                    j0 = S - a
                    assert 1 <= j0 <= 2 * c
                    Bpast = tuple(V[S - 1 - k] for k in range(j0, j0 + d))
                    assert tuple(reversed(Bpast)) == U
                    count += 1
print("offset/copy identities: PASS", count)

# 2. Pointwise exact inequality used in the list lemma:
# min(1/N,pq) <= sqrt(pq/N).  We check its squared rational form on
# a finite rational grid as a self-check; the report contains the proof.
gridchecks = 0
for N in [4, 16, 64, 256]:
    for den in [4, 8, 16]:
        for ip in range(den + 1):
            for iq in range(den + 1):
                p = Fraction(ip, den)
                q = Fraction(iq, den)
                m = min(Fraction(1, N), p * q)
                assert m * m <= p * q / Fraction(N, 1)
                gridchecks += 1
print("list-lemma pointwise rational grid: PASS", gridchecks)

# 3. Source scale implication, exact rational arithmetic.
# If (4c+1)^2*2^{-d} < 1/n^2, then (2c)^2*2^{-d} < 1/n^2,
# hence 2c*2^{-d/2} < 1/n.
scalechecks = 0
for n in range(2, 31):
    for c in range(1, 31):
        d = 1
        while Fraction((4 * c + 1) ** 2, 2 ** d) >= Fraction(1, n * n):
            d += 1
        assert Fraction((2 * c) ** 2, 2 ** d) < Fraction(1, n * n)
        scalechecks += 1
print("source scale implication: PASS", scalechecks)

print("PASS")
