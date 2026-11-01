"""Exact certificate generator. No third-party packages; writes only run/out."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json, sys, time

RUN=Path(__file__).resolve().parents[1]
START=time.monotonic()
CHECKS=0
def require(ok):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(CHECKS)

@lru_cache(None)
def ln_interval(x):
    x=Q(x)
    if x==1: return Q(0),Q(0)
    if x<1:
        lo,hi=ln_interval(1/x)
        return -hi,-lo
    # First reduce to [1,2]; ln(2) itself uses the same convergent series.
    k=0
    while x>2: x/=2; k+=1
    y=(x-1)/(x+1)
    total=sum((2*y**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0))
    tail=2*y**49/(49*(1-y*y))
    if k:
        a,b=ln_interval(Q(2))
        return total+k*a,total+tail+k*b
    return total,total+tail

LN2=ln_interval(Q(2))
@lru_cache(None)
def log2_interval(x):
    if x==1:return Q(0),Q(0)
    if x<1:
        lo,hi=log2_interval(1/x)
        return -hi,-lo
    lo,hi=ln_interval(x)
    return lo/LN2[1],hi/LN2[0]

def entropy(p):
    lo=hi=Q(0)
    for w in p:
        if w:
            a,b=log2_interval(w)
            lo-=w*b; hi-=w*a
    return lo,hi

def fwht(truth):
    v=list(truth); step=1
    while step<len(v):
        for i in range(0,len(v),2*step):
            for j in range(i,i+step):
                a,b=v[j],v[j+step];v[j]=a+b;v[j+step]=a-b
        step*=2
    return [Q(a,len(v)) for a in v]

def truth(mask,n):return [1 if mask>>j&1 else -1 for j in range(1<<n)]

def influences(v):
    n=(len(v)-1).bit_length()
    return Q(sum(v[j]!=v[j^(1<<i)] for i in range(n) for j in range(len(v))),len(v))

def ref(p,t):
    raw=[Q(i+1) for i in range(len(p))]; total=sum(raw);raw=[x/total for x in raw]
    nc=1<<t;v=sum(p[nc:]);den=sum(raw[nc:])
    calibrated=p[:nc]+[v*x/den if v else Q(0) for x in raw[nc:]]
    require(sum(calibrated)==1)
    require(all(not x or y>0 for x,y in zip(p,calibrated)))
    return calibrated

def embed(v,t,yprivate=False):
    out={}
    for j,w in enumerate(v):
        key=(j&((1<<t)-1)) | ((j>>t)<<(t+1) if yprivate else (j>>t)<<t)
        if w:out[key]=w
    return out

def debt_ratios(p,r):
    result={}
    for key,w in p.items():
        if w:
            ratio=w/r[key];result[ratio]=result.get(ratio,Q(0))+w
    return result

def pair(g,h,t,hprivate):
    ga,ha=fwht(g),fwht(h);gp=[a*a for a in ga];hp=[a*a for a in ha]
    a=embed(ga,t);b=embed(ha,t,hprivate)
    pg=embed(gp,t);ph=embed(hp,t,hprivate)
    rg=embed(ref(gp,t),t);rh=embed(ref(hp,t),t,hprivate)
    n=t+1+int(hprivate)
    fullg=[g[j&((1<<(t+1))-1)] for j in range(1<<n)]
    fullh=[h[(j&((1<<t)-1))|(((j>>(t+1))&1)<<t if hprivate else 0)] for j in range(1<<n)]
    d=Q(sum(x!=y for x,y in zip(fullg,fullh)),1<<n);ds=min(d,1-d)
    v=fullg+fullh;root=fwht(v);pf={i:w*w for i,w in enumerate(root) if w}
    require(influences(v)==(influences(g)+influences(h))/2+d)
    require(d==(1-sum(a.get(j,0)*b.get(j,0) for j in set(a)|set(b)))/2)
    qref={}; formula={};rootminor={}
    keys=set(a)|set(b)|set(rg)|set(rh)
    for j in keys:
        aa=a.get(j,Q(0));bb=b.get(j,Q(0));q=(aa*aa+bb*bb)/2
        r=(rg.get(j,Q(0))+rh.get(j,Q(0)))/2
        for u in (0,1):
            mass=(aa+(1 if u==0 else -1)*bb)**2/4
            key=j|(u<<n)
            if mass:formula[key]=mass
            kernel=mass/q if q else Q(u==0)
            if r*kernel:qref[key]=r*kernel
        if j<(1<<t):
            if d>Q(1,2):bb=-bb
            rootminor[j]=((aa*aa+bb*bb)/2,(aa-bb)**2/4)
    require(formula==pf)
    require(sum(qref.values())==1)
    require(all(qref.get(j,0)>0 for j in pf))
    target={}
    for ratios in (debt_ratios(pg,rg),debt_ratios(ph,rh)):
        for ratio,w in ratios.items():target[ratio]=target.get(ratio,Q(0))+w/2
    require(debt_ratios(pf,qref)==target) # Exact formal KL identity, no numerical log.
    delta=sum(e for m,e in rootminor.values())
    require(delta<=ds and delta<=(1<<t)*ds*ds)
    require(all(e<=ds*ds for m,e in rootminor.values()))
    hf=entropy(pf.values());hg=entropy(gp);hh=entropy(hp)
    dl=hf[0]-(hg[1]+hh[1])/2;du=hf[1]-(hg[0]+hh[0])/2
    if ds:
        require(du<=(t+2+3/LN2[1])*ds)
        blo=bhi=Q(0)
        for m,e in rootminor.values():
            if m:
                z=entropy([e/m,1-e/m]);blo+=m*z[0];bhi+=m*z[1]
        require(bhi<=(t+1/LN2[1])*ds)
        # Jensen can be tight; permit only the proved interval error overlap.
        bound=entropy([delta,1-delta]);require(blo<=bound[1])
    else:require(sorted(pf.values())==sorted(pg[j] for j in range(len(gp)) if gp[j]))

mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
count=0
limit=64 if mode=='pilot' else 4096
for gm in range(256):
    for hm in range(16):
        if count==limit:break
        pair(truth(gm,3),truth(hm,2),2,False);count+=1
    if count==limit:break
extra=0;compressed=[]
if mode!='pilot':
    menu=[0,1,3,15,23,85,105,255]
    for gm in menu:
        for hm in menu:pair(truth(gm,3),truth(hm,3),2,True);extra+=1
    for t in (4,6):
        g=[(-1)**sum(((j>>(2*k))&1)*((j>>(2*k+1))&1) for k in range(t//2)) for j in range(1<<t)]
        h=g[:];h[0]*=-1
        # Add one dummy private X bit to satisfy the checker embedding convention.
        pair(g+g,h,t,False);extra+=1
    for t in range(4,65,2):
        eps=Q(1,1<<t); e=Q(1,1<<(t//2));N=1<<t
        plus=(N+(1<<(t//2)))//2;minus=N-plus
        hflo=hfhi=hhlo=hhhi=Q(0)
        for sign,mult in ((1,plus),(-1,minus)):
            A=(sign*e-eps)**2;B=eps*eps
            require(A>=Q(9,16)*eps)
            x=entropy([A,B]);hflo+=mult*x[0];hfhi+=mult*x[1]
            x=entropy([(sign*e-2*eps)**2]);hhlo+=mult*x[0];hhhi+=mult*x[1]
        dl=(hflo-(t+hhhi)/2)/eps;du=(hfhi-(t+hhlo)/2)/eps
        # Lower estimate directly from the row inequality avoids sign decisions at equality.
        lower=t-log2_interval(Q(16,9))[1]
        require(dl>lower)
        require(du<t+2+3/LN2[1])
        compressed.append({'t':t,'delta_over_d_lower':str(dl),'delta_over_d_upper':str(du),'analytic_lower':str(lower)})
elapsed=time.monotonic()-START
require(elapsed<(60 if mode=='pilot' else 240))
result={'helper_version':'A095-shared-collision-v1','mode':mode,'status':'PASS','exact_assertions':CHECKS,'exhaustive_pairs':count,'additional_pairs':extra,'compressed_cases':len(compressed),'elapsed_seconds':elapsed,'arithmetic':'Fraction and rigorous atanh log intervals; exact KL ratio-mass identity','compressed_certificates':compressed}
(RUN/'out'/('PILOT.json' if mode=='pilot' else 'EXACT_RESULTS.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='compressed_certificates'}))
