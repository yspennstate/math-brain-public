from fractions import Fraction as F
from itertools import combinations
from math import pi, exp, gamma, cos, sqrt

beta=F(1,3)
b=float(beta)
C_pair=2+2*pi
C_beta=exp(b/2)*(4*pi)**b/(b*(1-2*b)*gamma(b)*cos(pi*b/2))
C_J2=C_pair*C_beta
branch=C_J2*144**(1/6)
partner=4*75**(1/8)

detB=F(-401,25)
u=[F(1,10),F(2,10),F(3,10),F(4,10)]
J=detB**2*((sum(x*x for x in u))**2-sum(x**4 for x in u))

# S = 2I + u u^T and N = det(B) S.  Every disjoint 2x2 minor
# sees only off-diagonal entries det(B) u_i u_j, hence must vanish.
def N(i,j):
    return detB*((F(2,1) if i==j else F(0,1))+u[i]*u[j])
D2=F(0,1)
for R in combinations(range(4),2):
    for T in combinations(range(4),2):
        if set(R).isdisjoint(T):
            d=N(R[0],T[0])*N(R[1],T[1])-N(R[0],T[1])*N(R[1],T[0])
            D2 += d*d

perturb=sqrt(126)/100+(126/10000)*(5/sqrt(401))
min_abs_lower=2-perturb
example_bound=C_J2*float(J)**(-1/6)

assert J == F(43898673,3125000)
assert D2 == 0
assert min_abs_lower > 1
assert C_J2 < 88.254
assert branch < 202.051
assert example_bound < 56.816
assert partner < 6.862

print('QFORM_B04_R53_J2_THIRD_RIESZ_CHECK_PASS')
print('C_pair=',repr(C_pair))
print('C_beta_1_3=',repr(C_beta))
print('C_J2=',repr(C_J2))
print('J2_ge_1_144_bound=',repr(branch))
print('example_J_exact=',J)
print('example_D2disj_exact=',D2)
print('example_density_bound=',repr(example_bound))
print('spectral_perturb_bound=',repr(perturb))
print('rigorous_min_abs_eigenvalue_lower=',repr(min_abs_lower))
print('partner_double_anchor_coeff=',repr(partner))
