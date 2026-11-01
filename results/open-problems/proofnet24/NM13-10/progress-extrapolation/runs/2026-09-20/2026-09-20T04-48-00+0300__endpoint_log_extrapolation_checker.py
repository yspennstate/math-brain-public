import math


def R(p):
    return 1.0 / (math.sqrt(2.0 / (p - 1.0)) - 1.0)


def R_eps(eps):
    p = 3.0 - eps
    s = math.sqrt(1.0 - eps / 2.0)
    exact = R(p)
    rationalized = 2.0 * s * (1.0 + s) / eps
    assert abs(exact - rationalized) <= 1e-10 * max(1.0, exact)
    assert exact <= 4.0 / eps + 1e-12
    return exact


R2 = R(2.0)
small_crude = 4.0 * math.sqrt(math.e) / 3.0
assert small_crude < R2

# Moderate quantiles: L=log(T/s) in [0,3], p=2.
# q2(L)=R2 exp(L/6)/(1+L); its logarithmic derivative is
# 1/6 - 1/(1+L)<0 on [0,3].
for j in range(10001):
    L = 3.0 * j / 10000.0
    q2 = R2 * math.exp(L / 6.0) / (1.0 + L)
    assert q2 <= R2 * (1.0 + 1e-12)

# Small quantiles: L>=3, choose eps=3/L and p=3-eps.
# The exact rearrangement coefficient is R_p exp(1/p)/(1+L).
max_q = 0.0
argmax = None
for j in range(200000):
    t = j / 199999.0
    L = 3.0 * math.exp(t * math.log(1e6 / 3.0))
    eps = 3.0 / L
    p = 3.0 - eps
    q = R(p) * math.exp(1.0 / p) / (1.0 + L)
    if q > max_q:
        max_q, argmax = q, L
    assert q <= small_crude * (1.0 + 1e-10)
assert max_q < R2

# Marcinkiewicz weak-(3,3) contradiction coefficient.
# If A=R2 is the strong-(2,2) norm and W is a hypothetical weak-(3,3)
# norm, then
# R_p^p <= p*2^p*A^{2(3-p)}*W^{3(p-2)}
#          *(1/(p-2)+1/(3-p)).
# For fixed W the RHS grows only like eps^{-1}, whereas R_p^p grows
# like 64 eps^{-3}.
for W in [1.0, 10.0, 100.0]:
    ratios = []
    for eps in [0.1, 0.05, 0.02, 0.01, 0.005, 0.002]:
        p = 3.0 - eps
        D = 1.0 / (p - 2.0) + 1.0 / (3.0 - p)
        rhs = (
            p
            * (2.0**p)
            * (R2 ** (2.0 * (3.0 - p)))
            * (W ** (3.0 * (p - 2.0)))
            * D
        )
        lhs = R(p) ** p
        ratios.append(lhs / rhs)
    assert ratios[-1] > ratios[0]

print("CHECK_PASS")
print(f"R2 = {R2:.15f}")
print(f"4*sqrt(e)/3 = {small_crude:.15f}")
print(
    f"small-quantile exact max over grid = {max_q:.15f} "
    f"at L={argmax:.6g}"
)
for eps in [1.0, 0.5, 0.2, 0.1, 0.05, 0.01, 0.001]:
    rp = R_eps(eps)
    print(
        f"eps={eps:g} R_{{3-eps}}={rp:.15f} "
        f"eps*R={eps*rp:.15f} 4/eps-R={4/eps-rp:.15f}"
    )
for eps in [0.1, 0.05, 0.02, 0.01, 0.005]:
    p = 3.0 - eps
    D = 1.0 / (p - 2.0) + 1.0 / (3.0 - p)
    rhs_unit = p * (2.0**p) * (R2 ** (2.0 * (3.0 - p))) * D
    lhs = R(p) ** p
    print(
        f"eps={eps:g} eps^3*lhs={eps**3*lhs:.12f} "
        f"eps^3*rhs(W=1)={eps**3*rhs_unit:.12f} "
        f"ratio={lhs/rhs_unit:.6g}"
    )
