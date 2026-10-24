import argparse, hashlib, itertools, json, math, time
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
START=time.perf_counter(); ASSERTIONS=0; LOGS={}; FACTORS={}; LEAVES={}
GRID=1<<80
def check(b):
    global ASSERTIONS
    ASSERTIONS+=1
    assert b
    if time.perf_counter()-START>60: raise RuntimeError('Frozen 60-second limit')
def ln(x):
    z=(x-1)/(x+1); check(0<=z<=Q(1,3)); zz=z*z; p=z; acc=Q(0)
    for j in range(20): acc+=2*p/(2*j+1);p*=zz
    return acc,acc+2*p/(41*(1-zz))
LN2=ln(Q(2))
def log(x):
    if x in LOGS:return LOGS[x]
    e=x.numerator.bit_length()-x.denominator.bit_length(); u=x/Q(2)**e
    while u<1:u*=2;e-=1
    while u>=2:u/=2;e+=1
    a,b=ln(u);a=e+a/LN2[1];b=e+b/LN2[0]
    lo=(a.numerator*GRID)//a.denominator
    hi=-((-b.numerator*GRID)//b.denominator)
    LOGS[x]=(Q(lo,GRID),Q(hi,GRID));return LOGS[x]
def factors(x):
    if x in FACTORS:return FACTORS[x]
    orig=x;d=2;out={}
    while d*d<=x:
        while x%d==0:out[d]=out.get(d,0)+1;x//=d
        d+=1
    if x>1:out[x]=out.get(x,0)+1
    FACTORS[orig]=out;return out
def combine(*pairs):
    out={}
    for p,c in pairs:
        for prime,value in p.items():out[prime]=out.get(prime,Q(0))+c*value
    return {p:v for p,v in out.items() if v}
def entropy(weights,den):
    # All weights are integers; den is a power of two. No log cancellation is numerical.
    out={2:Q(den.bit_length()-1)}
    for w,c in Counter(weights).items():
        if not w:continue
        for prime,e in factors(w).items():out[prime]=out.get(prime,Q(0))-Q(c*w*e,den)
    return {p:v for p,v in out.items() if v}
def interval(p):
    lo=hi=Q(0)
    for prime,c in p.items():
        a,b=log(Q(prime));lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
    return lo,hi
def fwht(v):
    a=list(v);h=1
    while h<len(a):
        for base in range(0,len(a),2*h):
            for j in range(base,base+h):u,w=a[j],a[j+h];a[j]=u+w;a[j+h]=u-w
        h*=2
    return a
def physical(v,coords):
    return Q(sum(v[x]!=v[x^(1<<i)] for i in coords for x in range(len(v))),len(v))
def info(v,need_u=False):
    n=len(v).bit_length()-1;a=fwht(v);den=len(v)**2
    check(sum(c*c for c in a)==den)
    out={'a':a,'H':entropy([c*c for c in a],den),'I':Q(sum(s.bit_count()*c*c for s,c in enumerate(a)),den)}
    if need_u:
        top=[s.bit_count() if c else -1 for s,c in enumerate(a)]
        for i in range(n):
            for s in range(len(a)):
                if not s&(1<<i):top[s]=max(top[s],top[s|(1<<i)])
        out['U']=Q(sum(c*c*(top[s]-s.bit_count()) for s,c in enumerate(a) if s and c),den)
    return out
def leaf(v):
    key=tuple(v)
    if key not in LEAVES:LEAVES[key]=info(v,True)
    return LEAVES[key]
def seed_values(m,code):return [1 if (code>>x)&1 else -1 for x in range(1<<m)]
def masks(m,r):
    domain=[()]+[(z,) for z in range(1<<r)]+list(itertools.combinations(range(1<<r),2))
    yield from itertools.product(domain,repeat=1<<m)
def presets(m,r,j):
    out=[]
    for x in range(1<<m):
        a=x.bit_count()&1
        d1=(not(x&1)) if j==3 else True
        d2=(not(x&2)) if j==3 else not(x&1)
        b=[a,a^1,x&3,a][j]
        # Sequential XOR: coincident event assignments cancel exactly.
        fiber=set()
        if d1:fiber.symmetric_difference_update([a])
        if d2:fiber.symmetric_difference_update([b])
        out.append(tuple(sorted(fiber)))
    return tuple(out)
def targeted():
    seeds=[('constant',3,[1]*8),('dictator',3,[1 if not(x&1) else -1 for x in range(8)]),
           ('Maj3',3,[1 if x.bit_count()<=1 else -1 for x in range(8)]),('pointdefect',3,[-1]+[1]*7),
           ('bent',4,[(-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1))) for x in range(16)]),
           ('address2',6,[(-1)**((x>>(2+(x&3)))&1) for x in range(64)])]
    for name,m,g in seeds:
        for r in [3,4]:
            for j in range(4):yield name,m,r,g,presets(m,r,j),2
