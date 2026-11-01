#!/usr/bin/env python3
"""Exact rational/Gaussian-rational coupling certificates for Lyons Q2.8."""
import json,itertools,sys
from pathlib import Path
import sympy as sp
I=sp.I
def S(x): return sp.cancel(sp.sympify(x,locals={"I":I}))
def MAT(rows): return sp.Matrix([[S(x) for x in row] for row in rows])
def combos(n,r): return list(itertools.combinations(range(n),r))
def probs(P,r):
    out={}
    for A in combos(P.rows,r):
        z=sp.simplify(sp.expand_complex(P.extract(A,A).det()))
        assert sp.simplify(sp.im(z))==0
        z=sp.cancel(sp.re(z)); assert z>=0
        out[A]=z
    assert sp.simplify(sum(out.values())-1)==0
    return out
def pair_order(n,r1,r2):
    As=combos(n,r1); Bs=combos(n,r2)
    return [(A,B) for A in As for B in Bs if set(A).isdisjoint(B)]
def check(c):
    n,r1,r2=c["n"],c["r1"],c["r2"]; d=sp.Integer(c["d"])
    P1,P2=MAT(c["P1"]),MAT(c["P2"]); PH=P1+P2
    Z=sp.zeros(n); E=sp.eye(n)
    assert sp.conjugate(P1).T==P1 and sp.conjugate(P2).T==P2
    assert sp.simplify(P1*P1-P1)==Z and sp.simplify(P2*P2-P2)==Z
    assert sp.simplify(P1*P2)==Z and sp.simplify(PH*PH-PH)==Z
    assert sp.trace(P1)==r1 and sp.trace(P2)==r2
    if c["field"]=="Q":
        G=MAT(c["generator_K"]); assert G.T==-G
        Q=((d*E-G)*(d*E+G).inv()).applyfunc(sp.cancel)
        assert sp.simplify(Q.T*Q-E)==Z
        P1g=(Q[:,:r1]*Q[:,:r1].T).applyfunc(sp.cancel)
        P2g=(Q[:,r1:r1+r2]*Q[:,r1:r1+r2].T).applyfunc(sp.cancel)
    else:
        G=MAT(c["generator_A"]); assert sp.conjugate(G).T==-G
        X=G/d
        Q=((E-X)*(E+X).inv()).applyfunc(sp.cancel)
        assert sp.simplify(sp.conjugate(Q).T*Q-E)==Z
        P1g=(Q[:,:r1]*sp.conjugate(Q[:,:r1]).T).applyfunc(sp.cancel)
        P2g=(Q[:,r1:r1+r2]*sp.conjugate(Q[:,r1:r1+r2]).T).applyfunc(sp.cancel)
    assert sp.simplify(P1g-P1)==Z and sp.simplify(P2g-P2)==Z
    p1,p2,pH=probs(P1,r1),probs(P2,r2),probs(PH,r1+r2)
    pairs=pair_order(n,r1,r2); q={}
    for idx,val in c["support"]:
        A,B=pairs[int(idx)]; z=S(val); assert z>=0; q[(A,B)]=z
    assert len(q)==c["support_size"] and sp.simplify(sum(q.values())-1)==0
    for A,z in p1.items(): assert sp.simplify(sum(v for (AA,BB),v in q.items() if AA==A)-z)==0
    for B,z in p2.items(): assert sp.simplify(sum(v for (AA,BB),v in q.items() if BB==B)-z)==0
    for U,z in pH.items(): assert sp.simplify(sum(v for (AA,BB),v in q.items() if tuple(sorted(AA+BB))==U)-z)==0
    mn,mx=min(q.values()),max(q.values())
    assert mn==S(c["min_q"]) and mx==S(c["max_q"])
    return (c["id"],c["field"],n,(r1,r2),len(q),c["incidence_rank"],str(mn),str(mx),0)
def main():
    D=json.loads(Path(sys.argv[1]).read_text())
    assert D["schema"]=="PROB20-12.exact_lp_margin_suite.v1"
    for c in D["candidates"]: print("PASS",check(c))
    assert D["suite_metric_max_certified_delta"]=="0"
    print("SUITE_CANDIDATES",len(D["candidates"]))
    print("FIXED_NORMALIZATION",D["dual_normalization"]["definition"])
    print("MAX_CERTIFIED_NORMALIZED_INFEASIBILITY_MARGIN 0")
    print("ALL EXACT CHECKS PASSED")
if __name__=="__main__": main()
