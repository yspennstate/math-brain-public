"""Pull the physical corner theorem into inherited zero-edge chart boxes."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import sys
sys.dont_write_bytecode=True
SOURCE=Path(__file__).resolve().parent/'STRAT10'
sys.path.insert(0,str(SOURCE))
from face_intervals import Interval as I


def permutations():
    """The fifteen distinct labeled two-edge equality graphs."""
    out=[]
    for isolate in range(5):
        rest=[j for j in range(5) if j!=isolate]
        for mate in rest[1:]:
            plus=(rest[0],mate);minus=tuple(j for j in rest if j not in plus)
            # Base order has edges {1,4}, {2,3}.
            out.append([isolate,plus[0],minus[0],minus[1],plus[1]])
    assert len(out)==15
    return out


def inv(a):
    if a.lo<=0<=a.hi:raise ZeroDivisionError
    return I(min(1/a.lo,1/a.hi),max(1/a.lo,1/a.hi))


def absmax(a):return max(abs(a.lo),abs(a.hi))


def corner_record(box):
    t,v1,z1,v2,z2,z=[I(*v) for v in box]
    V=[(v1,z1),(v2,z2),(1-t-v1-v2,-z-z1-z2),(t,I(0)),(I(-1),z)]
    tau=sum(a.square()+b.square() for a,b in V)
    D=20*t-tau
    if D.lo<=0:return None
    Dinv=inv(D)
    S=[[2*(V[i][0]*V[j][0]+V[i][1]*V[j][1])*Dinv for j in range(5)] for i in range(5)]
    for perm in permutations():
        U0=[-4,1,1,1,1];W0=[0,1,-1,-1,1]
        Q0=[[F(U0[i]*U0[j],20)+F(W0[i]*W0[j],4) for j in range(5)] for i in range(5)]
        # Cheap separation before computing the plane coordinates.
        if any(S[perm[i]][perm[j]].hi<Q0[i][j]-F(1,10) or S[perm[i]][perm[j]].lo>Q0[i][j]+F(1,10)
               for i in range(5) for j in range(i,5)):continue
        dist=max(absmax(S[perm[i]][perm[j]]-Q0[i][j]) for i in range(5) for j in range(i,5))
        if dist<=F(1,20800):
            return dict(kind='corner',method='matrix_ball',permutation=perm,bound=str(dist))
        VV=[V[j] for j in perm]
        X0=[0,1,1,-1,-1];Y0=[0,1,-1,1,-1]
        C=[[sum(U0[i]*VV[i][j] for i in range(5))*F(1,20) for j in range(2)],
           [sum(W0[i]*VV[i][j] for i in range(5))*F(1,4) for j in range(2)]]
        B=[[sum(X0[i]*VV[i][j] for i in range(5))*F(1,4) for j in range(2)],
           [sum(Y0[i]*VV[i][j] for i in range(5))*F(1,4) for j in range(2)]]
        det=C[0][0]*C[1][1]-C[0][1]*C[1][0]
        try:di=inv(det)
        except ZeroDivisionError:continue
        Ci=[[C[1][1]*di,-C[0][1]*di],[-C[1][0]*di,C[0][0]*di]]
        H=[[sum(B[i][j]*Ci[j][k] for j in range(2)) for k in range(2)] for i in range(2)]
        K=[[2*sum(C[i][j]*C[k][j] for j in range(2))*Dinv for k in range(2)] for i in range(2)]
        h=[20*K[0][0]-1,4*K[1][1]-1,20*K[0][1],H[0][0],H[1][0],H[0][1],H[1][1]]
        bound=sum(absmax(a) for a in h)
        if bound<=F(1,400):
            return dict(kind='corner',method='plane_chart',permutation=perm,bound=str(bound))
    return None
