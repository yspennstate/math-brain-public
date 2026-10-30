from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from itertools import product
import json,time,sys

R=Path(__file__).resolve().parents[1]
started=time.perf_counter(); asserts=0; nodes=0
LIMIT=60 if '--pilot' in sys.argv else 120
def ck(ok):
    global asserts
    assert ok
    asserts+=1
    if time.perf_counter()-started>LIMIT: raise RuntimeError('frozen watchdog')
def add(*es):
    d={}
    for e in es:
        for p,v in e.items(): d[p]=d.get(p,Q(0))+v
    return {p:v for p,v in d.items() if v}
def mul(e,a): return {p:v*a for p,v in e.items() if v*a}
@lru_cache(None)
def factors(a):
    d={};i=2
    while i*i<=a:
        while a%i==0: d[i]=d.get(i,0)+1;a//=i
        i+=1
    if a>1:d[a]=d.get(a,0)+1
    return d
def entropy(v):
    d={}
    for x in v:
        if not x: continue
        for a,s in [(x.numerator,-1),(x.denominator,1)]:
            for p,k in factors(a).items():d[p]=d.get(p,Q(0))+s*x*k
    return {p:v for p,v in d.items() if v}
@lru_cache(None)
def h(p): return entropy((p,1-p))
@lru_cache(None)
def ln_bounds(y):
    z=(y-1)/(y+1)
    l=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(32)),Q(0))
    return l,l+2*z**65/(65*(1-z*z))
LN2=ln_bounds(Q(2))
@lru_cache(None)
def log_bounds(x):
    x=Q(x);k=0
    # Avoid subtraction of unrelated ln(2) intervals at masses 1-epsilon.
    if Q(1,2)<=x<1:
        a,b=log_bounds(1/x)
        return -b,-a
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    l,u=ln_bounds(x); vals=[a/b for a in (l,u) for b in LN2]
    return min(vals)+k,max(vals)+k
def bounds(e):
    l=u=Q(0)
    for p,v in e.items():
        a,b=log_bounds(p)
        if v<0:a,b=b,a
        l+=v*a;u+=v*b
    return l,u
def nonnegative(e):ck(not e or bounds(e)[0]>=0)
def int_entropy(v):
    l=u=Q(0)
    for x in v:
        if x:
            a,b=log_bounds(x);l-=x*b;u-=x*a
    return l,u
def int_add(*xs):return sum((x[0] for x in xs),Q(0)),sum((x[1] for x in xs),Q(0))
def int_mul(x,v):
    a=[v*x[0],v*x[1]];return min(a),max(a)
