from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from collections import Counter
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1]
started=time.perf_counter()
checks=0
def ck(x):
    global checks
    assert x
    checks+=1
def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h]; a[k],a[k+h]=u+v,u-v
        h*=2
    return a
def spectrum(t):
    a=fwht(t); N=len(t); n=N.bit_length()-1
    ck(all(v in (-1,1) for v in t)); ck(sum(v*v for v in a)==N*N)
    p=[F(v*v,N*N) for v in a]
    I=sum((s.bit_count()*v for s,v in enumerate(p)),F(0))
    Ie=sum((F(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N) for i in range(n)),F(0))
    ck(I==Ie)
    return a,p,I
def ln_reduced(y,K=28):
    z=(y-1)/(y+1); total=F(0)
    for j in range(K): total+=2*z**(2*j+1)/(2*j+1)
    tail=2*z**(2*K+1)/((2*K+1)*(1-z*z))
    return total,total+tail
LN2=ln_reduced(F(2))
@lru_cache(None)
def log2(x):
    ck(x>0)
    k=0; y=x
    while y<1: y*=2; k-=1
    while y>=2: y/=2; k+=1
    l,u=ln_reduced(y)
    lo,hi=F(k)+l/LN2[1],F(k)+u/LN2[0]
    D=2**80
    return F((lo*D).__floor__(),D),F((hi*D).__ceil__(),D)
def ent(p):
    lo=hi=F(0)
    for v,c in Counter(p).items():
        if v:
            l,u=log2(1/v); lo+=c*v*l; hi+=c*v*u
    return lo,hi
def h(q): return ent([q,1-q])
def plus(a,b): return a[0]+b[0],a[1]+b[1]
def scale(a,c):
    return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def gm(m):
    n=2*m; table=[]
    for mask in range(1<<n):
        x=[bool(mask&(1<<i)) for i in range(n)]
        v=x[0]
        for i in range(n-1,1,-1): v=(x[i] and v) if i%2 else (x[i] or v)
        v=(x[0] or x[1]) and v
        table.append(-1 if v else 1)
    return table
results=[]
for m in (2,3,4,5,6):
    t=gm(m); a,p,I=spectrum(t); ck(sum(t)==0)
    ck(I==F(5,3)-F(2**3,3*2**(2*m)))
    H=ent(p); C=scale(H,1/(I-1))
    results.append({'family':'Hod gm','m':m,'n':2*m,'I':str(I),'H_interval':list(map(str,H)), 'amplified_C_interval':list(map(str,C)), 'walsh_histogram':dict(Counter(map(str,a)))})
ck(F(results[1]['amplified_C_interval'][0])>F(6278944,1000000))
ck(F(results[-1]['amplified_C_interval'][0])>F(63758,10000))
# Independent direct character summation for the 6-bit base.
t=gm(3); a,p,I=spectrum(t)
for s in range(64): ck(a[s]==sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)))
for n,clauses in [(6,[(0,1),(2,3),(0,2,4),(1,3,5)]),(8,[(0,1),(2,3),(2,4,5),(0,2,4,6),(1,2,5,7)])]:
    t=[-1 if all(any(mask&(1<<i) for i in c) for c in clauses) else 1 for mask in range(1<<n)]
    a,p,I=spectrum(t); ck(sum(t)==0); H=ent(p)
    results.append({'family':'Hod prime variant','n':n,'I':str(I),'H_interval':list(map(str,H)),'amplified_C_interval':list(map(str,scale(H,1/(I-1))))})
# All two-bit seeds: balance, tensor, spectator and activation coefficients.
for mask in range(16):
    t=[1 if mask&(1<<j) else -1 for j in range(4)]
    a,p,I=spectrum(t)
    b=[v*z for z in (1,-1) for v in t]; ba,bp,BI=spectrum(b)
    ck(BI==I+1); ck(sorted(bp)==sorted(p+[F(0)]*4))
    tensor=[u*v for u in t for v in t]; ta,tp,TI=spectrum(tensor)
    ck(TI==2*I); ck(sorted(tp)==sorted(u*v for u in p for v in p))
    r=2; q=F(1,4); act=b+[1]*24; aa,ap,AI=spectrum(act)
    ck(AI==q*(BI+r)); ck(ap[0]==(1-q)**2)
    expected=[(1-q)**2]+[q*q]*3+[q*q*v for v in bp[1:] for j in range(4)]
    ck(sorted(ap)==sorted(expected))
    H=ent(bp); AH=ent(ap)
    rem=scale(log2(1/(1-q)**2),(1-q)**2)
    form=plus(scale(H,q),plus((2*r*q*(2-q),)*2,rem))
    ck(max(AH[0],form[0])<=min(AH[1],form[1]))
# Hod limit recurrence: q_m=1/(1+q_(m-1)), pi_m=prod q_i.
q=F(1,2); pi=F(1); beta=(F(0),F(0)); records=[]
for m in range(49):
    if m:
        qprev=q; q=1/(1+q); pi*=q
        # Hplus/Iplus increment = h(qprev)*pi_prev/(1-qprev).
        beta=plus(beta,scale(h(qprev),(pi/q)/(1-qprev)))
    records.append({'m':m,'q':str(q),'pi':str(pi),'conditional_ratio_interval':list(map(str,beta))})
    ck(F(1,2)<=q<=F(2,3))
    if m>=2: ck(q*(1+qprev)==1)
# h<=1, 1-q>=1/3, pi_(k+1)<=2*pi_k/3: tail <=9*pi_48.
limit=(beta[0],beta[1]+9*pi)
ck(limit[0]>F(64547837,10000000)); ck(limit[1]<F(6454784,1000000))
out={'status':'PASS','assertions':checks,'runtime_seconds':time.perf_counter()-started,'arithmetic':'exact integer/Fraction; 28-term positive atanh remainder','literature_seeds':results,'Hod_limit_records':records,'Hod_beta_interval':list(map(str,limit)),'Hod_beta_decimal_display':[float(x) for x in limit],'finite_claim':'C > 6.4547837; C > 6.454784 is NOT certified by this construction'}
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out'/'CERTIFICATES.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'assertions':checks,'runtime_seconds':out['runtime_seconds'],'Hod_beta_decimal_display':out['Hod_beta_decimal_display'],'seed_displays':[{'n':r['n'],'family':r['family'],'I':r['I'],'C_lower_display':float(F(r['amplified_C_interval'][0]))} for r in results]},indent=2))