def domain(mode):
    if mode=='pilot':
        for m,g in [(0,[1]),(1,[1,-1]),(2,[-1,1,1,1])]:
            for j in range(4):yield 'pilot',m,3,g,presets(m,3,j),2
        return
    for m in [0,1]:
        for code in range(1<<(1<<m)):
            for fibers in itertools.product([()]+[(z,) for z in range(4)],repeat=1<<m):
                yield 'all_graph',m,2,seed_values(m,code),fibers,1
    for code in range(4):
        for fs in masks(1,3):yield 'all_m1_fibers',1,3,seed_values(1,code),fs,2
    points=range(32)
    for code in range(16):
        for es in itertools.chain([()],((x,) for x in points),itertools.combinations(points,2)):
            fs=[[] for _ in range(4)]
            for point in es:fs[point&3].append(point>>2)
            yield 'all_m2_two_points',2,3,seed_values(2,code),tuple(tuple(x) for x in fs),2
    yield from targeted()

def early(v,m,r):
    s=info(v,True)
    if s['U']<=s['I'] or r==0:
        return s['H'],s['I'],Q(0),s['U']<=s['I']
    half=len(v)//2
    a,b=early(v[:half],m,r-1),early(v[half:],m,r-1)
    spent=physical(v,[m+r-1])+(a[2]+b[2])/2
    return combine((a[0],Q(1,2)),(b[0],Q(1,2))),(a[1]+b[1])/2,spent,a[3] and b[3]

def verify(case):
    name,m,r,g,fs,k=case;size=1<<(m+r);den=size*size
    edit={x+(z<<m) for x,f in enumerate(fs) for z in f}
    v=[g[x&((1<<m)-1)]*(-1 if x in edit else 1) for x in range(size)]
    mask=[-1 if x in edit else 1 for x in range(size)]
    s=info(v);a=s['a']; iz=physical(v,range(m,m+r));ix=physical(v,range(m))
    check(s['I']==iz+ix)
    check(iz==Q(sum((j>>m).bit_count()*c*c for j,c in enumerate(a)),den))
    rho=Q(len(edit),size);epsilon=Q(sum(bool(f) for f in fs),1<<m)
    alpha=Q(sum(c*c for j,c in enumerate(a) if j>>m),den)
    check(alpha==sum(4*Q(len(f),1<<r)*(1-Q(len(f),1<<r)) for f in fs)/(1<<m))
    check(alpha<=4*rho<=1)
    maskix=physical(mask,range(m));check(ix>=maskix)
    rowweights=[sum(a[t+(z<<m)]**2 for z in range(1<<r)) for t in range(1<<m)]
    marginal=entropy(rowweights,den); le=[leaf(v[z*(1<<m):(z+1)*(1<<m)]) for z in range(1<<r)]
    leafh=combine(*[(x['H'],Q(1,1<<r)) for x in le]);leafi=sum(x['I'] for x in le)/(1<<r)
    check(leafi==ix)
    # Independent physical Parseval for each row, from actual restricted truth tables.
    for t,weight in enumerate(rowweights):check(Q(weight,den)==sum(Q(x['a'][t]**2,1<<(2*m)) for x in le)/(1<<r))
    bm=combine((s['H'],1),(marginal,-1));jm=combine((marginal,1),(leafh,-1));qm=combine((s['H'],1),(leafh,-1))
    check(not combine((qm,1),(bm,-1),(jm,-1)))
    b,j,q=interval(bm),interval(jm),interval(qm)
    kl=Q(4*r,r-(0 if k==1 else 1))+2/LN2[1]
    check(j[1]<=2*iz/LN2[1])
    check(b[1]<=Q(4*r,r-(0 if k==1 else 1))*iz+2*ix)
    margin=kl*iz+2*ix-q[1];check(margin>=0)
    check(iz>=2*rho*(r-(0 if k==1 else 1)))
    if epsilon:
        logeps=log(1/epsilon)
        check(ix>=2*rho*logeps[1])
    admitted=all(x['U']<=x['I'] for x in le)
    if admitted:check(interval(s['H'])[1]<=max(kl,Q(6))*(iz+ix))
    if name in ['pilot','constant','dictator','Maj3','pointdefect','bent','address2']:
        eh,ei,spent,early_admitted=early(v,m,r)
        check(s['I']==spent+ei)
        eq=interval(combine((s['H'],1),(eh,-1)))
        check(eq[1]<=kl*(iz)+2*ix)
        if early_admitted:check(interval(s['H'])[1]<=kl*spent+(kl+4)*ei)
    return margin,admitted,{'family':name,'m':m,'r':r,'seed':g,'fibers':fs,'rho':rho,'epsilon':epsilon,'I_controls':iz,'I_core':ix,'I_core_mask':maskix,'Q':q,'B':b,'J':j,'full_U_leaves':admitted}

