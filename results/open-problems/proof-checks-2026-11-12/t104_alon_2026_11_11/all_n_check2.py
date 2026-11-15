"""Coverage test for the elementary all-n proof: arbitrary sum-zero vectors (not built region by region) are
normalised, classified, and the step of the proof that applies is asserted exactly.  an agent, 11 Nov 2026."""
import random
import sys
from fractions import Fraction as F
from all_n_check import stats, psi_from


def sample(rnd, n):
    mode = rnd.randint(0, 7)
    den = 10**4
    r = lambda: F(rnd.randint(-den, den), den)
    if mode == 0:
        x = [r() for _ in range(n)]
    elif mode == 1:
        x = [r() ** 3 for _ in range(n)]
    elif mode == 2:   # near the edge vector
        e = F(1, rnd.choice([10, 100, 1000, 10**4, 10**6]))
        x = [F(1), F(-1)] + [e * r() for _ in range(n - 2)]
    elif mode == 3:   # near the star
        e = F(1, rnd.choice([10, 100, 1000, 10**5]))
        x = [F(n - 1)] + [-1 + e * r() for _ in range(n - 1)]
    elif mode == 4:   # few values
        vals = [r() for _ in range(rnd.randint(2, 4))]
        x = [rnd.choice(vals) for _ in range(n)]
    elif mode == 5:   # edge plus a few small of one sign
        e = F(1, rnd.choice([10, 100, 1000, 10**4]))
        k = rnd.randint(1, n - 2)
        x = [F(1), F(-1)] + [e * abs(r()) for _ in range(k)] + [F(0)] * (n - 2 - k)
    elif mode == 6:   # one big positive, two big negatives
        x = [F(1), -F(rnd.randint(1, den), den), -F(rnd.randint(1, den), den)] + [F(1, 10**3) * r() for _ in range(n - 3)]
    else:             # thresholds: second coordinate about 2/(n(n-1))
        t = F(2, n * (n - 1)) * F(rnd.randint(5000, 20000), den)
        x = [F(1), F(-1), t] + [t * r() for _ in range(n - 3)]
    s = sum(x) / n
    x = sorted((v - s for v in x), reverse=True)
    if x[0] == x[-1]:
        return None
    if x[0] + x[-1] < 0:
        x = sorted((-v for v in x), reverse=True)
    a = x[0]
    return [v / a for v in x]


def main():
    rnd = random.Random(99)
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    cases = {}
    least = None
    for n in list(range(14, 31)) + [40, 64, 101]:
        kappa = F(n - 1, n + 1)
        e1 = F(21, 10) / (n * (n - 1))
        e2 = F(2) / ((n - 2) * (n + 1))
        for _ in range(trials if n <= 30 else trials // 4):
            x = sample(rnd, n)
            if x is None:
                continue
            b = -x[-1]
            assert x[0] == 1 and 0 < b <= 1
            n_, T, P, Q, mT = stats(x)
            psi = psi_from(n, T, P, Q, mT)
            if x[1] + x[-2] >= 0:
                region, eps, M, thr = "I", x[1], x[1], e1
            else:
                region, eps, M, thr = "II", -x[-2], b * (-x[-2]), e2
            assert eps >= 0 and all(-eps <= v <= eps for v in x[1:-1]) and mT >= M
            if eps >= thr:
                key = region + " large"
                assert M / T >= F(1, n * (n - 1)), (n, region, [float(v) for v in x[:4]])
            else:
                key = region + " small"
                Y2 = sum(v * v for v in x[1:-1])
                G = (n - 4) * (2 * Q - T * T) * T - 2 * (n - 3) * P * P + (n - 1) * ((n * n - 6 * n + 6) * T * T + 2 * n * Q) * M
                L = (-(n - 4) * T * (4 * Y2 + Y2 * Y2) - 2 * (n - 3) * (3 * (n - 2) * eps + eps * Y2) ** 2
                     + (n - 1) * ((n * n - 6 * n + 6) * T * T + 2 * n) * kappa * eps)
                assert G >= L >= 0, (n, region, float(eps))
            assert psi >= 0
            cases[key] = cases.get(key, 0) + 1
            if least is None or psi < least[0]:
                least = (psi, n, key)
    print("cases:", cases)
    print(f"least Psi {float(least[0]):.3e} at n={least[1]} ({least[2]})")


if __name__ == "__main__":
    main()
