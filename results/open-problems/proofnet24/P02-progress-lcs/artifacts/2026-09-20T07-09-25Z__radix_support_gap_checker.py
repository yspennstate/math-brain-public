from fractions import Fraction
from itertools import product
from math import gcd

# Frozen C045 primitive data.
p = 256717
q = 800000
d = q - p
M = 5_000_000_000_000_000_000
a = int('1995237757733917147310102692686664915858011319606812684127301')
b = 4_220_452_010_631_561_279
S = q**6 * d
mult = [2,4,4,4,4,4,4,4]
c = [q**(6-k)*d*p**k for k in range(7)] + [p**7]

assert gcd(p,q) == gcd(p,d) == gcd(q,d) == 1
assert gcd(a,b) == 1
assert b <= M < 2*b

# Previous P02 support threshold and the new radix threshold.
D_prev = c[0] + c[7]
D_rad = c[0] + c[3] + c[6] + c[7]
assert D_rad > D_prev
assert a >= D_rad * M

# Tight-row extreme congruences.  If n0=0, z0=b*t0, t0 in {0,1,2}.
mod_p_fail = [((a - c[0]*b*t0) % p) for t0 in range(mult[0]+1)]
assert all(x != 0 for x in mod_p_fail)
# If n7=0, z7=b*t7, t7 in {0,...,4}.
mod_d_fail = [((a - c[7]*b*t7) % d) for t7 in range(mult[7]+1)]
assert all(x != 0 for x in mod_d_fail)

# Since n0,n7>0, z0 and z7 have forced residues.
r0 = (a * pow(c[0], -1, p)) % p
r7 = (a * pow(c[7], -1, d)) % d
res = a - c[0]*r0 - c[7]*r7
assert res % (p*d) == 0
A = res // (p*d)

# Global bounds on u0,u7 in z0=r0+p*u0, z7=r7+d*u7.
# n0 is 1 or 2; the largest possible z0 is 2M.
U0 = (2*M - r0) // p
# n7 is 1,...,4; since M>b, the largest possible z7 is 4M.
U7 = (4*M - r7) // d
assert 0 <= U0 < p**3
assert 0 <= U7 < q**3

# If n1=n2=n3=0, then z_k=b*t_k for k=1,2,3.
# Reduce the divided equation modulo p^3.  The residue uniquely determines u0
# because u0<p^3.  Exhaust the 5^3 possible tight counts.
mp = p**3
inv_q6 = pow(q**6, -1, mp)
p_residues = []
for t1,t2,t3 in product(range(5), repeat=3):
    rhs = A - b*(q**5*t1 + q**4*p*t2 + q**3*p**2*t3)
    u0 = (rhs * inv_q6) % mp
    p_residues.append((u0,t1,t2,t3))
p_min = min(p_residues)
assert p_min[0] > U0

# Symmetrically, if n4=n5=n6=0, reduce modulo q^3.  The residue uniquely
# determines u7 because u7<q^3.  Exhaust the 5^3 possible tight counts.
mq = q**3
inv_p6 = pow(p**6, -1, mq)
q_residues = []
for t4,t5,t6 in product(range(5), repeat=3):
    rhs = A - b*(q**2*p**3*t4 + q*p**4*t5 + p**5*t6)
    u7 = (rhs * inv_p6) % mq
    q_residues.append((u7,t4,t5,t6))
q_min = min(q_residues)
assert q_min[0] > U7

# Therefore every genuinely tight row has non-tight labels in four disjoint
# groups: {0}, {1,2,3}, {4,5,6}, {7}.  Since c_k decreases with k,
# W_N >= c0+c3+c6+c7 = D_rad.
assert c[1] > c[2] > c[3] > c[4] > c[5] > c[6] > c[7]

# Sharpness of this *relaxed successor-value abstraction*: exhibit exact
# counts/values at support n0=n3=n6=n7=1 that solve the tight-row scalar
# equation.  This is deliberately not claimed to be an actual C045 row.
n = [1,0,0,1,0,0,1,1]
tight = [1,2,3,3,3,4,3,0]
U = {
    0: 4_986_928_951_742_339_517,
    3: 4_991_857_513_517_926_901,
    6:   916_813_856_612_861_589,
    7:               181_363,
}
for k in range(8):
    assert 0 <= tight[k] <= mult[k]-n[k]
    if n[k]:
        assert n[k] <= U[k] <= n[k]*M
