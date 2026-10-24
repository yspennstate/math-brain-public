"""Monotone family F_n = Maj_n(y) OR (z AND y = y*), y* a maximal false point of Maj_n (n odd).

Exact facts used (proved in REPORT): D_z F = +-delta_{y*}, so fhat(T+z)^2 = 4^-n for every T in [n];
fhat(T) = Majhat(T) - c chi_T(y*) 2^-n with |c| = 1 (E_z F = Maj except 0 at y*).
Lower bound: B_z >= sum_T v_T^2 log2(1 + u_T^2/v_T^2) >= 4^-n sum_{T odd} log2(4^n (|Majhat(T)|-2^-n)^2),
and Inf_z = 2^-n.  |Majhat(T)| for |T| = k odd has the closed form
   2^{1-n} C(n-1,(n-1)/2) C((n-1)/2,(k-1)/2) / C(n-1,k-1),
checked here against the Walsh transform for n <= 15."""
import sys, os
import numpy as np
from mpmath import mp, mpf, binomial, log
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from feilib import *
mp.dps = 40

def majhat_abs(n, k):
    if k % 2 == 0:
        return mpf(0)
    return mpf(2) ** (1 - n) * binomial(n - 1, (n - 1) // 2) * binomial((n - 1) // 2, (k - 1) // 2) / binomial(n - 1, k - 1)

# 1. formula check
worst = 0.0
for n in (3, 5, 7, 9, 11, 13, 15):
    fh = wht(majority(n)[None, :].astype(float))[0]
    pc = popcounts(1 << n)
    for k in range(n + 1):
        vals = np.abs(fh[pc == k])
        pred = float(majhat_abs(n, k))
        worst = max(worst, float(np.max(np.abs(vals - pred))))
print("closed form for |Majhat| verified n<=15, max abs error", worst)

# 2. rigorous-in-exact-arithmetic lower bound on B_z/Inf_z
print(" n    lower bound on B_z/Inf_z    (n-1)/2 - log2(n)")
for n in (5, 9, 17, 33, 65, 129, 257, 513, 1025):
    tot = mpf(0)
    ok = True
    for k in range(1, n + 1, 2):
        a = majhat_abs(n, k) - mpf(2) ** (-n)
        if a <= 0:
            ok = False; continue
        tot += binomial(n, k) * log(mpf(4) ** n * a * a, 2)
    lb = tot * mpf(4) ** (-n) / mpf(2) ** (-n)
    print(f"{n:5d}   {float(lb):14.4f}   {(n-1)/2 - np.log2(n):10.4f}   all odd levels positive: {ok}")
