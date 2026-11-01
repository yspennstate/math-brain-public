#!/usr/bin/env python3
"""PROB20-12 exact finite coupling LP checker; generator matrices reconstruct P1,P2."""
import json,itertools,sys
from pathlib import Path
import sympy as sp
I=sp.I
def S(x): return sp.cancel(sp.sympify(x,locals={"I":I}))
def MAT(rows): return sp.Matrix([[S(x) for x in row] for row in rows])
def C(n,r): return list(itertools.combinations(range(n),r))
def PP(P,r):
    out={}
    for A in C(P.rows,r):
        z=sp.simplify(sp.expand_complex(P.extract(A,A).det()))
        assert sp.simplify(sp.im(z))==0
        z=sp.cancel(sp.re(z)); assert z>=0; out[A]=z
    assert sp.simplify(sum(out.values())-1)==0
    return out
def check(c):
    n,r1,r2,d=c["n"],c["r1"],c["r2"],sp.Integer(c["d"]); E=sp.eye(n); Z=sp.zeros(n)
    if c["field"]=="Q":
        G=MAT(c["generator_K"]); assert G.T==-G
        Q=((d*E-G)*(d*E+G).inv()).applyfunc(sp.cancel)
        assert sp.simplify(Q.T*Q-E)==Z
        V1,V2=Q[:,:r1],Q[:,r1:r1+r2]
        P1=(V1*V1.T).applyfunc(sp.cancel); P2=(V2*V2.T).applyfunc(sp.cancel)
    else:
        G=MAT(c["generator_A"]); assert sp.conjugate(G).T==-G
        X=G/d; Q=((E-X)*(E+X).inv()).applyfunc(sp.cancel)
        assert sp.simplify(sp.conjugate(Q).T*Q-E)==Z
        V1,V2=Q[:,:r1],Q[:,r1:r1+r2]
        P1=(V1*sp.conjugate(V1).T).applyfunc(sp.cancel)
        P2=(V2*sp.conjugate(V2).T).applyfunc(sp.cancel)
    PH=P1+P2
    assert sp.simplify(P1*P1-P1)==Z and sp.simplify(P2*P2-P2)==Z
    assert sp.simplify(P1*P2)==Z and sp.simplify(PH*PH-PH)==Z
    assert sp.trace(P1)==r1 and sp.trace(P2)==r2
    p1,p2,pH=PP(P1,r1),PP(P2,r2),PP(PH,r1+r2)
    As,Bs=C(n,r1),C(n,r2)
    pairs=[(A,B) for A in As for B in Bs if set(A).isdisjoint(B)]
    q={}
    for idx,val in c["support"]:
        z=S(val); assert z>=0; q[pairs[int(idx)]]=z
    assert len(q)==c["support_size"] and sp.simplify(sum(q.values())-1)==0
    for A,z in p1.items(): assert sp.simplify(sum(v for (AA,BB),v in q.items() if AA==A)-z)==0
    for B,z in p2.items(): assert sp.simplify(sum(v for (AA,BB),v in q.items() if BB==B)-z)==0
    for U,z in pH.items(): assert sp.simplify(sum(v for (AA,BB),v in q.items() if tuple(sorted(AA+BB))==U)-z)==0
    mn,mx=min(q.values()),max(q.values()); assert mn==S(c["min_q"]) and mx==S(c["max_q"])
    return {"id":c["id"],"field":c["field"],"n":n,"ranks":[r1,r2],"support":len(q),"min_q":str(mn),"max_q":str(mx),"delta":"0"}
def main():
    D=json.loads(Path(sys.argv[1]).read_text()); assert D["schema"]=="PROB20-12.exact_lp_margin_suite.v1"
    for c in D["candidates"]: print("PASS",check(c))
    assert D["suite_metric_max_certified_delta"]=="0"
    print("SUITE_CANDIDATES",len(D["candidates"]))
    print("FIXED_NORMALIZATION",D["dual_normalization"]["definition"])
    print("MAX_CERTIFIED_NORMALIZED_INFEASIBILITY_MARGIN 0")
    print("ALL EXACT CHECKS PASSED")
if __name__=="__main__": main()
