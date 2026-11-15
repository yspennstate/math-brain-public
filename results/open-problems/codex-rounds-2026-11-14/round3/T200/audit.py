"""Independent baseline audit and exact certificate for the capacity-moment lemma.

OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py moment
Only the Python standard library is used; no file writes occur here.
"""

import ctypes
from decimal import Decimal, getcontext
from fractions import Fraction as F
import math
import os
import resource
import sys


def guard():
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    libc = ctypes.CDLL(None, use_errno=True)
    ctypes.set_errno(0)
    priority = libc.getpriority(0, 0)
    assert ctypes.get_errno() == 0 and priority >= 15
    print(f"niceness={priority}; OMP_NUM_THREADS=1; CPU_limit=60s")


def dec(x):
    x = F(x)
    return Decimal(x.numerator) / Decimal(x.denominator)


def exp_partial(x, n):
    term = F(1)
    result = term
    for j in range(1, n + 1):
        term *= x / j
        result += term
    return result


def log_interval(x, n=100):
    """Rational lower/upper bounds; x must exceed one."""
    assert x > 1
    z = (x - 1) / (x + 1)
    term = z
    total = F(0)
    for j in range(n):
        total += 2 * term / (2 * j + 1)
        term *= z * z
    return total, total + 2 * term / ((2 * n + 1) * (1 - z * z))


def pi_geometric_lower():
    # pi > half the perimeter of an inscribed regular 48-gon:
    # 24 sqrt(2 - sqrt(2 + sqrt(2 + sqrt(3)))).
    a, b, c, d = F(173206, 100000), F(1931855, 1000000), F(1982891, 1000000), F(1308, 10000)
    assert a * a > 3
    assert b * b > 2 + a
    assert c * c > 2 + b
    assert d * d < 2 - c
    lower = 24 * d
    assert lower > F(177, 100) ** 2
    return lower


def decimal_pi():
    # Independent high-precision calculation by Machin's identity.
    def atan(x):
        value, term = Decimal(0), x
        for j in range(110):
            value += term / (2 * j + 1)
            term *= -x * x
        return value
    return 16 * atan(Decimal(1) / 5) - 4 * atan(Decimal(1) / 239)


def baseline():
    green = F(1, 3) - F(3, 11)
    assert green == F(2, 33)
    assert 2 * (F(2) - F(2, 3)) == F(8, 3)
    assert exp_partial(F(15, 2), 30) > 1800
    assert pi_geometric_lower() > F(177, 100) ** 2
    failure_upper = F(1, 120) + F(104, 885)
    assert failure_upper < F(63, 500)
    assert 775**31 * 225**9 > 3**40 * 126**31 * 874**9
    q, h = F(9, 40), F(13, 16500)
    l3, u3 = log_interval(F(3))
    # An independent -log(1-h) power series, with a geometric tail bound.
    lh = sum((h**j / j for j in range(1, 20)), F(0))
    uh = lh + h**20 / (20 * (1 - h))
    old_lo, old_hi = q * lh / u3, q * uh / l3
    assert F(1, 6250) < old_lo < old_hi
    pi = decimal_pi()
    p = 6 * Decimal(6).sqrt() * (Decimal(-15) / 2).exp() + dec(F(13, 1000)) * 16 / pi.sqrt()
    a, p0 = dec(F(31, 40)), dec(F(63, 500))
    tail = (a * (a / p0).ln() + (1-a) * ((1-a)/(1-p0)).ln()) / Decimal(3).ln()
    gap = -dec(q) * (1-dec(h)).ln() / Decimal(3).ln()
    assert dec(old_lo) <= gap <= dec(old_hi)
    assert p < p0 and tail > 1
    print(f"old_failure_upper={p}")
    print(f"old_tail_exponent={tail}")
    print(f"old_gap_interval=[{dec(old_lo)}, {dec(old_hi)}]")
    print(f"old_xi_upper={1-gap}")
    print("EARLIER RESULT VERIFIED independently")


def moment():
    pi_lower = pi_geometric_lower()
    assert exp_partial(F(15, 2), 30) > 1800
    # e > 27/10 from its fourth Taylor sum; e < 11/4 from a tail bound.
    e_lo = exp_partial(F(1), 4)
    e_hi = exp_partial(F(1), 4) + F(1, 120) / (1 - F(1, 6))
    assert e_lo > F(27, 10) and e_hi < F(11, 4)
    # sqrt(6)<5/2; sqrt(pi)>177/100.
    exit_upper = F(15, 1800)
    energy_upper = F(1600, 177)
    laplace_upper = exit_upper + energy_upper / (30 * F(27, 10))
    laplace_rounded = F(3, 25)
    assert laplace_upper < laplace_rounded
    tail_base = laplace_rounded * F(11, 4)
    assert tail_base == F(33, 100) < F(1, 3)
    green, average_capacity = F(2, 33), F(1, 30)
    numerator = green * average_capacity
    assert numerator == F(1, 495)
    l3, u3 = log_interval(F(3))
    delta_lo, delta_hi = numerator/u3, numerator/l3
    assert exp_partial(F(11, 10), 6) > 3
    assert numerator/F(11, 10) == F(2, 1089) > F(183, 100000)
    assert delta_lo > F(183, 100000)
    pi = decimal_pi()
    exact_exit = 6 * Decimal(6).sqrt() * (Decimal(-15) / 2).exp()
    exact_energy = 16/pi.sqrt()
    m = exact_exit + exact_energy/(30*Decimal(1).exp())
    tail = -(Decimal(33)/100).ln()/Decimal(3).ln()
    delta = dec(numerator)/Decimal(3).ln()
    assert m < dec(laplace_upper) < dec(laplace_rounded)
    assert dec(delta_lo) <= delta <= dec(delta_hi)
    # Independent double-precision evaluation uses libm constants/functions.
    float_delta = (2/33)/(30*math.log(3))
    assert abs(float(delta)-float_delta) < 1e-17
    print(f"polygon_pi_lower={pi_lower}")
    print(f"e_interval=({e_lo}, {e_hi})")
    print(f"rational_laplace_upper={laplace_upper}")
    print(f"rational_margin_below_3_over_25={laplace_rounded-laplace_upper}")
    print(f"unrounded_laplace_bound={m}")
    print(f"certified_tail_base={tail_base}")
    print(f"certified_tail_exponent={tail}")
    print(f"delta_interval=[{dec(delta_lo)}, {dec(delta_hi)}]")
    print(f"xi_upper={1-delta}")
    print(f"coarse_xi_upper={F(1087, 1089)} < 99817/100000")
    print("ALL CAPACITY-MOMENT CERTIFICATE CHECKS PASSED")


if __name__ == "__main__":
    guard()
    getcontext().prec = 65
    if sys.argv[1:] == ["baseline"]:
        baseline()
    elif sys.argv[1:] == ["moment"]:
        moment()
    else:
        raise SystemExit("choose baseline or moment")
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == "darwin" else rss*1024
    assert rss_bytes < 1024**3
    print(f"peak_RSS_bytes={rss_bytes}")
