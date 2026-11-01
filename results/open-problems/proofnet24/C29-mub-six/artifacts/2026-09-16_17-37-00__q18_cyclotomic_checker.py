#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction
from math import comb

def weak_compositions(total, parts):
    for bars in combinations(range(total + parts - 1), parts - 1):
        prev = -1
        out = []
        for b in bars + (total + parts - 1,):
            out.append(b - prev - 1)
            prev = b
        yield out

def autocorr_coeffs(c):
    q = len(c)
    return [sum(c[j] * c[(j+r) % q] for j in range(q)) for r in range(q)]

def reduce_phi18(coeffs):
    # Phi_18(x)=x^6-x^3+1, hence x^d -> x^(d-3)-x^(d-6) for d>=6.
    a = list(coeffs)
    for d in range(len(a)-1, 5, -1):
        c = a[d]
        if c:
            a[d] = 0
            a[d-3] += c
            a[d-6] -= c
    return tuple(a[:6])

def reduce_phi12(coeffs):
    # Phi_12(x)=x^4-x^2+1.
    a = list(coeffs)
    for d in range(len(a)-1, 3, -1):
        c = a[d]
        if c:
            a[d] = 0
            a[d-2] += c
            a[d-4] -= c
    return tuple(a[:4])

def multiplicative_order(a, n):
    x = 1
    for k in range(1, 100):
        x = (x*a) % n
        if x == 1:
            return k
    raise AssertionError("order not found")

def order_mod_pm(a, n):
    x = 1
    for k in range(1, 100):
        x = (x*a) % n
        if x in (1, n-1):
            return k
    raise AssertionError("order mod +/- not found")

expected = comb(23, 6)
checked = 0
norm6 = 0
for c in weak_compositions(6, 18):
    checked += 1
    N = autocorr_coeffs(c)   # |sum c_j zeta^j|^2 = sum_r N_r zeta^r
    N[0] -= 6
    if reduce_phi18(N) == (0,0,0,0,0,0):
        norm6 += 1

assert checked == expected == 100947
assert norm6 == 0

ord2 = multiplicative_order(2, 9)
ord2pm = order_mod_pm(2, 9)
assert ord2 == 6
assert ord2pm == 3
relative_f = ord2 // ord2pm
assert relative_f == 2

# Quantitative norm-gap consequence in K^+=Q(zeta_9+zeta_9^{-1}):
# each nonzero alpha=S*Sbar-6 has |Norm(alpha)|>=1; the other two real
# conjugates have absolute value <=30, hence |alpha|>=1/900.
alpha_gap = Fraction(1, 900)
entry_sq_gap = alpha_gap * alpha_gap / (36*36)
block_gap = 36 * entry_sq_gap
phi_gap = Fraction(15, 756) * block_gap
assert entry_sq_gap == Fraction(1, 1049760000)
assert block_gap == Fraction(1, 29160000)
assert phi_gap == Fraction(1, 1469664000)

# Exact q=12 limitation witness from the preceding run:
# S=2*zeta^6+zeta^7+zeta^10+2*zeta^11 has |S|^2=6.
c12 = [0]*12
c12[6]=2
c12[7]=1
c12[10]=1
c12[11]=2
N12 = autocorr_coeffs(c12)
N12[0] -= 6
assert reduce_phi12(N12) == (0,0,0,0)

print("C29 q=18 cyclotomic obstruction exact checker")
print(f"q18_compositions_expected={expected}")
print(f"q18_compositions_checked={checked}")
print(f"q18_norm6_witnesses={norm6}")
print("q18_scalar_obstruction=PASS")
print(f"ord_9_2={ord2}")
print(f"ord_mod_pm_9_2={ord2pm}")
print(f"relative_residue_degree_at_2={relative_f}")
print(f"restricted_entry_squared_residual_gap={entry_sq_gap}")
print(f"restricted_cross_block_gap={block_gap}")
print(f"restricted_seven_basis_Phi_gap={phi_gap}")
print("q12_previous_scalar_witness=PASS")
print("ALL_EXACT_CHECKS_PASS")
