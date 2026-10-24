#!/usr/bin/env python3
"""Exact checks of weighted-cycle apex transfer and real-rootedness."""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
from random import Random
from math import gcd
import json

HERE=Path(__file__).resolve().parent

def merge(part,u,v):
    a,b=part[u],part[v]
    if a==b:return None
    return tuple(a if x==b else x for x in part)

def direct(n,lambdas,betas):
    state={tuple(range(n)):F(1)}
    for i,w in enumerate(lambdas):
        out=defaultdict(F)
        for part,z in state.items():
            out[part]+=z
            q=merge(part,i,(i+1)%n)
            if q is not None:out[q]+=w*z
        state=out
    ans=[F(0)]*(sum(b>0 for b in betas)+1)
    for part,z in state.items():
        mass=defaultdict(F)
        for i,b in enumerate(betas):mass[part[i]]+=b
        P=[F(1)]
        for b in mass.values():
            if not b:continue
            Q=[F(0)]*(len(P)+1)
            for k,x in enumerate(P):Q[k]+=x;Q[k+1]+=b*x
            P=Q
        for k,x in enumerate(P):ans[k]+=z*x
    return ans

def padd(A,B):
    C=[F(0)]*max(len(A),len(B))
    for i,x in enumerate(A):C[i]+=x
    for i,x in enumerate(B):C[i]+=x
    return C
def pmul(A,B):
    C=[F(0)]*(len(A)+len(B)-1)
    for i,x in enumerate(A):
        for j,y in enumerate(B):C[i+j]+=x*y
    return C
def pscale(A,c):return [c*x for x in A]

def matmul(A,B):
    C=[[None,None],[None,None]]
    for i in range(2):
        for j in range(2):
            C[i][j]=[F(0)]
            for k in range(2):C[i][j]=padd(C[i][j],pmul(A[i][k],B[k][j]))
    return C

def transfer(lambdas,betas):
    M=[[[F(1)],[F(0)]],[[F(0)],[F(1)]]]
    Lambda=F(1)
    for w,b in zip(lambdas,betas):
        T=[[[1+w,b],[F(0),b*w]],[[F(1)],[w]]]
        M=matmul(M,T);Lambda*=w
    D=padd(M[0][0],M[1][1]);D[0]-=2*Lambda
    while len(D)>1 and D[-1]==0:D.pop()
    return D

def trim(P):
    while len(P)>1 and not P[-1]:P.pop()
    return P
def rem(A,B):
    A=list(map(F,A));B=list(map(F,B))
    while len(A)>=len(B) and any(A):
        q=A[-1]/B[-1];d=len(A)-len(B)
        for i,x in enumerate(B):A[i+d]-=q*x
        trim(A)
    return A
