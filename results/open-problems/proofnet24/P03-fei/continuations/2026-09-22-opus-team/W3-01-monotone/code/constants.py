"""Constants of Theorems 1-3 and Proposition 4 (mpmath, 30 digits).

B = 3 sqrt(3/pi), L1 = 2 ln B + 2,
C(K) = 3 + min_{a>1} [1 + ln(a/(a-1)) + a (L1 + ln K)] / ln 2      (Theorem 2; Theorem 1 is K = 1),
c3   = 1 + min_{a>1} [1 + ln(a/(a-1)) + a L1] / ln 2 = C(1) - 2      (Theorem 3).
The minimiser solves a(a-1) = 1/L with L = L1 + ln K.
"""
from mpmath import mp, mpf, sqrt, pi, log, findroot, diff

mp.dps = 30
B = 3 * sqrt(3 / pi)
L1 = 2 * log(B) + 2


def C(K):
    L = L1 + log(mpf(K))
    a = (1 + sqrt(1 + 4 / L)) / 2
    val = 3 + (1 + log(a / (a - 1)) + a * L) / log(2)
    # check stationarity numerically
    g = lambda t: (1 + log(t / (t - 1)) + t * L) / log(2)
    assert abs(diff(g, a)) < mpf(10) ** -20
    return val, a


if __name__ == "__main__":
    print(f"B  = {B}")
    print(f"L1 = {L1}")
    for K in (1, 2, 3, 4, 6, 8, 16, 64, 256, 1024):
        v, a = C(K)
        print(f"C({K:5d}) = {mp.nstr(v, 12):>16s}   (a = {mp.nstr(a, 10)})   C(K) - log2 K = {mp.nstr(v - log(K)/log(2), 8)}")
    v1, _ = C(1)
    print(f"c3 = C(1) - 2 = {v1 - 2}")
    print(f"Proposition 4 with the certified read-once constant 6.4573: 6.4573 + C(1) = {mpf('6.4573') + v1}")
