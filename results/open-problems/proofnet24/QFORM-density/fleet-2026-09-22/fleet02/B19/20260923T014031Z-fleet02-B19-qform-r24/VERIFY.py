from fractions import Fraction
from itertools import combinations
from math import sqrt, e


def det3(A):
    a,b,c=A[0]; d,e_,f=A[1]; g,h,i=A[2]
    return a*(e_*i-f*h)-b*(d*i-f*g)+c*(d*h-e_*g)

# Exact exterior-power identity on a deterministic symmetric rational test.
C=[
 [Fraction(0),Fraction(1,7),Fraction(2,9),Fraction(-1,8),Fraction(1,11)],
 [Fraction(1,7),Fraction(0),Fraction(1,5),Fraction(1,13),Fraction(-2,15)],
 [Fraction(2,9),Fraction(1,5),Fraction(0),Fraction(1,6),Fraction(1,10)],
 [Fraction(-1,8),Fraction(1,13),Fraction(1,6),Fraction(0),Fraction(1,12)],
 [Fraction(1,11),Fraction(-2,15),Fraction(1,10),Fraction(1,12),Fraction(0)]
]
n=len(C)
q=[Fraction(1),0,0,0,0]
Z=Fraction(0)
for I in combinations(range(n),3):
    for J in combinations(range(n),2):
        A=[[C[ii][J[0]],C[ii][J[1]],q[ii]] for ii in I]
        Z += det3(A)**2
T=[[Fraction(0) if i==0 else C[i][j] for j in range(n)] for i in range(n)]
M=[[sum(T[i][k]*T[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
tr=sum(M[i][i] for i in range(n))
tr2=sum(M[i][j]*M[j][i] for i in range(n) for j in range(n))
e2=(tr*tr-tr2)/2
assert Z==e2

g=Fraction(589,1180)
kappa=Fraction(1,64)
sigma0=Fraction(4,5)
zstar=Fraction(1,4)*sigma0**2*g**2*kappa**2
self_e2=zstar*590**2
zcross=zstar/Fraction(96)
dprime=9*sqrt(3*e)*float(zcross)**(-1/6)
pairatom=3*sqrt(e)*float(zstar/Fraction(4608))**(-1/6)
q1_first=zstar/Fraction(1536)
q1_second=zstar/Fraction(24576)
q2_energy=2*zstar/Fraction(2025)

print('exterior_identity_exact=', Z==e2)
print('test_Z=', float(Z))
print('zstar=', float(zstar))
print('tail_self_e2_threshold=', float(self_e2))
print('disjoint_cross_E3_threshold=', float(zcross))
print('Dprime_bound_at_threshold=', dprime)
print('R3_pairatom_bound_at_threshold=', pairatom)
print('q1_diag_x_secondcompound_threshold=', float(q1_first))
print('q1_starstarcore_threshold=', float(q1_second))
print('q2_one_of_five_energy_threshold=', float(q2_energy))
assert float(self_e2) > 3.387
assert dprime < 376.379
assert pairatom < 138.086
print('QFORM_B19_R24_TRANSVERSE_COMPOUND_CHECK_PASS')
