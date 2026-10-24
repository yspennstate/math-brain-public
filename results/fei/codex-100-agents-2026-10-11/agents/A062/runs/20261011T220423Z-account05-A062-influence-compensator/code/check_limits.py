from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import time,json
start=time.perf_counter()
assertions=0
def check(a,b):
    global assertions
    assert a==b,(a,b)
    assertions+=1
def walsh(values):
    if len(values)==1:
        return values
    half=len(values)//2
    left,right=walsh(values[:half]),walsh(values[half:])
    return [a+b for a,b in zip(left,right)]+[a-b for a,b in zip(left,right)]
def measure(values):
    size=len(values)
    n=size.bit_length()-1
    p=[F(v*v,size*size) for v in walsh(values)]
    inf=[sum(p[s] for s in range(size) if (s>>i)&1) for i in range(n)]
    edge=[F(sum(values[x]!=values[x^(1<<i)] for x in range(size)),size) for i in range(n)]
    check(inf,edge)
    check(sum(p),F(1))
    return p,inf
rows=[]
for k in (1,2,3):
    d=2**k
    m=d+1
    g=[]
    for y in range(2**m):
        exponent=(y&1)+sum(((y>>(2*j+1))&1)*((y>>(2*j+2))&1) for j in range(d//2))
        g.append((-1)**exponent)
    gp,gi=measure(g)
    check(sum(g),0)
    check(Counter(v for v in gp if v),Counter({F(1,2**d):2**d}))
    check(sum(gi),F(d,2)+1)
    values=[g[x>>k] if (x&((1<<k)-1))==0 else 1 for x in range(2**(k+m))]
    fp,fi=measure(values)
    p=F(1,2**k)
    expected=Counter()
    expected[(1-p)**2]+=1
    expected[p*p]+=2**k-1
    expected[p*p/F(2**d)]+=2**(k+d)
    check(Counter(v for v in fp if v),expected)
    check(sum(fi),p*(sum(gi)+k))
    check(fi[:k],[p]*k)
    check(sum(fi)-p*sum(gi),k*p)
    # Entropy is d in the active leaf, from its exact uniform spectrum.
    check(p*d,F(1))
    rows.append({'k':k,'dimension':k+m,'p':str(p),'rootI':str(sum(fi)),
                 'expected_leafI':str(p*sum(gi)),'expected_leafH':'1',
                 'expected_query_cost':str(k*p),
                 'root_spectrum_nonzero_histogram':{str(q):num for q,num in expected.items()}})
    assert time.perf_counter()-start<60
result={'helper_version':'A062-limit-check-v1','assertions':assertions,'failures':0,
        'runtime_seconds':time.perf_counter()-start,'cases':rows,'arithmetic':'integer recursive Walsh + Fraction + direct edges'}
(Path(__file__).resolve().parents[1]/'out'/'LIMIT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
