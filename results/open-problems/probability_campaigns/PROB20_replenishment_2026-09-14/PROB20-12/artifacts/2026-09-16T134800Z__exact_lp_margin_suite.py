#!/usr/bin/env python3
"""
PROB20-12 exact finite coupling-LP certificate checker.

Fixed normalized dual metric:
    delta(P1,P2) = max{-b^T y : M^T y >= 0, ||y||_infty <= 1}.
For every archived candidate this checker verifies an exact primal q>=0 with Mq=b.
Therefore delta=0 exactly for that candidate (weak duality + y=0 feasibility).
Any future delta>0 must be supplied by an exact normalized dual witness.
"""
import json, itertools, sys
from pathlib import Path
import sympy as sp

I = sp.I

def S(x):
    return sp.cancel(sp.sympify(x, locals={"I": I}))

def matrix(rows):
    return sp.Matrix([[S(x) for x in row] for row in rows])

def combos(n,r):
    return list(itertools.combinations(range(n),r))

def principal_probs(P, r):
    out={}
    for A in combos(P.rows,r):
        v=sp.cancel(sp.expand_complex(P.extract(A,A).det()))
        v=sp.simplify(v)
        assert sp.simplify(sp.im(v)) == 0, (A,v)
        v=sp.cancel(sp.re(v))
        assert v >= 0, (A,v)
        out[A]=v
    assert sp.simplify(sum(out.values())-1)==0
    return out

def check_candidate(c):
    cid=c["id"]; n=c["n"]; r1=c["r1"]; r2=c["r2"]; d=sp.Integer(c["d"])
    P1=matrix(c["P1"]); P2=matrix(c["P2"]); PH=matrix(c["PH"])
    eye=sp.eye(n); zero=sp.zeros(n)
    assert sp.simplify(sp.conjugate(P1).T-P1)==zero
    assert sp.simplify(sp.conjugate(P2).T-P2)==zero
    assert sp.simplify(P1*P1-P1)==zero
    assert sp.simplify(P2*P2-P2)==zero
    assert sp.simplify(P1*P2)==zero
    assert sp.simplify(PH-(P1+P2))==zero
    assert sp.simplify(PH*PH-PH)==zero
    assert sp.simplify(sp.trace(P1)-r1)==0
    assert sp.simplify(sp.trace(P2)-r2)==0

    if c["field"]=="Q":
        K=matrix(c["generator_K"])
        assert K.T == -K
        Q=(d*eye-K)*(d*eye+K).inv()
        Q=Q.applyfunc(sp.cancel)
        assert sp.simplify(Q.T*Q-eye)==zero
        V1=Q[:,:r1]; V2=Q[:,r1:r1+r2]
        P1g=(V1*V1.T).applyfunc(sp.cancel)
        P2g=(V2*V2.T).applyfunc(sp.cancel)
    else:
        A=matrix(c["generator_A"])
        assert sp.conjugate(A).T == -A
        X=A/d
        Q=(eye-X)*(eye+X).inv()
        Q=Q.applyfunc(sp.cancel)
        assert sp.simplify(sp.conjugate(Q).T*Q-eye)==zero
        V1=Q[:,:r1]; V2=Q[:,r1:r1+r2]
        P1g=(V1*sp.conjugate(V1).T).applyfunc(sp.cancel)
        P2g=(V2*sp.conjugate(V2).T).applyfunc(sp.cancel)
    assert sp.simplify(P1g-P1)==zero
    assert sp.simplify(P2g-P2)==zero

    p1=principal_probs(P1,r1)
    p2=principal_probs(P2,r2)
    pH=principal_probs(PH,r1+r2)

    q={}
    for rec in c["support"]:
        A=tuple(rec["A"]); B=tuple(rec["B"]); val=S(rec["q"])
        assert set(A).isdisjoint(B)
        assert val >= 0
        key=(A,B)
        assert key not in q
        q[key]=val
    assert len(q)==c["support_size"]
    assert sp.simplify(sum(q.values())-1)==0

    for A,val in p1.items():
        got=sum(v for (AA,BB),v in q.items() if AA==A)
        assert sp.simplify(got-val)==0, (cid,"p1",A,got,val)
    for B,val in p2.items():
        got=sum(v for (AA,BB),v in q.items() if BB==B)
        assert sp.simplify(got-val)==0, (cid,"p2",B,got,val)
    for U,val in pH.items():
        got=sum(v for (AA,BB),v in q.items() if tuple(sorted(AA+BB))==U)
        assert sp.simplify(got-val)==0, (cid,"pH",U,got,val)

    minq=min(q.values()); maxq=max(q.values())
    assert sp.simplify(minq-S(c["min_q"]))==0
    assert sp.simplify(maxq-S(c["max_q"]))==0

    delta=sp.Integer(0)
    assert c["certified_delta"]=="0"
    return {
        "id":cid,"field":c["field"],"n":n,"ranks":[r1,r2],
        "support":len(q),"incidence_rank":c["incidence_rank"],
        "min_q":str(minq),"max_q":str(maxq),"delta":str(delta)
    }

def main():
    if len(sys.argv)!=2:
        raise SystemExit("usage: checker.py data.json")
    data=json.loads(Path(sys.argv[1]).read_text())
    assert data["schema"]=="PROB20-12.exact_lp_margin_suite.v1"
    rows=[]
    for c in data["candidates"]:
        rows.append(check_candidate(c))
        print("PASS", rows[-1])
    assert all(r["delta"]=="0" for r in rows)
    assert data["suite_metric_max_certified_delta"]=="0"
    print("SUITE_CANDIDATES",len(rows))
    print("FIXED_NORMALIZATION",data["dual_normalization"]["definition"])
    print("MAX_CERTIFIED_NORMALIZED_INFEASIBILITY_MARGIN",0)
    print("ALL EXACT CHECKS PASSED")

if __name__=="__main__":
    main()
