#!/usr/bin/env python3
# NM13-12 / T03: low-rank arbitrary-row contamination + spectral-quantile Gaussian core.
# Numerical sanity checker for the theorem and concrete heavy-tailed application.
import math

def Phi(x):
    return 0.5*(1.0+math.erf(x/math.sqrt(2.0)))

def floor_rat_power(n, p, q):
    """floor(n**(p/q)) using exact integer arithmetic."""
    target = n**p
    lo, hi = 0, 1
    while hi**q <= target:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi)//2
        if mid**q <= target:
            lo = mid
        else:
            hi = mid
    return lo

L = 1.0/Phi(-1.0)
U = 12.78437096216
beta = 1.0

print("T03_LP_LOWER", format(L, ".15f"))
print("T03_RETAINED_UPPER", format(U, ".14f"))
print("T03_RETAINED_WIDTH", format(U-L, ".14f"))
print("BETA", beta)
print("SHIFTED_LOWER_LIMIT", format(beta+L, ".15f"))
print("SHIFTED_UPPER_LIMIT", format(beta+U, ".14f"))
print("SHIFTED_WIDTH", format((beta+U)-(beta+L), ".14f"))

def finite_lower(N):
    # Concrete model in report:
    # spectral exceptional dimension s=floor(N^(3/4)),
    # arbitrary contaminant row-span rank r=floor(N^(2/3)),
    # controlled bulk eigenvalue ceiling 1+eps, eps=N^(-1/3).
    s = floor_rat_power(N, 3, 4)
    r = floor_rat_power(N, 2, 3)
    eps = N**(-1.0/3.0)
    d = N-s-r
    assert d > 0
    # Gaussian-core density per ambient N guaranteed SAT by the theorem:
    # d/N times the fixed-margin LP threshold in d dimensions.
    a_core = (d/N)/Phi(-1.0/math.sqrt(1.0+eps))
    return s, r, eps, d, a_core, beta+a_core

for N in (10**6, 10**9, 10**12):
    s,r,eps,d,a_core,a_total = finite_lower(N)
    print(
        "FINITE",
        N,
        "s", s,
        "r", r,
        "eps", format(eps, ".12g"),
        "d_over_N", format(d/N, ".12f"),
        "core_lower", format(a_core, ".12f"),
        "total_lower", format(a_total, ".12f"),
    )
    assert a_core < L
    assert a_total < beta+L

# First-order comparison penalty around the isotropic limit.
# d/N = 1 - rho_spec - rho_B, u=1+eps.
phi1 = math.exp(-0.5)/math.sqrt(2.0*math.pi)
Ceps = phi1/(2.0*Phi(-1.0)**2)
print("FIRST_ORDER_RANK_COEFF", format(L, ".15f"))
print("FIRST_ORDER_EPS_COEFF", format(Ceps, ".15f"))

# Algebraic consistency of the shifted bracket.
assert abs(((beta+U)-(beta+L))-(U-L)) < 1e-12
assert abs(L-6.302974375068753) < 5e-15
assert Ceps > 4.80 and Ceps < 4.81
print("ALL_CHECKS_PASS")
