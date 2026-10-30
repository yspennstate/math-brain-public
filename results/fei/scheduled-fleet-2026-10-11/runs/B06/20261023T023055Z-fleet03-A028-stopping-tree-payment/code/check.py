"""Exact prescribed-profile reference ledger; frozen domains in out/FROZEN_SPEC.json."""
from pathlib import Path
import sys,json,time,hashlib
from fractions import Fraction as F
from functools import lru_cache
import exact_helper as e
ROOT=Path(__file__).resolve().parents[1]
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
START=time.monotonic(); LIMIT=60 if MODE=='pilot' else 600
checks=0; roots=0; queries=0; witnesses={}

def ck(ok,msg=''):
    global checks
    if not ok: raise AssertionError(msg)
    checks+=1

def eq(a,b,msg=''):
    ck(not e.add(a,e.scale(b,-1)),msg)

def nn(a,msg=''):
    ck(e.enclosure(a)[0]>=0,(msg,a,e.enclosure(a)))

def neg(a): return e.scale(a,-1)
def avg(a,b): return e.scale(e.add(a,b),F(1,2))
def kl(p,r):
    ck(len(p)==len(r))
    ck(sum(p)==sum(r)==1)
    return e.add(*(e.scale(e.lg(x/y),x) for x,y in zip(p,r) if x))

@lru_cache(None)
def spectrum(t): return e.stats(t)[0]

def insert(x,i,b):
    low=x&((1<<i)-1)
    return low|((x^low)<<1)|(b<<i)

