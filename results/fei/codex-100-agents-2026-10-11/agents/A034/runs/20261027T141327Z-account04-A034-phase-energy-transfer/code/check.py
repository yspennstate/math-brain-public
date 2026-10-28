from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
from math import isqrt
import importlib.util,itertools,json,time,hashlib,sys
RUN=Path(__file__).resolve().parents[1]
OLD=RUN.parent/'20261026T214048Z-account04-A034-phase-energy-transfer/code/check.py'
spec=importlib.util.spec_from_file_location('old_defs',OLD);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
START=time.monotonic();CHECKS=0
def need(v,msg):
    global CHECKS
    CHECKS+=1
    if not v:raise AssertionError(msg)
    if time.monotonic()-START>55:raise TimeoutError('frozen runtime55s')

@lru_cache(None)
def entropy_atom(a):
    p=Q(a)**2
    if not p:return Q(0),Q(0)
    assert p<=1
    l,h=old.logint(1/p)
    return p*l,p*h

def sqrt_interval(a):
    a=Q(a);assert a>=0
    D=10**60;n=isqrt(a.numerator*D*D//a.denominator)
    lo=Q(n,D);hi=lo if lo*lo==a else Q(n+1,D)
    assert lo*lo<=a<=hi*hi
    return lo,hi

def scalar_test(a):
    assert sum(map(abs,a))<=1
    B=entropy_atom(sum(a));parts=[entropy_atom(x) for x in a]
    lo=sum(sqrt_interval(p[0])[0] for p in parts)
    # The singleton nonzero case is an exact identity; do not certify by overlapping intervals.
    if sum(bool(x) for x in a)<=1:need(B==next((p for x,p in zip(a,parts) if x),(Q(0),Q(0))),'one coefficient identity')
    else:need(B[1]<=2*lo*lo,'signed scalar factor2 with rigorous intervals')
    if sum(map(abs,a))<=Q(1,2):
        if sum(bool(x) for x in a)<=1:need(True,'rare identity')
        else:need(B[1]<=lo*lo,'rare scalar factor1 with rigorous intervals')

def scalar():
    counts={};total=0
    for k,m,expected in [(1,16,33),(2,16,545),(3,12,2625),(4,8,3649)]:
        count=0
        for xs in itertools.product(range(-m,m+1),repeat=k):
            if sum(map(abs,xs))>m:continue
            scalar_test(tuple(Q(x,m) for x in xs));count+=1
        need(count==expected,'frozen scalar lattice count');counts[f'{k}/{m}']=count;total+=count
    need(total==6852,'all scalar cases')
    return dict(cases=total,domains=counts)

def sharpness():
    ratios=[]
    for k in range(2,65):
        eps=Q(1,1<<k);a=1-eps;b=-eps;scalar_test((a,b))
        target=entropy_atom(a+b);pa=entropy_atom(a);pb=entropy_atom(b)
        dlow=(sqrt_interval(pa[0])[0]+sqrt_interval(pb[0])[0])**2
        dhigh=(sqrt_interval(pa[1])[1]+sqrt_interval(pb[1])[1])**2
        lo,hi=target[0]/dhigh,target[1]/dlow
        need(hi<2,'strict scalar ratio below2')
        if k==64:need(lo>Q(199,100),'factor2 cannot be replaced by1.99 on this actual scalar tuple')
        if k in (2,8,16,32,64):ratios.append(dict(k=k,ratio_lower=str(lo),ratio_upper=str(hi)))
    a=Q(1);b=-Q(1,16);target=entropy_atom(a+b)
    rhs_hi=2*(sqrt_interval(entropy_atom(a)[1])[1]+sqrt_interval(entropy_atom(b)[1])[1])**2
    need(abs(a)+abs(b)>1 and target[0]>rhs_hi,'REAL negative control: l1 hypothesis necessary')
    return dict(cases=63,selected_ratio_intervals=ratios,missing_l1_control='FAILS as required')

def bill(v):
    N=len(v);counts=Counter(old.walsh(v));lo=hi=Q(0)
    for w,c in counts.items():
        a,b=entropy_atom(Q(w,N));lo+=c*a;hi+=c*b
    return lo,hi

def dense():
    n=14;N=1<<n;ks=[1,12,13,14];cases=0;max_groups=0
    # Frozen affine cells: prefix1^(k-1)0; intrinsic quadratic is global y12*y13.
    supports=[[y for y in range(N) if y&((1<<k)-1)==(1<<(k-1))-1] for k in ks]
    for signs in itertools.product((-1,1),repeat=4):
        for phase in (0,1):
            pieces=[]
            for support,sign in zip(supports,signs):
                v=[0]*N
                for y in support:v[y]=sign*(-1 if phase and (y>>12&1) and (y>>13&1) else 1)
                pieces.append(v)
            gs=old.groups(pieces);need(len(gs)==2,'actual unequal-four-cell geometry has2 mass groups')
            u=[sum(a) for a in zip(*pieces)];mu=Q(sum(x*x for x in u),N)
            eu=old.influences(u);eg=[old.influences(g) for g in gs]
            for i,e in enumerate(eu):need(11*e>=6*sum(v[i] for v in eg),'strong6/11 physical energy comparison')
            Bs=[bill(g) for g in gs];Bu=bill(u)
            squaresum=sum(sqrt_interval(x[0])[0] for x in Bs)**2
            need(Bu[1]<=2*squaresum,'new dimension-independent coherent group payment')
            E=sum(eu);need(Bu[1]<=Q(341,3)*E,'proper-four full rate341/3<114')
            # Fresh physical halfcube activation, exactly, without a new dense dimension.
            Bactive=Bu[1]/2+mu;Eactive=E/2+mu/4
            activeparts=[(b[0]/2+Q(sum(x*x for x in g),N)) for b,g in zip(Bs,gs)]
            need(Bactive<=sum(sqrt_interval(x)[0] for x in activeparts)**2,'rare coherent factor1 after actual activation')
            need(Bactive<=Q(341,6)*Eactive,'rare-four full rate341/6<57')
            cases+=1;max_groups=max(max_groups,len(gs))
    need(cases==32,'frozen dense cases')
    return dict(cases=cases,nY=14,mass_groups=max_groups,rare_activation='exact physical halfcube identity')

def shifted_corr(a,b,i):
    # Independent bit-mask implementation; no dictionaries and no dense Walsh table.
    ka,la,sa=a;kb,lb,sb=b
    ma=(1<<ka)-1;mb=(1<<kb)-1;va=(1<<(ka-1))-1;vb=((1<<(kb-1))-1)^((1<<i)&mb)
    if (va^vb)&(ma&mb):return Q(0)
    fixed=ma|mb;values=va|vb;linear=la^lb
    if linear&~fixed:return Q(0)
    sign=sa*sb*(-1 if (lb>>i&1)^((linear&values).bit_count()&1) else 1)
    return Q(sign,1<<fixed.bit_count())

def energy(cells,i):
    mu=sum((Q(1,1<<a[0]) for a in cells),Q(0))
    return (mu-sum((shifted_corr(a,b,i) for a in cells for b in cells),Q(0)))/2

def symbolic():
    cases=0;seen=set()
    for ks in ([1,12,23,34],[1,2,14,25],[1,2,14,15],[1,2,3,4]):
        for signs in itertools.product((-1,1),repeat=4):
            for pat in range(4):
                cells=[]
                for t,(k,sgn) in enumerate(zip(ks,signs)):
                    mask=((1<<35) if pat&1 else 0)^((1<<((t*7+3)%36)) if pat&2 else 0)
                    cells.append((k,mask,sgn))
                groups=[];prev=None
                for a in cells:
                    if prev is None or a[0]-prev>10:groups.append([])
                    groups[-1].append(a);prev=a[0]
                seen.add(len(groups))
                for i in range(36):
                    es=[energy(g,i) for g in groups];e=energy(cells,i)
                    need(e>=0 and all(v>=0 for v in es),'physical energy nonnegative')
                    need(11*e>=6*sum(es),'independent exact6/11 group domination')
                cases+=1
    need(cases==256 and seen=={1,2,3,4},'all frozen physical mass-group cases')
    return dict(cases=cases,nY=36,groups=sorted(seen))

def compositions(s):
    if s==0:yield []
    else:
        for first in range(1,s+1):
            for tail in compositions(s-first):yield [first]+tail

def boundaries():
    cases=0
    for s in range(1,13):
        for ms in compositions(s):
            need(sum(m-1 for m in ms)==s-len(ms),'piece-count conservation')
            need(all((1<<(m-1))>=m for m in ms),'integer log2(m)<=m-1')
            if s>=2 and len(ms)>=2:
                # A>=9>C, so replacing q by2 can only enlarge (s-q)A+qC.
                need((s-len(ms))*9+len(ms)*Q(9,2)<=(s-2)*9+9,'q elimination')
            cases+=1
    for e,a,total in itertools.product(range(4),repeat=3):
        if 9*a<=16*e and 32*total<=33*a:need(6*total<=11*e,'exact common-denominator rounding')
    # Activation identity independently at one explicit tiny physical row.
    v=[1,0,-1,1];activated=[x if z==0 else 0 for z in range(2) for x in v]
    mu=Q(sum(x*x for x in v),len(v))
    need(bill(activated)[0]==bill(v)[0]/2+mu,'activation entropy normalization')
    need(sum(old.influences(activated))==sum(old.influences(v))/2+mu/4,'activation influence normalization')
    need(cases==4095,'all ordered compositions up to12')
    return dict(compositions=cases,rounding_domain=64)

if __name__=='__main__':
    mode=sys.argv[1];result=globals()[mode]()
    result.update(status='PASS',mode=mode,assertions=CHECKS,seconds=time.monotonic()-START,
                  helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  prior_definition_sha256=hashlib.sha256(OLD.read_bytes()).hexdigest())
    (RUN/'out').mkdir(exist_ok=True)
    (RUN/'out'/f'{mode}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='selected_ratio_intervals'}))
