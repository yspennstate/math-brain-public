#!/usr/bin/env python3
import math, functools

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

BETA = 4*h2(0.25)-2

def scalar_grid(N=800):
    worst = (-1e100, None)
    for a in range(N+1):
        u=a/N
        for b in range(a,N+1):
            v=b/N
            if u+v > 1+1e-15: break
            m=(u+v)/2
            js=h2(m)-(h2(u)+h2(v))/2
            d=(v-u)/2
            c=max(v-0.5,0.0)
            slack=BETA*d+c-js
            if slack < worst[0] or worst[1] is None:
                worst=(slack,(u,v,js,d,c))
    return worst

def fwht(vals):
    a=[float(x) for x in vals]
    n=len(a); s=1
    while s<n:
        for i in range(0,n,2*s):
            for j in range(i,i+s):
                x=a[j]; y=a[j+s]
                a[j]=x+y; a[j+s]=x-y
        s*=2
    return [x/n for x in a]

@functools.lru_cache(None)
def stats(tt):
    N=len(tt); n=N.bit_length()-1
    hat=fwht(tt)
    probs=[x*x for x in hat]
    H=sum(-x*math.log2(x) for x in probs if x>0)
    infl=[]
    for i in range(n):
        bit=1<<i
        num=0
        for x in range(N):
            if not (x&bit) and tt[x]!=tt[x|bit]:
                num+=1
        infl.append(num/(N/2))
    J=sum(min(p,1-p) for p in infl)
    def jpot(p):
        s=.5+math.sqrt(max(0.0,p*(1-p)))
        return 1-h2(s)
    Phi=sum(jpot(p) for p in infl)
    return H,tuple(infl),J,Phi,H-Phi

def restrict_tt(tt,i,b):
    n=(len(tt)).bit_length()-1
    out=[]
    for y in range(1<<(n-1)):
        lo=y&((1<<i)-1); hi=y>>i
        x=lo|(b<<i)|(hi<<(i+1))
        out.append(tt[x])
    return tuple(out)

@functools.lru_cache(None)
def V(tt,j):
    H,inf,J,Phi,F=stats(tt)
    q=min(inf[j],1-inf[j])
    if q==0: return 0.0
    n=(len(tt)).bit_length()-1
    best=float("inf")
    for i in range(n):
        if i==j: continue
        t0=restrict_tt(tt,i,0); t1=restrict_tt(tt,i,1)
        j2=j-1 if i<j else j
        dF=F-.5*(stats(t0)[4]+stats(t1)[4])
        cand=dF+.5*(V(t0,j2)+V(t1,j2))
        best=min(best,cand)
    return best

def scan(n):
    N=1<<n
    total=0; max_k=(-1,None); max_r=(-1,None)
    for mask in range(1<<(N-1)):
        tt=(1,)+tuple(-1 if (mask>>(x-1))&1 else 1 for x in range(1,N))
        H,inf,J,Phi,F=stats(tt)
        if J==0: continue
        total+=1
        r=F/J
        if r>max_r[0]: max_r=(r,tt)
        vals=[]
        for j,p in enumerate(inf):
            q=min(p,1-p)
            if q>0:
                vals.append(V(tt,j)/h2(q))
        if vals:
            k=min(vals)
            if k>max_k[0]: max_k=(k,tt)
    return total,max_k[0],max_r[0]

if __name__=="__main__":
    print("beta", format(BETA,".16f"))
    worst=scalar_grid()
    print("scalar_grid_min_slack", format(worst[0],".16e"), "witness", worst[1])
    for n in (2,3,4):
        total,k,r=scan(n)
        print("n",n,"nonzero_J_global_sign_classes",total,
              "max_min_V_over_h",format(k,".16f"),
              "max_F_over_J",format(r,".16f"))
