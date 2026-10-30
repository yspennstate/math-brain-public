import itertools,json,time,sys
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic(); COUNT=0
def check(ok):
    global COUNT
    COUNT+=1
    if not ok: raise AssertionError(COUNT)
    if COUNT%1000==0 and time.monotonic()-START>58: raise RuntimeError('58-second frozen watchdog')
def vec(*terms):
    z={}
    for c,v in terms:
        for p,a in v: z[p]=z.get(p,F(0))+c*a
    return tuple(sorted((p,a) for p,a in z.items() if a))
@lru_cache(None)
def logint(n):
    ans=[];p=2
    while p*p<=n:
        a=0
        while n%p==0:n//=p;a+=1
        if a:ans.append((p,F(a)))
        p+=1
    if n>1:ans.append((n,F(1)))
    return tuple(ans)
def lograt(q):return vec((1,logint(q.numerator)),(-1,logint(q.denominator)))
def psi(q):return vec((-q,lograt(q))) if q else ()
def entropy(ps):return vec(*[(1,psi(p)) for p in ps if p])
@lru_cache(None)
def ln(q):
    z=(q-1)/(q+1);s=sum((z**(2*k+1)/F(2*k+1) for k in range(40)),F(0))*2
    tail=2*z**81/(81*(1-z*z));return s,s+tail
L2=ln(F(2))
@lru_cache(None)
def lg(p):
    q=F(p);shift=0
    while q>=2:q/=2;shift+=1
    a,b=ln(q);return shift+a/L2[1],shift+b/L2[0]
@lru_cache(None)
def interval(v):
    lo=hi=F(0)
    for p,c in v:
        a,b=lg(p)
        lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi
def nonnegative(v):return not v or interval(v)[0]>=0
def rational(q):return ((2,F(q)),) if q else ()
def restrict(t,i,b):return tuple(t[k] for k in range(len(t)) if (k>>i)&1==b)
@lru_cache(None)
def physical(st):
    labels,u,v=st;nc=len(labels).bit_length()-1;nu=len(u).bit_length()-1
    return tuple((1 if labels[c]==0 else u[a] if labels[c]==1 else v[b])
                 for b in range(len(v)) for a in range(len(u)) for c in range(len(labels)))
@lru_cache(None)
def law(t):
    w=list(t);step=1
    while step<len(w):
        for k in range(0,len(w),2*step):
            for j in range(step):a,b=w[k+j],w[k+j+step];w[k+j],w[k+j+step]=a+b,a-b
        step*=2
    return tuple(F(a*a,len(w)**2) for a in w)
@lru_cache(None)
def influence(t,i):return F(sum(t[k]!=t[k^(1<<i)] for k in range(len(t))),len(t))
@lru_cache(None)
def reserve(st):
    labels,u,v=st
    return vec(*[(1-F(sum(t),len(t))**2,psi(F(labels.count(j),len(labels)))) for j,t in [(1,u),(2,v)]])
def child(st,i,b):
    labs,u,v=st;nc=len(labs).bit_length()-1;nu=len(u).bit_length()-1
    if i<nc:return restrict(labs,i,b),u,v
    if i<nc+nu:return labs,restrict(u,i-nc,b),v
    return labs,u,restrict(v,i-nc-nu,b)
