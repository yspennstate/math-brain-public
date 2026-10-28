from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import hashlib, json, time, sys

ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic()
COUNT=0
def ck(ok):
    global COUNT
    COUNT+=1
    assert ok, COUNT
    if time.monotonic()-START>55: raise TimeoutError('frozen 55-second compute limit')

@lru_cache(None)
def ln(n):
    # n=2^e*x, 1<=x<2; artanh series has z<=1/3.
    e=n.bit_length()-1
    x=Q(n,2**e)
    def unit(x):
        z=(x-1)/(x+1); s=Q(0); power=z
        for j in range(70):
            s+=2*power/(2*j+1); power*=z*z
        tail=2*power/(141*(1-z*z))
        return s,s+tail
    lo,hi=unit(x)
    if e:
        l,h=unit(Q(2));lo+=e*l;hi+=e*h
    return lo,hi

@lru_cache(None)
def log2(n):
    if n & (n-1)==0:return Q(n.bit_length()-1),Q(n.bit_length()-1)
    l,h=ln(n); a,b=ln(2)
    return l/b,h/a

def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,x):return (x*a[0],x*a[1]) if x>=0 else (x*a[1],x*a[0])
def sub(a,b):return a[0]-b[1],a[1]-b[0]

def walsh(v):
    w=list(v);k=1
    while k<len(w):
        for j in range(0,len(w),2*k):
            for i in range(j,j+k):w[i],w[i+k]=w[i]+w[i+k],w[i]-w[i+k]
        k*=2
    return w

def direct(v):
    return [sum(a*(-1 if (s&x).bit_count()%2 else 1) for x,a in enumerate(v)) for s in range(len(v))]

def stats(v):
    w=walsh(v);den=len(v)**2
    ck(sum(a*a for a in w)==den)
    entropy=(Q(0),Q(0)); influence=Q(0)
    for s,a in enumerate(w):
        if a:
            p=Q(a*a,den)
            entropy=add(entropy,scale(sub(log2(den),log2(a*a)),p))
            influence+=s.bit_count()*p
    return entropy,influence,w

def restrict(v,i,b):
    return [v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(v)//2)]

def wrapper(r):
    n=5+2*r
    def value(x):
        b=(-1)**(((x>>0&1)*(x>>1&1))+((x>>2&1)*(x>>3&1)))
        if x&15!=15:return b
        g=1 if (x>>4&1) else -1
        for j in range(r):
            if (x>>(5+2*j))&3==3:g=-g
        return g
    return [value(x) for x in range(1<<n)]

def overlap(a,b):return a[0]<=b[1] and b[0]<=a[1]

def main(mode):
    k=Q(29,13);K=Q(9,2)
    ck(K-2*k==Q(1,26))
    e0=sub(sub((Q(8),Q(8)),scale(log2(3),Q(45,64))),scale(log2(5),Q(75,64)))
    if mode in ('pilot','all'):
        # Independent source transaction audit from exact Boolean spectra.
        for mask in range(256 if mode=='all' else 16):
            v=[1 if mask>>x&1 else -1 for x in range(8)]
            H,I,w=stats(v)
            for i in range(3):
                ss=[stats(restrict(v,i,b)) for b in (0,1)]
                d=sum(Q(a*a,64) for s,a in enumerate(w) if s>>i&1)
                Ic=(ss[0][1]+ss[1][1])/2
                ck(I==d+Ic)
                fee=sub(H,scale(add(ss[0][0],ss[1][0]),Q(1,2)))
                ck(fee[1]<=k*I)
                for q in (Q(0),Q(1,4),Q(1,2)):
                    A=k/(1-q)
                    release=sub((A*I-q*A*Ic,)*2,fee)
                    ck(release[0]>=q*A*d)
                    ck(A<=2*k)
                    ck(K-A>=Q(1,26))
        for r in (1,2):
            v=wrapper(r);H,I,w=stats(v)
            ck(direct(v)==w)
            ck(overlap(H,add(e0,(Q(r,8),)*2)))
            ck(I==Q(7,4)+Q(r+1,16))
            children=[stats(restrict(v,5,b)) for b in (0,1)]
            for h,_,_ in children:ck(overlap(h,add(e0,(Q(r-1,8),)*2)))
            ck((children[0][1]+children[1][1])/2==I-Q(1,32))
            ck(overlap(sub(H,scale(add(children[0][0],children[1][0]),Q(1,2))),(Q(1,8),)*2))
            if mode=='all':
                for q in (Q(0),Q(1,2),Q(1)):
                    leaves=[]
                    def tree(vv,indices,j,weight):
                        # Enumerate all physical answers, then both coin outcomes.
                        i=indices.index(5+2*j)
                        remaining=indices[:i]+indices[i+1:]
                        for b in (0,1):
                            child=restrict(vv,i,b);wgt=weight/2
                            if j==r-1:leaves.append((wgt,stats(child)))
                            else:
                                if q<1:leaves.append((wgt*(1-q),stats(child)))
                                if q>0:tree(child,remaining,j+1,wgt*q)
                    tree(v,list(range(5+2*r)),0,Q(1))
                    ck(sum(wt for wt,_ in leaves)==1)
                    SH=(Q(0),Q(0));SI=Q(0)
                    for wt,(hh,ii,_) in leaves:SH=add(SH,scale(hh,wt));SI+=wt*ii
                    S=sum(q**j for j in range(r))
                    ck(overlap(SH,add(e0,(Q(r,8)-S/8,)*2)))
                    ck(SI==I-S/32)
    profiles=[]
    if mode=='all':
        for r in (1,2,3,8,32,128):
            for q in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)):
                surv=[q**j for j in range(r)];S=sum(surv)
                # Independently sum the entire stopping-length law, BOTH outcomes.
                probs=[q**(l-1)*(1-q) for l in range(1,r)]+[q**(r-1)]
                ck(sum(probs)==1)
                ck(sum((i+1)*p for i,p in enumerate(probs))==S)
                ck(S==(Q(r) if q==1 else (1-q**r)/(1-q)))
                ck(Q(0)<=1-S/r<=Q(r-1,2)*(1-q))
                ck((Q(r)-S)/8+S/8==Q(r,8))
                ck(S/8==4*(S/32))
                for j in range(r):ck(q**j*(1+j*(1-q))<=1)
                profiles.append({'r':r,'q':str(q),'expected_queries':str(S),'core_residual_fraction':str(1-S/r)})
        # Heterogeneous stopping: unequal independent dyadic coins.
        for qs in ([Q(1),Q(1,2),Q(1)],[Q(1,4),Q(3,4),Q(1,2)],[Q(1)]*7,[Q(0)]*7):
            surv=[Q(1)]
            for q in qs:surv.append(surv[-1]*q)
            r=len(surv);p=[surv[j]*(1-qs[j]) for j in range(r-1)]+[surv[-1]]
            ck(sum(p)==1);ck(sum((j+1)*p[j] for j in range(r))==sum(surv))
        ck(1-k/K==Q(59,117))
        ck(1-k/(K-Q(1,26))==Q(1,2))
        # Deterministic exhaustion is affordable for THIS actual family.
        for r in range(1,129):ck(Q(r,8)<K*Q(r+1,16))
    out={'mode':mode,'checks':COUNT,'status':'PASS','compute_seconds':time.monotonic()-START,'profiles':profiles,'E0_interval':[str(x) for x in e0]}
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/f'{mode}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('profiles','E0_interval')}))

if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'all')
