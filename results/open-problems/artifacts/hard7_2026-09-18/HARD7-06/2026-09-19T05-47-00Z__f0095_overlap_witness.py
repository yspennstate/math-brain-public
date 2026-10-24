from fractions import Fraction

# Exact-arithmetic certificate for the balanced 3-colouring second-moment
# obstruction used in the HARD7-06 F0095 admission/rotation report.
#
# Symmetric overlap family A_s has diagonal (1+2s)/9 and off-diagonal
# (1-s)/9.  For G(n,m), m=(d/2)n, the normalized exponent is
#
# Phi_d(s) = -(1/3)(1+2s)log(1+2s)
#            -(2/3)(1-s)log(1-s)
#            +(d/2)log(1+s^2/2).
#
# We certify Phi_{383/100}(7/25)>0 using rational enclosures for log.

N = 30
s = Fraction(7, 25)
d = Fraction(383, 100)


def log_interval(q: Fraction):
    """Rigorous rational interval for log(q), q>0, via atanh series.

    log q = 2 * sum_{k>=0} y^(2k+1)/(2k+1), y=(q-1)/(q+1).
    The omitted absolute tail is bounded geometrically.
    """
    assert q > 0
    y = (q - 1) / (q + 1)
    partial = Fraction(0)
    for k in range(N + 1):
        partial += y ** (2 * k + 1) / Fraction(2 * k + 1)
    partial *= 2
    ay = abs(y)
    rem = 2 * ay ** (2 * N + 3) / (Fraction(2 * N + 3) * (1 - ay * ay))
    return partial - rem, partial + rem


def scale_interval(c: Fraction, interval):
    lo, hi = interval
    if c >= 0:
        return c * lo, c * hi
    return c * hi, c * lo


def add_intervals(*intervals):
    return (
        sum((x[0] for x in intervals), Fraction(0)),
        sum((x[1] for x in intervals), Fraction(0)),
    )


# s=7/25 gives 1+2s=39/25, 1-s=18/25,
# 1+s^2/2 = 1299/1250.
I1 = log_interval(Fraction(39, 25))
I2 = log_interval(Fraction(18, 25))
I3 = log_interval(Fraction(1299, 1250))

phi = add_intervals(
    scale_interval(Fraction(-13, 25), I1),
    scale_interval(Fraction(-12, 25), I2),
    scale_interval(Fraction(383, 200), I3),
)

lo, hi = phi

print("N =", N)
print("s =", s)
print("d =", d)
print("phi_lower_exact =", lo)
print("phi_upper_exact =", hi)
print("phi_lower_float =", float(lo))
print("phi_upper_float =", float(hi))
print("PHI_STRICTLY_POSITIVE =", lo > 0)
print("ALL_EXACT_CHECKS_PASS =", lo > 0 and lo <= hi)