@lru_cache(None)
def node(st,i):
    t=physical(st);n=len(t).bit_length()-1;nc=len(st[0]).bit_length()-1
    kids=[child(st,i,b) for b in (0,1)]
    gap=vec((1,reserve(st)),(-F(1,2),reserve(kids[0])),(-F(1,2),reserve(kids[1])))
    d=influence(t,i)
    check(nonnegative(gap))
    if i<nc:check(nonnegative(vec((1,rational(2*d)),(-1,gap))))
    else:
        nu=len(st[1]).bit_length()-1;j=1 if i<nc+nu else 2
        means=[F(sum(s[j]),len(s[j])) for s in kids];beta=(means[0]-means[1])/2
        q=F(st[0].count(j),len(st[0]));check(gap==vec((beta*beta,psi(q))))
        check(d==q*influence(st[j],i-nc if j==1 else i-nc-nu))
    p=law(t);rows=[(p[k],p[k|(1<<i)]) for k in range(1<<n) if not k&(1<<i)]
    erased=vec((1,entropy(p)),(-1,entropy([a+b for a,b in rows])))
    pk=[law(physical(s)) for s in kids]
    js=vec((1,entropy([a+b for a,b in rows])),(-F(1,2),entropy(pk[0])),(-F(1,2),entropy(pk[1])))
    delta=vec((1,entropy(p)),(-F(1,2),entropy(pk[0])),(-F(1,2),entropy(pk[1])))
    check(delta==vec((1,erased),(1,js)));check(nonnegative(js));check(nonnegative(erased))
    return tuple(kids),gap,d,erased,js
@lru_cache(None)
def walk(st,order,adaptive,depth):
    n=len(physical(st)).bit_length()-1
    if not n or depth==0:return (),(),reserve(st),F(0),entropy(law(physical(st))),(),()
    nc=len(st[0]).bit_length()-1
    i=max(range(n),key=lambda k:(influence(physical(st),k),-k)) if adaptive else order[0]
    rest=tuple(k-(k>i) for k in order[1:]) if not adaptive else ()
    kids,gap,d,b,j=node(st,i)
    rows=[walk(s,rest,adaptive,depth-1) for s in kids]
    avg=lambda k:vec((F(1,2),rows[0][k]),(F(1,2),rows[1][k]))
    gd=vec((1,avg(0)),(int(i>=nc),gap));gc=vec((1,avg(1)),(int(i<nc),gap))
    di=(rows[0][3]+rows[1][3])/2+(d if i>=nc else 0)
    return gd,gc,avg(2),di,avg(4),vec((1,b),(1,avg(5))),vec((1,j),(1,avg(6)))
def main():
    pilot='--pilot' in sys.argv;cores=list(itertools.product((-1,1),repeat=2));roots=trees=0
    maps=list(itertools.product(range(3),repeat=4));maps=maps[:8] if pilot else maps
    perms=list(itertools.permutations(range(4)))
    for labs in maps:
        for u,v in itertools.product(cores,repeat=2):
            st=(labs,u,v);t=physical(st);r=reserve(st);ctrl=sum((influence(t,i) for i in range(2)),F(0));data=sum((influence(t,i) for i in (2,3)),F(0))
            check(nonnegative(vec((1,rational(2*ctrl)),(-1,r))));roots+=1
            for order,adaptive,depth in [(p,False,4) for p in perms]+[((),True,4),((),True,2)]:
                gd,gc,rl,di,hl,b,j=walk(st,order,adaptive,depth)
                check(vec((1,gd),(1,gc),(1,rl))==r);check(di<=data)
                check(nonnegative(vec((1,r),(-1,gd))));check(entropy(law(t))==vec((1,hl),(1,b),(1,j)))
                trees+=1
    sharp=((1,2,1,2),(-1,1),(-1,1))
    _,release,d,_,_=node(sharp,0)
    check(reserve(sharp)==rational(1));check(release==rational(1));check(d==F(1,2))
    result={'status':'PASS','roots':roots,'trees':trees,'assertions':COUNT,'runtime_seconds':time.monotonic()-START,'cached_nodes':node.cache_info().currsize,'sharp_fixture':{'labels':[1,2,1,2],'cores':['dictator','dictator'],'reserve':'1','control_release':'1','control_influence':'1/2'},'arithmetic':'Fraction edge counts, exact prime-log identities, 40-term atanh enclosures','scope':'finite interleaved reserve/ownership/entropy ledgers; analytic proof supplies dimension-free quantifiers'}
    (ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
