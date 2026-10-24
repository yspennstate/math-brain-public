from fractions import Fraction
from itertools import combinations
import math, random

# Algebra/regression checks for QFORM-NESTED-E2-CROSSDISJOINT-OR-FOURHUB-v1.
# They are not proof evidence; the proof is in REPORT.md.

def det2(M, r1, r2, c1, c2):
    return M[r1][c1]*M[r2][c2]-M[r1][c2]*M[r2][c1]

def sqfro(block):
    return sum(x*x for row in block for x in row)

def hub_exact(M):
    m,n=len(M),len(M[0])
    hub=0
    for r1,r2 in combinations(range(m),2):
        for c1,c2 in combinations(range(n),2):
            if (r1 < 2 or r2 < 2) and (c1 < 2 or c2 < 2):
                hub += det2(M,r1,r2,c1,c2)**2
    A=[row[:2] for row in M[:2]]
    B=[row[2:] for row in M[:2]]
    C=[row[:2] for row in M[2:]]
    D=[row[2:] for row in M[2:]]
    detA=(A[0][0]*A[1][1]-A[0][1]*A[1][0])**2
    a,b,c,d=map(sqfro,(A,B,C,D))
    motifs=[detA,a*b,a*c,a*d,b*c]
    rhs=motifs[0]+motifs[1]+motifs[2]+2*motifs[3]+2*motifs[4]
    return hub,rhs,motifs

rng=random.Random(20260923)
cases=0
max_ratio=Fraction(0,1)
tight=0
for m in range(2,7):
    for n in range(2,7):
        for _ in range(200):
            M=[[rng.randint(-3,3) for _ in range(n)] for __ in range(m)]
            hub,rhs,motifs=hub_exact(M)
            assert hub <= rhs
            cases += 1
            if rhs:
                ratio=Fraction(hub,rhs)
                max_ratio=max(max_ratio,ratio)
            if hub==rhs and hub>0:
                tight += 1

# Constant propagation from r25/r26:
# J > theta^2 F^6/36,
# E > theta^4 F^4/35831808,
# hence JE > theta^6 F^10/1289945088.
den_E=35_831_808
den_JE=36*den_E
assert den_JE == 1_289_945_088

# At eta=1/16 the failure hub has >7E/8; after the 7-weight motif ledger
# at least one positive motif exceeds E/8.
den_motif=8*den_E
assert den_motif == 286_654_464

eta=Fraction(1,16)
paid_C=5*math.e**(4/5)*(den_JE/float(eta))**(1/10)
paid_C_theta=paid_C*16**(3/5)
projection_prefactor=4*math.sqrt(den_motif)

print('hub_exact_cases',cases)
print('max_H_over_rhs',f'{max_ratio.numerator}/{max_ratio.denominator}',float(max_ratio))
print('positive_tight_cases',tight)
print('E_lower_den',den_E)
print('JE_lower_den',den_JE)
print('hub_motif_den',den_motif)
print('paid_C_eta',repr(paid_C))
print('paid_C_theta_1_16',repr(paid_C_theta))
print('M5_joint_projection_prefactor',repr(projection_prefactor))
print('STATUS=PASS')
