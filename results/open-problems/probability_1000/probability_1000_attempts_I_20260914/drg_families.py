"""Aldous and Fill, Open Problem 7.31, over the standard infinite families of distance-regular graphs.

With the closed form tau_0 = k * sum_{i=1..d} (k_i + ... + k_d)/(k_i c_i), the conjecture tau_0 = O(n) is
a statement about intersection arrays, so every classical family can be checked directly.  Note first
that the i = 1 term alone is k*(n-1)/(k*c_1) = n-1, so tau_0 >= n-1 for every distance-regular graph:
the conjecture is that nothing beyond a constant factor is added by the remaining terms.

The cycles, which the conjecture excludes, are the case where every term contributes: k_i c_i = 2 = k for
all i, so the sum has d terms each of order n and tau_0 is of order n^2.
"""
from fractions import Fraction as F
from math import comb
from drg_hitting import tau0


def ratio(b, c):
    t, n = tau0(b, c)
    return float(t / n), int(n)


def hamming(d, q):
    b = [(d - i) * (q - 1) for i in range(d)]
    c = [i + 1 for i in range(d)]
    return b, c


def johnson(N, K):
    d = min(K, N - K)
    b = [(K - i) * (N - K - i) for i in range(d)]
    c = [(i + 1) ** 2 for i in range(d)]
    return b, c


def odd_graph(K):
    """O_K: vertices the (K-1)-subsets of a (2K-1)-set, diameter K-1, valency K"""
    d = K - 1
    b, c = [], []
    for i in range(d):
        if i % 2 == 0: b.append(K - i // 2)
        else: b.append(K - (i + 1) // 2)
    for i in range(1, d + 1):
        c.append((i + 1) // 2)
    return b, c


def doubled_odd(K):
    """the bipartite double of O_K, diameter 2K-1, valency K"""
    d = 2 * K - 1
    b = [K - (i // 2) if i % 2 == 0 else K - ((i + 1) // 2) for i in range(d)]
    c = [(i + 1) // 2 if (i + 1) % 2 == 0 else (i + 1) // 2 + (1 if False else 0) for i in range(1, d + 1)]
    b = [K] + [K - (i + 1) // 2 for i in range(d - 1)]
    c = [1] + [(i + 1) // 2 + ((i + 1) % 2) * 0 for i in range(1, d)]
    return b, c


print("HAMMING GRAPHS H(d,q):  n = q^d, valency d(q-1), diameter d")
print(f"{'d':>3} {'q':>3} {'n':>10} {'tau_0/n':>9}")
for q in (2, 3, 4):
    for d in (2, 4, 8, 12, 16):
        b, c = hamming(d, q)
        r, n = ratio(b, c)
        print(f"{d:>3} {q:>3} {n:>10} {r:>9.4f}")

print("\nJOHNSON GRAPHS J(N,K):  n = C(N,K), diameter min(K, N-K)")
print(f"{'N':>4} {'K':>3} {'n':>10} {'tau_0/n':>9}")
for N, K in ((10, 5), (20, 10), (30, 15), (40, 20), (50, 25), (24, 6), (40, 8)):
    b, c = johnson(N, K)
    r, n = ratio(b, c)
    print(f"{N:>4} {K:>3} {n:>10} {r:>9.4f}")

print("\nODD GRAPHS O_K:  valency K, diameter K-1, n = C(2K-1, K-1)")
print(f"{'K':>3} {'n':>12} {'diam':>5} {'tau_0/n':>9}")
for K in (3, 4, 5, 6, 8, 10, 12, 15):
    b, c = odd_graph(K)
    r, n = ratio(b, c)
    print(f"{K:>3} {n:>12} {len(b):>5} {r:>9.4f}")

print("\nCYCLES (excluded by the conjecture), for contrast")
print(f"{'n':>6} {'tau_0/n':>9}")
for m in (10, 40, 100, 400):
    d = m // 2
    r, n = ratio([2] + [1] * (d - 1), [1] * (d - 1) + [2])
    print(f"{n:>6} {r:>9.4f}")
