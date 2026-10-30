from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json, sys, time

run=Path(__file__).resolve().parents[1]
mode=sys.argv[1]
assert mode in ['pilot','full']
started=time.perf_counter(); assertions=0
def test(x):
    global assertions
    assert x
    assertions+=1
    if time.perf_counter()-started>60: raise RuntimeError('Frozen 60-second maximum exceeded')

@lru_cache(None)
def factor(n):
    result={}; p=2
    while p*p<=n:
        while n%p==0:
            result[p]=result.get(p,0)+1; n//=p
        p=3 if p==2 else p+2
    if n>1: result[n]=result.get(n,0)+1
    return result

def logadd(dst,arg,weight):
    if not weight: return
    assert arg>0
    for number,sign in [(arg.numerator,1),(arg.denominator,-1)]:
        for p,k in factor(number).items():
            dst[p]=dst.get(p,Q(0))+sign*k*weight
            if not dst[p]: del dst[p]

def combine(*terms):
    result={}
    for expression,scale in terms:
        for p,c in expression.items():
            result[p]=result.get(p,Q(0))+scale*c
            if not result[p]: del result[p]
    return result

def facts(values,physical=True):
    N=len(values); n=N.bit_length()-1
    w=list(values); width=1
    while width<N:
        for start in range(0,N,2*width):
            for j in range(width):
                a,b=w[start+j],w[start+j+width]
                w[start+j],w[start+j+width]=a+b,a-b
        width*=2
    p=[Q(a*a,N*N) for a in w]
    test(sum(p)==1)
    ei=[]; Mi=[]; WDi=[]; tail={}; totalM={}; jointD={}; jointP=jointQ=Q(0)
    for i in range(n):
        bit=1<<i
        e=sum(p[s] for s in range(N) if s&bit)
        ei.append(e)
        if physical: test(e==Q(sum(values[s]!=values[s^bit] for s in range(N)),N))
        M={}; WD={}; rsum=musum=Q(0)
        for t in range(N):
            if t&bit: continue
            b=p[t|bit]; r=p[t]+b
            rsum+=r
            if b:
                musum+=b/e
                logadd(M,r/b,b)
                logadd(WD,b/(e*r),b)
                if t.bit_count()>=2: logadd(tail,r/b,b)
        test(rsum==1)
        test(musum==(1 if e else 0))
        rarity={}
        if e: logadd(rarity,1/e,e)
        test(combine((rarity,1),(WD,-1))==M)
        Mi.append(M); WDi.append(WD)
        totalM=combine((totalM,1),(M,1))
    I=sum(ei)
    for i,e in enumerate(ei):
        if not e: continue
        bit=1<<i
        for t in range(N):
            if t&bit: continue
            b=p[t|bit]; r=p[t]+b
            actual=b/I; reference=e*r/I
            jointP+=actual; jointQ+=reference
            if b: logadd(jointD,actual/reference,actual*I)
    if I:
        test(jointP==1); test(jointQ==1)
        test(jointD==combine(*[(wd,1) for wd in WDi]))
    return {'p':p,'ei':ei,'I':I,'Mi':Mi,'WDi':WDi,'M':totalM,'tail':tail,'ID':jointD}

seeds=[]
for n in [1,2]:
    for mask in range(1,(1<<(1<<n))-1):
        seeds.append((n,mask,tuple(1 if mask>>x&1 else -1 for x in range(1<<n))))
if mode=='full':
    for mask in [1,7,105,150]:
        seeds.append((3,mask,tuple(1 if mask>>x&1 else -1 for x in range(8))))
count=0
for n,mask,seed in seeds:
    s=facts(seed)
    for m in ([1] if mode=='pilot' else [1,2]):
        for ell in ([2] if mode=='pilot' else [2,3]):
            nc=n*m+ell
            h=[]
            for x in range(1<<nc):
                value=(-1)**((x>>(n*m)).bit_count())
                for j in range(m): value*=seed[(x>>(n*j))&((1<<n)-1)]
                h.append(value)
            H=facts(h)
            test(H['I']==m*s['I']+ell)
            test(H['M']==combine((s['M'],m)))
            test(H['ID']==combine((s['ID'],m)))
            for k in ([1] if mode=='pilot' else [1,2,3]):
                q=Q(1,1<<k); d0=(1-q)**2+q*q
                vals=tuple(h[x>>k] if (x&((1<<k)-1))==0 else 1 for x in range(1<<(nc+k)))
                F=facts(vals)
                test(F['I']==q*(H['I']+k))
                Dc={}; logadd(Dc,Q(2),(1-q)*(k-1)); logadd(Dc,q/d0,q)
                Mc={}; logadd(Mc,Q(2),q*(1-q)); logadd(Mc,d0/(q*q),q*q)
                for i in range(k):
                    test(F['ei'][i]==q)
                    test(F['WDi'][i]==combine((Dc,q)))
                    test(F['Mi'][i]==Mc)
                for i,e in enumerate(H['ei']):
                    test(F['ei'][k+i]==q*e)
                    test(F['Mi'][k+i]==combine((H['Mi'][i],q)))
                    test(F['WDi'][k+i]==combine((H['WDi'][i],q),({2:Q(k)*e},q)))
                test(F['ID']==combine((s['ID'],q*m),({2:Q(k)*H['I']},q),(Dc,q*k)))
                test(F['M']==combine((s['M'],q*m),(Mc,k)))
                test(F['tail']==combine((s['M'],q*m),({2:k*q*(1-k*q)},1)))
                count+=1
test(count==(16 if mode=='pilot' else 240))
out={'mode':mode,'cases':count,'assertions':assertions,'elapsed_seconds':time.perf_counter()-started,
     'arithmetic':'Exact integer FWHT, physical flips, Fraction laws, prime-log coefficients; no numerical logs or floating sign tests',
     'independence':'New implementation from actual truth tables; no A096 author code loaded; alternate row/joint law checks',
     'max_ambient_dimension':5 if mode=='pilot' else 12}
(run/'out').mkdir(exist_ok=True)
(run/'out'/('REFUND_'+mode.upper()+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
