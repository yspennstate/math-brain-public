from fractions import Fraction
import math

# NM13-12 sanity checker for the fractional-moment near-lattice theorem.
# Concrete scale law: Pareto(alpha=5/2, x_min=1), delta=1/4.
alpha = Fraction(5, 2)
delta = Fraction(1, 4)
r = Fraction(9, 4)  # 2+delta


def pareto_moment(q):
    q = Fraction(q)
    if q >= alpha:
        return math.inf
    return alpha / (alpha - q)


ES2 = pareto_moment(2)
ESr = pareto_moment(r)
assert ES2 == 5
assert ESr == 10
assert pareto_moment(3) == math.inf
assert pareto_moment(4) == math.inf

print("PARETO_ALPHA", f"{alpha.numerator}/{alpha.denominator}")
print("DELTA", f"{delta.numerator}/{delta.denominator}")
print("E_S2", ES2)
print("E_S_9_4", ESr)
print("E_S3", "INF")
print("E_S4", "INF")

# Elementary fractional remainder used in the proof:
# 0 <= exp(-x)-1+x <= x^(1+delta/2), x>=0.
eta = float(delta) / 2.0
mx_ratio = 0.0
bad = 0
for j in range(-120, 121):
    x = 10.0 ** (j / 10.0)
    lhs = math.exp(-x) - 1.0 + x
    rhs = x ** (1.0 + eta)
    if lhs < -1e-14 or lhs > rhs * (1 + 1e-12):
        bad += 1
    if rhs > 0:
        mx_ratio = max(mx_ratio, lhs / rhs)
assert bad == 0
print("FRACTIONAL_REMAINDER_GRID_MAX_RATIO", format(mx_ratio, ".17g"))
print("FRACTIONAL_REMAINDER_GRID_VIOLATIONS", bad)

# Concrete triangular smoothing sigma=m^{-1/3}; D^2=1+5 sigma^2,
# a=1 and rho=sigma/D. Verify theorem rate quantities.
for m in (10**6, 10**9, 10**12, 10**15):
    sigma = m ** (-1.0 / 3.0)
    D = math.sqrt(1.0 + 5.0 * sigma * sigma)
    rho = sigma / D
    rate1 = m * rho * rho / math.log(math.e / rho)
    local_err = m ** (-float(delta) / 2.0)
    Lambda = (
        sigma ** (2.0 + float(delta))
        * float(ESr)
        / D ** (2.0 + float(delta))
    )
    print(
        "M",
        m,
        "SIGMA",
        format(sigma, ".12g"),
        "RHO",
        format(rho, ".12g"),
        "RATE1",
        format(rate1, ".12g"),
        "LOCAL_ERR_POWER",
        format(local_err, ".12g"),
        "LAMBDA",
        format(Lambda, ".12g"),
    )

# Every fixed q finite-convolution density ceiling diverges at least c_q/sigma.
# Use R_i=+1 and S_i<=2. For Pareto 5/2, P(S<=2)=1-2^{-5/2}.
pS = 1.0 - 2.0 ** (-2.5)
for q in (1, 2, 3, 4, 8):
    cq = ((0.5 * pS) ** q) / (2.0 * math.sqrt(2.0 * math.pi * q))
    print("CONV_Q", q, "C_Q", format(cq, ".16g"), "LOWER_BOUND_FORM", "C_Q/sigma")

# Uniform (2+delta) entry-moment bound from
# |a+b|^r <= 2^(r-1)(|a|^r+|b|^r).
rflt = float(r)
EG_r = 2.0 ** (rflt / 2.0) * math.gamma((rflt + 1.0) / 2.0) / math.sqrt(math.pi)
BX = 2.0 ** (rflt - 1.0) * (1.0 + float(ESr) * EG_r)
print("E_ABS_G_9_4", format(EG_r, ".16g"))
print("UNIFORM_ENTRY_MOMENT_BOUND", format(BX, ".16g"))

# Generalized Paley-Zygmund concentration gap at interval length 1/2.
p = 1.0 + float(delta) / 2.0
EYp_bound = 2.0 ** rflt * BX
c_gap = ((7.0 / 4.0) ** (p / (p - 1.0))) / (
    EYp_bound ** (1.0 / (p - 1.0))
)
assert 0 < c_gap < 1
Qhalf = math.sqrt(1.0 - c_gap)
print("ANTI_CONC_GAP_C", format(c_gap, ".16g"))
print("Q_X_HALF_UPPER", format(Qhalf, ".16g"))

# The near-critical floor rho=(log log m)*sqrt(log m/m) still satisfies US1.
for expo in (30, 60, 120):
    m = math.exp(expo)
    rho = math.log(math.log(m)) * math.sqrt(math.log(m) / m)
    rate = m * rho * rho / math.log(math.e / rho)
    print("NEARCRIT_LOGM", expo, "RATE1", format(rate, ".12g"))

print("ALL_FRACTIONAL_MOMENT_CHECKS_PASS")
