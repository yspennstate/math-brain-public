from fractions import Fraction as F
from itertools import combinations


def det(M):
    A=[list(map(F,row)) for row in M]
    n=len(A); out=F(1)
    for c in range(n):
        p=next((r for r in range(c,n) if A[r][c]),None)
        if p is None: return F(0)
        if p!=c:
            A[c],A[p]=A[p],A[c]; out=-out
        v=A[c][c]; out*=v
        for j in range(c,n): A[c][j]/=v
        for r in range(c+1,n):
            q=A[r][c]
            if q:
                for j in range(c,n): A[r][j]-=q*A[c][j]
    return out


def minor(M,I,J):
    return det([[M[i][j] for j in J] for i in I])

A=[[F(1 if i==j else 0)-F(1,3) for j in range(4)] for i in range(4)]
U=[[F(1,2),F(1,2),F(1,2)],
   [F(1,2),F(-1,2),F(-1,2)],
   [F(-1,2),F(1,2),F(-1,2)],
   [F(-1,2),F(-1,2),F(1,2)]]
T=list(combinations(range(4),3))
w={I:minor(U,I,(0,1,2))**2 for I in T}
assert set(w.values())=={F(1,4)} and sum(w.values())==1
p={I:minor(U,I,(0,1,2)) for I in T}
for I in T:
    assert sum(minor(A,I,J)*p[J] for J in T)==p[I]
row_energy={}; row_q={}
for I in T:
    e={q:F(0) for q in range(4)}
    for J in T:
        e[len(set(I)&set(J))]+=minor(A,I,J)**2
    row_q[I]=e; row_energy[I]=sum(e.values())
    assert row_energy[I]==F(1,3)
    assert e[2]==F(1,3) and e[0]==e[1]==e[3]==0
    assert row_energy[I]>=w[I]
Fpair={0,1}; R=[I for I in T if Fpair.issubset(I)]
packet_mass=sum(w[I] for I in R)
packet_energy=sum(row_energy[I] for I in R)
packet_q2=sum(row_q[I][2] for I in R)
assert packet_mass==F(1,2)
assert packet_energy==F(2,3)
assert packet_q2==F(2,3)
print('QFORM_EXTERIOR_PACKET_TRANSFER_CHECK_PASS')
print('pluecker_weights=' + ','.join(str(w[I]) for I in T))
print('row_energy_each=' + str(next(iter(row_energy.values()))))
print('row_overlap_q2_each=' + str(next(iter(row_q.values()))[2]))
print('fixed_pair_packet_mass=' + str(packet_mass))
print('fixed_pair_total_full_minor_energy=' + str(packet_energy))
print('fixed_pair_overlap_q2_energy=' + str(packet_q2))
