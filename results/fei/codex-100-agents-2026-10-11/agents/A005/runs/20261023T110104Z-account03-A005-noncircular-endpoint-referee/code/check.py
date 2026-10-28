from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools,json,sys,time
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();count=0
stats={'base_roots':0,'activation_roots':0,'first_queries':0,'branch_reset_query_options':0,'combined_policies_by_separability':0}
def ck(b):
    global count
    assert b
    count+=1
    if time.perf_counter()-start>55:raise RuntimeError('frozen55s cap')
def fw(a):
    a=list(a);k=1
    while k<len(a):
        for j in range(0,len(a),2*k):
            for i in range(j,j+k):
                x,y=a[i],a[i+k];a[i],a[i+k]=x+y,x-y
        k*=2
    return a
def dot(a,b):return (a&b).bit_count()%2
def rank(vs):
    span={0}
    for v in vs:span|={x^v for x in list(span)}
    return len(span).bit_length()-1
@lru_cache(None)
def factors(n):
    out={};d=2
    while d*d<=n:
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def add(*args):
    o={}
    for a in args:
        for k,v in a.items():o[k]=o.get(k,F(0))+v
    return {k:v for k,v in o.items() if v}
def mul(c,a):return {k:c*v for k,v in a.items() if c*v}
def logvec(q):
    q=F(q);o=dict(factors(q.numerator))
    for k,v in factors(q.denominator).items():o[k]=o.get(k,0)-v
    return {k:F(v) for k,v in o.items() if v}
