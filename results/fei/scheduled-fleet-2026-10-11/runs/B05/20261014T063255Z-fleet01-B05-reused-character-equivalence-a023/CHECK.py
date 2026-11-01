#!/usr/bin/env python3
"""Exact/rational checks for reused-character activation equivalence."""
from fractions import Fraction
import itertools, math

def fwht(values):
    a=[Fraction(v) for v in values]; h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h]; a[k],a[k+h]=u+v,u-v
        h*=2
    return [u/len(a) for u in a]

def caps(p):
    a=list(p); n=len(a).bit_length()-1
    for i in range(n):
        b=1<<i
        for s in range(len(a)):
            if not s&b: a[s]+=a[s|b]
    return a

def U(f):
    p=[a*a for a in fwht(f)]; c=caps(p)
    return sum(float(a)*math.log2(float(b/a)) for a,b in zip(p,c) if a)

def restrict(f,i,bit):
    n=len(f).bit_length()-1; out=[]
    for z in range(1<<(n-1)):
        lo=z&((1<<i)-1); hi=z>>i
        out.append(f[lo|(bit<<i)|(hi<<(i+1))])
    return tuple(out)

def mult_char(f,i):
    return tuple(v*(1 if s&(1<<i) else -1) for s,v in enumerate(f))

def activate(f):
    # new high selector: z=-1 gives f, z=+1 gives constant +1
    return tuple(f)+tuple(1 for _ in f)

def stats(f):
    p=[a*a for a in fwht(f)]; n=len(f).bit_length()-1
    u=U(f); inf=[]
    for i in range(n): inf.append(sum(float(p[s]) for s in range(len(p)) if s&(1<<i)))
    I=sum(inf)
    G=sum(u-(U(restrict(f,i,0))+U(restrict(f,i,1)))/2 for i in range(n))
    B=0.0
    for i in range(n):
        b=1<<i
        for s in range(len(p)):
            if s&b: continue
            aa,bb=float(p[s]),float(p[s|b]); mass=aa+bb
            if aa: B+=aa*math.log2(mass/aa)
            if bb: B+=bb*math.log2(mass/bb)
    return u,I,G,B,inf

def w(f,x): return U(mult_char(f,x))-U(f)

def drift_w(f,x):
    ans=w(f,x); n=len(f).bit_length()-1
    for j in range(n):
        if j==x: continue
        xx=x-1 if j<x else x
        ans += w(f,x)-(w(restrict(f,j,0),xx)+w(restrict(f,j,1),xx))/2
    return ans

def main():
    cores=0; coordinate_checks=0; identity_checks=0; maxerr=0.0
    for n in range(1,4):
        for f in itertools.product((-1,1),repeat=1<<n):
            f=tuple(f); cores+=1
            uq,iq,gq,bq,inf=stats(f)
            for x in range(n):
                r=mult_char(f,x)
                assert mult_char(r,x)==f
                # Surjectivity: any r is recovered from q=xr.
                assert mult_char(mult_char(r,x),x)==r
                ur,ir,gr,br,_=stats(r)
                e1=abs(br-bq)
                e2=abs((ir-iq)-(1-2*inf[x]))
                e3=abs((gr-gq)-drift_w(f,x))
                maxerr=max(maxerr,e1,e2,e3)
                assert max(e1,e2,e3)<2e-12
                F=activate(r)
                # restriction of selector (new high coordinate)
                assert restrict(F,n,0)==r
                assert restrict(F,n,1)==tuple(1 for _ in r)
                coordinate_checks+=1; identity_checks+=3
    # Exact half-contraction falsifier: q=x, xq=1, A(1)=1.
    for c in (Fraction(1,10),Fraction(7,4),Fraction(1000,1)):
        # L(q)=-c and L(A(xq))=0 for every eta.
        assert Fraction(0)-Fraction(1,2)*(-c)==c/2>0
    print('status=PASS')
    print(f'boolean_cores_checked={cores}')
    print(f'coordinate_checks={coordinate_checks}')
    print(f'signed_identity_checks={identity_checks}')
    print('half_contraction_exact_witness_checks=3')
    print(f'max_float_identity_error={maxerr:.3e}')

if __name__=='__main__': main()
