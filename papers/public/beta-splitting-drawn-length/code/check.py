"""Checks for "The drawn length of the critical beta-splitting tree grows linearly".

Notation as in the paper. DTCS(m) splits a clade of size m into (i, m - i) with probability
q(m, i) = m / (2 h_{m-1} i (m - i)), 1 <= i <= m - 1, where h_k = 1 + 1/2 + ... + 1/k.
Height: h(leaf) = 0, h(T) = 1 + max(h(L), h(R)).  Drawn length: l(leaf) = 0,
l(T) = l(L) + l(R) + 2 + |h(L) - h(R)|.  H_m = E h(DTCS(m)), L_m = E l(DTCS(m)),
c_m = E[2 + |h(L) - h(R)|] at the root of DTCS(m).  a(n, m) is the probability that the harmonic descent
chain (k -> j with probability 1 / (h_{k-1} (k - j))) started at n visits m, and a(m) = 6 h_{m-1} / (pi^2 (m - 1)).

Part A uses exact rational arithmetic (fractions) and enumeration; parts B-E use floating point.

Usage: python check.py [N]   (default N = 4000; about a minute and under 100 MB at the default)
"""
import math
import sys
from fractions import Fraction
from functools import lru_cache

import numpy as np

N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
X = 400                      # heights are truncated at X; the truncation error is printed below
failures = []


