#!/usr/bin/env python3
"""Exact author checks for the uniform-cycle apex Chebyshev identity."""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def merge(part,u,v):
    a,b=part[u],part[v]
    if a==b:return None
    return tuple(a if x==b else x for x in part)

def apex_dp(n,lam):
    # State on the n rim vertices; first process the cycle, rejecting cycles,
    # then choose any compatible subset of equal-weight apex spokes.
    state={tuple(range(n)):F(1)}
    for u in range(n):
        v=(u+1)%n; out=defaultdict(F)
        for part,w in state.items():
            out[part]+=w
            q=merge(part,u,v)
            if q is not None:out[q]+=lam*w
        state=out
    ans=[F(0)]*(n+1)
    for part,w in state.items():
        comps=len(set(part)); poly=[F(1)]
        sizes=defaultdict(int)
        for i,c in enumerate(part):sizes[c]+=1
        for size in sizes.values():
            nxt=[F(0)]*(len(poly)+1)
            for k,x in enumerate(poly):nxt[k]+=x;nxt[k+1]+=size*x
            poly=nxt
        for k,x in enumerate(poly):ans[k]+=w*x
    return ans

def add(P,Q):
    R=[F(0)]*max(len(P),len(Q))
    for i,x in enumerate(P):R[i]+=x
    for i,x in enumerate(Q):R[i]+=x
    return R
def mul(P,Q):
    R=[F(0)]*(len(P)+len(Q)-1)
    for i,x in enumerate(P):
        for j,y in enumerate(Q):R[i+j]+=x*y
    return R
def scale(P,c):return [c*x for x in P]

def lucas_formula(n,lam):
    p=lam/(1+lam)
    # A=(1+p)+(1-p)s; Lucas recurrence in polynomial s.
    A=[1+p,1-p]; L0=[F(2)];L1=A
    if n==0:L=L0
    elif n==1:L=L1
    else:
        for _ in range(2,n+1):
            L=add(mul(A,L1),scale(L0,-p));L0,L1=L1,L
    L[0]-=2*p**n
    return scale(L,(1+lam)**n) # D=Z*P=(1+lam)^n*(Lucas-2p^n)

def cyclic_gap_formula(n,lam):
    p=lam/(1+lam);z=1-p**n; out=[F(1)]
    # coefficient convolution of (1-z)^-k(1-pz)^-k
    for k in range(1,n+1):
        coeff=F(0);m=n-k
        for i in range(m+1):
            # binomial(k+i-1,i) binomial(k+m-i-1,m-i) p^(m-i)
            from math import comb
            coeff+=comb(k+i-1,i)*comb(k+m-i-1,m-i)*p**(m-i)
        out.append(F(n,k)*(1-p)**k/z*coeff)
    Z=(1+lam)**n*z
    return scale(out,Z)

def whole_graph_marked_coefficients(n,lam,rows):
    # Literal forest DP on n rim plus four new vertices.  Marked edges are
    # recorded as formal bits; all other weights are exact Fractions.
    N=n+4; state={(tuple(range(N)),0,0):F(1)}
    edges=[]
    for i in range(n):edges.append((i,(i+1)%n,lam,None))
    for r,row in enumerate(rows):
        for i in range(n):edges.append((n+r,i,row,None))
    edges += [(n,n+1,F(1),0),(n+2,n+3,F(1),1)]
    for u,v,w,mark in edges:
        out=defaultdict(F)
        for (part,be,bf),z in state.items():
            out[(part,be,bf)]+=z
            q=merge(part,u,v)
            if q is None:continue
            ne,nf=be,bf
            if mark==0:ne=1
            if mark==1:nf=1
            out[(q,ne,nf)]+=w*z
        state=out
    ans={(0,0):F(0),(1,0):F(0),(0,1):F(0),(1,1):F(0)}
    for (_,be,bf),z in state.items():ans[be,bf]+=z
    return ans

def derivative(P,s,j):
    out=F(0)
    for k in range(j,len(P)):
        fac=1
        for h in range(j):fac*=k-h
        out+=P[k]*fac*s**(k-j)
    return out

def predicted_rayleigh(D,s,rows):
    vals=[derivative(D,s,j) for j in range(5)];d=vals[0]
    l1=vals[1]/d
    l2=vals[2]/d-l1*l1
    l3=vals[3]/d-3*vals[2]*vals[1]/d**2+2*l1**3
    l4=(vals[4]/d-4*vals[3]*vals[1]/d**2
        -3*(vals[2]/d)**2+12*vals[2]*vals[1]**2/d**3-6*l1**4)
    A0=F(D[1],D[0]);U=(A0-l1)/s
    Up=(-l2*s-(A0-l1))/s**2
    Upp=(-l3*s*s+2*l2*s+2*(A0-l1))/s**3
    Gamma=-Up;Omega=Upp/2;T=-l2
    a,b,c,drow=rows;p=a+b;q=c+drow
    return d*d*a*b*c*drow*(2*(U*T-Omega)+p*q*(Gamma**2+U*U*T-2*U*Omega))

def main():
    cases=[]
    for n in range(3,11):
        for lam in [F(0),F(1,7),F(1),F(5,2),F(20)]:
            direct=apex_dp(n,lam);lucas=lucas_formula(n,lam)
            gaps=cyclic_gap_formula(n,lam) if lam else [F(1)] # p=0 handled below
            if lam==0:gaps=[F(1)]
            if lam==0:
                gaps=[F(1)]
                for _ in range(n):gaps=mul(gaps,[F(1),F(1)])
            assert direct==lucas==gaps,(n,lam,direct,lucas,gaps)
            assert direct[1]==n*direct[0]
            cases.append({'n':n,'lambda':str(lam),
                          'coefficients_ascending':list(map(str,direct))})
    rayleigh=[]
    for n in [3,4]:
        for lam,rows in [(F(0),(F(1),F(2),F(3),F(4))),
                         (F(1,2),(F(1,3),F(2,3),F(4,3),F(5,3))),
                         (F(3),(F(2),F(1),F(3),F(1,2)))]:
            coeff=whole_graph_marked_coefficients(n,lam,rows)
            delta=coeff[1,0]*coeff[0,1]-coeff[0,0]*coeff[1,1]
            pred=predicted_rayleigh(apex_dp(n,lam),sum(rows),rows)
            assert delta==pred and delta>0,(n,lam,rows,delta,pred)
            rayleigh.append({'n':n,'lambda':str(lam),'rows':list(map(str,rows)),
                             'EF_minus_AC':str(delta)})
    out={'status':'PASS exact direct-partition, cyclic-gap, Lucas, and literal marked-Rayleigh equality',
         'cases':len(cases),'n_range':[3,10],
         'activities':['0','1/7','1','5/2','20'],
         'literal_marked_cases':len(rayleigh),'records':cases,
         'marked_records':rayleigh}
    (HERE/'uniform_cycle_apex_real_rooted_exact_results.json').write_text(
        json.dumps(out,indent=2)+'\n')
    print({k:v for k,v in out.items() if k not in ('records','marked_records')})

if __name__=='__main__':main()
