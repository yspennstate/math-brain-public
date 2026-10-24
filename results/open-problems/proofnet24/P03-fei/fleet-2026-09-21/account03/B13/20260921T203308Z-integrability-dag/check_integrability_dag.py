#!/usr/bin/env python3
"""Finite self-check for the B13 low-defect proxy-integrability theorem.

Enumerates Boolean functions modulo global output negation through n=4,
median-character folds them, forms derivative rows, enumerates every coordinate
subcube proxy with support error <= j/16 and retains rows with depth defect
<=1/16. It checks the one-way q=5/14 scale inequalities and reciprocal proxy
compatibility. This is a finite self-check, not the proof of the theorem.
"""
from itertools import combinations
import math, json

DELTA=ETA=1/16
Q=(DELTA+4*ETA)/(1-2*DELTA)

def influence(v,n,i):
    N=1<<n
    return sum(v[x]!=v[x^(1<<i)] for x in range(N))/N

def fold(v,n):
    mask=sum(1<<i for i in range(n) if influence(v,n,i)>0.5)
    return [a*(-1 if ((x&mask).bit_count()&1) else 1) for x,a in enumerate(v)]

def row(v,n,i):
    others=[k for k in range(n) if k!=i]; g=[]
    for y in range(1<<(n-1)):
        x=sum((1<<k) for p,k in enumerate(others) if (y>>p)&1)
        g.append((v[x]-v[x|(1<<i)])//2)
    return g,others

def depth(g):
    m=len(g).bit_length()-1; N=len(g); ans=0.0
    for r in range(m):
        ans += sum(((g[x]-g[x^(1<<r)])/2)**2 for x in range(N))/N
    return ans

def proxies(g,others):
    N=len(g); m=len(others); E={x for x,a in enumerate(g) if a}
    j=len(E)/N; out=[]
    for mask in range(1<<m):
        pos=[p for p in range(m) if (mask>>p)&1]
        for ass in range(1<<len(pos)):
            pat={others[p]:(ass>>t)&1 for t,p in enumerate(pos)}
            Qset={y for y in range(N) if all(((y>>p)&1)==pat[others[p]] for p in pos)}
            eps=len(E^Qset)/N
            if eps<=DELTA*j+1e-15:
                out.append((frozenset(pat),pat,len(Qset)/N))
    return out

def check(n):
    N=1<<n
    st={"n":n,"functions_mod_global_sign":1<<(N-1),"qualifying_functions":0,
        "qualifying_rows":0,"proxy_incidence_pairs":0,"one_way":0,
        "reciprocal":0,"violations":0}
    deltas=[]
    for code in range(1<<(N-1)):
        v=[1]+[1 if (code>>(x-1))&1 else -1 for x in range(1,N)]
        v=fold(v,n); rows={}
        for i in range(n):
            g,others=row(v,n,i); j=sum(a*a for a in g)/len(g)
            if not (0<j<=0.5): continue
            D=depth(g)/j-0.5*math.log2(1/j); deltas.append(D)
            if D<=ETA+1e-12:
                ps=proxies(g,others)
                if ps: rows[i]=(j,ps); st["qualifying_rows"]+=1
        if rows: st["qualifying_functions"]+=1
        for i,k in combinations(sorted(rows),2):
            ji,pis=rows[i]; jk,pks=rows[k]
            for Fi,pi,si in pis:
                for Fk,pk,sk in pks:
                    a=k in Fi; b=i in Fk
                    if not (a or b): continue
                    st["proxy_incidence_pairs"]+=1
                    if a!=b:
                        st["one_way"]+=1
                        sj,tj,ss,ts=(ji,jk,si,sk) if a else (jk,ji,sk,si)
                        if sj>Q*tj+1e-10 or ss>Q*ts+1e-10: st["violations"]+=1
                    else:
                        st["reciprocal"]+=1
                        ok=abs(si-sk)<1e-12 and set(Fi)-{k}==set(Fk)-{i}
                        if ok:
                            ok=all(pi[c]==pk[c] for c in set(Fi)-{k})
                        if not ok: st["violations"]+=1
    st["qualifying_delta_values"]=sorted({round(x,15) for x in deltas if x<=ETA+1e-12})
    return st

if __name__=="__main__":
    print(json.dumps({"delta":DELTA,"eta":ETA,"q":Q,"results":[check(n) for n in range(1,5)]},indent=2,sort_keys=True))