def check(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        failures.append(msg)


# ---------------------------------------------------------------- A. exact identities on small trees
def shapes(n):
    """All ordered full binary trees with n leaves, as nested tuples; a leaf is None."""
    if n == 1:
        return [None]
    out = []
    for i in range(1, n):
        for left in shapes(i):
            for right in shapes(n - i):
                out.append((left, right))
    return out


def leaves(t):
    return 1 if t is None else leaves(t[0]) + leaves(t[1])


def height(t):
    return 0 if t is None else 1 + max(height(t[0]), height(t[1]))


def drawn(t):
    """Drawn length by the recursion (1.2)."""
    if t is None:
        return 0
    return drawn(t[0]) + drawn(t[1]) + 2 + abs(height(t[0]) - height(t[1]))


def internal_subtrees(t):
    """The subtrees T_v, one for each internal vertex v."""
    return [] if t is None else [t] + internal_subtrees(t[0]) + internal_subtrees(t[1])


def leaf_depths(t, d=0):
    return [d] if t is None else leaf_depths(t[0], d + 1) + leaf_depths(t[1], d + 1)


ok = {"a": True, "b": True, "c": True, "d": True}
count = 0
for n in range(1, 11):
    for t in shapes(n):
        count += 1
        l, ht, s, iv = drawn(t), height(t), sum(leaf_depths(t)), internal_subtrees(t)
        ok["a"] &= l == sum(height(u) for u in iv) + ht
        ok["b"] &= s == sum(leaves(u) for u in iv)
        ok["c"] &= ht <= n - 1
        ok["d"] &= 2 * (n - 1) <= l <= s
check(ok["d"], "2(n-1) <= l(T) <= S(T), all %d ordered binary trees with at most 10 leaves" % count)
check(ok["a"] and ok["b"] and ok["c"],
      "l(T) = sum of h(T_v) + h(T), S(T) = sum of n(T_v) over internal v, and h(T) <= n - 1, same trees")


def hq(k):
    return sum(Fraction(1, j) for j in range(1, k + 1))


def qx(m, i):
    return Fraction(m) / (2 * hq(m - 1) * i * (m - i))


@lru_cache(maxsize=None)
def law(m):
    """Exact joint law {(height, drawn length): probability} of DTCS(m)."""
    if m == 1:
        return {(0, 0): Fraction(1)}
    out = {}
    for i in range(1, m):
        w = qx(m, i)
        for (h1, l1), p1 in law(i).items():
            for (h2, l2), p2 in law(m - i).items():
                key = (1 + max(h1, h2), l1 + l2 + 2 + abs(h1 - h2))
                out[key] = out.get(key, 0) + w * p1 * p2
    return out


EX = {}
for m in range(1, 9):
    d = law(m)
    assert sum(d.values()) == 1
    EX[m] = (sum(p * h for (h, l), p in d.items()), sum(p * l for (h, l), p in d.items()))
print("exact values  m: H_m, L_m")
for m in range(1, 9):
    print("   %d: %s, %s" % (m, EX[m][0], EX[m][1]))
check(EX[4] == (Fraction(30, 11), Fraction(90, 11)), "H_4 = 30/11 and L_4 = 90/11")
cx = {m: 2 * EX[m][0] - 2 * sum(qx(m, i) * EX[i][0] for i in range(1, m)) for m in range(2, 9)}
rec = all(EX[m][1] == 2 * sum(qx(m, i) * EX[i][1] for i in range(1, m)) + cx[m] for m in range(2, 9))
check(rec, "L_m = 2 sum_i q(m,i) L_i + c_m with c_m = 2 H_m - 2 sum_i q(m,i) H_i, exactly for m <= 8")


@lru_cache(maxsize=None)
def a_exact(n, m):
    if n == m:
        return Fraction(1)
    if n < m:
        return Fraction(0)
    return sum(a_exact(j, m) / (hq(n - 1) * (n - j)) for j in range(m, n))


@lru_cache(maxsize=None)
def clades(n, m):
    """Exact expected number of clades of size m in DTCS(n), by first-step analysis."""
    if n == m:
        return Fraction(1)
    if n < m:
        return Fraction(0)
    return sum(qx(n, i) * (clades(i, m) + clades(n - i, m)) for i in range(1, n))


check(all(clades(n, m) == Fraction(n, m) * a_exact(n, m) for n in range(2, 13) for m in range(2, n + 1)),
      "E N_n(m) = (n/m) a(n,m) exactly for 2 <= m <= n <= 12")
check(all(EX[n][1] == n * sum(a_exact(n, m) * cx[m] / m for m in range(2, n + 1)) for n in range(2, 9)),
      "L_n = n sum_m a(n,m) c_m / m exactly for n <= 8")

# ---------------------------------------------------------------- B. heights, c_m and L_n to N
h = np.zeros(N + 1)
for k in range(1, N + 1):
    h[k] = h[k - 1] + 1.0 / k


def qrow(m):
    i = np.arange(1, m)
    return m / (2.0 * h[m - 1] * i * (m - i))


G = np.zeros((N + 1, X + 1))            # G[m, x] = P(h(DTCS(m)) <= x)
G[1, :] = 1.0
for m in range(2, N + 1):
    G[m, 1:] = qrow(m) @ (G[1:m, :-1] * G[m - 1:0:-1, :-1])
H = np.concatenate(([0.0], (1.0 - G[1:, :X]).sum(axis=1)))
print("height truncation: 1 - P(h(DTCS(%d)) <= %d) = %.1e (rounding level)" % (N, X, 1.0 - G[N, X]))
check(1.0 - G[N, X] < 1e-12, "height truncation negligible")
check(all(abs(H[m] - float(EX[m][0])) < 1e-12 for m in range(1, 9)), "floating H_m agrees with the exact values, m <= 8")

c = np.zeros(N + 1)
L = np.zeros(N + 1)
for m in range(2, N + 1):
    q = qrow(m)
    c[m] = 2.0 * H[m] - 2.0 * float(q @ H[1:m])
    L[m] = 2.0 * float(q @ L[1:m]) + c[m]
check(all(abs(L[m] - float(EX[m][1])) < 1e-11 for m in range(1, 9)), "floating L_m agrees with the exact values, m <= 8")
check(bool(np.all(c[2:] >= 2.0 - 1e-12) and np.all(c[2:] <= 1.0 + H[2:] + 1e-12)), "2 <= c_m <= 1 + H_m for 2 <= m <= N")
hb = np.array([4.0 * h[n - 1] * math.log(n) for n in range(2, N + 1)])
check(bool(np.all(H[2:] <= hb)), "H_n <= 4 h_{n-1} log n for 2 <= n <= N (Lemma 3.1)")
print("max of H_n / (4 h_{n-1} log n) over 2 <= n <= N: %.3f" % float(np.max(H[2:] / hb)))


def a_row(n):
    """a(n, m) for m = 1..n by the harmonic descent chain."""
    a = np.zeros(n + 1)
    a[n] = 1.0
    for m in range(n, 1, -1):
        a[1:m] += a[m] / (h[m - 1] * (m - np.arange(1, m)))
    return a


def clade_row(n):
    """E N_n(m) for m = 1..n, top down."""
    e = np.zeros(n + 1)
    e[n] = 1.0
    for m in range(n, 1, -1):
        e[1:m] += 2.0 * e[m] * qrow(m)
    return e


print("   n     H_n    H_n/log^2 n    L_n/n   (L_n/n by clade counts)")
for n in sorted({10, 100, 1000, N // 2, N}):
    e = clade_row(n)
    a = a_row(n)
    m = np.arange(2, n + 1)
    alt = float(e[2:] @ c[2:n + 1]) / n
    dev = float(np.max(np.abs(e[2:] - n / m * a[2:]) / (n / m * a[2:])))
    print("%5d %8.4f %10.4f %12.6f %12.6f   max rel |E N - (n/m)a| = %.1e" % (n, H[n], H[n] / math.log(n) ** 2,
                                                                            L[n] / n, alt, dev))
    check(abs(alt - L[n] / n) < 1e-9 and dev < 1e-9, "n = %d: clade-count identity and the two routes to L_n agree" % n)

# ---------------------------------------------------------------- C. occupation of blocks (Lemma 3.2)
a = a_row(N)
worst = 0.0
for b in range(1, N // 2 + 1):
    s = float(a[b + 1:2 * b + 1].sum())
    worst = max(worst, s / (2.0 * h[2 * b - 1]))
check(worst <= 1.0, "sum_{b<m<=2b} a(%d, m) <= 2 h_{2b-1} for every b <= %d (largest ratio %.3f)" % (N, N // 2, worst))

# ---------------------------------------------------------------- D. the limit lambda = sum_m a(m) c_m / m
am = np.zeros(N + 1)
am[2:] = 6.0 * h[1:N] / (math.pi ** 2 * np.arange(1, N))
rel = float(np.max(np.abs(a[2:31] - am[2:31]) / am[2:31]))
check(rel < 1e-3, "a(N, m) is within 0.1%% of a(m) = 6 h_{m-1} / (pi^2 (m-1)) for 2 <= m <= 30 (largest %.1e)" % rel)
terms = am[2:] * c[2:] / np.arange(2, N + 1)
partial = float(terms.sum())
print("partial sum sum_{m=2}^{%d} a(m) c_m / m = %.6f  (a rigorous lower bound for lambda, up to rounding)" % (N, partial))

# crude rigorous tail: c_m <= 1 + 4 h_m log m and a(m) as above, summed to 10^8 and bounded beyond
def tail_sum(fn, m0, m1=10 ** 8, chunk=10 ** 6):
    s = 0.0
    for lo in range(m0, m1, chunk):
        mm = np.arange(lo, min(lo + chunk, m1), dtype=float)
        hh = np.log(mm - 1) + 0.5772156649015329 + 0.5 / (mm - 1)   # h_{m-1}, error O(m^-2)
        s += float(np.sum(fn(mm, hh)))
    return s


crude = tail_sum(lambda mm, hh: 6.0 * hh / (math.pi ** 2 * (mm - 1)) * (1.0 + 4.0 * (hh + 1.0 / mm) * np.log(mm)) / mm,
                 N + 1)
far = 6.0 / math.pi ** 2 * 10 * math.log(1e8) ** 3 / 1e8               # generous bound for m >= 10^8
# For m >= M = 10^8 and u = log m, h_{m-1} <= h_m <= u + 0.578, so a term of the crude series is at most
# (6/pi^2)(1 + 1e-7) g(u)/m^2 with g(u) = (u + 0.578)(1 + 4u(u + 0.578)) = 4u^3 + 4.624u^2 + 2.336336u + 0.578.
# g(log x)/x^2 decreases for x >= M, so the sum over m >= M is at most g(log M)/M^2 plus the integral from M,
# and int_M^inf (log x)^k / x^2 dx = (k!/M) sum_{j<=k} (log M)^j / j!.
gco, uM = [0.578, 2.336336, 4.624, 4.0], math.log(1e8)
integ = sum(g * math.factorial(k) / 1e8 * sum(uM ** j / math.factorial(j) for j in range(k + 1))
            for k, g in enumerate(gco))
farbound = 6.0 / math.pi ** 2 * (1 + 1e-7) * (sum(g * uM ** k for k, g in enumerate(gco)) / 1e16 + integ)
check(far >= farbound, "the bound %.2e used for m >= 10^8 exceeds the integral bound %.2e" % (far, farbound))
print("crude tail bound (c_m <= 1 + 4 h_m log m) for m > %d: %.4f" % (N, crude + far))
check(4.800 < partial and crude + far < 0.5712 and partial + crude + far < 5.372,
      "4.800 < %.5f <= lambda <= %.5f + %.5f = %.5f < 5.372" % (partial, partial, crude + far, partial + crude + far))

# fitted tail: c_m ~ alpha log^2 m + beta log m + gamma on [N/4, N]
mfit = np.arange(N // 4, N + 1)
A = np.vstack([np.log(mfit) ** 2, np.log(mfit), np.ones_like(mfit, dtype=float)]).T
coef, *_ = np.linalg.lstsq(A, c[N // 4:N + 1], rcond=None)
resid = float(np.max(np.abs(A @ coef - c[N // 4:N + 1])))
print("fit c_m = %.4f log^2 m %+.4f log m %+.4f on [%d, %d], max residual %.1e" % (coef[0], coef[1], coef[2],
                                                                                    N // 4, N, resid))
fitted = tail_sum(lambda mm, hh: 6.0 * hh / (math.pi ** 2 * (mm - 1))
                  * (coef[0] * np.log(mm) ** 2 + coef[1] * np.log(mm) + coef[2]) / mm, N + 1)
A2 = np.vstack([np.log(mfit) ** 2, np.ones_like(mfit, dtype=float)]).T
coef2, *_ = np.linalg.lstsq(A2, c[N // 4:N + 1], rcond=None)
fitted2 = tail_sum(lambda mm, hh: 6.0 * hh / (math.pi ** 2 * (mm - 1)) * (coef2[0] * np.log(mm) ** 2 + coef2[1]) / mm,
                   N + 1)
print("fitted tail (three-term fit) = %.4f, (two-term fit) = %.4f" % (fitted, fitted2))
print("lambda estimate: %.4f (three-term) / %.4f (two-term); rigorous bracket [%.4f, %.4f]"
      % (partial + fitted, partial + fitted2, partial, partial + crude + far))
print("L_N / N = %.6f at N = %d" % (L[N] / N, N))

# second series for the same limit: lambda = sum_m a(m) H_m / m (Remark 4.1), with the same fitted-tail procedure
termsH = am[2:] * H[2:N + 1] / np.arange(2, N + 1)
coefH, *_ = np.linalg.lstsq(A, H[N // 4:N + 1], rcond=None)
fittedH = tail_sum(lambda mm, hh: 6.0 * hh / (math.pi ** 2 * (mm - 1))
                   * (coefH[0] * np.log(mm) ** 2 + coefH[1] * np.log(mm) + coefH[2]) / mm, N + 1)
estH = float(termsH.sum()) + fittedH
print("second series: sum_{m=2}^{%d} a(m) H_m / m = %.6f, fitted tail %.4f, lambda estimate %.4f"
      % (N, float(termsH.sum()), fittedH, estH))
check(abs(estH - (partial + fitted)) < 2e-3, "the two series give the same estimate of lambda to within 2e-3")

# ---------------------------------------------------------------- E. summary
print()
print("ALL CHECKS PASS" if not failures else "FAILURES: %d" % len(failures))
sys.exit(1 if failures else 0)
