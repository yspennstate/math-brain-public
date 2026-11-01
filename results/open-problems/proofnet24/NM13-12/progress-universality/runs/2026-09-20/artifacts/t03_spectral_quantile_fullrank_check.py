#!/usr/bin/env python3
import math

def Phi(x):
    return 0.5*(1.0 + math.erf(x/math.sqrt(2.0)))

def phi(x):
    return math.exp(-0.5*x*x)/math.sqrt(2.0*math.pi)

kappa = -1.0
L = 1.0/Phi(kappa)
Ceps = phi(1.0)/(2.0*Phi(-1.0)**2)

print("T03 spectral-quantile full-rank covariance sanity check")
print(f"L_iso={L:.15f}")
print(f"first_order_eps_coefficient={Ceps:.15f}")
print("Expansion: (1-rho)/Phi(-1/sqrt(1+eps)) = L_iso - L_iso*rho - Ceps*eps + o(rho+eps)")

def benchmark(N):
    rho = N**(-0.25)
    eps = N**(-1.0/3.0)
    b = (1.0-rho)/Phi(-1.0/math.sqrt(1.0+eps))
    first = L - L*rho - Ceps*eps
    return rho, eps, b, first

prev = -1.0
for N in (10**6, 10**9, 10**12, 10**15):
    rho, eps, b, first = benchmark(N)
    print(f"N={N:d} rho={rho:.12e} eps={eps:.12e} lower_benchmark={b:.15f} deficit={L-b:.15e} first_order={first:.15f}")
    assert b > prev
    assert b < L
    prev = b

# Concrete full-rank model at N=10^9:
# N-r bulk eigenvalues are 1 + eps*j/(N-r+1), j=1,...,N-r,
# and r eigenvalues are exp(N^0.1).
# Hence every eigenvalue differs from 1, so rank(Sigma-I)=N.
N = 10**9
r = int(N**0.75)
eps = N**(-1.0/3.0)
den = N-r+1
bulk_min_minus_1 = eps/den
bulk_max_minus_1 = eps*(N-r)/den
spike = math.exp(N**0.1)
print(f"example_N={N}")
print(f"example_r={r}")
print(f"example_r_over_N={r/N:.12e}")
print(f"example_eps={eps:.12e}")
print(f"bulk_min_minus_1={bulk_min_minus_1:.12e}")
print(f"bulk_max_minus_1={bulk_max_minus_1:.12e}")
print(f"spike_eigenvalue={spike:.12e}")
print("rank_Sigma_minus_I=N (all eigenvalues are strictly >1)")
assert bulk_min_minus_1 > 0.0
assert bulk_max_minus_1 < eps
assert r/N < 0.01
assert eps < 0.01

eps10 = 0.10
fixed_bulk = 1.0/Phi(-1.0/math.sqrt(1.0+eps10))
print(f"fixed_eps_0p10_LP_comparison_benchmark={fixed_bulk:.15f}")

print("ALL_CHECKS_PASS")
