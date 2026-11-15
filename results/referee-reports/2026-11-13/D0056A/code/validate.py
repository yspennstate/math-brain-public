#!/usr/bin/env python3
"""Independent rational checks of the fixed-point kernel and saved enclosures."""
import os,sys,csv,json,random
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).parent))
from certified import run,ceil_survival_scaled,init,S
import mpmath as mp
if os.getpriority(os.PRIO_PROCESS,0)<10:os.nice(10)
checks=[]
for m in (2,3):
    out=Path(f'data/validation_m{m}.csv');K=16;N=5
    run(m,'two2',N,K,out)
    p=[F(0)]*(K+1);p[2]=F(1,1+(2*(m-1)-1)*m*m);p[0]=1-p[2]
    exact=[]
    for n in range(N+1):
        exact.append(1-p[0])
        if n==N:break
        c=[F(1)]
        for j in range(m):
            d=[F(0)]*(len(c)+K)
            for i,x in enumerate(c):
                for k,y in enumerate(p):d[i+k]+=x*y
            c=d
        p=[F(0)]+c[2:K+2];p[0]=1-sum(p)
    for row,target in zip(csv.DictReader(out.open()),exact):
        lo=F(int(row['q_lower_numerator']),int(row['q_lower_denominator']))
        hi=F(int(row['q_upper_numerator']),int(row['q_upper_denominator']))
        assert lo<=target<=hi,(m,row['n'],lo,target,hi)
    checks.append(f'm={m}: all six exact rational survival values lie in the fixed-point intervals')
random.seed(56)
for m in (2,3):
    for _ in range(100):
        a=[0]+[random.randrange(1000) for _ in range(20)]
        x=sum((F(a[k],m**k) for k in range(1,len(a))),F(0))
        ceil=-(-x.numerator//x.denominator)
        assert ceil_survival_scaled(a,m)==ceil
checks.append('200 independent rational checks of the nested ceiling for q')
mp.mp.dps=80
for m in (2,3):
    for law in ('power3','sparse'):
        a,e=init(m,law,128)
        if law=='power3':
            c=1/((m-1)*mp.zeta(2)-mp.zeta(3)+mp.polylog(3,mp.mpf(1)/m))
            expected=[0]+[int(mp.floor(S*c/k**3)) for k in range(1,129)]
        else:
            A=(m-1)*mp.zeta(2)-mp.polylog(2,mp.mpf(1)/2)
            T=sum(mp.mpf(m)**(-2**j)/(j*j*2**j) for j in range(1,21));c=1/(A+T)
            expected=[0]*129
            for j in range(1,8):expected[2**j]=int(mp.floor(S*c/(j*j*2**j)))
        assert a==expected,(m,law)
        checks.append(f'm={m}, {law}: Arb floors agree with independent 80-digit mpmath values')
bounds=[]
for m in (2,3):
    meta=json.loads(Path(f'data/m{m}_sparse.json').read_text());c=mp.mpf(meta['initial']['c'])
    p=Path(f'data/cert_m{m}_sparse.csv')
    if not p.exists():p=Path(f'data/m{m}_sparse.csv')
    rr={int(r['n']):r for r in csv.DictReader(p.open())}
    for j in range(2,14):
        n=2**j-1;lam=c/(m*j*j*2**j);bound=-mp.expm1(-lam)
        observed=mp.mpf(rr[n]['q_mid'] if 'q_mid' in rr[n] else rr[n]['q'])
        assert observed>bound*(1-mp.mpf('1e-12')),(m,n,observed,bound)
        bounds.append({'m':m,'j':j,'n':n,'n2_leaf_bound':str(n*n*bound),'n2_observed':str(n*n*observed),'source':str(p)})
checks.append('24 sparse-law checkpoints exceed the independent one-large-leaf lower bound')
with Path('data/sparse_leaf_bounds.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=bounds[0]);w.writeheader();w.writerows(bounds)
Path('data/validation.json').write_text(json.dumps({'passed':True,'checks':checks},indent=2)+'\n')
print('\n'.join(checks))
