from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import itertools,json,time,math
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=0
def ck(x):
    global assertions
    assertions+=1
    assert x
def prod(xs):
    r=Q(1)
    for x in xs:r*=x
    return r
def series(x):
    z=(x-1)/(x+1);ck(0<=z<=Q(1,3))
    l=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0))
    return l,l+2*z**49/Q(49)/(1-z*z)
L2=series(Q(2))
@lru_cache(None)
def ln(x):
    ck(x>=1);k=0
    while x>=2:x/=2;k+=1
    lo,hi=series(x)
    return lo+k*L2[0],hi+k*L2[1]
def mesh(lo,hi):
    scale=10**12
    return [str(Q((lo*scale).__floor__(),scale)),str(Q((hi*scale).__ceil__(),scale))]
def expr(c,m,indices):
    result={}
    for s in indices:
        if not m[s]:continue
        x=1/c[s]**2
        if x!=1:result[x]=result.get(x,Q(0))+m[s]
    return {x:a for x,a in result.items() if a}
def bounds(e):
    lo=hi=Q(0)
    for x,a in e.items():
        l,h=ln(x)
        if a>=0:lo+=a*l;hi+=a*h
        else:lo+=a*h;hi+=a*l
    return lo,hi
def scalar_h(x):
    x=abs(x)
    if not x:return Q(0),Q(0)
    lo,hi=ln(1/x**2)
    return x*x*lo,x*x*hi

def tables(k):
    n=k+1;num=1<<n;data=(1<<k)-1
    a=[Q(1 if x&data==data else -1) for x in range(num)]
    b=[Q(1 if x&data==0 and x>>k&1 else -1) for x in range(num)]
    f=[x+y+1 for x,y in zip(a,b)]
    ck(all(x in (-1,1) for x in f))
    return a,b,f

def spectrum(t,p):
    n=len(p);num=1<<n
    # Tensor transformation of actual truth values to E[f product(Yj-pj)].
    mom=t.copy()
    for j in range(n):
        bit=1<<j
        for x in range(num):
            if x&bit:continue
            a,b=mom[x],mom[x|bit]
            mom[x]=(1-p[j])*a+p[j]*b
            mom[x|bit]=p[j]*(1-p[j])*(b-a)
    mob=t.copy()
    for j in range(n):
        for s in range(num):
            if s>>j&1:mob[s]-=mob[s^(1<<j)]
    c=[];m=[];v=[4*x*(1-x) for x in p]
    for s in range(num):
        partial=sum((mob[u]*prod(p[j] for j in range(n) if u>>j&1 and not s>>j&1)
                     for u in range(num) if u&s==s),Q(0))/2**s.bit_count()
        vv=prod(v[j] for j in range(n) if s>>j&1)
        denom=prod(p[j]*(1-p[j]) for j in range(n) if s>>j&1)
        direct=mom[s]**2/denom if denom else Q(0)
        if not denom:ck(mom[s]==0)
        ck(direct==vv*partial**2)
        ck(abs(partial)<=1)
        c.append(partial);m.append(direct)
    ck(sum(m)==1)
    I=sum((s.bit_count()*m[s] for s in range(num)),Q(0))
    var=1-m[0];delta=I-var
    R=sum(((s.bit_count()-2)*m[s] for s in range(num) if s.bit_count()>=3),Q(0))
    deriv=[];slack_base=Q(0)
    for j in range(n):
        mean=second=pos=neg=Q(0)
        for x in range(num):
            if x>>j&1:continue
            w=prod(p[h] if x>>h&1 else 1-p[h] for h in range(n) if h!=j)
            d=(t[x|(1<<j)]-t[x])/2
            mean+=w*d;second+=w*d*d
            if d==1:pos+=w
            if d==-1:neg+=w
        ck(mean==c[1<<j]);ck(second-abs(mean)==2*min(pos,neg))
        ck(second>=abs(mean))
        deriv.append((mean,second))
        slack_base+=2*v[j]*(second-mean*mean)
    ck(slack_base==4*delta-2*R)
    return {'c':c,'m':m,'I':I,'var':var,'delta':delta,'R':R,'deriv':deriv,
            'E':expr(c,m,range(1,num)),'singles':expr(c,m,(1<<j for j in range(n))),
            'higher':expr(c,m,(s for s in range(num) if s.bit_count()>=2))}

def prime_rows(t,n):
    ck(all(any(t[x]!=t[x^(1<<j)] for x in range(1<<n)) for j in range(n)))
    rowcounts=[]
    for size in range(2,n):
        for B in itertools.combinations(range(n),size):
            C=[j for j in range(n) if j not in B]
            rows={tuple(t[sum(((a>>j)&1)<<B[j] for j in range(size))+
                          sum(((z>>j)&1)<<C[j] for j in range(n-size))]
                        for z in range(1<<len(C))) for a in range(1<<size)}
            ck(len(rows)==3);rowcounts.append(len(rows))
    return len(rowcounts)

