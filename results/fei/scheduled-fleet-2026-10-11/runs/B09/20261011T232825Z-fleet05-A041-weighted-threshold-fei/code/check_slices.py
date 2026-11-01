"""A041 stage2 v1.1: exact coherent two-weight spectra and deficit ledgers."""
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
from pathlib import Path
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic(); assertions=0
def check(v):
    global assertions
    assert v
    assertions+=1
def transform(vals,qs):
    a=list(map(F,vals))
    for i,q in enumerate(qs):
        z=1<<i
        for k in range(0,len(a),2*z):
            for j in range(z):
                lo,hi=a[k+j],a[k+j+z]
                a[k+j]=(1-q)*lo+q*hi; a[k+j+z]=hi-lo
    factors=[]; vs=[]
    for s in range(len(a)):
        factor=F(1)
        for i,q in enumerate(qs):
            if s>>i&1:factor*=q*(1-q)
        factors.append(factor); vs.append(factor*4**s.bit_count())
    ps=[u*u*z for u,z in zip(a,factors)]
    return a,ps,factors,vs
def probability(mask,qs):
    z=F(1)
    for i,q in enumerate(qs):z*=q if mask>>i&1 else 1-q
    return z
def energy(ps):return sum(s.bit_count()*p for s,p in enumerate(ps))
def delta(ps):return energy(ps)-(sum(ps)-ps[0])
def cross(us,ut,factors,offset=0):
    return sum((s.bit_count()-offset)*us[s]*ut[s]*factors[s]
               for s in range(1,len(us)))
def corelog(x):
    assert 1<=x<=2
    z=(x-1)/(x+1)
    v=2*sum(z**(2*k+1)/F(2*k+1) for k in range(20))
    return v,v+2*z**41/(41*(1-z*z))
LN2=corelog(F(2))
@lru_cache(maxsize=12000)
def loginterval(x):
    check(x>0)
    exponent=0
    while x<1:x*=2;exponent-=1
    while x>2:x/=2;exponent+=1
    a,b=corelog(x);c,d=LN2
    if exponent>=0:return a+exponent*c,b+exponent*d
    return a+exponent*d,b+exponent*c
def entropy(ps,vs,minimum=1):
    lo=hi=F(0)
    for s,p in enumerate(ps):
        if p and s.bit_count()>=minimum:
            check(vs[s]>=p)
            a,b=loginterval(vs[s]/p);lo+=p*a;hi+=p*b
    return lo,hi
def fractioninterval_bits(a,b):
    c,d=LN2
    corners=(a/c,a/d,b/c,b/d)
    return min(corners),max(corners)
