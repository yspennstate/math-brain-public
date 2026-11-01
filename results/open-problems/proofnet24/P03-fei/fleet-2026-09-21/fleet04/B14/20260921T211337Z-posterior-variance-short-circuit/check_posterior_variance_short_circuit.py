#!/usr/bin/env python3
from fractions import Fraction
from itertools import product, combinations
import math, random

def event_stats(bits, n, A):
    pts = list(product((0,1), repeat=n))
    p = Fraction(sum(bits), 1<<n)
    groups = {}
    for x,y in zip(pts,bits):
        key = tuple(x[i] for i in A)
        s,m = groups.get(key,(0,0))
        groups[key] = (s+y,m+1)
    eu2 = Fraction(0)
    c = Fraction(0)
    for s,m in groups.values():
        u = Fraction(s,m)
        w = Fraction(m,1<<n)
        eu2 += w*u*u
        c += w*max(Fraction(0),2*u-1)
    return p, eu2-p*p, c

def exact_variance_crossing():
    cases=0; equal=0
    for n in range(1,5):
        N=1<<n
        for mask in range(1,1<<N):
            if 2*mask.bit_count()>N: continue
            bits=[(mask>>i)&1 for i in range(N)]
            for r in range(n+1):
                for A in combinations(range(n),r):
                    p,var,c=event_stats(bits,n,A)
                    rhs=max(Fraction(0), 2*(var-p*(Fraction(1,2)-p)))
                    assert c>=rhs, (n,mask,A,p,var,c,rhs)
                    if c==rhs: equal+=1
                    cases+=1
    return cases,equal

def walsh(a):
    a=list(map(float,a)); N=len(a); h=1
    while h<N:
        for i in range(0,N,2*h):
            for k in range(i,i+h):
                x,y=a[k],a[k+h]
                a[k],a[k+h]=x+y,x-y
        h*=2
    return [x/N for x in a]

def infl(v,n,j):
    return sum(v[x]!=v[x^(1<<j)] for x in range(1<<n))/(1<<n)

def center(v,n):
    p=[infl(v,n,j) for j in range(n)]
    T=[j for j,x in enumerate(p) if x>0.5]
    out=[]
    for x,y in enumerate(v):
        ch=-1 if sum((x>>j)&1 for j in T)%2 else 1
        out.append(y*ch)
    return out,[infl(out,n,j) for j in range(n)]

def crossing_eta(eta,n,A):
    groups={}
    for x,y in enumerate(eta):
        key=tuple((x>>i)&1 for i in A)
        s,m=groups.get(key,(0,0))
        groups[key]=(s+y,m+1)
    c=0.0
    for s,m in groups.values():
        u=s/m
        c += m/(1<<n)*max(0.0,2*u-1)
    return c

def aggregate_check():
    rng=random.Random(1404)
    cases=0; max_violation=0.0; max_identity=0.0
    for n in (2,3,4):
        for _ in range(160):
            v=[1 if rng.getrandbits(1) else -1 for _ in range(1<<n)]
            v,p=center(v,n)
            J=sum(p)
            if J==0: continue
            etas=[]
            M=0.0
            for j in range(n):
                eta=[1.0 if v[x]!=v[x^(1<<j)] else 0.0 for x in range(1<<n)]
                etas.append(eta)
                wh=walsh(eta)
                M += sum(S.bit_count()*c*c for S,c in enumerate(wh) if S)
            if M==0: continue
            T=sum(x*(0.5-x) for x in p)
            R1=sum(x*(1-x) for x in p)
            max_identity=max(max_identity,abs(R1-(T+J/2)))
            assert M+1e-12>=R1
            s=J/(4*M); t=1-s
            EC=0.0
            for mask in range(1<<n):
                r=mask.bit_count()
                w=(t**r)*(s**(n-r))
                A=[i for i in range(n) if (mask>>i)&1]
                C=sum(crossing_eta(etas[j],n,A) for j in range(n) if j not in A)
                EC += w*C
            lb=J*J/(8*M)
            max_violation=max(max_violation,lb-EC)
            assert EC+1e-10>=lb
            cases+=1
    return cases,max_violation,max_identity

def short_circuit_check():
    cases=0; max_violation=Fraction(0); max_depth_err=Fraction(0)
    for n in range(1,4):
        pts=list(product((0,1),repeat=n)); N=1<<n
        for mask in range(1,1<<N):
            bits=[(mask>>i)&1 for i in range(N)]
            p=Fraction(sum(bits),N)
            for r in range(1,n+1):
                for F in combinations(range(n),r):
                    for a in product((0,1),repeat=r):
                        Qin=[all(x[F[k]]==a[k] for k in range(r)) for x in pts]
                        q=Fraction(1,1<<r)
                        inter=Fraction(sum(y and z for y,z in zip(bits,Qin)),N)
                        delta=p+q-2*inter
                        leaves=[]
                        for t in range(r):
                            ids=[idx for idx,x in enumerate(pts)
                                 if all(x[F[k]]==a[k] for k in range(t))
                                 and x[F[t]]!=a[t]]
                            leaves.append(ids)
                        leaves.append([idx for idx,z in enumerate(Qin) if z])
                        c=Fraction(0); ed=Fraction(0)
                        for t,ids in enumerate(leaves):
                            if not ids: continue
                            w=Fraction(len(ids),N)
                            u=Fraction(sum(bits[i] for i in ids),len(ids))
                            c += w*max(Fraction(0),2*u-1)
                            depth=(t+1) if t<r else r
                            ed += w*depth
                        target=max(Fraction(0),p-delta)
                        if target>c: max_violation=max(max_violation,target-c)
                        exact_depth=2*(1-Fraction(1,1<<r))
                        max_depth_err=max(max_depth_err,abs(ed-exact_depth))
                        assert c>=target
                        assert ed==exact_depth
                        cases+=1
    return cases,max_violation,max_depth_err

if __name__=="__main__":
    a=exact_variance_crossing()
    b=aggregate_check()
    c=short_circuit_check()
    print("variance_event_block_cases",a[0])
    print("variance_equality_cases",a[1])
    print("aggregate_boolean_cases",b[0])
    print("max_aggregate_violation",format(b[1],".17g"))
    print("max_R1_identity_error",format(b[2],".17g"))
    print("short_circuit_event_subcube_cases",c[0])
    print("max_short_circuit_crossing_violation",c[1])
    print("max_short_circuit_depth_error",c[2])
    print("PASS")
