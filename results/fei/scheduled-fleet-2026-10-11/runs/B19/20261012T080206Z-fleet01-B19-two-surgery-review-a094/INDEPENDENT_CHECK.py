from fractions import Fraction
from itertools import combinations


def fwht(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                u, v = a[j], a[j + h]
                a[j], a[j + h] = u + v, u - v
        h *= 2
    return a


def bent_truth(k):
    out = []
    for x in range(1 << k):
        q = 0
        for j in range(0, k, 2):
            q ^= ((x >> j) & 1) & ((x >> (j + 1)) & 1)
        out.append(-1 if q else 1)
    return out


def char(s, x):
    return -1 if ((s & x).bit_count() & 1) else 1


def caps_direct(q, k):
    n = 1 << k
    return [sum(q[t] for t in range(n) if (t & s) == s) for s in range(n)]


def log2_dyadic(q):
    assert q > 0
    a, b = q.numerator, q.denominator
    assert a & (a - 1) == 0 and b & (b - 1) == 0
    return a.bit_length() - b.bit_length()


def direct_pair(k, x, y, do_walsh):
    n = 1 << k
    delta = Fraction(1, n)
    truth = bent_truth(k)
    gx, gy = truth[x], truth[y]
    z, r = x ^ y, (x ^ y).bit_count()
    tau = gx * gy
    sigma = tau * (-1 if r & 1 else 1)
    ex = [Fraction(-2 * gx * char(t, x), n) for t in range(n)]
    ey = [Fraction(-2 * gy * char(t, y), n) for t in range(n)]
    assertions = 0
    if do_walsh:
        base = fwht(truth)
        tx = list(truth); tx[x] *= -1
        txy = list(tx); txy[y] *= -1
        wx, wxy = fwht(tx), fwht(txy)
        for t in range(n):
            assert Fraction(wx[t] - base[t], n) == ex[t]
            assert Fraction(wxy[t] - wx[t], n) == ey[t]
            assertions += 2
    qx = [u * u for u in ex]
    qy = [u * u for u in ey]
    qxy = [(ex[t] + ey[t]) ** 2 for t in range(n)]
    dx, dy, dxy = caps_direct(qx, k), caps_direct(qy, k), caps_direct(qxy, k)
    for s in range(n):
        filt = (s & z) == z
        basecap = Fraction(1, 1 << s.bit_count())
        assert dx[s] == 4 * delta * basecap
        assert dy[s] == 4 * delta * basecap
        assert dxy[s] == 8 * delta * basecap * (1 + (sigma if filt else 0))
        cross = dxy[s] - dx[s] - dy[s]
        assert cross == (8 * sigma * delta * basecap if filt else 0)
        assertions += 4
    packets = []
    for q, d in [(qx, dx), (qy, dy), (qxy, dxy)]:
        val = Fraction(0)
        for t in range(n):
            if q[t]:
                val += q[t] * log2_dyadic(d[t] / q[t])
                assertions += 1
        packets.append(val)
    ux, uy, uxy = packets
    rho = ux + uy - uxy
    expected = 4 * delta if r == 1 else 8 * delta - (Fraction(16, 1 << r) * delta if sigma == 1 else 0)
    assert ux == uy == 2 * delta * k
    assert rho == expected
    assert 8 * delta * Fraction(1, 1 << r) <= rho
    assertions += 3
    return assertions


def scalar_all_parameters():
    assertions = 0
    for k in range(2, 202, 2):
        delta = Fraction(1, 1 << k)
        for r in range(1, k + 1):
            for sigma in (-1, 1):
                rho = 4 * delta if r == 1 else 8 * delta - (Fraction(16, 1 << r) * delta if sigma == 1 else 0)
                assert 4 * delta <= rho <= 8 * delta
                assert 8 * delta * Fraction(1, 1 << r) <= rho
                assertions += 2
    return assertions


def main():
    assertions = pairs = 0
    for k in (2, 4, 6):
        n = 1 << k
        for x, y in combinations(range(n), 2):
            assertions += direct_pair(k, x, y, do_walsh=(k <= 4))
            pairs += 1
    # Larger direct-cap spot checks remain deliberately bounded: caps_direct
    # enumerates supersets independently rather than using the author's zeta
    # transform.  The closed scalar endpoint inequalities are checked through
    # k=200 below.
    for k in (8,):
        n = 1 << k
        masks = [1, 2, 3, 5, 7, 15, (1 << (k // 2)) - 1, n - 1]
        for x in [0, 1, n // 3, n - 1]:
            for m in masks:
                y = x ^ m
                assertions += direct_pair(k, x, y, do_walsh=(k == 8 and x in (0, n - 1)))
                pairs += 1
    assertions += scalar_all_parameters()
    print(f"direct_pairs={pairs}")
    print(f"assertions={assertions}")
    print("status=PASS")


if __name__ == "__main__":
    main()
