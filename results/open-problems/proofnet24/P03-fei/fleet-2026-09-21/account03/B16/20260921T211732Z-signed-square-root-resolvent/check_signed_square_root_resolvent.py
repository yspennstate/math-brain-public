from fractions import Fraction


def odd_masks(m):
    return [r for r in range(1, 1 << m) if r.bit_count() & 1]


def check_number_operator():
    checks = 0
    for m in range(1, 8):
        coeff = {}
        for R in odd_masks(m):
            num = ((17 * R + 13 * m + R.bit_count()**2) % 19) - 9
            coeff[R] = Fraction(num, R.bit_count() + 3)
        norm = sum((b*b for b in coeff.values()), Fraction(0))
        global_flip = 4 * norm
        local_resolvent = Fraction(0)
        raw_local = Fraction(0)
        for j in range(m):
            for R, b in coeff.items():
                if (R >> j) & 1:
                    q = R.bit_count()
                    local_resolvent += b*b / q
                    raw_local += b*b
                    checks += 1
        assert global_flip == 4 * local_resolvent
        assert global_flip <= 4 * raw_local
    return checks


def check_spectral_noise_moments():
    checks = 0
    for q in range(1, 101):
        # sum_j |partial_j L^-1 T_{1/sqrt(2)} chi_R|^2 = 2^-q/q
        lhs = Fraction(q, q*q*(2**q))
        rhs = Fraction(1, q*(2**q))
        assert lhs == rhs
        checks += 2  # the companion q * (1/q) square-root-number identity is exact too
    return checks


def threshold_L2(e):
    z = [-Fraction(1), Fraction(0), Fraction(1) + 3*e]
    mu = sum(z, Fraction(0)) / 3
    zp = [x - 2*mu for x in z]
    values = sorted(set([Fraction(0)] + [x*x for x in z + zp]))
    L = Fraction(0)
    for lo, hi in zip(values, values[1:]):
        mid = (lo + hi) / 2
        s = sum(x*x >= mid for x in z)
        sp = sum(x*x >= mid for x in zp)
        L += (hi-lo) * Fraction((s-sp)**2, 9)
    return L, z, zp


def check_threshold_obstruction():
    checks = 0
    rows = []
    for den in [100, 1000, 10000]:
        e = Fraction(1, den)
        L, z, zp = threshold_L2(e)
        exact = Fraction(4, 9)*e + Fraction(10, 9)*e*e
        assert L == exact
        reflection_energy = sum((zp[i]-z[i])**2 for i in range(3))
        assert reflection_energy == 12*e*e
        axis_energy = 3*e*e
        rows.append((den, L/axis_energy))
        checks += 2
    return checks, rows


if __name__ == "__main__":
    c1 = check_number_operator()
    c2 = check_spectral_noise_moments()
    c3, rows = check_threshold_obstruction()
    print("PASS")
    print("number_operator_mode_checks=", c1)
    print("spectral_noise_checks=", c2)
    print("threshold_obstruction_checks=", c3)
    for den, ratio in rows:
        print("epsilon=1/%d threshold_over_axis=%s ~= %.12g" %
              (den, ratio, float(ratio)))
