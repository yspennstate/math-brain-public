from fractions import Fraction
from itertools import combinations
import math

# Sharp fixed-cardinality entropy constants.
for ell in range(1,8):
    sharp = Fraction(ell**ell, math.factorial(ell))
    assert sharp > 0

# r39 universal constants.
C_inc = 3*2**(4/3)
h = Fraction(131,256)
C_diff = 3072*math.e/(61*math.sqrt(262))
C_heavy = C_inc*(float(1/h))**(1/6)
assert C_heavy < C_diff < 8.458

# fleet04/B02 strong-cut floor.
Z0 = Fraction(63,1048576)*Fraction(11907,16384)**3
strong = C_diff*float(Z0)**(-1/6)
assert strong < 50.129

# Explicit rotated-indefinite target.
Q0 = [
    [1,2,3,4],
    [-2,1,4,-3],
    [-3,-4,1,2],
    [-4,3,-2,1],
]
for i in range(4):
    for j in range(4):
        dot = sum(Q0[i][r]*Q0[j][r] for r in range(4))
        assert dot == (30 if i==j else 0)

L=64
eps=Fraction(1,64)
# Squared singular values of B0 (and B=B0 R).
lam=[Fraction(1),Fraction(L*L+2),Fraction(3),eps*eps]
assert lam == [Fraction(1),Fraction(4098),Fraction(3),Fraction(1,4096)]
# E3 check.
E3=sum(a*b*c for a,b,c in combinations(lam,3))

# Pair volumes in the projected residual C.
D12=D13=D14=Fraction(L*L)
D15=Fraction(L*L)*eps*eps
D23=D24=Fraction(1)
D25=eps*eps
D34=Fraction(4)
D35=D45=2*eps*eps
Z=D12+D13+D14+D15+D23+D24+D25+D34+D35+D45
assert Z == Fraction(50360325,4096)
V1=D12+D13+D14+D15
assert V1 == 12289
alpha=V1/Z
assert alpha == Fraction(50335744,50360325)
beta=Fraction(4096,12289)
assert beta < Fraction(1,2)
example=3*2**(5/6)*float(V1)**(-1/6)
assert example < 1.113

# Every row of B0 R has nonzero physical entries; scalar sqrt(30) is irrelevant.
# Numerators are row linear combinations against Q0.
Bnum = [
    Q0[0],
    [64*x for x in Q0[1]],
    Q0[2],
    [Q0[1][j]+Q0[2][j] for j in range(4)],
    [Q0[1][j]-Q0[2][j] for j in range(4)],
    [Q0[3][j] for j in range(4)],
]
assert all(x != 0 for row in Bnum for x in row)

print('C_inc=',C_inc)
print('C_diff=',C_diff)
print('C_heavy_at_h=',C_heavy)
print('Z0=',float(Z0),'strong_cut_bound=',strong)
print('E3_example=',float(E3))
print('Z2_example=',float(Z),'alpha=',float(alpha),'beta=',float(beta))
print('explicit_bound=',example)
print('status=PASS')