def entropy_mass(q):return {} if not q else mul(-q,logvec(q))
def lnunit(x):
    y=(x-1)/(x+1);n=24
    lo=2*sum((y**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
    return lo,lo+2*y**(2*n+1)/(F(2*n+1)*(1-y*y))
LN2=lnunit(F(2))
@lru_cache(None)
def logprime(p):
    x=F(p);s=0
    while x>2:x/=2;s+=1
    lo,hi=lnunit(x)
    return s+lo/LN2[1],s+hi/LN2[0]
@lru_cache(None)
def bounds_tuple(t):
    lo=hi=F(0)
    for p,c in t:
        l,h=logprime(p)
        lo+=c*(l if c>=0 else h);hi+=c*(h if c>=0 else l)
    return lo,hi
def bounds(h):return bounds_tuple(tuple(sorted(h.items())))
@lru_cache(None)
def phi(a):
    if not a:return F(0),F(0)
    h=add(entropy_mass(a),entropy_mass(1-a));lo,hi=bounds(h)
    return lo+2*a/LN2[1],hi+2*a/LN2[0]
@lru_cache(None)
def profile(a):
    n=len(a);d=n.bit_length()-1;w=fw(a);sq=[v*v for v in w];den=n*n
    h=add(*(entropy_mass(F(v,den)) for v in sq if v))
    ps=[F(sum(v for s,v in enumerate(sq) if (s>>j)&1),den) for j in range(d)]
    corr=fw(sq);cost=[min(F(den-c,2*den),F(den+c,2*den)) for c in corr]
    err=F(n-max(abs(x) for x in w),2*n)
    return {'H':h,'I':sum(ps,F(0)),'ps':ps,'e':err,'m':cost,'w':w}
def child(a,i,b):
    return tuple(a[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(a)//2))
@lru_cache(None)
def canonical(a):
    pr=profile(a);n=len(a);d=n.bit_length()-1
    rows=[]
    for v in sorted(range(1,n),key=lambda v:(pr['m'][v],v)):
        if rank(rows+[v])>len(rows):rows.append(v)
        if len(rows)==d:break
    den=n*n;sq=[v*v for v in pr['w']]
    center=[int(sum(c for s,c in enumerate(sq) if dot(v,s))>den//2) for v in rows]
    outw=[0]*n
    for s,c in enumerate(pr['w']):
        u=sum((dot(v,s)^b)<<j for j,(v,b) in enumerate(zip(rows,center)))
        outw[u]=c
    out=fw(outw);ck(all(x%n==0 for x in out));out=tuple(x//n for x in out)
    ck(all(abs(x)==1 for x in out));ck(profile(out)['H']==pr['H']);ck(profile(out)['e']==pr['e']);ck(profile(out)['I']<=pr['I'])
    return out
@lru_cache(None)
def smallorbit(a):
    d=len(a).bit_length()-1;n=len(a)
    out=set()
    for rows in itertools.permutations(range(1,n),d):
        if rank(rows)!=d:continue
        for shift in range(n):
            for c in range(n):
                aa=tuple(a[sum(dot(row,x)<<j for j,row in enumerate(rows))^shift]*(-1)**dot(c,x) for x in range(n))
                for sign in [1,-1]:
                    b=tuple(sign*x for x in aa)
                    if profile(b)['I']<=profile(a)['I']:out.add(b)
    if not out:out.add(a)
    return tuple(sorted(out))
def resetoptions(a,exhaust):
    if exhaust:return smallorbit(a)
    out={a,canonical(a)}
    d=len(a).bit_length()-1
    if d>=2:
        # An actual mixed-coordinate shear, retained only if nonincreasing.
        b=tuple(a[x^(((x>>(d-1))&1))] for x in range(len(a)))
        if profile(b)['I']<=profile(a)['I']:out.add(b)
    return tuple(out)
def validate_root(a,exhaust):
    pr=profile(a);d=len(a).bit_length()-1;a0=min(2*pr['e'],F(1,2));budget=phi(a0)[0]
    ck(all(x<=2*pr['e'] for x in pr['m']))
    for i in range(d):
        stats['first_queries']+=1
        children=[child(a,i,b) for b in [0,1]];cp=[profile(x) for x in children]
        ck(sum(x['e'] for x in cp)/2<=pr['e'])
        ck(sum(x['I'] for x in cp)/2==pr['I']-pr['ps'][i])
        L=add(pr['H'],mul(-F(1,2),add(*(x['H'] for x in cp))))
        m=min(pr['ps'][i],1-pr['ps'][i])
        ck(bounds(L)[1]<=phi(m)[0])
        maxima=[];maxm=[];optioncounts=[]
        for a1,p1 in zip(children,cp):
            losses=[F(0)];ms=[F(0)];options=0
            for reset in resetoptions(a1,exhaust):
                p2=profile(reset)
                ck(p2['H']==p1['H'] and p2['e']==p1['e'] and p2['I']<=p1['I'])
                # Stop is a complete valid frontier.
                options+=1
                for j in range(len(reset).bit_length()-1):
                    options+=1
                    leaves=[child(reset,j,b) for b in [0,1]];lp=[profile(x) for x in leaves]
                    ee=sum(x['e'] for x in lp)/2;ii=sum(x['I'] for x in lp)/2
                    ck(ee<=p2['e']);ck(ii==p2['I']-p2['ps'][j])
                    ll=add(p1['H'],mul(-F(1,2),add(*(x['H'] for x in lp))))
                    mm=min(p2['ps'][j],1-p2['ps'][j]);ck(mm<=2*p2['e'])
                    ck(bounds(ll)[1]<=phi(mm)[0])
                    for K in [F(0),F(15,4)]:
                        Dpre=add(p1['H'],{2:-K*p1['I']})
                        Dl=mul(F(1,2),add(*(add(x['H'],{2:-K*x['I']}) for x in lp)))
                        ck(add(Dpre,mul(-1,Dl))==add(ll,{2:-K*(p1['I']-ii)}))
                    losses.append(bounds(ll)[1]);ms.append(mm)
            stats['branch_reset_query_options']+=options;optioncounts.append(options)
            maxima.append(max(losses));maxm.append(max(ms))
        ck(sum(maxm)/2<=a0)
        ck(sum(maxima)/2<=budget)
        ck(bounds(L)[1]+sum(maxima)/2<=2*budget)
        stats['combined_policies_by_separability']+=optioncounts[0]*optioncounts[1]
def product(a,b):return tuple(x*y for y in b for x in a)
def compressed(a):
    a=canonical(a);ps=profile(a)['ps'];used=[j for j,p in enumerate(ps) if p]
    return tuple(a[sum(((x>>i)&1)<<j for i,j in enumerate(used))] for x in range(1<<len(used)))
pilot='--pilot' in sys.argv
seeds=[]
for d in range(3 if pilot else 4):
    for mask in range(1<<(1<<d)):
        a=tuple(1-2*((mask>>x)&1) for x in range(1<<d))
        validate_root(a,True);stats['base_roots']+=1
        if d<=2:seeds.append(a)
for seed in seeds:
    g=compressed(seed)
    for t,k in ([(1,2)] if pilot else [(1,2),(2,2),(1,3)]):
        core=(1,)
        for _ in range(t):core=product(core,g)
        root=core+(1,)*(len(core)*((1<<k)-1));pp=profile(root)
        ck(pp['e']<=F(1,1<<k));validate_root(root,False)
        stats['activation_roots']+=1
        if profile(g)['H']:
            ck(all(pp['ps'][j]<=pp['m'][v] for v in range(1,len(root)) for j in range(len(pp['ps'])) if (v>>j)&1))
            support=[s for s,c in enumerate(pp['w']) if c]
            ck(rank([s^support[0] for s in support])==len(pp['ps']))
ck(LN2[0]>F(2,3))
result={'status':'PASS','helper_version':'A005-character-error-frontier-v1','pilot':pilot,'assertions':count,'runtime_seconds':time.perf_counter()-start,'domain':stats,'profiles_cached':profile.cache_info().currsize}
(R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(result))
