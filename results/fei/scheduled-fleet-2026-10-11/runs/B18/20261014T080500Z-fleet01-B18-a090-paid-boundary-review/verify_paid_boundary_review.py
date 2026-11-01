#!/usr/bin/env python3
"""Independent exhaustive audit of the paid-boundary tree identities."""
import math
import random

C0=2/math.log(2)
TOL=3e-11
CASES=NODES=REUSE=0
MAXU=MAXI=MAXK=0.0

def walsh(t):
    a=[float(x) for x in t]; h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return [x/len(a) for x in a]

def UI(t):
    c=walsh(t); n=(len(t)-1).bit_length(); p=[x*x for x in c]; u=p[:]
    for i in range(n):
        for s in range(1<<n):
            if not (s>>i)&1: u[s]+=u[s|(1<<i)]
    U=sum(m*math.log2(u[s]/m) for s,m in enumerate(p) if m)
    I=sum(s.bit_count()*m for s,m in enumerate(p))
    return U,I

def cut(t,n,i,b):
    return [y for x,y in enumerate(t) if ((x>>i)&1)==b]

def inf(t,n,i):
    return sum(t[x]!=t[x|(1<<i)] for x in range(1<<n) if not ((x>>i)&1))/(1<<(n-1))

def kroot(t,n,i):
    a=sum(t)/len(t)
    d=sum(y*(1 if (x>>i)&1 else -1) for x,y in enumerate(t))/len(t)
    m=a*a+d*d
    if not m: return 0.0,d
    z=(1+2*a*d/m)/2
    h=0 if z<=0 or z>=1 else -z*math.log2(z)-(1-z)*math.log2(1-z)
    return m*(1-h),d

def trees(rem):
    if not rem: return [None]
    out=[]
    for i in rem:
        tail=tuple(x for x in rem if x!=i)
        sub=trees(tail)
        for l in sub:
            for r in sub: out.append((i,l,r))
    return out

def random_tree(rem,rng):
    if not rem or rng.random()<.22: return None
    i=rng.choice(rem); tail=tuple(x for x in rem if x!=i)
    return i,random_tree(tail,rng),random_tree(tail,rng)

def audit(table,n,tree):
    global CASES,NODES,REUSE,MAXU,MAXI,MAXK
    CASES+=1; ur,ir=UI(table)
    sdu=si=sk=lu=li=0.0; labels_seen=[]
    def rec(t,labels,node,w):
        nonlocal sdu,si,sk,lu,li
        global NODES,MAXK
        if node is None:
            u,z=UI(t); lu+=w*u; li+=w*z; return
        physical,l,r=node; j=labels.index(physical); dim=len(labels)
        t0,t1=cut(t,dim,j,0),cut(t,dim,j,1)
        u,z=UI(t); u0,_=UI(t0); u1,_=UI(t1)
        sdu+=w*(u-(u0+u1)/2)
        si+=w*inf(t,dim,j)
        k,d=kroot(t,dim,j); sk+=w*k
        MAXK=max(MAXK,k-C0*d*d); assert k<=C0*d*d+TOL
        labels_seen.append(physical); nxt=tuple(x for x in labels if x!=physical)
        rec(t0,nxt,l,w/2); rec(t1,nxt,r,w/2); NODES+=1
    rec(table,tuple(range(n)),tree,1.0)
    MAXU=max(MAXU,abs(sdu-(ur-lu))); MAXI=max(MAXI,abs(si-(ir-li)))
    assert abs(sdu-(ur-lu))<=TOL and abs(si-(ir-li))<=TOL
    mean=sum(table)/len(table)
    assert sk<=C0*(1-mean*mean)+TOL
    if len(labels_seen)!=len(set(labels_seen)): REUSE+=1

def main():
    for n in range(1,4):
        for mask in range(1<<(1<<n)):
            t=[1 if (mask>>x)&1 else -1 for x in range(1<<n)]
            for tr in trees(tuple(range(n))): audit(t,n,tr)
    rng=random.Random(180900)
    for n in (4,5,6):
        for _ in range(700):
            t=[rng.choice((-1,1)) for _ in range(1<<n)]
            audit(t,n,random_tree(tuple(range(n)),rng))
    print("audited_claim=B06-A028-PAID-U-BOUNDARY-v1")
    print("verdict=HOLDS_AT_CONDITIONAL_SCOPE")
    print("tree_function_cases",CASES)
    print("internal_node_checks",NODES)
    print("branch_reuse_cases",REUSE)
    print("max_U_telescope_error",f"{MAXU:.3e}")
    print("max_I_telescope_error",f"{MAXI:.3e}")
    print("max_root_KL_surplus",f"{MAXK:.3e}")
    print("first_unpaid_line=universal_tree_residual_existence")
    print("universal_GU=OPEN")

if __name__=="__main__": main()