def enc(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [enc(v) for v in x]
    return x
def fixed_certificates():
    lower=Q(4*127,128)*(1-Q(1,1<<128))*Q(842,1215)
    check(lower>Q(11,4))
    g=[1,-1];mask=[-1,1,1,-1];f=[g[x&1]*mask[x] for x in range(4)]
    check(physical(f,[0])==0 and physical(mask,[0])==1)
    # Root-only two-bit tree length: 1 at empty, 3 otherwise.
    e1=[-2,0,0,0];e2=[0,2,0,0]
    aa,bb=fwht(e1),fwht(e2)
    cross=Q(sum(aa[s]*bb[s]*(1 if s==0 else 3) for s in range(4)),16)
    check(cross==Q(1,2))
    return {'A066_n128_lower_rate':lower,'ownership_cap_counterexample':{'g':g,'mask':mask,'F':f},'A070_disjoint_edit_cross':cross}
def main():
    mode=argparse.ArgumentParser();mode.add_argument('mode',choices=['pilot','full']);args=mode.parse_args()
    count=0;admitted=0;minimum=None;rows=[];digest=hashlib.sha256();families=Counter()
    for case in domain(args.mode):
        margin,yes,row=verify(case);count+=1;admitted+=yes;families[case[0]]+=1
        digest.update(json.dumps(enc(row),sort_keys=True).encode())
        if minimum is None or (margin>0 and (minimum['margin']==0 or margin<minimum['margin'])):minimum={'margin':margin,'case':row}
        if case[0] in ['pilot','constant','dictator','Maj3','pointdefect','bent','address2']:rows.append(row)
    check(count==(12 if args.mode=='pilot' else 14098))
    result={'complete':True,'mode':args.mode,'case_count':count,'families':dict(families),'admitted_complete_trees':admitted,
            'assertions':ASSERTIONS,'elapsed_seconds':time.perf_counter()-START,'arithmetic':'integer transforms and prime-log maps; 20-term rigorous intervals rounded outward to 2^-80',
            'domain_digest':digest.hexdigest(),'minimum_positive_reserve_margin':minimum,'fixed_certificates':fixed_certificates(),'targeted_rows':rows}
    result['assertions']=ASSERTIONS
    (ROOT/'out'/('CHECK_'+args.mode.upper()+'.json')).write_text(json.dumps(enc(result),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in enc(result).items() if k not in ['targeted_rows','minimum_positive_reserve_margin']}))
if __name__=='__main__':main()
