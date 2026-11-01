from fractions import Fraction as F
from pathlib import Path
from math import comb
import json,time
RUN=Path(__file__).resolve().parents[1]
spec=json.loads((RUN/'out/FROZEN_ORBIT_SPEC.json').read_text())
t0=time.perf_counter(); checks=0; rows=[]
def check(x):
    global checks
    checks+=1
    assert x,checks
def walsh(values):
    a=values[:];d=1
    while d<len(a):
        for b in range(0,len(a),2*d):
            for j in range(b,b+d):
                u,v=a[j],a[j+d];a[j],a[j+d]=u+v,u-v
        d*=2
    return a
for w in spec['domain_widths']:
    k=1<<w;n=w*k;delta=F(1,k)
    # G=1-A on a single block; its coefficients tensorize exactly.
    block=[0]+[1]*(k-1);bw=walsh(block)
    check(bw==[k-1]+[-1]*(k-1))
    a=(1-delta)**(2*(k-1));check(a>F(1,9))
    factor=4*k*delta**2*a
    high_count=sum(comb(w,m) for m in range((w+1)//2,w+1))
    check(high_count>=k//2)
    high_mass=factor*high_count;check(high_mass>=F(2,9))
    for m in range((w+1)//2,w+1):
        check(comb(n,m)>=k**m)
        check(2*m>=w)
    eps=2*delta*(1-delta)**(k-1);I=n*eps
    check(I<=2*w)
    entropy_lower=high_mass*F(w*w,2)
    check(entropy_lower/I>=F(w,18))
    # Parseval of the tensor G and the actual sign 1-2 prod G.
    check((1-delta)**2+(k-1)*delta**2==1-delta)
    mean=1-2*(1-delta)**k
    nonempty_mass=4*((1-delta)**k-(1-delta)**(2*k))
    check(mean**2+nonempty_mass==1)
    if w==2:
        N=1<<n
        values=[1 if any(((x>>(j*w))&((1<<w)-1))==0 for j in range(k)) else -1 for x in range(N)]
        fw=walsh(values)
        check(F(fw[0],N)==mean)
        for s,c in enumerate(fw):
            if s:
                touched=sum(bool((s>>(j*w))&((1<<w)-1)) for j in range(k))
                check(F(c*c,N*N)==4*delta**(2*touched)*(1-delta)**(2*(k-touched)))
        for i in range(n):
            check(F(sum(values[x]!=values[x^(1<<i)] for x in range(N)),N)==eps)
    # Save modest-size bounds, not huge rational denominators.
    rows.append(dict(w=w,k=k,n=n,constant_influence=True,one_block_high_mass_at_least='2/9',orbit_entropy_at_least=str(F(w*w,9)),I_at_most=2*w,CE_over_I_at_least=str(F(w,18))))
result=dict(status='PASS',assertions=checks,failures=0,cases=len(rows),runtime_seconds=time.perf_counter()-t0,rows=rows,finite_to_infinite='Analytic orbit argument in REPORT.md; no finite extrapolation',full_FEI='OPEN')
(RUN/'out/ORBIT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
