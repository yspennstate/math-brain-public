#!/usr/bin/env python3
import itertools,json,sys
from pathlib import Path
import sympy as sp

def combs(n,r):
    return list(itertools.combinations(range(n),r))

def build_Q(n,ops):
    Q=sp.eye(n)
    for i,j,a,b,c in ops:
        cc=sp.Rational(a,c); ss=sp.Rational(b,c)
        assert sp.cancel(cc*cc+ss*ss-1)==0
        G=sp.eye(n)
        G[i,i]=cc; G[i,j]=-ss
        G[j,i]=ss; G[j,j]=cc
        Q=G*Q
    return Q.applyfunc(sp.cancel)

def atoms_from_frame(V,subs):
    r=V.cols
    out=[]
    for A in subs:
        z=sp.cancel(V.extract(A,range(r)).det()**2)
        assert z>=0
        out.append(z)
    assert sp.cancel(sum(out)-1)==0
    return out

def main():
    D=json.loads(Path(sys.argv[1]).read_text())
    assert D["schema"]=="PROB20-12.exact_givens_support_basis.v1"
    assert D["fixed_dual_normalization"]=="delta=max{-b^T y: M^T y>=0, -1<=y_j<=1}"
    n=D["profile"]["n"]; r1=D["profile"]["r1"]; r2=D["profile"]["r2"]
    Q=build_Q(n,D["givens_ops"])
    I=sp.eye(n); Z=sp.zeros(n)
    assert sp.simplify(Q.T*Q-I)==Z
    V1=Q[:,:r1]; V2=Q[:,r1:r1+r2]; VH=Q[:,:r1+r2]
    P1=(V1*V1.T).applyfunc(sp.cancel)
    P2=(V2*V2.T).applyfunc(sp.cancel)
    PH=(VH*VH.T).applyfunc(sp.cancel)
    assert sp.simplify(P1*P1-P1)==Z
    assert sp.simplify(P2*P2-P2)==Z
    assert sp.simplify(P1*P2)==Z
    assert sp.simplify(PH-(P1+P2))==Z
    assert sp.trace(P1)==r1 and sp.trace(P2)==r2 and sp.trace(PH)==r1+r2

    As,Bs,Us=combs(n,r1),combs(n,r2),combs(n,r1+r2)
    p1=atoms_from_frame(V1,As)
    p2=atoms_from_frame(V2,Bs)
    pH=atoms_from_frame(VH,Us)
    b=sp.Matrix(p1+p2+pH)

    pairs=[(A,B) for A in As for B in Bs if set(A).isdisjoint(B)]
    support=[int(i) for i in D["support_indices"]]
    assert len(support)==D["support_size"] and len(set(support))==len(support)
    assert all(0<=i<len(pairs) for i in support)
    ra={A:i for i,A in enumerate(As)}
    rb={B:len(As)+i for i,B in enumerate(Bs)}
    ru={U:len(As)+len(Bs)+i for i,U in enumerate(Us)}
    M=sp.zeros(len(b),len(support))
    for j,idx in enumerate(support):
        A,B=pairs[idx]; U=tuple(sorted(A+B))
        M[ra[A],j]=1
        M[rb[B],j]=1
        M[ru[U],j]=1

    assert M.rank()==len(support)
    solset=sp.linsolve((M,b))
    q=next(iter(solset))
    assert len(q)==len(support)
    assert not any(x.free_symbols for x in q)
    assert all(x>0 for x in q)
    assert M*sp.Matrix(q)==b
    assert sp.cancel(sum(q)-1)==0
    assert min(q)==sp.Rational(D["min_q"])
    assert max(q)==sp.Rational(D["max_q"])

    # Fixed-normalization dual witness y=0 has objective 0.
    # Exact primal feasibility gives b^T y = q^T M_full^T y >= 0
    # for every dual-feasible y, hence all dual objectives -b^T y <= 0.
    # Therefore the optimum is exactly zero.
    y=sp.zeros(len(b),1)
    assert max(abs(v) for v in y)==0
    assert sp.cancel(-(b.T*y)[0])==0
    assert D["delta"]=="0"

    print("PROFILE",(n,r1,r2))
    print("GIVENS_OPS",len(D["givens_ops"]))
    print("PAIR_VARIABLES",len(pairs))
    print("MARGINAL_ROWS",len(b))
    print("SUPPORT_RANK",M.rank())
    print("EXACT_SUPPORT",len(q))
    print("MIN_POSITIVE_Q",D["min_q"])
    print("MAX_Q",D["max_q"])
    print("DPP_ATOMS",(len(p1),len(p2),len(pH)))
    print("DUAL_ZERO_CERTIFICATE PASS")
    print("FIXED_NORMALIZED_DELTA 0")
    print("ALL EXACT CHECKS PASSED")

if __name__=="__main__":
    main()
