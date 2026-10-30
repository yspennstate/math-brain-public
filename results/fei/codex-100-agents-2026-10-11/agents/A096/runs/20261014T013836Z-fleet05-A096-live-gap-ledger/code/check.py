from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import time,json,sys
RUN=Path(__file__).resolve().parent.parent;t0=time.perf_counter();checks=0
def ck(v):
    global checks
    checks+=1
    assert v,checks
    assert time.perf_counter()-t0<60
@lru_cache(None)
def fac(n):
    a={};d=2
    while d*d<=n:
        while n%d==0:a[d]=a.get(d,0)+1;n//=d
        d+=1
    if n>1:a[n]=a.get(n,0)+1
    return a
def add(a,b,c=F(1)):
    a=dict(a)
    for p,v in b.items():
        a[p]=a.get(p,F(0))+c*v
        if not a[p]:del a[p]
    return a
def lg(x,c=F(1)):
    return add({p:c*v for p,v in fac(x.numerator).items()},{p:c*v for p,v in fac(x.denominator).items()},F(-1))
def scale(a,c):return {p:c*v for p,v in a.items() if c*v}
def spectrum(t):
    a=t[:];w=1
    while w<len(a):
        for i in range(0,len(a),2*w):
            for j in range(i,i+w):a[j],a[j+w]=a[j]+a[j+w],a[j]-a[j+w]
        w*=2
    return [F(v*v,len(a)**2) for v in a]
def row(p,i,partner=None):
    bit=1<<i;e=sum(p[s] for s in range(len(p)) if s&bit);buckets={}
    for s in range(len(p)):
        if s&bit:continue
        v=s if partner is None else s&~(1<<partner)
        x,y=buckets.get(v,(F(0),F(0)));buckets[v]=(x+p[s],y+p[s|bit])
    ck(sum(x+y for x,y in buckets.values())==1)
    M={};D={}
    for x,y in buckets.values():
        if y:M=add(M,lg((x+y)/y,y));D=add(D,lg((y/e)/(x+y),y/e))
    if e:ck(M==add(lg(1/e,e),D,-e))
    return e,M,D,buckets
def audit(t):
    p=spectrum(t);n=len(t).bit_length()-1;ck(sum(p)==1)
    rs=[row(p,i) for i in range(n)]
    for i,(e,_,_,_) in enumerate(rs):ck(e==F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)))
    H={};M={}
    for v in p:
        if v:H=add(H,lg(1/v,v))
    for _,mi,_,_ in rs:M=add(M,mi)
    return p,rs,H,M
def test(seed,n,J):
    p,rs,H,M=audit(seed);positions=[];pos=0
    for i in range(n):
        positions.append((pos,pos+1) if i in J else (pos,));pos+=2 if i in J else 1
    parent=[]
    for x in range(1<<pos):
        s=0
        for i,ps in enumerate(positions):s|=(sum((x>>j)&1 for j in ps)%2)<<i
        parent.append(seed[s])
    pp,rr,HH,MM=audit(parent);ck(HH==H)
    expected=[F(0)]*len(pp)
    for s,v in enumerate(p):
        dest=sum(sum(1<<j for j in positions[i]) for i in range(n) if (s>>i)&1);expected[dest]=v
    ck(pp==expected)
    MJ={};loss={}
    for i,ps in enumerate(positions):
        if i in J:
            MJ=add(MJ,rs[i][1])
            for j,partner in [ps,ps[::-1]]:
                e,mi,di,_=rr[j];ce,cm,cd,buckets=row(pp,j,partner)
                ck(e==rs[i][0] and ce==e);ck(mi=={})
                if e:ck(di==lg(1/e));ck(cd==rs[i][2])
                R=[F(0),F(0)];U=[F(0),F(0)]
                for s in range(len(pp)):
                    if (s>>j)&1:continue
                    v=(s>>partner)&1;R[v]+=pp[s]+pp[s|(1<<j)]
                    if e:U[v]+=pp[s|(1<<j)]/e
                ck(R==[1-e,e])
                if e:ck(U==[0,1]);ck(di==lg(1/R[1]))
                ck(cm==rs[i][1]);loss=add(loss,add(cm,mi,F(-1)))
        else:ck(rr[ps[0]][:3]==rs[i][:3])
    ck(MM==add(M,MJ,F(-1)));ck(loss==scale(MJ,F(2)))
    ck(sum(r[0] for r in rr)==sum(r[0] for r in rs)+sum(rs[i][0] for i in J))
    return dict(p=pp,rows=rr,seedrows=rs,positions=positions)
cases=0
for n in ([1,2] if '--targeted' in sys.argv else [1,2,3]):
    for mask in range(1<<(1<<n)):
        seed=[1 if (mask>>x)&1 else -1 for x in range(1<<n)]
        for bits in range(1,1<<n):test(seed,n,{i for i in range(n) if (bits>>i)&1});cases+=1
bent=[]
for d in [2,4,6]:
    seed=[];delta=F(1,1<<d)
    for x in range(1<<(d+1)):
        s=x&1;y=x>>1;b=(-1)**sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(d//2))
        seed.append(-b if s and y==0 else b)
    a=test(seed,d+1,{0});p=spectrum(seed)
    ck(a['seedrows'][0][0]==delta)
    for j in range(1,d+1):ck(a['seedrows'][j][0]==F(1,2)+delta)
    for T in range(1<<d):
        x,y=p[T<<1],p[(T<<1)|1];ck(y==delta*delta);ck(x+y>=delta/2)
    for j,partner in [(0,1),(1,0)]:
        e,M,D,bk=row(a['p'],j,partner);ck(e==delta)
        ck(M==a['seedrows'][0][1]);ck(a['rows'][j][2]==lg(1/delta))
    # At least two different conditional reference probabilities: genuinely correlated spectator.
    cond=set()
    for T in range(1<<d):
        x,y=p[T<<1],p[(T<<1)|1];cond.add(y/(x+y))
    ck(len(cond)==2)
    bent.append({'d':d,'query_influence':str(delta),'M_loss_per_query_influence_lower_bound':d-1,'upper_bound':d,'total_influence':str(F(d,2)+(d+2)*delta),'H_over_I_upper_bound':'3'})
    cases+=1
ck(cases==(55 if '--targeted' in sys.argv else 1847))
out={'status':'PASS','cases':cases,'assertions':checks,'runtime_seconds':time.perf_counter()-t0,'arithmetic':'Integer Walsh, exact Fraction and prime-log coefficient identities','bent_flip_certificates':bent}
(RUN/'out').mkdir(exist_ok=True);(RUN/'out/CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
