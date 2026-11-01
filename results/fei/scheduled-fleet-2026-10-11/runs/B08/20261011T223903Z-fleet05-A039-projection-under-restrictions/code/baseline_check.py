from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); COUNT=0
def check(v):
    global COUNT
    COUNT+=1
    assert v, COUNT
    assert time.perf_counter()-START<59, 'pilot runtime cap'

@lru_cache(None)
def factors(n):
    out={}; p=2
    while p*p<=n and p<=1000:
        while n%p==0: out[p]=out.get(p,0)+1; n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def L(x):
    out={}
    for n,s in [(x.numerator,1),(x.denominator,-1)]:
        for p,e in factors(n).items(): out[p]=out.get(p,F(0))+s*e
    return {p:e for p,e in out.items() if e}
def add(*terms):
    out={}
    for c,t in terms:
        for p,e in t.items(): out[p]=out.get(p,F(0))+c*e
    return {p:e for p,e in out.items() if e}
def ent(p): return add(*[(-x,L(x)) for x in p if x])
def h(x): return ent([x,1-x])
def walsh(tab):
    n=len(tab); v=list(tab); w=1
    while w<n:
        for j in range(0,n,2*w):
            for t in range(j,j+w): v[t],v[t+w]=v[t]+v[t+w],v[t]-v[t+w]
        w*=2
    return [F(x,n) for x in v]
