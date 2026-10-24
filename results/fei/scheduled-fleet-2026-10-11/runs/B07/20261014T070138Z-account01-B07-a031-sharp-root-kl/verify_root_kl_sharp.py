#!/usr/bin/env python3
"""Independent full-identity check for B07-A031-SHARP-ROOT-KL-v2."""
import math

TOL = 3e-11
CASES = ASSERTIONS = 0
MAX_ID_ERR = MAX_SURPLUS = MAX_RATIO = 0.0

def check(x, msg):
    global ASSERTIONS
    ASSERTIONS += 1
    if not x: raise AssertionError(msg)

def fwht(v):
    a=list(map(float,v)); N=len(a); h=1
    while h<N:
        for j in range(0,N,2*h):
            for k in range(j,j+h):
                x,y=a[k],a[k+h]; a[k],a[k+h]=x+y,x-y
        h*=2
    return [x/N for x in a]

def h2(t):
    if t<=0 or t>=1: return 0.0
    return -t*math.log2(t)-(1-t)*math.log2(1-t)

def dhalf(x):
    if abs(x)==1: return 1.0
    return ((1+x)*math.log1p(x)+(1-x)*math.log1p(-x))/(2*math.log(2))

def kl(p,q):
    z=0.0
    if p:
        if q<=0: return math.inf
        z+=p*math.log2(p/q)
    if p<1:
        if q>=1: return math.inf
        z+=(1-p)*math.log2((1-p)/(1-q))
    return z

def upper(p,n):
    z=p[:]
    for i in range(n):
        for s in range(1<<n):
            if not (s>>i)&1: z[s]+=z[s|(1<<i)]
    return z

def U(v):
    n=len(v).bit_length()-1; p=[x*x for x in fwht(v)]; pi=upper(p,n)
    return sum(x*math.log2(pi[s]/x) for s,x in enumerate(p) if x)

def child(v,i,e):
    n=len(v).bit_length()-1; low=(1<<i)-1; z=[]
    for s in range(1<<(n-1)):
        old=(s&low)|((s>>i)<<(i+1))|(e<<i); z.append(v[old])
    return z

def terms(v,i):
    n=len(v).bit_length()-1; c=fwht(v); p=[x*x for x in c]; pi=upper(p,n)
    bit=1<<i; base=[s for s in range(1<<n) if not s&bit]
    B=Ga=K=root=0.0
    for A in base:
        u,w=c[A],c[A|bit]; m=u*u+w*w
        if not m: continue
        B+=m*h2(w*w/m)
        V=pi[A|bit]
        if w: Ga+=w*w*math.log2(pi[A]/V)
        C=sum(c[T]*c[T|bit] for T in base if (T&A)==A)
        al=max(-1.0,min(1.0,2*u*w/m)); be=max(-1.0,min(1.0,2*C/pi[A]))
        q=m*kl((1+al)/2,(1+be)/2); K+=q
        if A==0:
            root=q; check(abs(C)<TOL,"root convolution")
    return B,Ga,K,root,c[bit]

def audit(v):
    global CASES,MAX_ID_ERR,MAX_SURPLUS,MAX_RATIO
    CASES+=1; n=len(v).bit_length()-1; u=U(v); roots=sing=0.0
    for i in range(n):
        delta=u-(U(child(v,i,0))+U(child(v,i,1)))/2
        B,Ga,K,root,d=terms(v,i); err=abs(delta-(B-Ga+K))
        MAX_ID_ERR=max(MAX_ID_ERR,err); check(err<TOL,"local identity")
        surplus=root-(2/math.log(2))*d*d; MAX_SURPLUS=max(MAX_SURPLUS,surplus)
        check(surplus<TOL,"sharp root bound"); roots+=root; sing+=d*d
    check(roots<=(2/math.log(2))*sing+TOL,"summed root bound")
    if sing: MAX_RATIO=max(MAX_RATIO,roots/sing)

def main():
    for n in range(1,5):
        N=1<<n
        for mask in range(1<<N):
            audit([1 if (mask>>x)&1 else -1 for x in range(N)])
    defect=[]
    for n in range(2,28):
        t=2.0**(1-n); a,d=1-t,t; m=a*a+d*d; x=2*a*d/m
        ratio=m*dhalf(x)/(d*d); check(ratio<=2/math.log(2)+TOL,"defect")
        defect.append(ratio)
    print("claim=B07-A031-SHARP-ROOT-KL-v2")
    print("verdict=PROVED_PENDING_FRESH_REVIEW")
    print("boolean_truth_tables",CASES)
    print("assertions",ASSERTIONS)
    print("max_local_identity_error",f"{MAX_ID_ERR:.3e}")
    print("max_sharp_root_surplus",f"{MAX_SURPLUS:.3e}")
    print("max_finite_root_ratio",f"{MAX_RATIO:.15g}")
    print("point_defect_n27_ratio",f"{defect[-1]:.15g}")
    print("sharp_constant_2_over_ln2",f"{2/math.log(2):.15g}")
    print("universal_GU=OPEN")

if __name__=="__main__": main()
