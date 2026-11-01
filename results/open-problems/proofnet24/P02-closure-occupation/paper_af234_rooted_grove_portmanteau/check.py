#!/usr/bin/env python3
from fractions import Fraction as Q
from itertools import combinations, product
import sympy as sp

CHAINS = {
    "rev_lazy3": [
        [Q(1,2),Q(1,2),Q(0)],
        [Q(1,4),Q(1,2),Q(1,4)],
        [Q(0),Q(1,2),Q(1,2)],
    ],
    "periodic_directed_cycle3": [
        [Q(0),Q(1),Q(0)],
        [Q(0),Q(0),Q(1)],
        [Q(1),Q(0),Q(0)],
    ],
    "nonrev4": [
        [Q(1,2),Q(1,3),Q(1,6),Q(0)],
        [Q(1,5),Q(2,5),Q(1,5),Q(1,5)],
        [Q(1,4),Q(0),Q(1,2),Q(1,4)],
        [Q(1,3),Q(1,6),Q(1,6),Q(1,3)],
    ],
}

def S(q):
    return sp.Rational(q.numerator, q.denominator)

def forest_sum(P, roots, start=None, target_root=None):
    n=len(P)
    roots=set(roots)
    non=[v for v in range(n) if v not in roots]
    options=[[w for w in range(n) if w != v and P[v][w] != 0] for v in non]
    total=Q(0)
    for dests in product(*options) if options else [()]:
        f=dict(zip(non,dests))
        valid=True
        root_of={}
        for v in non:
            x=v
            seen=set()
            while x not in roots:
                if x in seen or x not in f:
                    valid=False
                    break
                seen.add(x)
                x=f[x]
            if not valid:
                break
            root_of[v]=x
        if not valid:
            continue
        if start is not None:
            r=start if start in roots else root_of[start]
            if r != target_root:
                continue
        wt=Q(1)
        for v,w in f.items():
            wt *= P[v][w]
        total += wt
    return total

def stationary_and_Z(P):
    n=len(P)
    M=sp.Matrix([[S(x) for x in row] for row in P])
    L=sp.eye(n)-M
    pv=sp.symbols("p0:"+str(n))
    equations=[sum(pv[r]*M[r,c] for r in range(n))-pv[c] for c in range(n)]
    equations.append(sum(pv)-1)
    sol=sp.solve(equations,pv,dict=True)[0]
    pi=sp.Matrix([sp.factor(sol[x]) for x in pv])
    Pi=sp.ones(n,1)*pi.T
    Z=(L+Pi).inv()-Pi
    return L,pi,Z

def delta(pi,Z,A):
    A=list(A); m=len(A)
    block=Z.extract(A,A).T.row_join(-pi.extract(A,[0]))
    block=block.col_join(sp.ones(1,m).row_join(sp.zeros(1,1)))
    return sp.factor(block.det())

def numerator(pi,Z,A,i,j):
    A=list(A); m=len(A)
    top=Z.extract(A,A).T.row_join(-pi.extract(A,[0]))
    top=top.row_join(sp.Matrix([[Z[i,a]] for a in A]))
    mid=sp.ones(1,m).row_join(sp.zeros(1,1)).row_join(sp.ones(1,1))
    bot=sp.Matrix([[Z[a,j] for a in A]])
    bot=bot.row_join(sp.Matrix([[-pi[j]]])).row_join(sp.Matrix([[Z[i,j]]]))
    return sp.factor(top.col_join(mid).col_join(bot).det())

den_cases=num_cases=0
for name,P in CHAINS.items():
    n=len(P)
    L,pi,Z=stationary_and_Z(P)
    tree_total=sum((forest_sum(P,{r}) for r in range(n)),Q(0))
    detK=sp.factor((L+sp.ones(n,1)*pi.T).det())
    assert detK == S(tree_total)
    for size in range(1,n):
        for A in combinations(range(n),size):
            FA=forest_sum(P,set(A))
            D=delta(pi,Z,A)
            assert sp.factor(D*S(tree_total)) == S(FA)
            den_cases += 1
            U=[v for v in range(n) if v not in A]
            for i in U:
                for j in U:
                    FN=forest_sum(P,set(A)|{j},start=i,target_root=j)
                    N=numerator(pi,Z,A,i,j)
                    assert sp.factor(N*S(tree_total)) == S(FN)
                    num_cases += 1
    print(f"{name}: pi={list(pi)}, tree_total={tree_total}")

print(f"PASS denominator forest identities: {den_cases}")
print(f"PASS numerator forest identities: {num_cases}")
print("PASS all exact rational forest/determinant bridge checks")
