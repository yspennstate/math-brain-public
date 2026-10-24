from fractions import Fraction as F
from itertools import combinations


def det2(a,b,c,d):
    return a*d-b*c


def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

# Exact rational regression for T=U-V coefficientwise and
# <T,U>-<T,V>=||T||^2. This is corroboration only; REPORT.md has the proof.
b=F(2)
r=[F(1),F(-2),F(3)]
c=[F(2),F(1),F(-1)]
C=[[F(1),F(0),F(2)],
   [F(-1),F(3),F(1)],
   [F(2),F(1),F(-2)]]

M=U2=V2=TU=TV=F(0)
for K in combinations(range(3),2):
    for L in combinations(range(3),2):
        Tmat=[[b,r[L[0]],r[L[1]]],
              [c[K[0]],C[K[0]][L[0]],C[K[0]][L[1]]],
              [c[K[1]],C[K[1]][L[0]],C[K[1]][L[1]]]]
        t=det3(Tmat)
        d=det2(C[K[0]][L[0]],C[K[0]][L[1]],
               C[K[1]][L[0]],C[K[1]][L[1]])
        u=b*d
        # v is defined by the proved coefficient identity T=U-V.
        # Check it independently against the explicit contraction formula.
        k1,k2=K; l1,l2=L
        v_exp=(c[k1]*(r[l1]*C[k2][l2]-r[l2]*C[k2][l1])
               -c[k2]*(r[l1]*C[k1][l2]-r[l2]*C[k1][l1]))
        assert t == u-v_exp
        v=v_exp
        M += t*t; U2 += u*u; V2 += v*v; TU += t*u; TV += t*v

assert M == F(642)
assert U2 == F(772)
assert V2 == F(994)
assert TU == F(210)
assert TV == F(-432)
assert TU-TV == M
assert max(abs(TU),abs(TV))*2 >= M
print('QFORM_ANCHORED_THIRD_WEDGE_CHECK_PASS')
print('M00=',M,'U2=',U2,'V2=',V2,'TU=',TU,'TV=',TV)