@lru_cache(None)
def restrict(t,i,b): return tuple(t[insert(x,i,b)] for x in range(len(t)//2))

def physical(t,r,i):
    """Pair erasure then true-phase outcome; all reference mass kept."""
    N=len(t); p=spectrum(t); a=e.walsh(t)
    q=[]; s=[]; joint=[[],[]]
    for T in range(N//2):
        j,k=insert(T,i,0),insert(T,i,1)
        u=p[j]+p[k]; v=r[j]+r[k]
        q.append(u);s.append(v)
        for b in (0,1):
            prob=F((a[j]+(-1)**b*a[k])**2,2*(a[j]**2+a[k]**2)) if u else F(1,2)
            joint[b].append(v*prob)
            ck((u*prob)==spectrum(restrict(t,i,b))[T]/2)
    rho=tuple(sum(x) for x in joint)
    ck(sum(rho)==1 and min(rho)>0)
    rr=tuple(tuple(x/rho[b] for x in joint[b]) for b in (0,1))
    D=kl(p,r); E=e.add(D,neg(kl(tuple(q),tuple(s))))
    O=kl((F(1,2),F(1,2)),rho)
    dc=tuple(kl(spectrum(restrict(t,i,b)),rr[b]) for b in (0,1))
    eq(D,e.add(E,O,avg(*dc)),'physical exact chain')
    nn(E,'erasure');nn(O,'outcome')
    return rr,E,O,rho

@lru_cache(None)
def mux(a,g,h): return tuple((g if v==1 else h)[x] for x in range(len(g)) for v in a)

def profile(a,g,h,rg,rh):
    p=F(sum(v==-1 for v in a),len(a)); pg=spectrum(g); ph=spectrum(h)
    q=tuple((1-p)*x+p*y for x,y in zip(pg,ph))
    r=tuple((1-p)*x+p*y for x,y in zip(rg,rh))
    pf=spectrum(mux(a,g,h)); NA=len(a)
    rf=[]
    for t,qt in enumerate(q):
        ck(sum(pf[t*NA:(t+1)*NA])==qt)
        rf.extend(r[t]*(pf[t*NA+u]/qt if qt else F(u==0)) for u in range(NA))
    rf=tuple(rf); D=kl(pf,rf)
    eq(D,kl(q,r),'profile marginal KL')
    W=e.add(e.scale(kl(pg,rg),1-p),e.scale(kl(ph,rh),p))
    Z=e.add(W,neg(D)); nn(Z,'mixture slack')
    # Second definition uses posterior source labels and keeps off-target reference mass.
    post={}
    for t,qt in enumerate(q):
        if qt:
            pp=((1-p)*pg[t]/qt,p*ph[t]/qt)
            rp=((1-p)*rg[t]/r[t],p*rh[t]/r[t])
            post=e.add(post,e.scale(kl(pp,rp),qt))
    eq(Z,post,'posterior identity')
    return dict(D=D,W=W,Z=Z,H=e.entropy(pf),rf=rf,p=p)

def encoded(d): return {str(k):str(v) for k,v in d.items()}
def interval(d): return [str(x) for x in e.enclosure(d)]

def one(a,g,h,rg,rh,label):
    global roots,queries
    roots+=1; parent=profile(a,g,h,rg,rh)
    f=mux(a,g,h); na=len(a).bit_length()-1; nx=len(g).bit_length()-1
    for i in range(na+nx):
        queries+=1
        inh,Ef,Of,rhof=physical(f,parent['rf'],i)
        if i<na:
            kids=[profile(restrict(a,i,b),g,h,rg,rh) for b in (0,1)]
            srcA={}
        else:
            j=i-na
            rgg,Eg,Og,rhog=physical(g,rg,j)
            rhh,Eh,Oh,rhoh=physical(h,rh,j)
            kids=[profile(a,restrict(g,j,b),restrict(h,j,b),rgg[b],rhh[b]) for b in (0,1)]
            srcA=e.add(e.scale(e.add(Eg,Og),1-parent['p']),e.scale(e.add(Eh,Oh),parent['p']))
        A=e.add(parent['W'],neg(avg(*(k['W'] for k in kids))))
        eq(A,srcA,'source contraction'); nn(A,'A')
        sigma=e.add(avg(*(k['D'] for k in kids)),neg(parent['D']))
        eq(sigma,e.add(parent['Z'],neg(avg(*(k['Z'] for k in kids))),neg(A)),'signed reset')
        dinh=[kl(spectrum(restrict(f,i,b)),inh[b]) for b in (0,1)]
        kappa=e.add(avg(*(k['D'] for k in kids)),neg(avg(*dinh)))
        eq(kappa,e.add(sigma,Ef,Of),'raw reset/refund')
        # Both children retained in the complete CE payment.
        dh=e.add(parent['H'],neg(avg(*(k['H'] for k in kids))))
        lhs=e.add(dh,avg(*(e.add(k['H'],k['D']) for k in kids)))
        rhs=e.add(parent['H'],parent['W'],neg(A),neg(avg(*(k['Z'] for k in kids))))
        eq(lhs,rhs,'full terminal ledger')
        for name,v in [('positive_net_reset',sigma),('positive_raw_reset',kappa)]:
            if name not in witnesses and e.enclosure(v)[0]>0:
                witnesses[name]=dict(label=label,a=list(a),g=list(g),h=list(h),rg=[str(x) for x in rg],rh=[str(x) for x in rh],coordinate=i,controls=na,charge=encoded(v),interval=interval(v),Zroot=encoded(parent['Z']),A=encoded(A),child_D=[encoded(k['D']) for k in kids],child_Z=[encoded(k['Z']) for k in kids],Ef=encoded(Ef),Of=encoded(Of),rhoF=[str(x) for x in rhof])
    if roots%100==0 and time.monotonic()-START>LIMIT: raise TimeoutError('Frozen runtime reached')

def refs(t):
    p=spectrum(t); N=len(t); u=tuple(F(1,N) for _ in t)
    return (u,tuple((x+y)/2 for x,y in zip(p,u)))

if __name__=='__main__':
    ds=list(e.tables(1 if MODE=='pilot' else 2))
    for na,ca,a in e.tables(1):
        for ng,cg,g in ds:
            for nh,ch,h in ds:
                if ng!=nh: continue
                for ig,rg in enumerate(refs(g)):
                    for ih,rh in enumerate(refs(h)):
                        one(a,g,h,rg,rh,[na,ca,ng,cg,ch,ig,ih])
    coreg=tuple(-1 if x==0 else 1 for x in range(8))
    coreh=tuple(-1 if x.bit_count()>=2 else 1 for x in range(8))
    g=tuple(coreg[x&7]*(-1 if x&8 else 1) for x in range(16))
    h=tuple(coreh[x&7]*(-1 if x&8 else 1) for x in range(16))
    a=tuple(-1 if x in (0,1,2) else 1 for x in range(8))
    if MODE=='full':
        for ig,rg in enumerate(refs(g)):
            for ih,rh in enumerate(refs(h)): one(a,g,h,rg,rh,['seven_variable',ig,ih])
    result=dict(status='PASS',mode=MODE,roots=roots,queries=queries,assertions=checks,seconds=time.monotonic()-START,witnesses=witnesses,arithmetic='exact prime-log vectors; rational outward sign bounds',script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (ROOT/'out'/('check_'+MODE+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='witnesses'}))
