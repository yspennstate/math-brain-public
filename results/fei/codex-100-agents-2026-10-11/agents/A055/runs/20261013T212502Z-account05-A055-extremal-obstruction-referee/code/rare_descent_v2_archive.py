from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from math import isqrt
import json, sys, time

ROOT=Path(__file__).resolve().parents[1]
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
START=time.perf_counter(); ASSERTIONS=0; CANDIDATES=0
CAP=55 if MODE=='pilot' else 600

def ck(v):
    global ASSERTIONS
    assert v
    ASSERTIONS+=1
    if time.perf_counter()-START>CAP: raise RuntimeError('frozen runtime cap')

def plus(*items):
    d={}
    for item in items:
        for x,c in item.items():d[x]=d.get(x,Q(0))+c
    return {x:c for x,c in d.items() if c}
def times(e,c):return {x:v*c for x,v in e.items() if v*c}

@lru_cache(None)
def intlog(n):
    if n==1:return {}
    k=(n&-n).bit_length()-1; odd=n>>k
    if odd==1:return {2:Q(k)} if k else {}
    sq=isqrt(odd)
    if sq*sq==odd:return plus({2:Q(k)},times(intlog(sq),2))
    power=odd.bit_length()-1
    if odd*2>=3*(1<<power):power+=1
    return plus({2:Q(k+power)},{Q(odd,1<<power):Q(1)})
def logterm(c,x):
    if c==0:return {}
    assert x>0
    return times(plus(intlog(x.numerator),times(intlog(x.denominator),-1)),c)
def Hmass(ps):return plus(*(logterm(-x,x) for x in ps if x))
def Phi(a,b):return plus(logterm(a+b,a+b),logterm(-a,a) if a else {},logterm(-b,b) if b else {})
def A(d):return plus(logterm(-(1-d)**2,(1-d)**2) if d!=1 else {},logterm(d*d,d*d) if d else {})

@lru_cache(None)
def lnint(n):
    # All non-2 atoms are exact rational residuals near one; powers of
    # two were already combined in the expression, preventing lost
    # correlated ln2 cancellation at large rarity.
    z=Q(1,3) if n==2 else (n-1)/(n+1)
    lo=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0))
    tail=2*abs(z)**49/(49*(1-z*z))
    return (lo,lo+tail) if z>=0 else (lo-tail,lo)
def interval(e):
    lo=hi=Q(0)
    for x,c in e.items():
        a,b=lnint(x);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi
def ip(*xs):return sum((x[0] for x in xs),Q(0)),sum((x[1] for x in xs),Q(0))
def im(x,c):return (x[0]*c,x[1]*c) if c>=0 else (x[1]*c,x[0]*c)
def bits(x):
    a,b=lnint(2);v=[x[0]/a,x[0]/b,x[1]/a,x[1]/b];return min(v),max(v)
def display(x):return {'interval':[str(x[0]),str(x[1])],'display':float((x[0]+x[1])/2)}
def small(x):return [float(x[0]),float(x[1])]

def fwht(f):
    w=f.copy();stride=1
    while stride<len(w):
        for start in range(0,len(w),2*stride):
            for j in range(start,start+stride):w[j],w[j+stride]=w[j]+w[j+stride],w[j]-w[j+stride]
        stride*=2
    return [Q(a,len(w)) for a in w]
def inf(f):
    return [Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(len(f).bit_length()-1)]
def project(f,B,x):
    n=len(f).bit_length()-1;fixed=[i for i in range(n) if B>>i&1];free=[i for i in range(n) if not B>>i&1]
    base=sum(((x>>j)&1)<<i for j,i in enumerate(fixed))
    return [f[base|sum(((y>>j)&1)<<i for j,i in enumerate(free))] for y in range(1<<len(free))]
def hdata(f):
    a=fwht(f);i=inf(f);ck(sum(x*x for x in a)==1)
    ck(i==[sum(a[s]*a[s] for s in range(len(a)) if s>>j&1) for j in range(len(i))])
    mu=Q(sum(f),len(f));b=a.copy();b[0]-=1
    return {'a':a,'inf':i,'mu':mu,'c':1-mu,'H':Hmass([x*x for x in a]),'T':Hmass([x*x for x in b])}

@lru_cache(None)
def bias_interval(r,c):return interval(times(A(Q(1,1<<r)*c),1<<r))
def activation_expr(core,r):
    p=Q(1,1<<r)
    return plus(times(core['T'],p),{2:4*r*p*core['c']},A(p*core['c']))
def profiles(f,core):
    out=[];n=len(f).bit_length()-1
    for B in range(1<<n):
        q=sum(core['inf'][i] for i in range(n) if B>>i&1)
        children=[hdata(project(f,B,x)) for x in range(1<<B.bit_count())]
        weight=Q(1,len(children));avgT=times(plus(*(child['T'] for child in children)),weight)
        delta=plus(core['T'],times(avgT,-1)); hist={}
        for child in children:hist[child['c']]=hist.get(child['c'],Q(0))+weight
        ck(sum(c*v for c,v in hist.items())==core['c'])
        out.append({'B':B,'q':q,'delta':delta,'di':interval(delta),'hist':hist})
    return out

