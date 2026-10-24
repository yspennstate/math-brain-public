from fractions import Fraction
import math

def folded_influences(bits,n):
    N=1<<n
    out=[]
    for i in range(n):
        e=0
        for x in range(N):
            if (x>>i)&1: continue
            if bits[x]!=bits[x^(1<<i)]: e+=1
        p=Fraction(e,1<<(n-1))
        out.append(min(p,1-p))
    return out

def folded_event(bits,n,j):
    pnum=0
    eta={}
    for x in range(1<<n):
        if (x>>j)&1: continue
        v=int(bits[x]!=bits[x^(1<<j)])
        eta[x]=v
        pnum+=v
    p=Fraction(pnum,1<<(n-1))
    if p>Fraction(1,2):
        eta={x:1-v for x,v in eta.items()}
        p=1-p
    return eta,p

def event_influence(eta,n,j,i):
    e=0
    for x,v in eta.items():
        if (x>>i)&1: continue
        if v!=eta[x^(1<<i)]: e+=1
    return Fraction(e,1<<(n-2))

for n in range(1,5):
    N=1<<n
    classes=1<<(N-1)
    active=viol=eq=0
    nonconst=maxeq=branch=0
    for mask in range(classes):
        bits=[0]*N
        for k in range(1,N):
            bits[k]=(mask>>(k-1))&1
        q=folded_influences(bits,n)
        J=sum(q,Fraction(0))
        if any(x>0 for x in q):
            nonconst+=1
            pmax=max(q)
            L=math.log2(1/float(pmax))
            theta=float((J-pmax)/pmax)-L
            if abs(theta)<1e-12: maxeq+=1
            if float(pmax)<=0.25+1e-15 and theta<=1/(16*L)+1e-12:
                branch+=1
        for j,qj in enumerate(q):
            if qj==0: continue
            active+=1
            eta,p=folded_event(bits,n,j)
            assert p==qj
            b=sum((event_influence(eta,n,j,i) for i in range(n) if i!=j),Fraction(0))
            if b>2*(J-qj): raise AssertionError(("capacity",n,mask,j,b,J,qj))
            rhs=2*float(qj)*math.log2(1/float(qj))
            if float(b)+1e-12<rhs: raise AssertionError(("isoperimetry",n,mask,j,float(b),rhs))
            lhs=float(J-qj)
            pr=float(qj)*math.log2(1/float(qj))
            if lhs+1e-12<pr:
                viol+=1
            if abs(lhs-pr)<1e-12:
                eq+=1
    print(f"n={n} classes={classes} active_checks={active} violations={viol} equality={eq} "
          f"nonconstant={nonconst} max_theta_zero={maxeq} max_branch_condition={branch}")
