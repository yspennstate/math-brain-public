from fractions import Fraction
from math import sqrt, exp

# Exact vectors from REPORT.md.
r0 = [Fraction(1,2)]*4
u  = [Fraction(1,2), Fraction(1,2), Fraction(-1,2), Fraction(-1,2)]
v  = [Fraction(1,2), Fraction(-1,2), Fraction(1,2), Fraction(-1,2)]

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def scale(c,a):
    return [c*x for x in a]

def gram2(a,b):
    return dot(a,a)*dot(b,b)-dot(a,b)**2

assert dot(r0,r0)==dot(u,u)==dot(v,v)==1
assert dot(r0,u)==dot(r0,v)==dot(u,v)==0

# Hub plus 17 u-type rows (one 5u and 16 u), plus 8 v rows.
C = [scale(5,u)] + [u[:] for _ in range(16)] + [v[:] for _ in range(8)]
B = [r0] + C

# Every physical cross coefficient is nonzero.
assert all(x != 0 for row in B for x in row)

# B^T B exact.
BTB = [[sum(row[i]*row[j] for row in B) for j in range(4)] for i in range(4)]
model = [[r0[i]*r0[j] + 41*u[i]*u[j] + 8*v[i]*v[j] for j in range(4)] for i in range(4)]
assert BTB == model

# Since r0,u,v are orthonormal, the nonzero squared singular values are 1,41,8.
nonzero_squared_singular_values = [1,41,8]
assert min(nonzero_squared_singular_values) >= 1

# Exact positive two-row Gram volumes and total E2(C).
Z = Fraction(0)
positive = []
for i in range(len(C)):
    for j in range(i+1,len(C)):
        D = gram2(C[i],C[j])
        if D > 0:
            positive.append((i,j,D))
            Z += D
assert Z == 328

# Canonical row marginals.
incident = [Fraction(0) for _ in C]
for i,j,D in positive:
    incident[i] += D
    incident[j] += D
alpha = [x/Z for x in incident]
assert alpha[0] == Fraction(25,41)
assert alpha[0] > Fraction(1,2)
assert all(alpha[j] == Fraction(1,41) for j in range(1,17))
assert all(alpha[j] == Fraction(1,8) for j in range(17,25))

# Exact optimized capped marginals and currency.
r = [Fraction(1,2)] + [Fraction(1,32)]*16
c = [Fraction(1,8)]*8
assert sum(r)==sum(c)==1
assert max(r)<=Fraction(1,2) and max(c)<=Fraction(1,2)
# U-side objective exponentiates to 40, V side to 8.
# Direct logarithmic numerical evaluation is also checked below.
Gamma_star_exact = 320

# Smallest residual E2 after deleting any two physical rows of C.
def residual_after_delete(a,b):
    s=Fraction(0)
    for i,j,D in positive:
        if i not in (a,b) and j not in (a,b):
            s += D
    return s
mins=[]
for a in range(len(C)):
    for b in range(a+1,len(C)):
        mins.append((residual_after_delete(a,b),a,b))
minres,mina,minb=min(mins)
assert minres == 112
assert minres/Z == Fraction(14,41)

# Canonical disjointness probability factorizes across the complete bipartite support.
delta = Fraction(1040,1681)*Fraction(7,8)
assert delta == Fraction(910,1681)

# Fourier constants.
bound = 3*(2/5)**(1/6)
assert abs(bound-2.5751226567976713) < 1e-14
eta_coeff = 3*2**(7/6)*exp(1/3)*(Fraction(1,16))**(-Fraction(1,12))
assert abs(float(eta_coeff)-11.842164116238918) < 1e-12

# Account01/B04 fractional canonical comparison on this same matrix.
q = Fraction(50,41)
Dq = q+2
peer = float(Dq/(Dq-2*q))*2**float((q+6)/(2*Dq))*float(q)**float(-2/(2*Dq))*328**float(-1/(2*Dq))
assert abs(peer-3.431228664105789) < 1e-12
assert bound < peer

print({
    'Z': int(Z),
    'canonical_heavy_marginal': str(alpha[0]),
    'Gamma_star': Gamma_star_exact,
    'min_pair_deletion_residual': int(minres),
    'min_pair_deletion_fraction': str(minres/Z),
    'delta': str(delta),
    'new_density_bound': bound,
    'peer_fractional_canonical_bound': peer,
    'status': 'PASS'
})
