from itertools import combinations, product
from pathlib import Path
import sys
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import HalfspaceIntersection, ConvexHull
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'C012'))
from exact_core import AB, SETS, D

# Pair groups (0,1), (2,3), (4,5); row 2r has spin +.
pairs=[(0,1),(1,2),(0,2)]
def coeff(X):
    out=np.zeros(5)
    if len(X)==4: X=tuple(i for i in range(6) if i not in X)
    if len(X)==2:
        i,j=X;r,s=i//2,j//2
        if r==s:out[0]=1/9
        else:
            out[0]=1/18;out[1+pairs.index((r,s))]=-(-1)**(i+j)/18
    else:
        if len(set(i//2 for i in X))<3:out[0]=-1/9
        else:
            sig=[(-1)**i for i in X]
            out[0]=-1/12
            for k,(r,s) in enumerate(pairs):out[1+k]=sig[r]*sig[s]/36
            out[4]=-np.prod(sig)/36
    return out
C=np.array([coeff(X) for X in SETS]);D=np.array(D)

def lp(p):
    b=C@np.r_[1,p]
    return linprog(np.zeros(90),A_eq=D,b_eq=b,bounds=(0,None),method='highs')

def marginal_polytope(cut=0,tbound=0,newcut=False):
    hs=[]
    for j in range(3):
        for sig in [-1,1]:
            v=np.zeros(5);v[j]=sig;v[4]=-1;hs.append(v)
    for e in product([-1,1],repeat=3):
        if np.prod(e)!=1:continue
        for sig in [-1,1]:hs.append(np.r_[e,sig,-3])
        if cut:hs.append(np.r_[-np.array(e),0,-cut])
        if newcut:
            for sig in [-1,1]:hs.append(np.r_[-1.5*np.array(e),sig,-4.5])
    if tbound:
        for sig in [-1,1]:hs.append(np.array([0,0,0,sig,-tbound]))
    vs=HalfspaceIntersection(np.array(hs),np.zeros(4)).intersections
    print('marginal vertices',len(vs))
    for p in sorted(vs.tolist()):
        res=lp(p);print(np.round(p,5).tolist(),res.success)

def samples():
    rng=np.random.default_rng(39)
    for i in range(100):
        ns=rng.normal(size=(3,3));ns/=np.linalg.norm(ns,axis=1)[:,None]
        p=np.array([ns[0]@ns[1],ns[1]@ns[2],ns[0]@ns[2],np.sqrt(3)*np.linalg.det(ns)])
        res=lp(p)
        if not res.success:print('failure',p);return
    print('100 physical passed')

if __name__=='__main__':marginal_polytope(float(sys.argv[1]) if len(sys.argv)>1 else 0,float(sys.argv[2]) if len(sys.argv)>2 else 0,len(sys.argv)>3);samples()