z = []
for k in range(8):
    z.append(b*tight[k] + (U[k] if n[k] else 0))
assert sum(c[k]*z[k] for k in range(8)) == a
assert sum(c[k]*n[k] for k in range(8)) == D_rad

# New two-step spectral rate.
R = Fraction(a,b)
t = Fraction(p,q)
scale = t*t/S
base = 4*t*t
beta_prev = R - Fraction(D_prev, 2*a*b)
beta_rad = R - Fraction(D_rad, 2*a*b)
lambda_prev = scale * beta_prev
lambda_rad = scale * beta_rad
assert 0 < base < 1
assert 0 < lambda_rad < lambda_prev < 1
# sqrt((a^2-D)/b^2) < a/b-D/(2ab) because of the positive square correction.
assert beta_rad*beta_rad > R*R - Fraction(D_rad,b*b)

# Exact positive atanh-series enclosures for -log.
def neglog_bounds(z, K=200):
    assert 0 < z < 1
    u = (1-z)/(1+z)
    u2 = u*u
    pw = u
    s = Fraction(0,1)
    for k in range(K):
        s += 2*pw/Fraction(2*k+1,1)
        pw *= u2
    tail = 2*pw/Fraction(2*K+1,1)/(1-u2)
    return s, s+tail

Alo,Ahi = neglog_bounds(base)
Nlo,Nhi = neglog_bounds(lambda_rad)
Plo,Phi = neglog_bounds(lambda_prev)
U_rad_upper = Ahi/Nlo
U_prev_lower = Alo/Phi
Q = Fraction(
    8262759427622826250151065815372966328234619961931900238808061833125629444302995503,
    10**82,
)
assert U_rad_upper < Q < U_prev_lower
L = Fraction(99083249,125000000)
assert L < U_rad_upper

print('P02 T02 radix support-gap checker')
print('D_prev=' + str(D_prev))
print('D_rad=' + str(D_rad))
print('D_rad_over_D_prev=' + str(Fraction(D_rad,D_prev)))
print('mod_p_fail_residues=' + ','.join(map(str,mod_p_fail)))
print('mod_d_fail_residues=' + ','.join(map(str,mod_d_fail)))
print('r0=' + str(r0))
print('r7=' + str(r7))
print('A=' + str(A))
print('U0_global=' + str(U0))
print('p3=' + str(mp))
print('min_p3_residue=' + str(p_min[0]))
print('min_p3_residue_counts=' + ','.join(map(str,p_min[1:])))
print('U7_global=' + str(U7))
print('q3=' + str(mq))
print('min_q3_residue=' + str(q_min[0]))
print('min_q3_residue_counts=' + ','.join(map(str,q_min[1:])))
print('relaxed_sharp_support_n=' + ','.join(map(str,n)))
print('relaxed_sharp_tight_counts=' + ','.join(map(str,tight)))
print('relaxed_sharp_U=' + ','.join(str(U.get(k,0)) for k in range(8)))
print('beta_rad_num=' + str(beta_rad.numerator))
print('beta_rad_den=' + str(beta_rad.denominator))
print('lambda_rad_num=' + str(lambda_rad.numerator))
print('lambda_rad_den=' + str(lambda_rad.denominator))
print('Q_num=' + str(Q.numerator))
print('Q_den=' + str(Q.denominator))
print('EXTREME_RESIDUE_FORCES_N0_N7_PASS')
print('P3_LIFT_FORCES_GROUP_123_PASS')
print('Q3_LIFT_FORCES_GROUP_456_PASS')
print('RELAXED_THRESHOLD_SHARPNESS_PASS')
print('TWO_STEP_SPECTRAL_STRICTIFICATION_PASS')
print('EXACT_LOG_SEPARATOR_PASS')
print('SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS')
print('ALL_EXACT_CHECKS_PASS')
