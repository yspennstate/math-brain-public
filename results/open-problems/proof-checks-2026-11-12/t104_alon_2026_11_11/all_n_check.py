"""Check of the elementary proof that Psi >= 0 for every n >= 14 (an agent, 11 Nov 2026).

Normalise x_1 = 1 >= b = -x_n > 0 (negate x if necessary), x sorted decreasingly, sum 0.
  (I)  x_2 + x_(n-1) >= 0:  eps = x_2 >= 0, the middle coordinates lie in [-eps, eps], M = x_1 x_2 = eps.
  (II) x_2 + x_(n-1) <= 0:  eps = -x_(n-1) >= 0, the middle coordinates lie in [-eps, eps], M = x_n x_(n-1) = b eps.
Step 1: Psi >= 2(n-3)(q - p^2 - 1/n) + C (m - 1/(n(n-1))), and q - p^2 >= 1/n (Gram determinant of 1, x, x^2).
Step 2: M / T >= 1/(n(n-1)) when eps >= e1 = 2.1/(n(n-1)) in (I), eps >= e2 = 2/((n-2)(n+1)) in (II).
Step 3: for eps below that, G = T^3 Psi_M >= L := -(n-4) T (4 Y2 + Y2^2) - 2(n-3)(3(n-2) eps + eps Y2)^2
        + (n-1)((n^2-6n+6) T^2 + 2n) kappa eps  >= 0,  kappa = (n-1)/(n+1).
The script tests every step exactly (Fractions) on random and extreme vectors, and the scalar facts for n = 14..2000.
"""
import random
import sys
from fractions import Fraction as F


def stats(x):
    n = len(x)
    T = sum(v * v for v in x)
    P = sum(v**3 for v in x)
    Q = sum(v**4 for v in x)
    xs = sorted(x, reverse=True)
    mT = max(xs[0] * xs[1], xs[-1] * xs[-2])
    return n, T, P, Q, mT


def psi_from(n, T, P, Q, mT):
    q, p2, m = Q / T**2, P * P / T**3, mT / T
    return (n - 4) * (2 * q - 1) - 2 * (n - 3) * p2 + (n - 1) * (n * n - 6 * n + 6 + 2 * n * q) * m


def make(rnd, n, region, small):
    """a vector of the region with x_1 = 1; small: eps below the threshold."""
    e1 = F(21, 10) / (n * (n - 1))
    e2 = F(2) / ((n - 2) * (n + 1))
    thr = e1 if region == "I" else e2
    den = 10**6
    for _ in range(200):
        if small:
            eps = thr * F(rnd.randint(1, den), den) * F(rnd.choice([1, 1, 1, 100, 10000]), 10000) * 1
            eps = min(eps, thr)
        else:
            eps = thr + (1 - thr) * F(rnd.randint(0, den), den) ** rnd.choice([1, 3, 8])
        mode = rnd.randint(0, 4)
        mid = []
        for i in range(n - 2):
            if mode == 0:
                mid.append(eps * F(rnd.randint(-den, den), den))
            elif mode == 1:
                mid.append(eps * rnd.choice([-1, 1]))
            elif mode == 2:
                mid.append(-eps * F(rnd.randint(0, den), den))
            elif mode == 3:
                mid.append(eps * rnd.choice([-1, 0, 0, 0, 1]))
            else:
                mid.append(-eps if rnd.random() < 0.9 else eps * F(rnd.randint(-den, den), den))
        mid.sort(reverse=True)
        if region == "I":
            mid[0] = eps          # x_2 = eps, the others in [-eps, eps]
        else:
            mid[-1] = -eps        # x_(n-1) = -eps
        b = 1 + sum(mid)
        if not (0 < b <= 1):
            continue
        if -b > mid[-1]:
            continue              # x_n must be the least coordinate
        x = [F(1)] + mid + [-b]
        if region == "I" and not (x[1] + x[-2] >= 0):
            continue
        if region == "II" and not (x[1] + x[-2] <= 0):
            continue
        return x, eps, b
    return None


def main():
    rnd = random.Random(2026)
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    # scalar facts
    for n in range(14, 2001):
        e1 = F(21, 10) / (n * (n - 1))
        e2 = F(2) / ((n - 2) * (n + 1))
        assert e2 <= e1
        assert (n - 2) * e1 * e1 - n * (n - 1) * e1 + 2 <= 0 and (n - 2) - n * (n - 1) + 2 <= 0
        g = lambda c: -(n - 2) * (n * n - 1) * c * c + (n * n + n - 4) * c - 2
        assert g(e2) == 0 and g(F(1, n - 1)) == 0
        kappa = F(n - 1, n + 1)
        eta = (n - 2) * e1 * e1
        assert eta <= F(2, 1000)
        # final scalar inequality of step 3, per unit eps, with T in [1, 2 + eta]
        neg1_over_pos1 = (F(4002, 1000) * (n - 4) * (n - 2) * e1) / ((n - 1) * (n * n - 6 * n + 6) * kappa)
        assert neg1_over_pos1 <= F(1, 100)
        neg2 = 2 * (n - 3) * (3 * (n - 2) + F(2, 1000)) ** 2 * e1
        pos = F(99, 100) * (n - 1) * (n * n - 6 * n + 6) * kappa
        assert pos >= neg2, n
    print("scalar facts hold for n = 14..2000")
    worst = None
    cnt = 0
    for n in list(range(14, 41)) + [50, 64, 100, 150, 257]:
        kappa = F(n - 1, n + 1)
        for region in ("I", "II"):
            for small in (True, False):
                for _ in range(trials if n <= 40 else max(20, trials // 6)):
                    r = make(rnd, n, region, small)
                    if r is None:
                        continue
                    x, eps, b = r
                    cnt += 1
                    n_, T, P, Q, mT = stats(x)
                    psi = psi_from(n, T, P, Q, mT)
                    M = eps if region == "I" else b * eps
                    assert mT >= M
                    # step 1
                    q, p2 = Q / T**2, P * P / T**3
                    C = (n - 1) * (n * n - 6 * n + 6 + 2 * n * q)
                    assert q - p2 >= F(1, n)
                    assert psi == 2 * (n - 3) * (q - p2 - F(1, n)) + C * (mT / T - F(1, n * (n - 1)))
                    if not small:
                        assert M / T >= F(1, n * (n - 1)), (n, region, float(eps))
                        assert psi >= 0
                    else:
                        Y2 = sum(v * v for v in x[1:-1])
                        assert Y2 <= (n - 2) * eps * eps
                        G = (n - 4) * (2 * Q - T * T) * T - 2 * (n - 3) * P * P + (n - 1) * ((n * n - 6 * n + 6) * T * T + 2 * n * Q) * M
                        L = (-(n - 4) * T * (4 * Y2 + Y2 * Y2) - 2 * (n - 3) * (3 * (n - 2) * eps + eps * Y2) ** 2
                             + (n - 1) * ((n * n - 6 * n + 6) * T * T + 2 * n) * kappa * eps)
                        assert G >= L >= 0, (n, region, float(eps), float(G), float(L))
                        assert psi >= 0
                        if eps > 0:
                            ratio = L / G if G > 0 else None
                    if worst is None or psi < worst[0]:
                        worst = (psi, n, region, small)
    print(f"{cnt} vectors, every step holds; least Psi {float(worst[0]):.3e} at n={worst[1]} region {worst[2]} small={worst[3]}")


if __name__ == "__main__":
    main()
