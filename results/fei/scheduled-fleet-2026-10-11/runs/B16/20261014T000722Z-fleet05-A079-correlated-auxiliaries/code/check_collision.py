import json,time,sys
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
PILOT='--pilot' in sys.argv
CAP=60 if PILOT else 600
old=ROOT.parent/'20261012T044009Z-fleet05-A079-correlated-auxiliaries'/'code'/'check_transport.py'
scope={'__file__':str(ROOT/'code'/'check_collision.py')}
exec(compile(old.read_text().split('for k,m in [(1,1),(2,1)]:')[0],str(old),'exec'),scope)
walsh,H,plus,law,I,rank_dummy=map(scope.get,['walsh','H','plus','law','I','rank'])
START=time.perf_counter();ASSERTIONS=0;COUNTS=Counter();EQUAL=Counter();HIST=Counter()
KAPPA={2:Q(12),3:-Q(9,2)};CSTAR={2:Q(16,3),3:-Q(3,2)}

def check(ok):
    global ASSERTIONS
    ASSERTIONS+=1;assert ok,ASSERTIONS
    if time.perf_counter()-START>CAP:raise RuntimeError('Frozen runtime cap exceeded')

def rank(rows):
    piv={}
    for r in rows:
        while r:
            p=r.bit_length()-1
            if p in piv:r^=piv[p]
            else:piv[p]=r;break
    return len(piv)

