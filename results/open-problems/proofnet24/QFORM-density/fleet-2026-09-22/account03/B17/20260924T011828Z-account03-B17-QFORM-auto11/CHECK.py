import math

sqrt2 = math.sqrt(2.0)

# Canonical maximally mixed zero-pivot Householder matrix.
n = [0.5, 1.0/sqrt2, 0.5]
B = [[(1.0 if i == j else 0.0) - 2.0*n[i]*n[j] for j in range(3)] for i in range(3)]

# B^2 = I numerically.
for i in range(3):
    for j in range(3):
        val = sum(B[i][k]*B[k][j] for k in range(3))
        target = 1.0 if i == j else 0.0
        assert abs(val-target) < 1e-12

assert abs(B[1][1]) < 1e-12
assert all(abs(B[i][j]) > 1e-12 for i,j in [(0,1),(0,2),(1,2)])

# Coupling vector and marginal-cap range.
a = B[0][1]
d = B[1][2]
assert abs(a*a+d*d-1.0) < 1e-12
m = max(abs(a), abs(d))
M = 1.0/m
assert abs(M-sqrt2) < 1e-12

# Water-filling constants.
u0 = M*M/8.0
R = (M**3 + 12.0)/(24.0*M)
core_mass = M**3/6.0
assert core_mass < 1.0
assert R > u0
assert abs(core_mass + 2.0*M*(R-u0) - 1.0) < 1e-12

ratio = R/u0
assert abs(ratio - (sqrt2 + 1.0/3.0)) < 1e-12
C = M*(2.0 + math.log(ratio))
frontier = 3.0*sqrt2
assert C < frontier

# Monotonicity endpoint certificate.
r = sqrt2 + 1.0/3.0
lower_Bprime = 4.0*r/(r+1.0) - 18.0/(6.0+sqrt2)
assert lower_Bprime > 0.0
assert 422**2 - 2*297**2 == 1666

# Partner orientation penalty.
t = [0.25, 0.5, 0.25]
s = [1.0-x for x in t]
mix = sum(si*ti for si,ti in zip(s,t))
assert abs(mix - 5.0/8.0) < 1e-15
gamma = 15.0/4.0 - math.sqrt(171.0/32.0)
assert gamma > 0.0
penalty = gamma/32.0

print('PASS QFORM_ZERO_PIVOT_HOUSEHOLDER_GLOBAL')
print(f'C_ZPH={C:.15f}')
print(f'3sqrt2={frontier:.15f}')
print(f'gap={frontier-C:.15f}')
print(f'partner_mix={mix:.15f}')
print(f'partner_penalty_coeff={penalty:.15f}')
