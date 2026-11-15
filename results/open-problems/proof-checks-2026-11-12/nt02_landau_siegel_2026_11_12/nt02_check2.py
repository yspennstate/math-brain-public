# Zero estimate used in Kerr's variant (Masser 1981): a nonzero polynomial in three variables vanishing at all
# N^4 points (theta_n, sigma theta_n, sigma tau theta_n) has total degree at least ((N-1)/3)^(4/3).
# Here: the largest D such that the monomials of total degree <= D are linearly independent as functions on the
# points (so no nonzero polynomial of degree <= D vanishes on all of them), from the retained set for H = 1.
import math, time
from nt02_check import greedy, split_primes

T0 = time.time()
d = 13
print("  N     M   largest D with no vanishing polynomial   Masser bound ((N-1)/3)^(4/3)   counting bound (first D with C(D+3,3) > M) - 1", flush=True)
for N in (2, 3, 4, 5, 6):
    p = split_primes(d, 10 ** 9 + 555, 1)[0]
    kept = greedy(d, N, 1, p)
    by = {}
    for al in kept:
        by[sum(al)] = by.get(sum(al), 0) + 1
    D = -1
    w = 0
    while by.get(w, 0) == (w + 1) * (w + 2) // 2:
        D = w
        w += 1
    c = 0
    while math.comb(c + 3, 3) <= N ** 4:
        c += 1
    print("  %d  %4d   %3d   %31.2f   %3d   [%.0fs]" % (N, N ** 4, D, ((N - 1) / 3) ** (4 / 3), c - 1, time.time() - T0), flush=True)
