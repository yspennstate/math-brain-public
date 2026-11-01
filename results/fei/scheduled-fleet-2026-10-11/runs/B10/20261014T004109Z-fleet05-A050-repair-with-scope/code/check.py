"""A050 active-label v1. Log-vector primitives independently copied from own stage2.
Every joint is rebuilt from exact coherent kernels, not from reported MI formulas.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from collections import defaultdict
import time,json,sys
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); COUNT=0; CASES=0
PILOT='--pilot' in sys.argv
LIMIT=60 if PILOT else 300
def ck(ok):
    global COUNT
    assert ok
    COUNT+=1
    if time.perf_counter()-START>LIMIT:raise RuntimeError('frozen watchdog')
@lru_cache(None)
def factor(n):
    d={};i=2
    # A residual integer is a valid logarithm atom; primality is unnecessary.
    # Do not spend shared-machine time factoring large marginal numerators.
    while i*i<=n and i<=97:
        while n%i==0:d[i]=d.get(i,0)+1;n//=i
        i+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def ent(ps):
    out={}
    for p in ps:
        if not p:continue
        for n,s in [(p.numerator,-1),(p.denominator,1)]:
            for prime,k in factor(n).items():out[prime]=out.get(prime,F(0))+s*p*k
    return {p:v for p,v in out.items() if v}
def add(*vs):
    d={}
    for v in vs:
        for p,x in v.items():d[p]=d.get(p,F(0))+x
    return {p:x for p,x in d.items() if x}
def scale(v,a):return {p:a*x for p,x in v.items() if a*x}
@lru_cache(None)
def ln(x):
    z=(x-1)/(x+1)
    lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
    return lo,lo+2*z**65/(65*(1-z*z))
LN2=ln(F(2))
@lru_cache(None)
def log(x):
    x=F(x);k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    lo,hi=ln(x);v=[a/b for a in (lo,hi) for b in LN2]
    grid=1<<256
    lo=(min(v)+k)*grid;hi=(max(v)+k)*grid
    return F(lo.numerator//lo.denominator,grid),F(-((-hi).numerator//(-hi).denominator),grid)
def bounds(v):
    lo=hi=F(0)
    for p,x in v.items():
        a,b=log(p)
        if x<0:a,b=b,a
        lo+=x*a;hi+=x*b
    return lo,hi
def nonneg(v):ck(not v or bounds(v)[0]>=0)
def serial(v):return {str(p):str(x) for p,x in v.items()}
@lru_cache(None)
def stats(t):
    n=len(t).bit_length()-1;a=list(t);step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step):u,v=a[k],a[k+step];a[k],a[k+step]=u+v,u-v
        step*=2
    mass={s:F(x*x,len(t)**2) for s,x in enumerate(a) if x}
    inf=tuple(sum((v for s,v in mass.items() if s>>i&1),F(0)) for i in range(n))
    ck(sum(mass.values())==1)
    return mass,inf,F(t.count(-1),len(t))
@lru_cache(None)
def split(t,i,b):
    return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))
def embed(s,coords):return sum(1<<i for j,i in enumerate(coords) if s>>j&1)
def build(t,coords,policy,depth=0,path=(),q=0):
    mass,inf,neg=stats(t)
    essential=[j for j,x in enumerate(inf) if x]
    if policy in ('ctrl','fixedctrl','common'):
        choices=[j for j,i in enumerate(coords) if i<3 and (policy=='fixedctrl' or inf[j])]
        if policy=='common':choices=[j for j,i in enumerate(coords) if i==0]
    elif policy=='prefix':choices=[j for j,i in enumerate(coords) if i<2 and inf[j]]
    elif policy=='partial':choices=essential if depth<1 else []
    elif policy=='adaptive':
        if depth>=2:choices=[]
        elif not path:choices=[0] if coords else []
        else:
            target=1 if path[0][1]==0 else 2
            choices=[j for j,i in enumerate(coords) if i==target]
    elif policy=='indexed':
        r,k=INDEXED
        if depth<r:target=depth*k
        elif depth==r:target=r*k+sum(b<<j for j,(_,b) in enumerate(path))
        else:target=-1
        choices=[j for j,i in enumerate(coords) if i==target]
    else:choices=essential
    node={'P':{embed(s,coords):v for s,v in mass.items()},'I':sum(inf,F(0)),
          'IA':sum((v for j,v in enumerate(inf) if coords[j] in ACTIVE),F(0)),
          'neg':neg,'path':path,'Q':q,'coords':coords}
    if not choices:
        node['children']=[];return node
    j=choices[0];i=coords[j];node['i']=i
    node['children']=[build(split(t,j,b),coords[:j]+coords[j+1:],policy,depth+1,path+((i,b),),q|(1<<i)) for b in (0,1)]
    return node
def evaluate(t,policy,active,name=None):
    global CASES,ACTIVE
    ACTIVE=set(active);n=len(t).bit_length()-1
    tree=build(t,tuple(range(n)),policy);leaves=[]
    def visit(v,w):
        if not v['children']:v['id']=len(leaves);v['reach']=w;leaves.append(v)
        else:
            for c in v['children']:visit(c,w/2)
    visit(tree,F(1))
    joint=defaultdict(F)
    def lift(v,s,wgt,current):
        if not v['children']:
            ck(current==s&~v['Q']);joint[(s,v['id'],current,s&v['Q'])]+=wgt;return
        i=v['i'];retained=current&~(1<<i)
        q=v['P'].get(retained,F(0))+v['P'].get(retained|(1<<i),F(0))
        ck(q>0)
        for c in v['children']:
            b=c['P'].get(retained,F(0))/(2*q)
            if b:lift(c,s,wgt*b,retained)
    for s,p in tree['P'].items():lift(tree,s,p,s)
    ck(sum(joint.values())==1)
    def marginal(indices):
        d=defaultdict(F)
        for key,p in joint.items():d[tuple(key[i] for i in indices)]+=p
        return d
    HS=ent(marginal((0,)).values());HW=ent(marginal((2,)).values())
    HP=ent(marginal((1,)).values())
    e=add(ent(marginal((0,3)).values()),scale(HS,-1))
    j=add(HS,HP,scale(ent(marginal((0,1)).values()),-1))
    jw=add(HW,HP,scale(ent(marginal((1,2)).values()),-1))
    ck(e==add(ent(marginal((0,2)).values()),scale(HS,-1)))
    nonneg(add(j,e,scale(jw,-1)))
    rootI=tree['I'];a=tree['IA'];leafI=sum((v['reach']*v['I'] for v in leaves),F(0))
    leafIA=sum((v['reach']*v['IA'] for v in leaves),F(0));R=rootI-leafI
    ck(a-R==leafIA)
    ck(sum((p*key[3].bit_count() for key,p in joint.items()),F(0))==R)
    ck(sum((p*(key[0]&sum(1<<i for i in active)).bit_count() for key,p in joint.items()),F(0))==a)
    ml=marginal((1,2))
    for v in leaves:
        for s,p in v['P'].items():ck(ml.get((v['id'],s),F(0))==v['reach']*p)
        ck(sum((p for (s,l,w,d),p in joint.items() if l==v['id']),F(0))==v['reach'])
    theta=R/a if a else F(0)
    capacity=scale(ent((theta,1-theta)),a)
    nonneg(add(capacity,scale(e,-1)))
    if R==0 or R==a:ck(not e)
    if policy in ('ctrl','fixedctrl','prefix'):ck(leafIA==0 and not e)
    hi=bounds(j)[1];ck(hi*LN2[1]<=2*R or not j)
    # Normalization of the ONE deletion reference by exact binomial expansion.
    for s in tree['P']:
        k=(s&sum(1<<i for i in active)).bit_count()
        from math import comb
        ck(sum((F(comb(k,h))*theta**h*(1-theta)**(k-h) for h in range(k+1)),F(0))==1)
    # Physical output information and explicit signed conversion.
    output=ent((tree['neg'],1-tree['neg']))
    o=add(output,scale(add(*(scale(ent((v['neg'],1-v['neg'])),v['reach']) for v in leaves)),-1))
    nonneg(add({2:R},scale(o,-1)))
    gamma=add(jw,scale(o,-1))
    # Conditional bank identity Gamma=j_W-o is checked using joint output law.
    yp=[]
    for v in leaves:yp.extend((v['reach']*v['neg'],v['reach']*(1-v['neg'])))
    cy=add(ent(yp),scale(output,-1));cw=add(ent(ml.values()),scale(HW,-1))
    ck(gamma==add(cy,scale(cw,-1)))
    CASES+=1
    if CASES%100==0:
        (ROOT/'out'/'CHECKPOINT.json').write_text(json.dumps({'cases':CASES,'seconds':time.perf_counter()-START,'assertions':COUNT}),encoding='utf-8')
    if name:return {'name':name,'a':str(a),'R':str(R),'terminal_I':str(leafI),'terminal_active_I':str(leafIA),
                   'active_injection_vector':serial(e),'capacity_vector':serial(capacity),
                   'root_information_vector':serial(j),'descendant_information_vector':serial(jw),
                   'output_information_vector':serial(o),'leaf_query_sets':sorted(set(v['Q'] for v in leaves)),
                   'joint_atoms':len(joint),'normalization_and_marginals':'EXACT'}
fixtures=[];roots=0
for n in range(4):
    for mask in range(1<<(1<<n)):
        if PILOT and roots>=12:break
        t=tuple(1-2*(mask>>x&1) for x in range(1<<n));roots+=1
        for policy in ('complete','partial','adaptive','prefix'):
            evaluate(t,policy,range(min(n,2)) if policy=='prefix' else range(n))
if not PILOT:
    for gm in range(16):
        for hm in range(16):
            t=[]
            for x in range(32):
                s,a,b=x&1,x>>1&1,x>>2&1;y=x>>3
                t.append(1 if not s else 1-2*(gm>>y&1) if a else 1-2*(hm>>y&1) if b else 1)
            for pol in ('ctrl','fixedctrl','common'):
                name=f'shared-data-{gm}-{hm}-{pol}' if gm==6 and hm==8 else None
                q=evaluate(tuple(t),pol,range(3),name)
                if q:fixtures.append(q)
    for r,k in ((1,2),(2,2),(3,2)):
        INDEXED=(r,k);n=r*k+(1<<r);t=[]
        for x in range(1<<n):
            sign=(-1)**((x>>(r*k)).bit_count())
            for z in range(r):
                if (x>>(z*k))&((1<<k)-1)==(1<<k)-1:sign=-sign
            t.append(sign)
        q=evaluate(tuple(t),'indexed',list(range(0,r*k,k))+list(range(r*k,n)),f'indexed-r{r}-k{k}')
        d=F(1,2**(k-1));p=d;v=4*p*(1-p)
        jk=add(ent((v/2,1-v/2)),scale(ent((v,1-v)),F(-1,2)))
        ck(q['active_injection_vector']==serial(add({2:F(r)},scale(jk,-r))))
        ck(q['a']==str((1<<r)+r*d) and q['R']==str(1+r*d))
        fixtures.append(q)
out={'status':'PASS','helper_version':'A050-active-label-v1.2','mode':'pilot' if PILOT else 'main',
     'cases':CASES,'all_small_roots':roots,'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,
     'arithmetic':'Fraction joint kernels; integer-log entropy identities; 32-term rational atanh intervals rounded outward to 2^-256',
     'cache_states':stats.cache_info().currsize}
if not PILOT:ck(CASES==1883)
(ROOT/'out'/('PILOT.json' if PILOT else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
if not PILOT:(ROOT/'out'/'FIXTURES.json').write_text(json.dumps(fixtures,indent=2),encoding='utf-8')
print(json.dumps(out))