def singleton(core,r,j):
    p=Q(1,1<<r);a=core['a'];c=core['c'];aj=a[1<<j];b=1-p*c
    raw=plus(*(Phi(a[T]**2,a[T|(1<<j)]**2) for T in range(len(a)) if not(T>>j&1) and T),Phi(c*c,aj*aj))
    vr=sum(min(a[T]**2,a[T|(1<<j)]**2) for T in range(len(a)) if not(T>>j&1) and T)+min(c*c,aj*aj)
    B=plus(times(raw,p),times(Phi(c*c,aj*aj),-p*p),Phi(b*b,p*p*aj*aj))
    beta=p*vr-p*p*min(c*c,aj*aj)+min(b*b,p*p*aj*aj)
    return B,beta

def case(f,name,r,core,profs):
    global CANDIDATES
    p=Q(1,1<<r);c=core['c'];I=sum(core['inf']);ln2=lnint(2);rootbias=bias_interval(r,c)
    Hexpr=activation_expr(core,r);H=interval(Hexpr);R=bits(im(H,1/(p*(I+r*c))))
    lamc=[(Q(4),Q(4))]+[bits(im(b['di'],1/b['q'])) for b in profs if b['q']]
    lam=(min(x[0] for x in lamc),min(x[1] for x in lamc))
    candidates=[]
    for b in profs:
        for k in range(r+1):
            if b['B']==len(f)-1 and k==r:continue
            denom=b['q']+k*c
            if not denom:continue
            childbias=ip(*(im(bias_interval(r-k,z),w) for z,w in b['hist'].items()))
            numerator=ip(b['di'],im(ln2,4*k*c),rootbias,im(childbias,-1))
            ratio=bits(im(numerator,1/denom))
            candidates.append((ratio,b['B'],k));CANDIDATES+=1
    phi=(min(x[0][0] for x in candidates),min(x[0][1] for x in candidates))
    witness=min(candidates,key=lambda x:x[0][1])
    ck(phi[0]>=-Q(1,10**18))
    if r>=2:
        d0=min([c]+[x for x in core['inf'] if x]);s=r//2
        ds=Q(8*s+19,1<<s);dr=Q(8*r+19,1<<r)
        err=2*ds/d0+(30+2*dr)/(r*c)
        ck(phi[1]-lam[0]<=err);ck(lam[1]-phi[0]<=err)
    else:err=None
    d=p*c
    bc=plus({2:2*d-2*d*d},Phi((1-d)**2,d*d));betac=min(d,1-d)
    lc=plus({2:4*d},A(d),times(A(2*d),Q(-1,2)))
    Uc=ip(interval(bc),(2*betac,2*betac))
    D=ip(im(H,1/p),im(ln2,-2*(I+r*c)))
    row={'name':name,'r':r,'p':str(p),'mean':str(core['mu']),'H_over_I':display(R),'phi':display(phi),'lambda_raw':display(lam),'upper_witness':{'data_mask':witness[1],'control_count':witness[2],'ratio_interval':[str(witness[0][0]),str(witness[0][1])]},'argmin_scope':'Interval-certified value; this witness supplies the least computed upper endpoint, unique argmin not asserted','convergence_error_bound':str(err) if err is not None else None,'control_actual_price':display(bits(im(interval(lc),1/d))),'control_R2_price':display(bits(im(Uc,1/d))),'C2_deficit_over_p':display(bits(D)),'control_C2_R2_gap_over_p':display(bits(ip(D,im(ln2,2*c),im(Uc,-1/p))))}
    if name.startswith('balanced'):
        j=len(core['inf'])-1;bj,beta=singleton(core,r,j);q=core['inf'][j]
        Uz=ip(interval(bj),(2*beta,2*beta))
        L=next(b for b in profs if b['B']==1<<j)
        Li=ip(L['di'],rootbias,im(ip(*(im(bias_interval(r,z),w) for z,w in L['hist'].items())),-1))
        row.update({'balancing_actual_price':display(bits(im(Li,1/q))),'balancing_R2_price':display(bits(im(Uz,1/(p*q)))),'balancing_C2_R2_gap_over_p':display(bits(ip(D,im(ln2,2*q),im(Uz,-1/p))))})
    return row

def fixture(m):
    h=[-1]+[1]*7;g=[1]
    for _ in range(m):g=[x*y for y in h for x in g]
    return g+[-x for x in g]

