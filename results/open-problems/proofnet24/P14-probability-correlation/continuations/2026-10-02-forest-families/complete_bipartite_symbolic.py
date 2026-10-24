"""Exact forest transfer on K_{m,s}, with symbolic common edge weight.

The Rayleigh differences are evaluated for the three automorphism types:
same hub, same terminal, and disjoint.  Positive coefficients in the
binomial basis of t=s-2 imply positivity for all integer s>=2 and lambda>0.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial
from pathlib import Path
import json


def add(a,b):
    c=dict(a)
    for k,v in b.items():
        c[k]=c.get(k,0)+v
        if not c[k]:del c[k]
    return c


def scale(a,v):return {k:x*v for k,x in a.items() if x*v}


def mul(a,b):
    c={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            ij=(i+k,j+l);c[ij]=c.get(ij,0)+x*y
    return {k:v for k,v in c.items() if v}


def power(a,n):
    b={(0,0):F(1)}
    for _ in range(n):b=mul(b,a)
    return b


def binomial_t(k,shift=0):
    p={(0,0):F(1)}
    for j in range(k):p=mul(p,{(0,1):F(1),(0,0):F(shift-j)})
    return scale(p,F(1,factorial(k)))


def partitions(m):
    out=[]
    def step(p):
        if len(p)==m:out.append(tuple(p));return
        for b in range(max(p)+2 if p else 1):step(p+[b])
    step([])
    return out


def canonical(p):
    d={};q=[]
    for x in p:
        if x not in d:d[x]=len(d)
        q.append(d[x])
    return tuple(q)


def merge(p,S):
    blocks=[p[i] for i in S]
    if len(blocks)!=len(set(blocks)):return None
    if len(S)<2:return p
    selected=set(blocks)
    return canonical([blocks[0] if x in selected else x for x in p])


def transfer(m,required=(),non_diagonal=False):
    states=partitions(m);ix={p:i for i,p in enumerate(states)};T=[]
    for p in states:
        row={}
        for mask in range(1<<m):
            S=[i for i in range(m) if mask>>i&1]
            if any(i not in S for i in required):continue
            if non_diagonal and len(S)<2:continue
            q=merge(p,S)
            if q is not None:
                j=ix[q];mon={(len(S)-len(required),0):F(1)}
                row[j]=add(row.get(j,{}),mon)
        T.append(row)
    return states,T


def row_multiply(row,T):
    out={}
    for i,p in row.items():
        for j,q in T[i].items():out[j]=add(out.get(j,{}),mul(p,q))
    return out


def row_sum(row):
    out={}
    for p in row.values():out=add(out,p)
    return out


def sequence_coefficients(m,operators):
    states,N=transfer(m,non_diagonal=True)
    row={states.index(tuple(range(m))):{(0,0):F(1)}}
    hs=[]
    for k in range(m):
        temp=row
        for T in operators:temp=row_multiply(temp,T)
        hs.append(row_sum(temp))
        row=row_multiply(row,N)
    assert not row
    return hs


def normalized(m,hs,shift):
    a={(0,0):F(1),(1,0):F(4 if m==4 else m)}
    p={}
    for k,h in enumerate(hs):p=add(p,mul(mul(h,binomial_t(k,shift)),power(a,m-1-k)))
    return p


def evaluate_t(p,t):
    out={}
    for (i,j),v in p.items():out[i]=out.get(i,0)+v*t**j
    return {i:v for i,v in out.items() if v}


def binomial_basis(p):
    degree=max((j for i,j in p),default=0)
    rows=[evaluate_t(p,t) for t in range(degree+1)]
    out=[]
    while rows:
        out.append(rows[0])
        rows=[{i:b.get(i,0)-a.get(i,0) for i in a.keys()|b.keys() if b.get(i,0)-a.get(i,0)} for a,b in zip(rows,rows[1:])]
    return out


def readable(p):
    return {str(i):str(v) for i,v in sorted(p.items())}


def derive(m):
    states,U0=transfer(m,required=(0,))
    _,U1=transfer(m,required=(1,))
    _,V01=transfer(m,required=(0,1))
    Z=normalized(m,sequence_coefficients(m,[]),shift=2)
    A=normalized(m,sequence_coefficients(m,[U0]),shift=1)
    Bh=normalized(m,sequence_coefficients(m,[V01]),shift=1)
    Bt=normalized(m,sequence_coefficients(m,[U0,U0]),shift=0)
    Bd=normalized(m,sequence_coefficients(m,[U0,U1]),shift=0)
    a={(0,0):F(1),(1,0):F(m)}
    differences={
        'same_hub':add(mul(A,A),scale(mul(mul(a,Z),Bh),-1)),
        'same_terminal':add(mul(A,A),scale(mul(Z,Bt),-1)),
        'disjoint':add(mul(A,A),scale(mul(Z,Bd),-1)),
    }
    result={'m':m,'state_count':len(states),'normalization':'R(lambda)= (1+m*lambda)^(2*s-2*m) * P(s-2,lambda)','types':{}}
    for kind,p in differences.items():
        coeffs=binomial_basis(p)
        positive=all(v>=0 for row in coeffs for v in row.values())
        result['types'][kind]={'nonnegative_binomial_coefficients':positive,'coefficients':[readable(c)for c in coeffs]}
        print('m=',m,kind,'positive=',positive,'terms=',len(p),'lowest lambda=',min((i for i,j in p),default=None),flush=True)
        if not positive:
            print('negative coefficients:',[(k,i,str(v))for k,row in enumerate(coeffs)for i,v in row.items()if v<0],flush=True)
    return result


if __name__=='__main__':
    results=[derive(m)for m in [3,4,5,6]]
    Path(__file__).with_name('complete_bipartite_symbolic_results.json').write_text(json.dumps(results,indent=2))