@lru_cache(None)
def phase(mask,n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    table=[]
    for x in range(1<<n):
        bit=mask&1
        for i in range(n):bit^=((mask>>(1+i))&1)*((x>>i)&1)
        for z,(i,j) in enumerate(pairs):bit^=((mask>>(1+n+z))&1)*((x>>i)&1)*((x>>j)&1)
        table.append((-1)**bit)
    matrix=[0]*n
    for z,(i,j) in enumerate(pairs):
        if mask>>(1+n+z)&1:matrix[i]^=1<<j;matrix[j]^=1<<i
    return table,rank(matrix)

@lru_cache(None)
def ln_bounds(x):
    z=Q(x-1,x+1);s=Q(0)
    for j in range(120):s+=2*z**(2*j+1)/Q(2*j+1)
    tail=2*z**241/(241*(1-z*z))
    return s,s+tail

@lru_cache(None)
def log_bounds(x):
    a,b=ln_bounds(x);c,d=ln_bounds(2);return a/d,b/c

def enclose(expr):
    lo=hi=Q(0)
    for p,c in expr.items():
        if p==2:a=b=Q(1)
        else:a,b=log_bounds(p)
        lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi

@lru_cache(None)
def cached_certificate(items):
    if not items:return 'equal'
    lo,hi=enclose(dict(items));assert lo>0
    return 'strict'

def certify(expr):
    result=cached_certificate(tuple(sorted(expr.items())))
    check(result in ('equal','strict'))
    return result

def case(n,m0,m1,group):
    g0,r0=phase(m0,n);g1,r1=phase(m1,n);ny=1<<n
    w0,w1=walsh(g0),walsh(g1)
    p0,p1=law(g0),law(g1);G=g0+g1;pw=walsh(G);pg=[Q(w*w,4*ny*ny) for w in pw]
    check(pw==[a+b for a,b in zip(w0,w1)]+[a-b for a,b in zip(w0,w1)])
    check(H(p0)==({2:Q(r0)} if r0 else {}));check(H(p1)==({2:Q(r1)} if r1 else {}))
    mu=Q(sum(a*b for a,b in zip(g0,g1)),ny);d=(1-mu)/2
    check(d==Q(sum(a!=b for a,b in zip(g0,g1)),ny))
    delta=plus((1,H(pg)),(-Q(1,2),H(p0)),(-Q(1,2),H(p1)))
    coreI=(I(p0)+I(p1))/2
    check(I(pg)==coreI+d)
    check(coreI>=Q(r0+r1,4))
    _,rd=phase(m0^m1,n)
    check(abs(r0-r1)<=rd<=r0+r1)
    if mu:check(mu*mu==Q(1,1<<rd))
    S0={i for i,p in enumerate(p0) if p};S1={i for i,p in enumerate(p1) if p}
    if len(S0)>len(S1):S0,S1=S1,S0
    ratio=Q(len(S1),len(S0));u=Q(len(S0&S1),len(S0))
    check(mu*mu<=u*u/ratio)
    if ratio==1:check(delta=={2:2*(1-u)} if u!=1 else delta=={})
    if ratio==4:
        gamma={2:-Q(1),3:Q(9,8)}
        check(delta==plus((1,{2:Q(2)}),(-u,gamma)))
    if ratio==16:
        gamma={2:-Q(2),3:Q(9,32),5:Q(25,32)}
        check(delta==plus((1,{2:Q(2)}),(-u,gamma)))
    e=certify(plus((d,KAPPA),(-1,delta)))
    EQUAL['local_'+e]+=1
    e=certify(plus((I(pg),CSTAR),(-1,H(pg))))
    EQUAL['whole_'+e]+=1
    # Conditional orientation of the physical selector retained explicitly.
    pz=[sum(pg[:ny]),sum(pg[ny:])]
    conditional=plus((1,H(pg)),(-1,H(pz)))
    check(plus((1,conditional),(1,H(pz)))==H(pg))
    COUNTS[group]+=1;HIST[str((n,r0,r1,str(mu),str(ratio),str(u)))]+=1

def receipt():
    out={'status':'PASS','cases':dict(COUNTS),'total_cases':sum(COUNTS.values()),'assertions':ASSERTIONS,'equality_counts':dict(EQUAL),'runtime_seconds':time.perf_counter()-START,'arithmetic':'integer Walsh/Fraction/GF(2) rank/prime-log identities; rational atanh enclosure with 120 terms','independent_review':False}
    (ROOT/'out'/('pilot_validation.json' if PILOT else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n');return out

for n in range(3 if PILOT else 4):
    bits=1+n+n*(n-1)//2
    for m0 in range(0,1<<bits,2):
        for m1 in range(1<<bits):case(n,m0,m1,'exhaustive_n'+str(n))
    receipt()
n=4;bits=1+n+n*(n-1)//2
if not PILOT:
    for j in range(256):case(n,(j*37)% (1<<bits),(j*83+1)% (1<<bits),'targeted_n4')
for m1 in [0,1,1<<(1+4),(1<<(1+4))|(1<<(1+4+5))]:case(4,0,m1,'rank_endpoints_n4')
if not PILOT:
    for j in range(8):case(6,(j*73)% (1<<22),(j*157+32)% (1<<22),'targeted_n6')
# Exact rational/integer certificates used in the analytic case proof.
check(3**5<2**8);check(3**12>2**19);check(5**10>2**23)
check(Q(32,7)<Q(24,5));check(Q(75,16)<Q(24,5))
check(Q(80,31)<Q(44,15));check(Q(481,176)<Q(44,15))
witness={'truth_table':[1,1,1,1,1,1,1,-1],'selector_influence':'1/4','data_influence':'1/2','H':{'log2_2':'4','log2_3':'-9/8'},'selector_decrement':{'log2_2':'3','log2_3':'-9/8'},'sharp_local_ratio':{'log2_2':'12','log2_3':'-9/2'},'sharp_full_ratio':{'log2_2':'16/3','log2_3':'-3/2'},'interpretation':'g0=1, g1=(-1)^(y0*y1); exact actual Boolean collision. No full FEI counterexample.'}
(ROOT/'out'/'sharp_witness.json').write_text(json.dumps(witness,indent=2)+'\n')
(ROOT/'out'/'rank_overlap_histogram.json').write_text(json.dumps(dict(HIST),indent=2)+'\n')
print(json.dumps(receipt(),indent=2))