def primitive(P):
    den=1
    for x in P:den=den*x.denominator//gcd(den,x.denominator)
    I=[x.numerator*(den//x.denominator) for x in P];g=0
    for x in I:g=gcd(g,abs(x))
    return [F(x//g) for x in I] if g else [F(0)]
def real_roots(P):
    P=list(map(F,P));total=0
    while len(P)>1:
        seq=[P,[i*P[i] for i in range(1,len(P))]]
        while len(seq[-1])>1:
            R=primitive([-x for x in rem(seq[-2],seq[-1])])
            if not any(R):break
            seq.append(R)
        pos=[1 if R[-1]>0 else -1 for R in seq]
        neg=[sgn*(-1 if (len(R)-1)%2 else 1) for R,sgn in zip(seq,pos)]
        changes=lambda S:sum(a!=b for a,b in zip(S,S[1:]))
        total+=changes(neg)-changes(pos)
        if len(seq[-1])==1:break
        P=seq[-1]
    return total

def whole_marked(lambdas,betas,rows):
    n=len(lambdas);N=n+4
    state={(tuple(range(N)),0,0):F(1)};edges=[]
    for i,w in enumerate(lambdas):edges.append((i,(i+1)%n,w,None))
    for r,a in enumerate(rows):
        for i,b in enumerate(betas):edges.append((n+r,i,a*b,None))
    edges.extend([(n,n+1,F(1),0),(n+2,n+3,F(1),1)])
    for u,v,w,mark in edges:
        out=defaultdict(F)
        for (part,be,bf),z in state.items():
            out[part,be,bf]+=z
            q=merge(part,u,v)
            if q is None:continue
            ne,nf=be,bf
            if mark==0:ne=1
            if mark==1:nf=1
            out[q,ne,nf]+=w*z
        state=out
    ans={(0,0):F(0),(1,0):F(0),(0,1):F(0),(1,1):F(0)}
    for (_,be,bf),z in state.items():ans[be,bf]+=z
    return ans

def deriv(P,s,j):
    out=F(0)
    for k in range(j,len(P)):
        fac=1
        for h in range(j):fac*=k-h
        out+=P[k]*fac*s**(k-j)
    return out

def predicted(D,s,rows):
    v=[deriv(D,s,j) for j in range(5)];d=v[0];l1=v[1]/d
    l2=v[2]/d-l1*l1
    l3=v[3]/d-3*v[2]*v[1]/d**2+2*l1**3
    A0=F(D[1],D[0]) if len(D)>1 else F(0)
    U=(A0-l1)/s;Up=(-l2*s-(A0-l1))/s**2
    Upp=(-l3*s*s+2*l2*s+2*(A0-l1))/s**3
    G=-Up;O=Upp/2;T=-l2;a,b,c,e=rows
    return d*d*a*b*c*e*(2*(U*T-O)+(a+b)*(c+e)*(G*G+U*U*T-2*U*O))

def main():
    rng=Random(17032027);records=[]
    fixed=[
      ([F(0),F(2),F(3)],[F(1),F(4),F(2)]),
      ([F(1,3),F(2),F(7,2)],[F(2),F(0),F(5)]),
      ([F(1),F(2),F(3),F(4)],[F(1),F(3),F(2),F(5)]),
    ]
    cases=[]
    for ls,bs in fixed:cases.append((ls,bs))
    for n in range(2,10):
        for _ in range(8):
            ls=[F(rng.choice([1,2,3,5,8]),rng.choice([1,2,4])) for _ in range(n)]
            bs=[F(rng.choice([0,1,1,2,3,5]),rng.choice([1,2,3])) for _ in range(n)]
            if not any(bs):bs[0]=F(1)
            cases.append((ls,bs))
    for ls,bs in cases:
        A=direct(len(ls),ls,bs);B=transfer(ls,bs)
        assert A==B,(ls,bs,A,B)
        count=real_roots(A);assert count==len(A)-1,(ls,bs,A,count)
        records.append({'n':len(ls),'lambdas':list(map(str,ls)),
                        'betas':list(map(str,bs)),
                        'degree':len(A)-1,'real_roots_with_multiplicity':count,
                        'coefficients_ascending':list(map(str,A))})
    marked=[]
    marked_cases=[
      ([F(1),F(2),F(3)],[F(1),F(4),F(2)],(F(1),F(2),F(3),F(4))),
      ([F(1,2),F(3),F(2)],[F(2),F(0),F(5)],(F(1,3),F(2),F(4,3),F(5))),
      ([F(0),F(2),F(3),F(4)],[F(1),F(3),F(2),F(5)],(F(2),F(1),F(3),F(1,2))),
      ([F(1),F(2),F(3)],[F(7),F(0),F(0)],(F(1),F(2),F(3),F(4))),
      ([F(1),F(2),F(3)],[F(1),F(4),F(2)],(F(0),F(2),F(3),F(4))),
    ]
    for ls,bs,rows in marked_cases:
        C=whole_marked(ls,bs,rows)
        delta=C[1,0]*C[0,1]-C[0,0]*C[1,1]
        pred=predicted(direct(len(ls),ls,bs),sum(rows),rows)
        assert delta==pred,(ls,bs,rows,delta,pred)
        strict=all(rows) and sum(b>0 for b in bs)>=2
        assert (delta>0)==strict,(ls,bs,rows,delta)
        marked.append({'n':len(ls),'lambdas':list(map(str,ls)),
                       'betas':list(map(str,bs)),'rows':list(map(str,rows)),
                       'EF_minus_AC':str(delta),'strict':strict})
    out={'status':'PASS exact literal partition = independent 2x2 transfer; exact Sturm all-real; literal marked Rayleigh match',
         'cases':len(records),'n_range':[2,9],
         'literal_marked_cases':len(marked),'records':records,
         'marked_records':marked}
    (HERE/'weighted_cycle_apex_real_rooted_exact_results.json').write_text(
      json.dumps(out,indent=2)+'\n')
    print({k:v for k,v in out.items() if k not in ('records','marked_records')})

if __name__=='__main__':main()
