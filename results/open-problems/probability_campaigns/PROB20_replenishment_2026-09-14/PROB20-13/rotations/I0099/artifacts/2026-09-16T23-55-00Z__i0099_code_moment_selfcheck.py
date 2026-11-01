#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import comb

def qrset(p):
    return {x*x % p for x in range(1,p)}

def find_clique(p, r):
    Q=qrset(p)
    for C in combinations(range(p), r):
        ok=True
        for a,b in combinations(C,2):
            if (a-b)%p not in Q:
                ok=False; break
        if ok:
            return C
    raise AssertionError((p,r))

def chi(x,p,Q):
    x%=p
    if x==0:return 0
    return 1 if x in Q else -1

def inv(a,p):
    return pow(a,p-2,p)

def sqrt_mod_square(a,p,Q):
    a%=p
    assert a in Q
    for x in range(1,p):
        if x*x%p==a:return x
    raise AssertionError

def kraw(k,j,r):
    s=0
    for a in range(j+1):
        if a<=r and j-a<=k-r:
            s += (-1)**a * comb(r,a)*comb(k-r,j-a)
    return s

def paley_clique_checks(p,r):
    Q=qrset(p)
    C=find_clique(p,r)
    k=len(C); rows=[]
    for x in range(p):
        if x in C: continue
        rows.append([chi(x-c,p,Q) for c in C])
    N=p-k
    for i in range(k):
        for j in range(k):
            g=sum(row[i]*row[j] for row in rows)
            target=(p-1 if i==j else 0) - (k-1)
            assert g==target,(p,C,i,j,g,target)
    B={}
    for mask in range(1<<k):
        T=[i for i in range(k) if mask>>i&1]
        b=sum(__import__('functools').reduce(lambda a,i:a*row[i],T,1) for row in rows)
        A=0
        for x in range(p):
            prod=1
            for i in T: prod*=chi(x-C[i],p,Q)
            A+=prod
        assert b==A-(k-len(T))
        B[mask]=b
    Nr=[0]*(k+1)
    for row in rows:
        q=sum(1 for s in row if s==-1)
        Nr[q]+=1
    for j in range(k+1):
        Sj=sum(B[m] for m in range(1<<k) if m.bit_count()==j)
        rhs=sum(Nr[q]*kraw(k,j,q) for q in range(k+1))
        assert Sj==rhs,(p,C,j,Sj,rhs)
    assert sum(q*Nr[q] for q in range(k+1)) == k*(p-1)//2
    assert sum(q*(q-1)*Nr[q] for q in range(k+1)) == k*(k-1)*(p-1)//4
    for n in range(2,k+1,2):
        for idxs in combinations(range(k),n):
            S=[C[i] for i in idxs]
            L=[]
            for i,a in enumerate(S):
                z=1
                for j,b in enumerate(S):
                    if i!=j:z=z*((a-b)%p)%p
                assert z in Q,(p,S,z)
                L.append(z)
            v=[sqrt_mod_square(inv(z,p),p,Q) for z in L]
            m=n//2
            G=[[v[i]*pow(S[i],a,p)%p for i in range(n)] for a in range(m)]
            for a in range(m):
                for b in range(m):
                    assert sum(G[a][i]*G[b][i] for i in range(n))%p==0,(p,S,a,b)
    return C

def abstract_no_extension_distribution(p,k):
    assert k>=4 and p>=2*k*k
    N=p-k
    mu=Fraction(k*(p-1),2*N)
    nu=Fraction(k*(k-1)*(p-1),4*N)
    var=nu+mu-mu*mu
    a=mu.numerator//mu.denominator
    th=mu-a
    dmin={a:1-th,a+1:th} if th else {a:Fraction(1)}
    vmin=th*(1-th)
    wk=(mu-1)/(k-1)
    dmax={1:1-wk,k:wk}
    vmax=(mu-1)*(k-mu)
    assert var>=vmin and var<=vmax,(p,k,mu,var,vmin,vmax)
    lam=(var-vmin)/(vmax-vmin) if vmax!=vmin else Fraction(0)
    D={}
    for q,w in dmin.items():D[q]=D.get(q,Fraction(0))+(1-lam)*w
    for q,w in dmax.items():D[q]=D.get(q,Fraction(0))+lam*w
    D={q:w for q,w in D.items() if w}
    assert 0 not in D and all(1<=q<=k and w>=0 for q,w in D.items())
    assert sum(D.values())==1
    Em=sum(Fraction(q)*w for q,w in D.items())
    Enu=sum(Fraction(q*(q-1))*w for q,w in D.items())
    assert Em==mu and Enu==nu
    Es=1-2*Em/k
    Eqkq=sum(Fraction(q*(k-q))*w for q,w in D.items())
    Epair=1-4*Eqkq/(k*(k-1))
    target=Fraction(-(k-1),N)
    assert Es==target and Epair==target
    return mu,var,D,target

def main():
    print("I0099 exact identity self-check")
    for p,r in [(13,3),(29,4),(37,4),(41,4)]:
        C=paley_clique_checks(p,r)
        print(f"PALEY_CHECK p={p} clique={C} PASS")
    for p,k in [(3613,15),(1009,10),(10009,20),(100003,30)]:
        mu,var,D,target=abstract_no_extension_distribution(p,k)
        print(f"ABSTRACT_NO_EXTENSION p={p} k={k} mu={mu} var={var} corr={target} support={D} PASS")
    print("ALL_I0099_CODE_MOMENT_SELF_CHECKS_PASS")

if __name__=="__main__":
    main()
