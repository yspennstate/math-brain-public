#!/usr/bin/env python3
import sympy as sp

I = sp.I
sqrt3 = sp.sqrt(3)
zeta6 = sp.Rational(1, 2) + I*sqrt3/2
n = 6

def perm_matrix(p):
    P = sp.zeros(n)
    for j, k in enumerate(p):
        P[k, j] = 1
    return P

def exact_zero(M):
    return all(sp.simplify(x) == 0 for x in M)

# Exact Fourier CHM of order six.
F = sp.Matrix([[sp.expand_complex(zeta6**(i*j)) for j in range(n)] for i in range(n)])
assert exact_zero(F*F.conjugate().T - 6*sp.eye(n))

# A nontrivial standard-equivalence transform H = D_r P_r F P_c D_c.
pr = [2, 0, 5, 1, 4, 3]
pc = [4, 2, 0, 5, 1, 3]
Pr, Pc = perm_matrix(pr), perm_matrix(pc)
rowph = [1, -1, I, -I, zeta6, sp.conjugate(zeta6)]
colph = [-1, I, zeta6, sp.conjugate(zeta6), -I, 1]
Dr, Dc = sp.diag(*rowph), sp.diag(*colph)
H = sp.simplify(Dr*Pr*F*Pc*Dc)
assert exact_zero(H*H.conjugate().T - 6*sp.eye(n))

# Diagonal-only dephasing of an arbitrary displayed CHM representative.
R = sp.diag(*[sp.conjugate(H[0, j]) for j in range(n)])
HR = sp.simplify(H*R)
L = sp.diag(*[sp.conjugate(HR[i, 0]) for i in range(n)])
A = sp.simplify(L*HR)
assert all(sp.simplify(A[0, j] - 1) == 0 for j in range(n))
assert all(sp.simplify(A[i, 0] - 1) == 0 for i in range(n))
assert exact_zero(A*A.conjugate().T - 6*sp.eye(n))

# Anchor-gauge identity:
# start with (I, F/sqrt(6)), apply common left monomial M=Dr*Pr,
# then restore the identity by the allowed right monomial M^*, and
# place the anchor in the standard-equivalent representative H by Q1=Pc*Dc.
M = Dr*Pr
Q0 = M.conjugate().T
Q1 = Pc*Dc
B0p = sp.simplify(M*sp.eye(n)*Q0)
B1p = sp.simplify(M*(F/sp.sqrt(6))*Q1)
assert B0p == sp.eye(n)
assert exact_zero(B1p - H/sp.sqrt(6))

# Check the source normalization exactly after the gauge operation:
# every identity/anchor squared overlap is 1/6.
for i in range(n):
    for j in range(n):
        ip = (B0p[:, i].conjugate().T*B1p[:, j])[0]
        assert sp.simplify(ip*sp.conjugate(ip) - sp.Rational(1, 6)) == 0

# Independent right monomial changes preserve the multiset of squared
# cross-overlaps after a common left unitary. Verify on an exact example.
Qleft = perm_matrix([1, 5, 3, 0, 2, 4]) * sp.diag(1, I, -1, -I, zeta6, sp.conjugate(zeta6))
Qright = perm_matrix([5, 1, 4, 2, 0, 3]) * sp.diag(-I, 1, zeta6, -1, I, sp.conjugate(zeta6))
C0 = sp.eye(n)
C1 = F/sp.sqrt(6)
T = Dr*Pr
C0t = sp.simplify(T*C0*Qleft)
C1t = sp.simplify(T*C1*Qright)

def sq_overlap_multiset(B, C):
    vals = []
    for i in range(n):
        for j in range(n):
            ip = (B[:, i].conjugate().T*C[:, j])[0]
            vals.append(sp.simplify(ip*sp.conjugate(ip)))
    return sorted([sp.srepr(sp.simplify(v)) for v in vals])

assert sq_overlap_multiset(C0, C1) == sq_overlap_multiset(C0t, C1t)

print("C29 atlas/gauge exact symbolic self-check")
print("order=6")
print("source_squared_overlap=1/6")
print("Fourier_CHM_exact=PASS")
print("standard_equivalence_CHM_exact=PASS")
print("diagonal_only_dephasing_first_row_first_col=PASS")
print("anchor_common_left_plus_right_monomial_identity=PASS")
print("identity_anchor_all_36_squared_overlaps_1_over_6=PASS")
print("common_left_and_independent_right_monomial_overlap_multiset_invariance=PASS")
print("ALL_EXACT_CHECKS_PASS")