def seq(m):
    # r=ceil(2log2(m+1)) via integer inequalities, no floating choice.
    target=(m+1)**2;r=(target-1).bit_length();p=Q(1,1<<r);v=Q(3,4)**(2*m)
    seed=hdata([-1]+[1]*7);Hg=times(seed['H'],m);mu=Q(0)
    core={'T':Hg,'c':Q(1),'H':Hg}
    H=activation_expr(core,r);I=Q(3*m,4)+1+r
    Bj=plus(times(Phi(Q(1),v),p-p*p),Phi((1-p)**2,p*p*v))
    u=bits(ip(im(interval(Bj),1/p),(2*v,2*v)))
    D=bits(ip(im(interval(H),1/p),im(lnint(2),-2*I)))
    gap=ip(im(lnint(2),2),im(interval(H),1/p),im(lnint(2),-2*I),im(interval(Bj),-1/p),(-2*v,-2*v))
    R=bits(im(interval(H),1/(p*I)))
    ck(D[0]>0)
    return {'m':m,'r':r,'p':str(p),'v':str(v),'H_over_I':display(R),'C2_deficit_over_p':display(D),'balancing_R2_price':display(u),'balancing_C2_R2_gap_over_p':display(bits(gap)),'phi_upper_bound':str(u[1]),'R2_failure_certified':gap[0]>0,'strong_failure_u_less_than_C':u[1]<2}

def replay():
    cases=blocks=0
    domain=[]
    for n in [1,2,3]:
        for word in range(1,(1<<(1<<n))-1):domain.append(([ -1 if word>>x&1 else 1 for x in range(1<<n)], [1,2]))
    domain.extend((fixture(m),[1]) for m in [1,2])
    for f,rs in domain:
        core=hdata(f);n=len(f).bit_length()-1
        for r in rs:
            F=f+[1]*((1<<r)-1)*len(f) if False else [a for y in range(1<<r) for a in (f if y==0 else [1]*len(f))]
            af=fwht(F);ix=inf(F);p=Q(1,1<<r);d=p*core['c']
            ck(ix==[p*x for x in core['inf']]+[d]*r)
            ck(Hmass([a*a for a in af])==activation_expr(core,r))
            for j in range(n+r):
                pairs=[(af[T]**2,af[T|(1<<j)]**2) for T in range(len(af)) if not(T>>j&1)]
                bj=plus(*(Phi(a,b) for a,b in pairs));beta=sum(min(a,b) for a,b in pairs)
                if j<n:expected,betax=singleton(core,r,j)
                else:expected=plus({2:2*d-2*d*d},Phi((1-d)**2,d*d));betax=min(d,1-d)
                ck(bj==expected);ck(beta==betax)
            Hparent=Hmass([a*a for a in af])
            for mask in range(1,len(F)-1):
                B=mask&((1<<n)-1);k=(mask>>n).bit_count();a=mask.bit_count()
                children=[project(F,mask,x) for x in range(1<<a)]
                direct=plus(Hparent,times(plus(*(Hmass([t*t for t in fwht(child)]) for child in children)),Q(-1,len(children))))
                data_children=[hdata(project(f,B,x)) for x in range(1<<B.bit_count())]
                compressed=plus(Hparent,times(plus(*(activation_expr(child,r-k) for child in data_children)),Q(-1,(1<<k)*len(data_children))))
                ck(direct==compressed);blocks+=1
            cases+=1
    result={'status':'PASS','roots':cases,'all_labelled_blocks':blocks,'assertions':ASSERTIONS,'elapsed_seconds':time.perf_counter()-START}
    (ROOT/'out/REPLAY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result));return

if MODE=='replay':replay();sys.exit(0)
cores=[]
if MODE=='pilot':cores=[([-1]+[1]*7,'point_defect3'),(fixture(1),'balanced_pd3_m1')];rs=[1,2,4]
else:
    for n in [1,2,3]:
        for word in range(1,(1<<(1<<n))-1):cores.append(([-1 if word>>x&1 else 1 for x in range(1<<n)],f'n{n}_mask{word}'))
    cores.extend((fixture(m),f'balanced_pd3_m{m}') for m in [1,2]);rs=[1,2,3,4,6,8,16,32,64]
rows=[]
for f,name in cores:
    core=hdata(f);profs=profiles(f,core)
    for r in rs:rows.append(case(f,name,r,core,profs))
    if MODE=='full' and len(rows)%90==0:print('CHECKPOINT',len(rows),round(time.perf_counter()-START,2),flush=True)
sequence=[seq(m) for m in [1,2,4,8,16,32]]
result={'status':'PASS','helper_version':'A055-rare-descent-v2','cores':len(cores),'roots':len(rows),'block_candidates':CANDIDATES,'assertions':ASSERTIONS,'elapsed_seconds':time.perf_counter()-START,'precision':'24 atanh terms after exact common-ln2 collection; interval minima, no uncertified numerical argmin','sequence':sequence}
write_name='PILOT' if MODE=='pilot' else 'FULL'
(ROOT/f'out/{write_name}_SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
if MODE=='pilot':chosen=rows
else:chosen=[row for row in rows if row['name'].startswith('balanced') or row['name'] in ['n3_mask1','n2_mask6','n3_mask105']]
(ROOT/f'out/{write_name}_CERTIFICATES.json').write_text(json.dumps(chosen,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='sequence'},indent=2))
for row in chosen[:12]:print(row['name'],row['r'],'phi',row['phi']['display'],'R',row['H_over_I']['display'])
for row in sequence:print('SEQUENCE',row['m'],row['r'],'u_z',row['balancing_R2_price']['display'],'R',row['H_over_I']['display'],'R2fail',row['R2_failure_certified'])