def fixture(k,p):
    ta,tb,tf=tables(k);n=k+1
    a=spectrum(ta,p);b=spectrum(tb,p);f=spectrum(tf,p)
    pa=prod(p[:k]);pb=p[k]*prod(1-x for x in p[:k])
    ck(f['I']==a['I']+b['I'])
    ck(f['var']==a['var']+b['var']-8*pa*pb)
    ck(f['delta']==a['delta']+b['delta']+8*pa*pb)
    for s in range(1,1<<n):
        ck(f['c'][s]==a['c'][s]+b['c'][s])
        if s.bit_count()>=2:ck(abs(a['c'][s])<=Q(1,2) and abs(b['c'][s])<=Q(1,2))
    for j in range(n):
        for x in range(1<<n):
            if x>>j&1:continue
            ck((ta[x|(1<<j)]-ta[x])*(tb[x|(1<<j)]-tb[x])==0)
    Ea=bounds(a['E']);Eb=bounds(b['E']);Ef=bounds(f['E'])
    single=bounds(f['singles']);high=bounds(f['higher'])
    ck(single[1]<=4*f['delta']-2*f['R'])
    ck(Ea[1]<=(4+2*L2[0])*a['delta'])
    ck(Eb[1]<=(4+2*L2[0])*b['delta'])
    ck(high[1]<=2*(bounds(a['higher'])[0]+bounds(b['higher'])[0]))
    margin=(12+4*L2[0])*f['delta']-Ef[1]
    ck(margin>0)
    # Exact coefficient/mass identity gives A042's retained singleton ledger.
    v=[4*x*(1-x) for x in p]
    local_base=sum((v[j]*(2*(d-abs(t))+2*abs(t)*(1-abs(t))) for j,(t,d) in enumerate(f['deriv'])),Q(0))
    ck(local_base==4*f['delta']-2*f['R'])
    local_logs={}
    for j,(t,d) in enumerate(f['deriv']):
        if not t:continue
        x=1/(t*t)
        if x!=1:local_logs[x]=local_logs.get(x,Q(0))+v[j]*t*t
    ck({x:w for x,w in local_logs.items() if w}==f['singles'])
    return f, {'k':k,'probabilities':[str(x) for x in p],
               'delta':str(f['delta']),'K_margin_lower':str(Q((margin*10**12).__floor__(),10**12))}

domain=[Q(-1,2),Q(-1,4),Q(-1,16),Q(0),Q(1,16),Q(1,4),Q(1,2)]
for a,b in itertools.product(domain,repeat=2):
    lhs=scalar_h(a+b);ha=scalar_h(a);hb=scalar_h(b)
    if not a and not b:ck(lhs==(Q(0),Q(0)))
    else:ck(lhs[1]<=2*(ha[0]+hb[0]))

records=[];prime_records=[]
for k in range(2,7):
    ta,tb,tf=tables(k)
    prime_records.append({'k':k,'proper_blocks':prime_rows(tf,k+1),'all_row_counts':3})
    laws=[[Q(1,2)]*(k+1),[Q([1,2,6,7][j%4],8) for j in range(k+1)],
          [Q(127,128)]*k+[Q(1,1024)], [Q(1,128)]*k+[Q(1023,1024)]]
    for p in laws:
        f,record=fixture(k,p);records.append(record)
for p in itertools.product([Q(1,8),Q(1,2),Q(7,8)],repeat=4):
    f,record=fixture(3,p);records.append(record)

selectors=[]
for z in [Q(0),Q(1,1024),Q(1,16),Q(1,4),Q(1,2),Q(3,4),Q(15,16),Q(1023,1024),Q(1)]:
    f,record=fixture(3,[Q(1,2)]*3+[z]);records.append(record)
    ck(f['delta']==(5+14*z-7*z*z)/16)
    for s in range(1,16):
        if s&8:ck(abs(f['c'][s])==Q(1,8))
        else:ck(f['c'][s]==(1+z)/4 if s.bit_count()==2 else f['c'][s]==(1-z)/4)
    # Exact log-expression equality with explicit continuum formula.
    expected={}
    for coef,count in (((1-z)/4,4),((1+z)/4,3)):
        if coef:
            x=1/coef**2;expected[x]=expected.get(x,Q(0))+count*coef**2
    if z*(1-z):expected[Q(64)]=expected.get(Q(64),Q(0))+z*(1-z)/2
    ck(expected==f['E'])
    lo,hi=bounds(f['E'])
    marginlo=(4+2*L2[0])*f['delta']-hi
    # Endpoints exactly give the equality; do not compare overlapping intervals.
    if z:ck(marginlo>Q(47,100))
    else:ck(f['E']=={Q(16):Q(7,16)})
    selectors.append({'z':str(z),'delta':str(f['delta']),'margin_interval':mesh((4+2*L2[0])*f['delta']-hi,(4+2*L2[1])*f['delta']-lo)})
ck(L2[1]<Q(52,75))
out={'helper':'A043-separated-conjunction-payment-v1','fixtures':159,
     'boolean_cases':len(records),'scalar_cases':49,'assertions':assertions,
     'prime_records':prime_records,'all_passed':True,'runtime_seconds':time.perf_counter()-start,
     'K_bit_interval':mesh(4+12/L2[1],4+12/L2[0]),'log_terms':24,
     'arithmetic':'Fraction tensor moments, Mobius partials, signed derivatives; exact uncombined-rational log dictionaries for equalities; outward rational logarithm intervals for strict signs',
     'review_selector_records':selectors,'theorem_fixture_records':records}
(ROOT/'out/checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('prime_records','review_selector_records','theorem_fixture_records')}))
