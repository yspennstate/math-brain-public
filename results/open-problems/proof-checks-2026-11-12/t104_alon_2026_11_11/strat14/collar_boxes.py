"""Exact interval pullback of the physical collars into zero-edge boxes."""
import sys,json
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
from collar_algebra import BASES,local_data,physical_ball_data

HERE=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE))
sys.path.append(str(HERE/'STRAT8'))
from face_intervals import Interval as I
from quadratic_field import evaluate,mul,add,ZERO,ONE

def inv(a):
    if a.lo<=0<=a.hi:raise ZeroDivisionError
    return I(min(1/a.lo,1/a.hi),max(1/a.lo,1/a.hi))

def absmax(a):return max(abs(a.lo),abs(a.hi))

def base_matrix(kind):
    U,W,_,_=BASES[kind];nu=sum(a*a for a in U);nw=sum(a*a for a in W)
    return [[F(U[i]*U[j],nu)+F(W[i]*W[j],nw) for j in range(5)] for i in range(5)]

@lru_cache(None)
def point_bank():
    records=json.loads((HERE/'limit_points.json').read_text())['records']
    result={}
    for r in records:
        d=r['radicand'];point=[tuple(map(F,x)) for x in r['point']]
        t,v1,z1,v2,z2,z=point
        V=[(v1,z1),(v2,z2),(add(add(add(ONE,(-t[0],-t[1])),(-v1[0],-v1[1])),(-v2[0],-v2[1])),
                             (-z[0]-z1[0]-z2[0],-z[1]-z1[1]-z2[1])),(t,ZERO),((-F(1),F(0)),z)]
        R=[[add(mul(V[i][0],V[j][0],d),mul(V[i][1],V[j][1],d)) for j in range(5)]for i in range(5)]
        tau=ZERO
        for i in range(5):tau=add(tau,R[i][i])
        D=add((20*t[0],20*t[1]),(-tau[0],-tau[1]))
        assert D[1]==0 and D[0]>0
        assert all(x[1]==0 for row in R for x in row)
        gap=[[2*x[0]/D[0] for x in row] for row in R]
        kind='edges' if d==5 else 'triangle';base=base_matrix(kind)
        perm=next(p for p in permutations(range(5)) if all(gap[p[i]][p[j]]==base[i][j] for i in range(5) for j in range(5)))
        for node in r['nodes']:
            assert node not in result
            result[node]=dict(kind=kind,permutation=list(perm),point=r['point'],radicand=d)
    assert len(result)==9
    return result

@lru_cache(None)
def ball_data(kind):return physical_ball_data(kind)

def collar_record(box,node,method='matrix_ball'):
    info=point_bank()[node];kind=info['kind'];perm=info['permutation']
    t,v1,z1,v2,z2,z=[I(*v) for v in box]
    V=[(v1,z1),(v2,z2),(1-t-v1-v2,-z-z1-z2),(t,I(0)),(I(-1),z)]
    tau=sum(a.square()+b.square() for a,b in V);D=20*t-tau
    if D.lo<=0:return None
    Dinv=inv(D);VV=[V[j] for j in perm]
    if method=='matrix_ball':
        base=base_matrix(kind);radius=F(ball_data(kind)['matrix_ball_radius'])
        dist=F(0)
        for i in range(5):
            for j in range(i,5):
                sij=2*sum(VV[i][a]*VV[j][a]for a in range(2))*Dinv
                dist=max(dist,absmax(sij-base[i][j]))
                if dist>radius:return None
        return dict(kind='collar',type=kind,permutation=perm,method='matrix_ball',
                    bound=str(dist),radius=str(radius),D_lower=str(D.lo))
    assert method=='plane_chart'
    U,W,X,Y=BASES[kind]
    nu,nw,nx,ny=[sum(a*a for a in row) for row in (U,W,X,Y)]
    C=[[sum(b[i]*VV[i][j] for i in range(5))*F(1,n) for j in range(2)] for b,n in ((U,nu),(W,nw))]
    E=[[sum(b[i]*VV[i][j] for i in range(5))*F(1,n) for j in range(2)] for b,n in ((X,nx),(Y,ny))]
    det=C[0][0]*C[1][1]-C[0][1]*C[1][0]
    try:di=inv(det)
    except ZeroDivisionError:return None
    Ci=[[C[1][1]*di,-C[0][1]*di],[-C[1][0]*di,C[0][0]*di]]
    H=[[sum(E[i][j]*Ci[j][k] for j in range(2)) for k in range(2)] for i in range(2)]
    K=[[2*sum(C[i][j]*C[k][j] for j in range(2))*Dinv for k in range(2)] for i in range(2)]
    h=[nu*K[0][0]-1,nw*K[1][1]-1,nu*K[0][1],H[0][0],H[1][0],H[0][1],H[1][1]]
    bound=sum(absmax(a) for a in h)
    if bound>F(local_data(kind)['collar_radius_l1']):return None
    return dict(kind='collar',type=kind,permutation=perm,method='plane_chart',bound=str(bound),
                coordinates=[[str(a.lo),str(a.hi)]for a in h],D_lower=str(D.lo))
