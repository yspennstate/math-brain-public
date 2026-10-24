#!/usr/bin/env python3
import json,itertools,sys
from pathlib import Path
import sympy as sp

def C(n,r): return list(itertools.combinations(range(n),r))
def MAT(rows): return sp.Matrix([[sp.Rational(x) for x in row] for row in rows])
def dpp_atoms(P,r):
    out={}
    for A in C(P.rows,r):
        z=sp.cancel(P.extract(A,A).det())
        assert z>=0
        out[A]=z
    assert sp.cancel(sum(out.values())-1)==0
    return out

def check(rec):
    n,r1,r2,d=rec['n'],rec['r1'],rec['r2'],sp.Integer(rec['d'])
    K=MAT(rec['generator']); I=sp.eye(n); Z=sp.zeros(n)
    assert K.T==-K
    Q=((d*I-K)*(d*I+K).inv()).applyfunc(sp.cancel)
    assert sp.simplify(Q.T*Q-I)==Z
    V1,V2=Q[:,:r1],Q[:,r1:r1+r2]
    P1=(V1*V1.T).applyfunc(sp.cancel); P2=(V2*V2.T).applyfunc(sp.cancel); PH=P1+P2
    assert sp.simplify(P1*P1-P1)==Z and sp.simplify(P2*P2-P2)==Z
    assert sp.simplify(P1*P2)==Z and sp.simplify(PH*PH-PH)==Z
    assert sp.trace(P1)==r1 and sp.trace(P2)==r2 and sp.trace(PH)==r1+r2
    p1,p2,pH=dpp_atoms(P1,r1),dpp_atoms(P2,r2),dpp_atoms(PH,r1+r2)
    As,Bs=C(n,r1),C(n,r2)
    pairs=[(A,B) for A in As for B in Bs if set(A).isdisjoint(B)]
    q={pairs[int(i)]:sp.Rational(v) for i,v in rec['support']}
    assert len(q)==rec['support_size']; assert all(v>=0 for v in q.values())
    assert sp.cancel(sum(q.values())-1)==0
    for A,z in p1.items(): assert sp.cancel(sum(v for (AA,B),v in q.items() if AA==A)-z)==0
    for B,z in p2.items(): assert sp.cancel(sum(v for (A,BB),v in q.items() if BB==B)-z)==0
    for U,z in pH.items(): assert sp.cancel(sum(v for (A,B),v in q.items() if tuple(sorted(A+B))==U)-z)==0
    assert min(q.values())==sp.Rational(rec['min_q'])
    # Fixed metric delta is exactly zero because q is primal-feasible and y=0 is dual-feasible.
    assert rec['delta']=='0'
    return {'profile':(n,r1,r2),'support':len(q),'min_q':str(min(q.values())),'delta':'0'}

def main():
    D=json.loads(Path(sys.argv[1]).read_text())
    assert D['schema']=='PROB20-12.exact_compact_replay.v1'
    assert D['fixed_dual_normalization']=='delta=max{-b^T y: M^T y>=0, -1<=y_j<=1}'
    for rec in D['records']:
        print('PASS',check(rec))
    assert D['max_certified_normalized_infeasibility_margin']=='0'
    print('CERTIFIED_RECORDS',len(D['records']))
    print('MAX_CERTIFIED_NORMALIZED_INFEASIBILITY_MARGIN 0')
    print('ALL EXACT CHECKS PASSED')
if __name__=='__main__': main()