def law(tab): return [a*a for a in walsh(tab)]
def marg(p,n): return [sum((x for s,x in enumerate(p) if s>>j&1),F(0)) for j in range(n)]
def restrict(tab,i,y):
    return [tab[(s&((1<<i)-1))|((s>>i)<<(i+1))|(y<<i)] for s in range(len(tab)//2)]
def kl(p,q): return add(*[(x,add((1,L(x)),(-1,L(y)))) for x,y in zip(p,q) if x])
def product(d):
    return [__import__('math').prod(d[j] if s>>j&1 else 1-d[j] for j in range(len(d))) for s in range(1<<len(d))]

def split_check(tab,i):
    n=len(tab).bit_length()-1; p=law(tab); d=marg(p,n)
    ps=[law(restrict(tab,i,y)) for y in [0,1]]
    ds=[marg(t,n-1) for t in ps]
    q=[(a+b)/2 for a,b in zip(*ps)]
    parentq=[]
    for s in range(1<<(n-1)):
        idx=(s&((1<<i)-1))|((s>>i)<<(i+1)); parentq.append(p[idx]+p[idx|(1<<i)])
    check(q==parentq); check(sum(p)==sum(q)==1)
    for j in range(n-1): check((ds[0][j]+ds[1][j])/2==d[j+(j>=i)])
    HP=ent(p); HC=add((F(1,2),ent(ps[0])),(F(1,2),ent(ps[1])))
    B=add((1,HP),(-1,ent(q))); J=add((1,ent(q)),(-1,HC))
    G=add(*[(1,h(d[j])) for j in range(n) if j!=i],*[(-F(1,2),h(x)) for row in ds for x in row])
    KP=add(*[(1,h(x)) for x in d],(-1,HP))
    KC=add(*[(F(1,2),h(x)) for row in ds for x in row],(-1,HC))
    check(add((1,KC),(-1,KP),(-1,B),(-1,J),(1,h(d[i])),(1,G))=={})
    dr=[d[j] for j in range(n) if j!=i]; R=product(dr)
    k=[[ps[y][s]/(2*q[s]) if q[s] else F(1,2) for s in range(len(q))] for y in [0,1]]
    QY=[sum((R[s]*k[y][s] for s in range(len(q))),F(0)) for y in [0,1]]
    Qc=[[R[s]*k[y][s]/QY[y] for s in range(len(q))] for y in [0,1]]
    reset=add(*[(F(1,2)*x,add((1,L(Qc[y][s])),(-1,L(product(ds[y])[s])))) for y in [0,1] for s,x in enumerate(ps[y]) if x])
    Dout=kl([F(1,2),F(1,2)],QY)
    check(add((1,reset),(-1,Dout),(-1,J),(1,G))=={})
    Kq=kl(q,R)
    check(add((1,Kq),(-1,Dout),(-F(1,2),kl(ps[0],Qc[0])),(-F(1,2),kl(ps[1],Qc[1])))=={})
    return KP,KC

# Fixed-point directed arithmetic for transcendental enclosures.
SCALE=1<<110
def down(x): return F((x*SCALE).__floor__(),SCALE)
def up(x): return F((x*SCALE).__ceil__(),SCALE)
def plus(a,b): return a[0]+b[0],a[1]+b[1]
def minus(a,b): return a[0]-b[1],a[1]-b[0]
def mul(a,b):
    v=[x*y for x in a for y in b]; return down(min(v)),up(max(v))
def div(a,b):
    assert b[0]>0
    v=[x/y for x in a for y in b]; return down(min(v)),up(max(v))
def fixedlnunit(x):
    t=(x-1)/(x+1); lo=(t*SCALE).__floor__(); hi=(t*SCALE).__ceil__()
    t2lo=lo*lo//SCALE; t2hi=(hi*hi+SCALE-1)//SCALE
    plo,phi=lo,hi; slo=shi=0
    for j in range(40):
        den=2*j+1; slo+=plo//den; shi+=(phi+den-1)//den
        plo=plo*t2lo//SCALE; phi=(phi*t2hi+SCALE-1)//SCALE
    tail=F(2,81*3**81)*F(9,8)
    return F(2*slo,SCALE),F(2*shi,SCALE)+tail
LN2=fixedlnunit(F(2))
@lru_cache(None)
def log2(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length(); unit=x/F(2)**k
    if unit<1: unit*=2; k-=1
    if unit>=2: unit/=2; k+=1
    a=fixedlnunit(unit); b=div(a,LN2)
    return down(b[0]+k),up(b[1]+k)
def log_iv(iv): return log2(iv[0])[0],log2(iv[1])[1]
def eta(x): return mul((-x,-x),log2(x)) if x else (F(0),F(0))
def Hiv(p):
    out=(F(0),F(0))
    for x in p: out=plus(out,eta(x))
    return out
def hiv(x): return Hiv([x,1-x])
def evalformal(t):
    out=(F(0),F(0))
    for p,c in t.items(): out=plus(out,mul((c,c),log2(F(p))))
    return out
def weighted(iv,c): return mul(iv,(c,c))
def encloseszero(iv): check(iv[0]<=0<=iv[1])
def decimal(iv):
    z=10**10
    return {'lower':str(F((iv[0]*z).__floor__(),z)), 'upper':str(F((iv[1]*z).__ceil__(),z))}

def projection(d,v):
    if v==0: return (F(0),F(0))
    r=[x/v for x in d if x]; mu=sum(r,F(0))
    if mu==1: HM=Hiv(r)
    elif 1 in r:
        HM=(F(0),F(0))
        for x in r: HM=plus(HM,hiv(x))
    else:
        lo,hi=F(0),F(1)
        for _ in range(90):
            c=(lo+hi)/2
            z=1-c-__import__('math').prod(1-c*x for x in r)
            if z>0: lo=c
            elif z<0: hi=c
            else: lo=hi=c; break
        check(lo>0)
        # F(c)=1-c-product is positive between zero and its positive root.
        HM=log_iv((lo,hi))
        for x in r:
            HM=minus(HM,weighted(log_iv((lo*x,hi*x)),x))
            HM=minus(HM,weighted(log_iv((1-hi*x,1-lo*x)),1-x))
    return plus(hiv(v),weighted(HM,v))

def state(core,k,r):
    c=walsh(core); n=len(core).bit_length()-1; m=c[0]; p=F(1,1<<r); t=1-m
    d=[p*x for x in marg([x*x for x in c],n)]+[p*t]*r
    v=1-(1-p*t)**2
    HH=plus(eta((1-p*t)**2),weighted(eta(p*p*t*t),(1<<r)-1))
    for x in c[1:]: HH=plus(HH,weighted(eta(p*p*x*x),1<<r))
    EE=projection(d,v)
    HHm=(F(0),F(0))
    for x in d: HHm=plus(HHm,hiv(x))
    return dict(H=HH,E=EE,A=minus(EE,HH),Delta=minus(HHm,EE),K=minus(HHm,HH),d=d,v=v,m=m)

def main():
    for bits in range(256):
        tab=[1 if bits>>s&1 else -1 for s in range(8)]
        for i in range(3): split_check(tab,i)
    k4=[(-1)**sum(((x>>i)&1)*((x>>j)&1) for i in range(4) for j in range(i+1,4)) for x in range(16)]
    check(law(k4)==[F(1,16)]*16)
    for i in range(4):
        a,b=split_check(k4,i); check(a=={}); check(b=={2:F(1)})
    dec=split_check([-1]+[1]*7,0)
    check(dec[1]=={}); check(evalformal(dec[0])[0]>0)
    point=[]
    for m in range(3,21):
        a=F(1,1<<(m-1)); p=[(1-a)**2]+[a*a]*((1<<m)-1) if m<=8 else None
        def HH(m,a): return plus(eta((1-a)**2),weighted(log2(1/a),2*a*(2-a)))
        # nonempty entropy coefficient uses log(1/a), not log(1/a^2).
        hp=HH(m,a); hc=HH(m-1,2*a)
        kp=minus(weighted(hiv(a),m),hp); kc=minus(weighted(hiv(2*a),m-1),hc)
        drop=minus(kp,weighted(kc,F(1,2)))
        if p is not None:
            encloseszero(minus(hp,Hiv(p))); encloseszero(minus(projection([a]*m,2*a-a*a),hp))
        check(drop[0]>0)
        point.append({'m':m,'Delta_drop_over_removed_influence':decimal(div(drop,(a,a)))})
    check(point[-1]['m']==20)
    sparse=[]
    for k in [4,6,8]:
        b=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2)) for x in range(1<<k)]
        bp=b.copy(); bp[0]=-bp[0]
        j=[b[x>>1] if x&1==0 else bp[x>>1] for x in range(1<<(k+1))]
        cores={'b':b,'bprime':bp,'selector':j}; states={}
        for name,core in cores.items():
            seq=[state(core,k,r) for r in range(2*k+1)]; states[name]=seq
            for r,z in enumerate(seq):
                encloseszero(minus(z['K'],plus(z['A'],z['Delta'])))
                check(z['A'][1]>=0 and z['Delta'][1]>=0)
                if r:
                    child=seq[r-1]; removed=z['d'][-1]
                    dh=minus(z['H'],weighted(child['H'],F(1,2)))
                    G=(F(0),F(0))
                    for x in z['d'][:-1]: G=plus(G,minus(hiv(x),weighted(hiv(2*x),F(1,2))))
                    kd=minus(z['K'],weighted(child['K'],F(1,2)))
                    encloseszero(minus(plus(kd,dh),plus(hiv(removed),G)))
                    DD=minus(z['Delta'],weighted(child['Delta'],F(1,2)))
                    sparse.append({'k':k,'r':r,'core':name,'Delta_drop_over_removed_influence':decimal(div(DD,(removed,removed))), 'Delta_drop_sign':'positive' if DD[0]>0 else 'negative' if DD[1]<0 else 'undecided'})
            # Complete control path keeps the terminal core account.
            total=(F(0),F(0))
            for r in range(1,2*k+1):
                total=plus(total,weighted(minus(seq[r]['Delta'],weighted(seq[r-1]['Delta'],F(1,2))),F(1,1<<(2*k-r))))
            encloseszero(minus(total,minus(seq[2*k]['Delta'],weighted(seq[0]['Delta'],F(1,1<<(2*k))))))
        R=2*k; parent=states['selector'][R]
        DD=minus(parent['Delta'],weighted(plus(states['b'][R]['Delta'],states['bprime'][R]['Delta']),F(1,2)))
        sparse.append({'k':k,'r':R,'core':'selector_query','Delta_drop_over_removed_influence':decimal(div(DD,(parent['d'][0],parent['d'][0]))),'Delta_drop_sign':'positive' if DD[0]>0 else 'negative' if DD[1]<0 else 'undecided'})
        if k==4:
            for name,core in cores.items():
                n=len(core).bit_length()-1
                for r in [0,1,2]:
                    tab=[core[x&((1<<n)-1)] if x>>n==0 else 1 for x in range(1<<(n+r))]
                    pp=law(tab); z=states[name][r]
                    check(marg(pp,n+r)==z['d']); check(1-pp[0]==z['v'])
                    encloseszero(minus(Hiv(pp),z['H']))
    out={'status':'PASS','assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'point_defect':point,'sparse_bent_transfers':sparse,'exhaustive_splits':768,'arithmetic':'exact rational probabilities/formal logarithm identities and directed rational intervals'}
    (ROOT/'out'/'VALIDATION.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ['point_defect','sparse_bent_transfers']}))
if __name__=='__main__': main()
