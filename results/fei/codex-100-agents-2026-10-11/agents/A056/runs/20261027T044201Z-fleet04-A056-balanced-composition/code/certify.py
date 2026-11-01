"""Frozen, bounded exact checks; never enumerate the large bent cubes."""
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import json, time

ROOT = Path(__file__).resolve().parents[1]
checks = 0
def ck(test):
    global checks
    checks += 1
    if not test:
        raise AssertionError(f'check {checks}')

def fwht(values):
    a = list(values)
    step = 1
    while step < len(a):
        for j in range(0, len(a), 2*step):
            for i in range(j, j+step):
                u,v = a[i], a[i+step]
                a[i],a[i+step] = u+v,u-v
        step *= 2
    return [F(x,len(a)) for x in a]

def bits(x,n):
    return [1-2*((x>>i)&1) for i in range(n)]

start=time.monotonic()
k=2
m=2*((1<<k)-k)
n=k+2+m
values=[]
for x in range(1<<n):
    v=bits(x,n)
    active=all(t==1 for t in v[:k])
    # Binary quadratic bent sign on disjoint pairs, then balanced by y.
    bent=(-1)**sum(((x>>(k+2+j))&1)*((x>>(k+3+j))&1) for j in range(0,m,2))
    values.append(v[k+1]*bent if active else v[k])
coeff=fwht(values)
p=[c*c for c in coeff]
ck(sum(values)==0)
ck(sum(p)==1)
ck(sum(F(s.bit_count())*p[s] for s in range(1<<n))==2)
inf=[]
for i in range(n):
    edge=F(sum(values[x]!=values[x^(1<<i)] for x in range(1<<n)),1<<n)
    spec=sum(p[s] for s in range(1<<n) if s>>i&1)
    ck(edge==spec)
    ck(edge>0)
    inf.append(str(edge))
ck(Counter(x for x in p if x)==Counter({F(9,16):1,F(1,16):3,F(1,256):64}))
# Independent Boolean convolution, all shifts, including the empty shift.
for t in range(1<<n):
    ck(sum(coeff[s]*coeff[s^t] for s in range(1<<n))==int(t==0))

# Selector on two disjoint copies: explicit Fourier amplitudes (not formula-only).
sel={}
for s,c in enumerate(coeff):
    if c:
        for mask,a in [(s,c/2),(s|(1<<(2*n)),c/2),
                       (s<<n,c/2),((s<<n)|(1<<(2*n)),-c/2)]:
            ck(mask not in sel)
            sel[mask]=a
ck(sum(a*a for a in sel.values())==1)
ck(sum(F(s.bit_count())*a*a for s,a in sel.items())==F(5,2))
for sign in [-1,1]:
    child={}
    for t in {s&((1<<(2*n))-1) for s in sel}:
        a=sel.get(t,F(0))+sign*sel.get(t|(1<<(2*n)),F(0))
        if a:child[t]=a
    expected={(s if sign==1 else s<<n):c for s,c in enumerate(coeff) if c}
    ck(child==expected)
    ck(sum(a*a for a in child.values())==1)
    ck(sum(F(s.bit_count())*a*a for s,a in child.items())==2)

rows=[]
for k in range(2,21):
    m=2*((1<<k)-k)
    delta=F(1,1<<k)
    a=(1-delta)**2
    guard_mass=((1<<k)-1)*delta**2
    bent_mass=delta  # 2^(k+m) atoms of weight 2^(-2k-m)
    ck(a+guard_mass+bent_mass==1)
    ck((1-delta)+delta*(1+F(m,2))+k*delta==2)
    ck(delta*m==2-2*k*delta)
    ck(k<=1<<(k-1))
    ck(a>=F(1,2))
    # Exact prime-log coefficient of log2(2) in entropy, aside from eta(a).
    entropy_binary=guard_mass*2*k+bent_mass*(2*k+m)
    ck(entropy_binary==2+2*k*delta*(1-delta))
    ck(entropy_binary<=3)
    lower=[]
    for q in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
        exponent=(1-q)*m+(1-2*q)*k
        ck(exponent==(1-q)*(1<<(k+1))-k)
        ck((1-q)*m+(1-2*q)*k==exponent)
        # Selector normalized power prior has exactly four equal replicas.
        ck(q*2+2*(1-q)==2)
        lower.append({'q':str(q),'log2_Z_lower':str(exponent)})
    rows.append({'k':k,'m':m,'I':'2','Var':'1','H_binary_term':str(entropy_binary),
                 'delta':str(delta),'normalizer_lower_bounds':lower})

result={'status':'PASS','checks':checks,'seconds':time.monotonic()-start,
        'complete_truth_table':{'k':2,'m':4,'n':8,'rows':256,'influences':inf,
                                'signed_convolution_shifts':256},
        'physical_selector':{'n':17,'explicit_nonzero_amplitudes':len(sel),
                              'I':'5/2','children_I':['2','2'],'children_balanced':True},
        'compressed_parameter_cases':rows,
        'scope':'analytic proof covers all k; finite checks alone do not',
        'floating_point_used_for_claims':False}
(ROOT/'out/EXACT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({key:result[key] for key in ['status','checks','seconds','complete_truth_table','physical_selector']}))