def outward(interval):
    # Fixed output grid, exact outward rounding; no precision escalation.
    scale=1<<80
    a,b=interval
    return (F((a.numerator*scale)//a.denominator,scale),
            F(-((-b.numerator*scale)//b.denominator),scale))
def scores(weights):
    return sorted({sum(w for j,w in enumerate(weights) if x>>j&1)
                   for x in range(1<<len(weights))}-{F(0)})

rows=[];max_ratio=(F(0),None)
def case(h,b,w,qs,t,label):
    global max_ratio
    n=h+b;weights=[w]*h+[F(1)]*b
    vals=[2*int(sum(z for j,z in enumerate(weights) if x>>j&1)>=t)-1
          for x in range(1<<n)]
    u,ps,factors,vs=transform(vals,qs)
    check(sum(ps)==1)
    dF=delta(ps);check(dF>=0)
    check(ps[0]==sum(probability(x,qs)*vals[x] for x in range(1<<n))**2)
    qb=qs[h:];qa=qs[:h]
    merged={}
    for x in range(1<<h):
        child=tuple(vals[x|(y<<h)] for y in range(1<<b))
        merged[child]=merged.get(child,F(0))+probability(x,qa)
    children=[]
    for child,pi in merged.items():
        uc,pc,facb,vb=transform(child,qb)
        check(sum(pc)==1)
        children.append((pi,uc,pc))
    check(sum(z[0] for z in children)==1)
    childD=sum(pi*delta(pc) for pi,uc,pc in children)
    iA=sum((s&((1<<h)-1)).bit_count()*p for s,p in enumerate(ps))
    pureAvar=sum(ps[s] for s in range(1,1<<h))
    deltaA=iA-pureAvar
    check(deltaA>=0);check(dF==childD+deltaA)
    avg=[sum(pi*uc[s] for pi,uc,pc in children) for s in range(1<<b)]
    for s in range(1<<b):check(avg[s]==u[s<<h])
    iB=sum((s>>h).bit_count()*p for s,p in enumerate(ps))
    check(iB==sum(pi*energy(pc) for pi,uc,pc in children))
    iBavg=sum(s.bit_count()*avg[s]*avg[s]*facb[s] for s in range(1<<b))
    check(iBavg==sum(pi*pi*energy(pc) for pi,uc,pc in children))
    mixed=sum((s>>h).bit_count()*p for s,p in enumerate(ps)
              if s&((1<<h)-1) and s>>h)
    check(mixed==iB-iBavg)
    check(mixed==sum(pi*(1-pi)*energy(pc) for pi,uc,pc in children))
    check(mixed<=dF)
    covbudget=F(0)
    G=[]
    for i,(pi,ui,pi_s) in enumerate(children):
        row=[]
        for j,(pj,uj,pj_s) in enumerate(children):
            dd=cross(ui,uj,facb,offset=1)
            row.append(str(dd))
            if i!=j:
                check(cross(ui,uj,facb)==0)
                cov=sum(ui[s]*uj[s]*facb[s] for s in range(1,1<<b))
                check(cov>=0);check(dd==-cov)
                check(cov*cov<=delta(pi_s)*delta(pj_s))
                if i<j:covbudget+=2*pi*pj*cov
            else:check(dd==delta(pi_s))
        G.append(row)
    diagonal=sum(pi*pi*delta(pc) for pi,uc,pc in children)
    check(covbudget<=diagonal)
    if h==1:
        # Direct child spectra, preserving their physical order.
        f0=[vals[y<<1] for y in range(1<<b)]
        f1=[vals[1|(y<<1)] for y in range(1<<b)]
        u0,p0,fb,vb=transform(f0,qb);u1,p1,_,_=transform(f1,qb)
        p=qa[0];v=4*p*(1-p)
        rho=sum(probability(y,qb)*((f1[y]-f0[y])//2) for y in range(1<<b))
        check(dF==(1-p)*delta(p0)+p*delta(p1)+v*rho*(1-rho))
        if f0!=f1:
            gd=[a-bb-1 for a,bb in zip(f1,f0)]
            ug,pg,_,_=transform(gd,qb)
            check(all(z in (-1,1) for z in gd))
            check(energy(pg)==energy(p0)+energy(p1))
            check(delta(pg)<=2*(delta(p0)+delta(p1)))
            for s in range(1,1<<b):
                check(u[s<<1]==(1-p)*u0[s]+p*u1[s])
                check(u[1|(s<<1)]==ug[s])
                check(ps[1|(s<<1)]==v*pg[s]/4)
                if pg[s]:check(vs[1|(s<<1)]/ps[1|(s<<1)]==4*vb[s]/pg[s])
        elo,ehi=entropy(ps,vs,minimum=2)
        slo,shi=entropy(ps,vs,minimum=1)
        if dF:
            # Proved theorem K is >2000 nats. Use c lower bound and e>2
            # to certify the slightly weaker explicit rational constant.
            check(ehi<=F(2100)*dF)
            check(shi<=F(2110)*dF)
            if ehi/dF>max_ratio[0]:max_ratio=(ehi/dF,label)
            ratio=outward(fractioninterval_bits(elo/dF,ehi/dF))
        else:
            check(elo==ehi==slo==shi==0);ratio=(F(0),F(0))
    else:
        ratio=None
    rows.append({'label':label,'A':h,'B':b,'w':str(w),'t':str(t),
        'biases':[str(q) for q in qs],'Delta':str(dF),'averaged_child_Delta':str(childD),
        'delta_A':str(deltaA),'mixed_B_energy':str(mixed),
        'covariance_budget':str(covbudget),'diagonal_deficit_budget':str(diagonal),
        'deficit_Gram_matrix':G,
        'E_ge2_over_Delta_bits_interval':None if ratio is None else [str(a) for a in ratio]})
    if time.monotonic()-START>60:raise RuntimeError('Frozen 60-second pilot cap reached')

for b in (2,3):
    profiles=[(F(1,4),)*b,(F(1,2),)*b,
              (F(1,4),F(3,4)) if b==2 else (F(1,8),F(1,2),F(7,8))]
    for p in (F(1,8),F(1,2),F(7,8)):
        for qb in profiles:
            for w in (F(1,2),F(2),F(4)):
                for t in scores([w]+[F(1)]*b):case(1,b,w,(p,)+qb,t,'one-exceptional')
check(len(rows)==297)
for h,b in ((2,2),(3,3)):
    profiles=[(F(1,2),)*(h+b)]
    if h==2:profiles.extend([(F(1,8),F(7,8),F(1,4),F(3,4)),(F(1,8),)*4])
    else:profiles.append((F(1,8),F(1,2),F(7,8),F(1,4),F(1,2),F(3,4)))
    for qs in profiles:
        for w in (F(1,2),F(2),F(4)):
            for t in scores([w]*h+[F(1)]*b):case(h,b,w,qs,t,'full-two-group-ledger')
check(len(rows)==423)
for m in range(2,7):
    q=F(1,m*m);a=q**m;q0=(m-1)*a/(1+(m-1)*a)
    case(1,m,F(m),(q0,)+(q,)*m,F(m),'global-weighted-control')
for m in range(2,6):
    for q in (F(1,8),F(1,32)):
        a=q**m;q0=a/(1+a)
        case(1,m,F(m),(q0,)+(q,)*m,F(m),'local-weighted-control')
check(len(rows)==436)
out={'helper_version':'A041-stage2-v1.1','status':'PASS','case_count':len(rows),
     'assertions':assertions,'arithmetic':'Fraction exact spectra and Gram budgets; rigorous rational log intervals',
     'elapsed_seconds':time.monotonic()-START,'max_E_ge2_over_Delta_nats_upper':str(outward((max_ratio[0],max_ratio[0]))[1]),
     'max_ratio_label':max_ratio[1],
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows}
(ROOT/'out'/'EXACT_SLICES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
