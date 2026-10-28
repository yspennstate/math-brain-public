from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,hashlib
R=Path(__file__).resolve().parents[1]
start=time.monotonic(); counts={}
def ck(b,s):
    assert b,s
    counts[s]=counts.get(s,0)+1
    assert time.monotonic()-start<55,'runtime cap'
def walsh(f):
    a=list(f);h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h): a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
        h*=2
    return tuple(F(v,len(a)) for v in a)
def direct(f):
    return tuple(F(sum(v*(-1 if (s&t).bit_count()%2 else 1) for t,v in enumerate(f)),len(f)) for s in range(len(f)))
def law(f):return tuple(z*z for z in walsh(f))
def restrict(f,i,b):
    return tuple(f[(t&((1<<i)-1))+((t>>i)<<(i+1))+(b<<i)] for t in range(len(f)//2))
def add(*args):
    d={}
    for c,e in args:
        for q,v in e.items():d[q]=d.get(q,F(0))+c*v
    return {q:v for q,v in d.items() if v and q!=1}
def D(p,q):
    d={}
    for a,b in zip(p,q):
        if a:
            ck(b>0,'cover')
            ratio=a/b; d[ratio]=d.get(ratio,F(0))+a
    return add((1,d))
@lru_cache(None)
def ln(q):
    z=(q-1)/(q+1);pw=z;s=F(0)
    for j in range(32):s+=2*pw/(2*j+1);pw*=z*z
    return s,s+2*pw/(65*(1-z*z))
@lru_cache(None)
def log(q):
    e=0
    while q<1:q*=2;e-=1
    while q>=2:q/=2;e+=1
    a,b=ln(q);c,d=ln(F(2));den=1<<80
    return F(((e+a/d)*den).__floor__(),den),F(((e+b/c)*den).__ceil__(),den)
def bounds(e):
    lo=hi=F(0)
    for q,c in e.items():
        a,b=log(q);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
    return lo,hi
def enc(e):return {'log_terms':{str(q):str(c) for q,c in e.items()},'interval':[str(v) for v in bounds(e)]}
def tilt(p,ctrl,lam):
    q=list(p)
    for t in range(len(p)):
        if t&(1<<ctrl):continue
        j=t+(1<<ctrl);mass=p[t]+p[j]
        if mass:
            k=p[j]/mass; ell=lam*k/(1+(lam-1)*k)
            q[t]=mass*(1-ell);q[j]=mass*ell
    ck(sum(q)==1,'odds target normalized')
    return tuple(q)
def query(f,q,i):
    p=law(f);h=walsh(f);children=[restrict(f,i,b) for b in (0,1)];ps=[law(c) for c in children];raw=[[],[]]
    for t in range(len(f)//2):
        j=(t&((1<<i)-1))+((t>>i)<<(i+1));j1=j+(1<<i);a=p[j]+p[j1];b=q[j]+q[j1]
        for z in (0,1):
            kernel=(h[j]+(-1 if z else 1)*h[j1])**2/(2*a) if a else F(1,2)
            ck(a*kernel==ps[z][t]/2,'actual fair phase channel')
            raw[z].append(b*kernel)
    zs=[sum(v) for v in raw];ck(sum(zs)==1 and min(zs)>0,'own normalizers positive and complete')
    refs=[tuple(v/zs[b] for v in raw[b]) for b in (0,1)]
    delta=add((1,D(p,q)),(-F(1,2),D(ps[0],refs[0])),(-F(1,2),D(ps[1],refs[1])))
    return children,ps,refs,zs,delta
rows=[]
for m in range(2,7):
    f=(-1,)+(1,)*((1<<(m+1))-1)
    ck(walsh(f)==direct(f),'independent direct character spectrum')
    ck(sum(law(f))==1,'Parseval')
    # First query core 0, starting from the TRUE reference, just as v10 depth zero.
    ch,ps,inh,zs,d0=query(f,law(f),0)
    ck(not d0 and zs==[F(1,2)]*2,'initial exact reference has no contraction')
    ck(ch[0][0]==-1 and len(set(ch[1]))==1,'proper data split with full opposite terminal')
    for lam in (F(1,2),F(1),F(2)):
        q=tilt(ps[0],m-1,lam);debt=D(ps[0],q)
        grand,gps,grefs,gzs,loss=query(ch[0],q,m-1)
        ck(grefs==gps,'controller query consumes sector debt completely')
        ck(gzs==[F(1,2)]*2,'sector tilt preserves data marginal normalizers')
        ck(loss==debt,'all incoming sector KL is actual query loss')
        raw_booking=add((F(1,2),debt))
        terminal_divergence={}
        ck(raw_booking==add((F(1,2),loss)),'raw bill minus terminal functional is reached query loss')
        ck(all(not D(p,r) for p,r in zip(gps,grefs)),'BOTH full final divergences zero')
        ck(len(grand)==2 and len(ch)==2,'full physical siblings retained')
        if lam!=1:ck(bounds(raw_booking)[0]>0,'strict missing query bill')
        else:ck(not raw_booking,'identity odds boundary')
        eta=F(1,1<<m)
        # Original eta at root; child active disagreement doubles, reach halves.
        cap=add((1,{F(2):F(4,9)*eta}),(-1,raw_booking))
        ck(bounds(cap)[0]>=0,'positive loss does NOT refute original odds allowance')
        rows.append({'m':m,'lambda':str(lam),'root_negative_probability':str(F(1,1<<(m+1))), 'query_loss':enc(raw_booking),'allowance_slack':enc(cap)})
out={'status':'PASS','cases':len(rows),'assertions':sum(counts.values()),'counts':counts,'elapsed_seconds':time.monotonic()-start,'rows':rows,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'out/EXACT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['rows','counts']}))
