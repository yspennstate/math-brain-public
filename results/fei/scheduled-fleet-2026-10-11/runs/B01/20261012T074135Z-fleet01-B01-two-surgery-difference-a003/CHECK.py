from fractions import Fraction


def chi(mask, point):
    return -1 if ((mask & point).bit_count() & 1) else 1


def bent_value(point, k):
    q = 0
    for j in range(0, k, 2):
        q ^= ((point >> j) & 1) & ((point >> (j + 1)) & 1)
    return -1 if q else 1


def upper_zeta(values, k):
    out = list(values)
    for bit in range(k):
        step = 1 << bit
        for s in range(1 << k):
            if not (s & step):
                out[s] += out[s | step]
    return out


def log2_power_of_two(q):
    assert q > 0
    num, den = q.numerator, q.denominator
    assert num & (num - 1) == 0
    assert den & (den - 1) == 0
    return num.bit_length() - den.bit_length()


def check_pair(k, x, y):
    n = 1 << k
    delta = Fraction(1, n)
    z = x ^ y
    r = z.bit_count()
    gx, gy = bent_value(x, k), bent_value(y, k)
    tau = gx * gy
    sigma = tau * (-1 if r & 1 else 1)
    ex = [Fraction(-2 * gx * chi(t, x), n) for t in range(n)]
    ey = [Fraction(-2 * gy * chi(t, y), n) for t in range(n)]
    qx = [v * v for v in ex]
    qy = [v * v for v in ey]
    q = [(ex[t] + ey[t]) ** 2 for t in range(n)]
    dx, dy, dc = upper_zeta(qx, k), upper_zeta(qy, k), upper_zeta(q, k)
    assertions = 0
    for s in range(n):
        filt = (s & z) == z
        expected = 8 * delta * Fraction(1, 1 << s.bit_count())
        expected *= 1 + (sigma if filt else 0)
        assert dc[s] == expected
        cross = dc[s] - dx[s] - dy[s]
        expected_cross = 8 * sigma * delta * Fraction(1, 1 << s.bit_count()) if filt else 0
        assert cross == expected_cross
        assertions += 2
    ux = uy = ud = Fraction(0)
    for t in range(n):
        ux += qx[t] * log2_power_of_two(dx[t] / qx[t])
        uy += qy[t] * log2_power_of_two(dy[t] / qy[t])
        if q[t]:
            ud += q[t] * log2_power_of_two(dc[t] / q[t])
        assertions += 3
    assert ux == 2 * delta * k
    assert uy == 2 * delta * k
    rho = 4 * delta if r == 1 else 8 * delta - (Fraction(1 << (4-r), 1) * delta if r <= 4 and sigma == 1 else (Fraction(1, 1 << (r-4)) * delta if r > 4 and sigma == 1 else 0))
    assert ux + uy - ud == rho
    assert 4 * delta <= rho <= 8 * delta
    first_var = 8 * delta * Fraction(1, 1 << r)
    assert first_var <= rho
    return assertions + 5


def pair_set(k):
    n = 1 << k
    if k <= 6:
        return [(x, y) for x in range(n) for y in range(x + 1, n)]
    out = set()
    seeds = [0, 1, 3, 5, n // 3, n // 2, n - 2, n - 1]
    for x in seeds:
        for rmask in [1, 2, 3, 5, 7, 15, (1 << (k // 2)) - 1, n - 1]:
            y = x ^ rmask
            if x != y:
                out.add(tuple(sorted((x, y))))
    return sorted(out)


def main():
    total = pairs = 0
    for k in [2, 4, 6, 8, 10, 12]:
        for x, y in pair_set(k):
            total += check_pair(k, x, y)
            pairs += 1
    print(f"pairs={pairs}")
    print(f"assertions={total}")
    print("status=PASS")


if __name__ == "__main__":
    main()
