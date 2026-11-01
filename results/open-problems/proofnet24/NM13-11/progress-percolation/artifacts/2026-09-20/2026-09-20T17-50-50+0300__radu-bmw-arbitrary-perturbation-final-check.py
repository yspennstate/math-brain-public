from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 80

# Theorem endpoint: Radu degree (6,4n), n=8, k=n arbitrary pairs.
assert Fraction(39, 7) ** 2 > 31          # sqrt(31) < 39/7
assert Fraction(9, 4) ** 2 > 5            # sqrt(5) < 9/4
m8 = Fraction(30) + Fraction(53, 30) - Fraction(78, 7) - Fraction(9, 2) - 16
assert m8 == Fraction(13, 105) and m8 > 0
assert 30**2 - 53 == 847 > 0
assert Fraction(1, 30) - Fraction(1, 31) == Fraction(1, 930)

# Monotonicity of the k=n margin for all real n>=8.
# M(x)=2x-2 +(6x+5)/(4x-2) -2sqrt(4x-1)-2sqrt(5)
# M'(x)=2 -32/(4x-2)^2 -4/sqrt(4x-1).
der1 = Fraction(2) - Fraction(8, 225) - Fraction(8, 11)
assert der1 == Fraction(3062, 2475) and der1 > 0
assert 16 * 8**2 - 22 * 8 - 1 == 847
assert 32 * 8 - 22 > 0

# Stronger explicit density: k <= 3n/2 for all n>=25.
# Worst-case continuous margin is
# M_3/2(x)=x-2 +(7x+5)/(4x-2)-2sqrt(4x-1)-2sqrt(5).
assert Fraction(10) ** 2 > 99             # sqrt(99)<10
m25 = Fraction(23) + Fraction(90, 49) - 20 - Fraction(9, 2)
assert m25 == Fraction(33, 98) and m25 > 0
# M_3/2'(x)=1-34/(4x-2)^2-4/sqrt(4x-1), x>=25;
# use 34/98^2=17/4802 and sqrt(99)>9.
der15 = Fraction(1) - Fraction(17, 4802) - Fraction(4, 9)
assert der15 == Fraction(23857, 43218) and der15 > 0
assert (4 * 25 - 2) ** 2 - (7 * 25 + 5) > 0

# Asymptotic arbitrary-density theorem: for 0<eps<=2,
# n>=16/eps^2 and k<=(2-eps)n. Dropping the positive Q/z term gives
# margin > 2 eps n -4sqrt(n)-13/2. If sqrt(n)>=4/eps,
# this is >=16/eps-13/2 >= 8-13/2 >0.
assert Fraction(8) > Fraction(13, 2)

# High-precision sanity checks (not load-bearing) for selected eps values.
def dsqrt(x: int) -> Decimal:
    return Decimal(x).sqrt()

def margin(n: int, k: int) -> Decimal:
    z = Decimal(4 * n - 2)
    Q = Decimal(4 * n + 5 + 2 * k)
    a = 2 * dsqrt(4 * n - 1) + 2 * dsqrt(5) + Decimal(2 * k)
    return z + Q / z - a

samples = []
for eps in (Fraction(1), Fraction(1, 2), Fraction(1, 4)):
    n0q = Fraction(16, 1) / (eps * eps)
    assert n0q.denominator == 1
    n0 = int(n0q)
    best = None
    best_arg = None
    for n in range(n0, min(n0 + 150, 800)):
        kmax = ((Fraction(2) - eps) * n).__floor__()
        for k in (0, kmax):
            mm = margin(n, k)
            assert mm > 0
            if best is None or mm < best:
                best = mm
                best_arg = (n, k)
    samples.append((str(eps), n0, best, best_arg))

print("n8_margin_lower =", m8)
print("n8_derivative_lower =", der1)
print("n8_gap =", Fraction(1, 930))
print("n25_3over2_margin_lower =", m25)
print("n25_3over2_derivative_lower =", der15)
for eps, n0, best, arg in samples:
    print("eps_sample", eps, "n0", n0, "min_margin", best, "at", arg)
print("ALL_EXACT_CHECKS_PASS")
