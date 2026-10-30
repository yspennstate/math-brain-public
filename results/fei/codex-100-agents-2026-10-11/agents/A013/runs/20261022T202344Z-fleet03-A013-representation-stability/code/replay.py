"""A013 independent replay: binary-squaring logs, exact Walsh/log signatures.
No author module is imported. All writes are confined to this run.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product, permutations
from functools import lru_cache
import json, time, hashlib, sys

R=Path(__file__).resolve().parents[1]
SRC=Path(r'agents\A012\runs\20261021T212009Z-fleet03-A012-sparse-activation-accounting')
CHECKS=0
def ck(x):
    global CHECKS
    if not x: raise AssertionError(CHECKS)
    CHECKS+=1
def save(name,obj):
    (R/'out').mkdir(exist_ok=True)
    (R/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')

@lru_cache(None)
def upperlog(n,d):
    """ceil enclosure for log2(n/d)*2^64; repeated interval squaring."""
    assert n>=d>0
    k=0
    while n>=2*d: d*=2;k+=1
    S=1<<160; O=1<<64
    lo=n*S//d;hi=(n*S+d-1)//d;prefix=k*O
    for bit in range(1,65):
        lo=lo*lo//S;hi=(hi*hi+S-1)//S
        if lo>=2*S:
            prefix+=1<<(64-bit);lo//=2;hi=(hi+1)//2
        elif hi>=2*S:
            # Prefix before this bit + full remaining binary tail.
            return prefix+(1<<(65-bit))
    return prefix+1

def char(s,t):return 1-2*((s&t).bit_count()%2)
def walsh(v):
    a=list(v);h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for i in range(j,j+h):a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
        h*=2
    return a
def canon(m):
    c=[1-2*((m>>s)&1) for s in range(8)]
    return min(sum((sg*c[s]*char(s,t)<0)<<s for s in range(8)) for sg in (-1,1) for t in range(8))

def continuum():
    start=time.perf_counter();total=pruned=0;minimum=None
    reps=sorted({canon(m) for m in range(256)})
    ck(reps==[0,1,2,3,4,5,6,7,16,17,18,19,20,21,22,23])
    # Verify every ordered triple has an invertible affine map to the fixed triple.
    for x,y,z in permutations(range(8),3):
        u=x^y;v=x^z
        t=next(t for t in range(1,8) if t not in (u,v,u^v))
        im=[x^((i&1)*u)^(((i>>1)&1)*v)^(((i>>2)&1)*t) for i in range(8)]
        ck(len(set(im))==8 and im[:3]==[x,y,z])
    for job,m in enumerate(reps):
        data=json.loads((SRC/'out'/f'CONTINUUM_{job}.json').read_text(encoding='utf-8'))
        ck(data['mask']==m and data['status']=='PASS' and data['unresolved']==[])
        c=[1-2*((m>>s)&1) for s in range(8)]
        P=[(sum(c[s]*char(s,t) for s in range(8)),tuple(c[j]*char(j,t) for j in range(3))) for t in range(8)]
        seen=set();vol=F(0)
        for ix,dep,kind in data['leaves']+data['pruned']:
            ck(dep>=2 and len(ix)==3 and all(0<=i<2**dep for i in ix))
            key=(tuple(ix),dep);ck(key not in seen);seen.add(key);vol+=F(1,2**(3*dep))
            den=2**dep
            if kind=='rare':ck(4*(sum(ix)+3)<=den);pruned+=1;continue
            if kind=='moderate':ck(3*sum(ix)>=4*den);pruned+=1;continue
            sl=[];O=1<<64
            for a,v in P:
                if a==0:continue
                b=sum(v[j]*(2*ix[j]+1) for j in range(3));aa=(2*den*a-b)**2;bb=b*b
                n,e=(1,1024) if bb==0 else ((1023,1024) if aa==0 else (bb,aa+bb))
                lam=upperlog(e,e-n);mu=upperlog(e,n)
                ck(lam+mu>=2*O);sl.append((a,v,lam,mu))
            worst=None
            for bits in product((0,1),repeat=3):
                q=[ix[j]+bits[j] for j in range(3)]
                z=-16*den*O*sum(q)
                for a,v,lam,mu in sl:
                    b=sum(v[j]*q[j] for j in range(3))
                    z+=lam*(a*den-b)**2+(mu-2*O)*b*b
                worst=z if worst is None else max(z,worst)
            ck(worst<0);gap=F(-worst,64*den*den*O)
            minimum=gap if minimum is None else min(gap,minimum);total+=1
            if time.perf_counter()-start>50:raise RuntimeError('50s cap; incomplete')
        ck(vol==1)
        for ix,dep in seen:
            for p in range(2,dep):ck((tuple(i>>(dep-p) for i in ix),p) not in seen)
    save('CONTINUUM_REPLAY.json',dict(status='PASS',checks=CHECKS,leaves=total,analytic_boxes=pruned,minimum_gap=str(minimum),seconds=time.perf_counter()-start,arithmetic='160-bit outward interval binary squaring;64-bit logarithm upper bounds; no atanh series'))

@lru_cache(None)
def factors(n):
    a=[];p=2
    while p*p<=n:
        k=0
        while n%p==0:n//=p;k+=1
        if k:a.append((p,k))
        p+=1
    if n>1:a.append((n,1))
    return tuple(a)
def addlog(out,q,w):
    if not w:return
    assert q>0
    for n,sg in ((q.numerator,1),(q.denominator,-1)):
        for p,k in factors(n):out[p]=out.get(p,F(0))+sg*k*w
def sigclean(a):return {p:q for p,q in a.items() if q}
def entropy(p):
    s={}
    for q in p:
        if q:addlog(s,q,-q)
    return sigclean(s)
def erasure(p):
    s={};n=len(p)//2
    for j in range(n):
        a,b=p[j],p[j+n]
        if a:addlog(s,(a+b)/a,a)
        if b:addlog(s,(a+b)/b,b)
    return sigclean(s)
def divergence(p,q):
    s={}
    for x,y in zip(p,q):
        if x:addlog(s,x/y,x)
    return sigclean(s)
def influence(p,n):return sum(q*i.bit_count() for i,q in enumerate(p))
def fixtures():
    start=time.perf_counter();cases=0;debtcases=0
    # Includes empty/full events, equality, complements, nonindependence and unequal marginals.
    triples=[(0,0,0),(15,15,15),(3,5,6),(1,3,7),(1,1,1),(3,12,15),(7,11,13),(0,1,14)]
    for m in range(256):
        c=[1-2*((m>>s)&1) for s in range(8)];a=walsh(c)
        for ev in triples:
            h=[c[s]*(1-2*(s<3 and ((ev[s]>>v)&1))) for v in range(4) for s in range(8)]
            g=c*4;f=g+h;wh=walsh(h);wg=walsh(g);wf=walsh(f)
            ph=[F(x*x,1024) for x in wh];pg=[F(x*x,1024) for x in wg];pf=[F(x*x,4096) for x in wf]
            q=[F(x.bit_count(),4) for x in ev];d=sum(q)/8;delta=sum(x*x for x in q)/8
            ck(sum(pf)==sum(ph)==sum(pg)==1)
            ck(sum(pf[32:])==d)
            ck(influence(pf,6)==(influence(pg,5)+influence(ph,5))/2+d)
            expected={2:2*(d-delta)}
            for t in range(8):
                b=sum(c[j]*char(j,t)*q[j] for j in range(3))/8;aa=(F(a[t],8)-b)**2;bb=b*b
                ck(pf[t]==aa and pf[t+32]==bb)
                if aa:addlog(expected,(aa+bb)/aa,aa)
                if bb:addlog(expected,(aa+bb)/bb,bb)
            ck(erasure(pf)==sigclean(expected))
            ck(sum(ph[8:])==4*(d-delta))
            # Independent common terminal stays complete under an arbitrary supplied private reference.
            if m%16==0:
                rho=1-sum(ph[:8]);weights=list(range(9,33));norm=sum(weights)
                rh=ph[:8]+[rho*F(x,norm) for x in weights]
                Q=pf[:];
                for t in range(8,32):Q[t]=Q[t+32]=rh[t]/4
                ck(sum(rh)==sum(Q)==1)
                dh=divergence(ph,rh);df=divergence(pf,Q)
                ck(df==sigclean({p:v/2 for p,v in dh.items()}));debtcases+=1
            cases+=1
            if time.perf_counter()-start>50:raise RuntimeError('50s cap; incomplete')
    save('BOOLEAN_REPLAY.json',dict(status='PASS',checks=CHECKS,cases=cases,full_reference_cases=debtcases,seconds=time.perf_counter()-start,arithmetic='integer fast Walsh;Fraction probabilities;exact rational prime-log signatures'))

def boundary():
    start=time.perf_counter()
    c=[(-1)**(((s&1)*((s>>1)&1))+(((s>>2)&1)*((s>>3)&1))) for s in range(16)]
    h=c[:];h[0]*=-1
    a=walsh(c);b=walsh(h);z=walsh(c+h)
    pc=[F(x*x,256) for x in a];ph=[F(x*x,256) for x in b];pf=[F(x*x,1024) for x in z]
    # Reduce entropy vectors independently from the actual Walsh transform.
    delta=entropy(pf)
    for p,v in entropy(pc).items():delta[p]=delta.get(p,F(0))-v/2
    for p,v in entropy(ph).items():delta[p]=delta.get(p,F(0))-v/2
    ck(sigclean(delta)=={2:F(3),3:F(9,64),5:F(-75,64)})
    d=sum(pf[16:]);ck(d==F(1,16))
    ck(a.count(4)==10 and a.count(-4)==6)
    # Delta > 7d follows from this exact integer comparison, with log monotonicity.
    ck(3**9*2**164>5**75)
    # B > 4d is a separate exact integer comparison of its Phi expression.
    ck(10**100*26**156>2**64*9**90*25**150)
    ck(influence(pf,5)==(influence(pc,4)+influence(ph,4))/2+d)
    ck(influence(pc,4)==2 and influence(ph,4)==F(5,2) and influence(pf,5)==F(37,16))
    save('FOUR_BIT_BOUNDARY.json',dict(status='PASS',checks=CHECKS,d=str(d),delta_log_signature={str(p):str(v) for p,v in sigclean(delta).items()},B_gt_4d=True,Delta_gt_7d=True,I_parent='37/16',seconds=time.perf_counter()-start,scope='Actual four-bit shared bent phase with one deterministic row edit; refutes extension of three-bit local surcharge only; full FEI unaffected'))

if __name__=='__main__':
    {'continuum':continuum,'fixtures':fixtures,'boundary':boundary}[sys.argv[1]]()
    print(json.dumps({'status':'PASS','mode':sys.argv[1],'checks':CHECKS}))
