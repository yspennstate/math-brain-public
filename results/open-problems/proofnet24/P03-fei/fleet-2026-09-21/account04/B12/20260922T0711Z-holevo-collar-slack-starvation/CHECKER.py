#!/usr/bin/env python3
from fractions import Fraction
from math import log2

kappa = Fraction(512,511)
A = Fraction(49096,10000) - 4*kappa
B = Fraction(4,1) + 4*kappa
C = Fraction(222,100) - 6 - 4*kappa

p = Fraction(8881,1000)
K = Fraction(87,10)

assert A == Fraction(576007,638750)
assert B == Fraction(4092,511)
assert C == -Fraction(198979,25550)

slope = p*A - B
intercept = K*A + C
source_exp = K + 2*p
dominance_exp = Fraction(10,1)-K + 2*(Fraction(9,1)-p)

assert slope == Fraction(518167,638750000)
assert intercept == Fraction(367859,6387500)
assert slope > 0
assert intercept > 0
assert source_exp == Fraction(13231,500) and source_exp > 10
assert dominance_exp == Fraction(769,500) and dominance_exp > 0

# If d=log2(1/delta)>=2 and ell>=K+p*d, the inherited scalar
# envelope A*ell-B*d+C is bounded below by slope*d+intercept.
for m in range(20,10001):
    d = Fraction(m,10)
    lb = slope*d + intercept
    assert lb > 0

# Exact starvation implication sanity checks on a rational grid.
# W=u*d_rare+(1-u)*d_common<u*delta*R implies the displayed bounds.
for den in (1024,2048,4096):
    u = Fraction(1,den)
    delta = Fraction(1,4)
    R = Fraction(7,3)
    cap = u*delta*R
    for a_num in range(5):
        d_rare = Fraction(a_num,20)*delta*R
        rem = cap-u*d_rare
        if rem <= 0:
            continue
        d_common = rem/(2*(1-u))
        W = u*d_rare+(1-u)*d_common
        assert W < cap
        assert d_rare < delta*R
        assert d_common < u/(1-u)*delta*R
        assert d_common < Fraction(1024,1023)*u*delta*R

print("PASS")
print(f"kappa={kappa}={float(kappa):.15f}")
print(f"A={A}={float(A):.15f}")
print(f"B={B}={float(B):.15f}")
print(f"C={C}={float(C):.15f}")
print(f"B_over_A={B/A}={float(B/A):.15f}")
print(f"minus_C_over_A={-C/A}={float(-C/A):.15f}")
print(f"p={p}={float(p):.6f}")
print(f"K={K}={float(K):.6f}")
print(f"pA_minus_B={slope}={float(slope):.15f}")
print(f"KA_plus_C={intercept}={float(intercept):.15f}")
print(f"K_plus_2p={source_exp}={float(source_exp):.6f}")
print(f"old_threshold_uniform_domination_exponent={dominance_exp}={float(dominance_exp):.6f}")
print(f"uniform_threshold_improvement_factor_at_delta_1_over_4={2**float(dominance_exp):.15f}")
print("new_collar: u <= 2^(-87/10) * delta^(8881/1000), 0<delta<=1/4")
print("starvation: W<u*delta*R => d_rare<delta*R, d_common<u/(1-u)*delta*R")
