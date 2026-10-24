"""Exact checks of the elementary majority bounds used in the proof of Proposition M.

n = 2m+1, k = 2j+1 odd, M_k = 4^-m C(2m,m) C(m,j)/C(2m,2j), W_k = C(n,k) M_k^2, I(Maj_n) = n 4^-m C(2m,m).
 (B1) C(m,j)^2 <= C(2m,2j) <= (1 + sqrt(2 pi j)) C(m,j)^2
 (B2) M_k <= 1/(sqrt(pi m) C(m,j))
 (B3) W_k >= 1/(6 k^{3/2})
 (B4) I(Maj_n) <= sqrt(n)
 (B5) the closed-form lower bound on the forced constant A is below the exact forced value.
Exact integer / rational arithmetic via Python ints and fractions where possible; mpmath (80 digits) for roots.
"""
from math import comb
from fractions import Fraction
import mpmath as mp
from fei_core import limit_process

mp.mp.dps = 80


def check(nmax=801, big=(10001, 100001, 1000001)):
    worst = {"B1lo": mp.inf, "B1hi": mp.inf, "B2": mp.inf, "B3": mp.inf, "B4": mp.inf}
    for n in list(range(3, nmax + 1, 2)) + list(big):
        m = (n - 1) // 2
        c2m = comb(2 * m, m)
        Imaj = Fraction(n * c2m, 4 ** m)
        worst["B4"] = min(worst["B4"], mp.sqrt(n) - mp.mpf(Imaj.numerator) / Imaj.denominator)
        ks = range(1, n + 1, 2) if n <= nmax else [1, 3, 5, 7, 9, 33, 101, 301, 1001, 3001]
        for k in ks:
            if k > n:
                continue
            j = (k - 1) // 2
            cmj, c2 = comb(m, j), comb(2 * m, 2 * j)
            worst["B1lo"] = min(worst["B1lo"], c2 - cmj * cmj)
            worst["B1hi"] = min(worst["B1hi"], (1 + mp.sqrt(2 * mp.pi * j)) * cmj * cmj - c2)
            Mk = mp.mpf(c2m) * cmj / (mp.mpf(4) ** m * c2)
            worst["B2"] = min(worst["B2"], 1 / (mp.sqrt(mp.pi * m) * cmj) - Mk)
            Wk = comb(n, k) * Mk ** 2
            worst["B3"] = min(worst["B3"], (Wk - 1 / (6 * mp.mpf(k) ** 1.5)) * mp.mpf(k) ** 1.5)
    for key, v in worst.items():
        print(f"{key}: minimum slack {mp.nstr(v, 6)}  -> {'OK' if v >= 0 else 'FAIL'}")


def forced_exact_vs_closed(k, n, b=1.0, beta=2.0):
    """exact forced A for g = level k versus the closed-form lower bound of Proposition M."""
    m, j = (n - 1) // 2, (k - 1) // 2
    Mk = mp.mpf(comb(2 * m, m)) * comb(m, j) / (mp.mpf(4) ** m * comb(2 * m, 2 * j))
    Wk = comb(n, k) * Mk ** 2
    Imaj = n * mp.mpf(comb(2 * m, m)) / mp.mpf(4) ** m
    B = b * mp.mpf(k) ** (-beta)
    C3 = 1 / (14 * mp.mpf(k) ** 0.75)
    num = Wk / 4 - B * mp.sqrt(Imaj * k * Wk) / 4 - C3 * mp.sqrt(Wk / 2) / 2
    den = mp.mpf(2) ** (-mp.mpf(3) / 8) * (Wk / 4) ** (mp.mpf(3) / 8) * mp.sqrt(Mk / 2)
    exact = num / den
    closed = mp.mpf(2) ** (-mp.mpf(11) / 8) * (6 * mp.mpf(k) ** 1.5) ** (-mp.mpf(5) / 8) * (mp.mpf(m) / j) ** (mp.mpf(j) / 2)
    cond = B <= (1 / (4 * mp.sqrt(6))) * mp.mpf(k) ** (-1.25) * mp.mpf(n) ** (-0.25)
    return exact, closed, cond


if __name__ == "__main__":
    limit_process()
    check()
    print()
    print("Proposition M: exact forced A versus closed-form bound (B = k^-2, C3 = k^-3/4/14)")
    for k in (5, 9, 17, 33, 65, 129, 257, 513, 1025):
        n0 = int((1 / (4 * mp.sqrt(6))) ** 4 * mp.mpf(k) ** (4 * 2 - 5))
        n = n0 if n0 % 2 == 1 else n0 - 1
        if n <= k:
            print(f"k={k}: admissible n = {n} <= k, skipped")
            continue
        ex, cl, cond = forced_exact_vs_closed(k, n)
        print(f"k={k:4d} n={n:>9d} condition(B)={bool(cond)} log2 exact={mp.nstr(mp.log(ex, 2), 8):>12s} "
              f"log2 closed={mp.nstr(mp.log(cl, 2), 8):>12s} closed<=exact: {cl <= ex}")