def serialize_interval(x):
    grid=1<<1024
    lo=Q((x[0]*grid).numerator//(x[0]*grid).denominator,grid)
    hi=Q(-((-x[1]*grid).numerator//(-x[1]*grid).denominator),grid)
    ck(lo<=x[0] and hi>=x[1])
    return [str(lo),str(hi)]
@lru_cache(None)
def weights(ps):return tuple(product_weight(x,ps) for x in range(1<<len(ps)))
def product_weight(x,ps):
    w=Q(1)
    for i,p in enumerate(ps):w*=p if x>>i&1 else 1-p
    return w
@lru_cache(None)
def split(t,i,b):
    n=len(t).bit_length()-1
    return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(1<<(n-1)))
@lru_cache(None)
def stats(t,ps):
    n=len(ps);ws=weights(ps)
    neg=sum((w for f,w in zip(t,ws) if f==-1),Q(0))
    masses=[]
    for S in range(1<<n):
        moment=Q(0); norm=Q(1)
        for i,p in enumerate(ps):
            if S>>i&1:norm*=p*(1-p)
        for x,w in enumerate(ws):
            m=Q(t[x])*w
            for i,p in enumerate(ps):
                if S>>i&1:m*=Q(x>>i&1)-p
            moment+=m
        masses.append(moment*moment/norm)
    ck(sum(masses)==1)
    inf=[]
    for i in range(n):
        rp=ps[:i]+ps[i+1:]
        g,hc=split(t,i,0),split(t,i,1)
        inf.append(sum((w for w,x,y in zip(weights(rp),g,hc) if x!=y),Q(0)))
    return {'neg':neg,'out':h(neg),'P':tuple(masses),'fourier':entropy(masses),'inf':tuple(inf),'I':sum(inf,Q(0))}
@lru_cache(None)
def node(t,ps,i):
    global nodes
    nodes+=1
    st=stats(t,ps);p=ps[i];rp=ps[:i]+ps[i+1:]
    children=[stats(split(t,i,b),rp) for b in [0,1]]
    N=1<<(len(ps)-1); marginal=[]
    for x in range(N):
        y=(x&((1<<i)-1))|((x>>i)<<(i+1))
        q=st['P'][y]+st['P'][y|(1<<i)]
        ck(q==(1-p)*children[0]['P'][x]+p*children[1]['P'][x])
        marginal.append(q)
    HQ=entropy(marginal)
    M=add(st['fourier'],mul(HQ,-1))
    J=add(HQ,mul(children[0]['fourier'],-(1-p)),mul(children[1]['fourier'],-p))
    Iv=add(st['out'],mul(children[0]['out'],-(1-p)),mul(children[1]['out'],-p))
    c=add(h(p),mul(Iv,-1))
    Dbar=add(mul(h(p),Q(1,2)),M,mul(J,-1))
    for e in [M,J,Iv,c,Dbar]:nonnegative(e)
    ck(add(M,J)==add(st['fourier'],mul(children[0]['fourier'],-(1-p)),mul(children[1]['fourier'],-p)))
    ck(st['I']==st['inf'][i]+(1-p)*children[0]['I']+p*children[1]['I'])
    return M,J,Iv,c,Dbar

def tree(t,ps,policy,depth=0,path=()):
    st=stats(t,ps)
    if len(set(t))==1 or not ps or policy=='partial' and depth==1:
        return {'M':{},'J':{},'HP':{},'C':{},'Info':{},'Dbar':{},'leafF':st['fourier'],'leafOut':st['out'],'leafI':st['I'],'removed':Q(0),'leaves':[(path,Q(1),st['neg'])]}
    essential=[i for i,d in enumerate(st['inf']) if d]
    i=max(essential) if policy=='reverse' else max(essential,key=lambda i:(st['inf'][i],-i)) if policy=='max' else min(essential)
    p=ps[i];M,J,Iv,c,D=node(t,ps,i)
    rp=ps[:i]+ps[i+1:]
    cc=[tree(split(t,i,b),rp,policy,depth+1,path+((i,b),)) for b in [0,1]]
    ret={}
    for key,v in [('M',M),('J',J),('HP',h(p)),('C',c),('Info',Iv),('Dbar',D)]:ret[key]=add(v,mul(cc[0][key],1-p),mul(cc[1][key],p))
    for key in ['leafF','leafOut']:ret[key]=add(mul(cc[0][key],1-p),mul(cc[1][key],p))
    for key,initial in [('leafI',Q(0)),('removed',st['inf'][i])]:ret[key]=initial+(1-p)*cc[0][key]+p*cc[1][key]
    ret['leaves']=[(a,w*(1-p if b==0 else p),q) for b in [0,1] for a,w,q in cc[b]['leaves']]
    return ret

laws=[(Q(1,2),)*3,(Q(1,8),)*3,(Q(1,8),Q(1,4),Q(3,8)),(Q(3,4),Q(7,8),Q(1,2))]
roots=trees=0;psigns=0
for n in range(4):
    for law in laws:
        ps=law[:n]
        for mask in range(1<<(1<<n)):
            if '--pilot' in sys.argv and roots>=32:break
            t=tuple(1-2*(mask>>x&1) for x in range(1<<n))
            st=stats(t,ps);roots+=1
            weighted={}
            for p,d in zip(ps,st['inf']):weighted=add(weighted,mul(h(p),d))
            nonnegative(add(weighted,mul(st['out'],-1)))
            for policy in ['forward','reverse','max','partial']:
                r=tree(t,ps,policy);trees+=1
                joint=[w*a for _,w,q in r['leaves'] for a in [q,1-q]]
                ck(entropy([w for _,w,q in r['leaves']])==r['HP'])
                ck(add(entropy(joint),mul(st['out'],-1))==r['C'])
                ck(add(st['out'],mul(r['leafOut'],-1))==r['Info'])
                ck(add(r['C'],r['Info'])==r['HP'])
                ck(add(r['leafF'],r['M'],r['J'])==st['fourier'])
                ck(add(r['leafF'],mul(r['M'],2),mul(r['C'],Q(1,2)),mul(r['Info'],Q(1,2)),mul(r['Dbar'],-1))==st['fourier'])
                ck(st['I']==r['leafI']+r['removed'])
                nonnegative(add({2:st['I']/2},mul(r['Info'],Q(-1,2))))

extras={}
if '--pilot' not in sys.argv:
    for t,ps,name in [((1,-1),(Q(1,2),),'character'),((1,1,1,-1),(Q(1,2),)*2,'bent_AND')]:
        r=tree(t,ps,'forward');st=stats(t,ps)
        # A037 lift has I(S0;Pi)=J_tree; a complete tree has I(Y;Pi)=H(Y).
        difference=add(r['J'],mul(st['out'],-1))
        if name=='character':ck(difference=={2:Q(-1)})
        else:ck(bounds(difference)[0]>0)
        extras[name]={'conditional_entropy_difference_vector':{str(k):str(v) for k,v in difference.items()}}
    for n in range(1,9):
        q=Q(1,8);delta=q**n;reach=(1-delta)/(1-q)
        hp=mul(h(q),reach);cy=add(hp,mul(h(delta),-1));info=h(delta)
        ck(add(cy,info)==hp)
        ck(sum((q**j for j in range(n)),Q(0))==reach)
        nonnegative(add({2:Q(n)*q**(n-1)},mul(info,-1)))
    scalar=[]
    for k in [2,8,128]:
        t=Q(2**k-1,2**k);p=1-t*t;s=(1-t)/2
        hp=int_entropy([p,1-p]);hs=int_entropy([s,1-s])
        lower=int_add(hp,int_mul(hs,-2))
        if k==128:
            lam=Q(49,100);n=4;delta=p**n;geom=(1-delta)/(1-p)
            conditional=int_add(int_mul(hp,geom),int_mul(int_entropy([delta,1-delta]),-1))
            net=int_add(int_mul(lower,geom),int_mul(conditional,-lam))
            inf=Q(n)*p**(n-1)
            ck(net[0]>inf)
            ck(int_add(lower,int_mul(hp,-lam))[0]>0)
            extras['underrefund']={'q':str(p),'lambda':'49/100','dimension':4,'certified_net_tax_gt_physical_I':True,'net_interval':serialize_interval(net),'Iphys':str(inf)}
        scalar.append({'k':k,'p':str(p),'midpoint_tax_lower_interval':serialize_interval(lower)})
    extras['scalar']=scalar
out={'status':'PASS','mode':'pilot' if '--pilot' in sys.argv else 'main','roots':roots,'trees':trees,'distinct_queried_states':nodes,'assertions':asserts,'arithmetic_runtime_seconds':time.perf_counter()-started,'extras':extras,'arithmetic':'Fraction probabilities, rational prime-log identity vectors, 32-term atanh sign intervals; no tau optimizer','cache_states':stats.cache_info().currsize}
(R/'out'/('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='extras'}))
