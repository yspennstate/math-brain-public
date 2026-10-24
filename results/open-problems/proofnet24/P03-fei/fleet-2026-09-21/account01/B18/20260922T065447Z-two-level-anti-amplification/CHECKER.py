from fractions import Fraction


def ln_bounds(q, N=50):
    q = Fraction(q)
    if q <= 0:
        raise ValueError("q must be positive")
    if q == 1:
        return Fraction(0), Fraction(0)
    if q < 1:
        lo, hi = ln_bounds(1 / q, N)
        return -hi, -lo
    x = (q - 1) / (q + 1)
    s = Fraction(0)
    for k in range(N + 1):
        s += x ** (2 * k + 1) / Fraction(2 * k + 1)
    lo = 2 * s
    tail = 2 * x ** (2 * N + 3) / Fraction(2 * N + 3) / (1 - x * x)
    return lo, lo + tail


def h2_bounds(p, N=50):
    p = Fraction(p)
    q = 1 - p
    lp_lo, lp_hi = ln_bounds(p, N)
    lq_lo, lq_hi = ln_bounds(q, N)
    n_lo = p * (-lp_hi) + q * (-lq_hi)
    n_hi = p * (-lp_lo) + q * (-lq_lo)
    l2_lo, l2_hi = ln_bounds(Fraction(2), N)
    return n_lo / l2_hi, n_hi / l2_lo


C = Fraction(6521851214, 10**9)
ln2_lo, ln2_hi = ln_bounds(Fraction(2), 50)
assert ln2_lo > Fraction(693, 1000)

# A = C - 2/ln 2.  For a lower bound on A, divide by the lower
# bound for ln 2.
A_lower = C - Fraction(2) / ln2_lo
assert A_lower > Fraction(363, 100)

# M = log_2(1+2^{-A}).  The report uses the elementary chain
# A>3.63, ln2>.693, e^t>1+t+t^2/2, and ln(1+x)<x.
t0 = Fraction(63, 100) * Fraction(693, 1000)
exp_lb = 1 + t0 + t0 * t0 / 2
r_ub = Fraction(1) / (8 * exp_lb)
M_ub = r_ub / Fraction(693, 1000)
assert M_ub < Fraction(59, 500)  # 0.118

p_both = Fraction(131, 500)  # 0.262
p_one = Fraction(39, 125)    # 0.312
_, h_both_hi = h2_bounds(p_both, 50)
_, h_one_hi = h2_bounds(p_one, 50)
assert h_both_hi < Fraction(83, 100)    # 0.83
assert h_one_hi < Fraction(112, 125)    # 0.896

# F(d) >= A d - h2(d) on [0,1/2].  Use the coarse certified A>3.63.
pay_both_lb = Fraction(363, 100) * p_both - Fraction(83, 100)
pay_one_lb = Fraction(363, 100) * p_one - Fraction(112, 125)
assert pay_both_lb == Fraction(6053, 50000)  # 0.12106
assert pay_one_lb == Fraction(2957, 12500)   # 0.23656
assert pay_both_lb > Fraction(59, 500)
assert pay_one_lb > 2 * Fraction(59, 500)

print("PASS")
print("ln2_lower", float(ln2_lo))
print("A_lower", float(A_lower))
print("M_upper_hand", float(M_ub))
print("h2_0.262_upper", float(h_both_hi))
print("F_0.262_lower", float(pay_both_lb))
print("margin_0.262_over_0.118", float(pay_both_lb - Fraction(59, 500)))
print("h2_0.312_upper", float(h_one_hi))
print("F_0.312_lower", float(pay_one_lb))
print("margin_0.312_over_0.236", float(pay_one_lb - 2 * Fraction(59, 500)))
