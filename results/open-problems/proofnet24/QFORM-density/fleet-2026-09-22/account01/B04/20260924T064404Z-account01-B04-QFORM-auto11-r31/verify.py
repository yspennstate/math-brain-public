from fractions import Fraction as F
from itertools import combinations
from math import sqrt, e

R = [
    [F(1), F(0), F(0)],
    [F(0), F(1), F(0)],
    [F(3,5), F(4,5), F(0)],
    [F(-4,5), F(3,5), F(0)],
    [F(0), F(0), F(2)],
    [F(1,100), F(1,50), F(2)],
]
V = [
    [F(6,7), F(-2,7), F(-3,7)],
    [F(-2,7), F(3,7), F(-6,7)],
    [F(-3,7), F(-6,7), F(-2,7)],
]

def T(A):
    return [list(x) for x in zip(*A)]

def mm(A,B):
    BT=T(B)
    return [[sum(x*y for x,y in zip(r,c)) for c in BT] for r in A]

def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

def gramdet(S):
    X=[R[i] for i in S]
    return det3(mm(X,T(X)))

assert mm(T(V),V) == [[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(1)]]
M=mm(R,V)
assert all(x != 0 for row in M for x in row)

weights={S:gramdet(S) for S in combinations(range(6),3) if gramdet(S) != 0}
Z=sum(weights.values(),F(0))
tight={S:z for S,z in weights.items() if ((4 in S) ^ (5 in S))}
Tmass=sum(tight.values(),F(0))
Wa=sum(z for S,z in tight.items() if 4 in S)
Wb=sum(z for S,z in tight.items() if 5 in S)
Wab=sum(z for S,z in weights.items() if 4 in S and 5 in S)
marg={i:sum(z for S,z in tight.items() if i in S)/Tmass for i in range(6)}

assert Z == F(8001,250)
assert Tmass == F(32)
assert Wa == F(16) and Wb == F(16)
assert Wab == F(1,250)
assert all(v == F(1,2) for v in marg.values())

new_bound=6*sqrt(e)*(32**(-1/6))
partner_bound=3*(2**(5/6))*((1/250)**(-1/6))
assert abs(partner_bound-6*sqrt(5)) < 1e-12

print('QFORM_B04_R31_EXACT_CHECK_PASS')
print('M =', M)
print('E3 =', Z)
print('tight_mass =', Tmass)
print('Wa =', Wa, 'Wb =', Wb, 'Wab =', Wab)
print('marginals =', marg)
print('new_bound =', repr(new_bound))
print('partner_bound =', repr(partner_bound))
print('ratio =', repr(partner_bound/new_bound))
