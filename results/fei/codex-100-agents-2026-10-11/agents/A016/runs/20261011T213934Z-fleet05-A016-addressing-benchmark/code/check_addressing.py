from fractions import Fraction as F
from math import comb, log2
from pathlib import Path
import json, time

RUN = Path(__file__).resolve().parents[1]
start = time.perf_counter()
checks = 0
def check(b):
    global checks
    assert b
    checks += 1

def fwht(v):
    v = list(v)
    h = 1
    while h < len(v):
        for i in range(0,len(v),2*h):
            for j in range(i,i+h):
                u,w=v[j],v[j+h]
                v[j],v[j+h]=u+w,u-w
        h*=2
    return v

def ln_interval(q, terms=40):
    q=F(q)
    assert q>0
    k=0
    while q>=2: q/=2; k+=1
    while q<1: q*=2; k-=1
    def core(x):
        z=(x-1)/(x+1)
        total=sum((2*z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
        tail=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
        return total,total+tail
    lo,hi=core(q)
    l2,h2=core(F(2))
    return (lo+k*l2,hi+k*h2) if k>=0 else (lo+k*h2,hi+k*l2)

def log2_interval(q):
    lo,hi=ln_interval(q)
    l2,h2=ln_interval(2)
    assert lo>=0
    return lo/h2,hi/l2

tables=[]
for a in range(4):
    N=1<<a; n=a+N; size=1<<n
    truth=[1-2*((z>>(a+(z&(N-1))))&1) for z in range(size)]
    walsh=fwht(truth)
    spectral=[F(t*t,size*size) for t in walsh]
    expected={t | (1<<(a+u)): F(1,N*N) for u in range(N) for t in range(N)}
    for mask,p in enumerate(spectral): check(p==expected.get(mask,F(0)))
    check(sum(spectral)==1)
    influence=[]
    for j in range(n):
        edge=F(sum(truth[z]!=truth[z^(1<<j)] for z in range(size)),size)
        spec=sum((p for s,p in enumerate(spectral) if s&(1<<j)),F(0))
        check(edge==spec)
        check(edge==(F(1,2) if j<a else F(1,N)))
        influence.append(str(edge))
    H=sum((p*(2*a) for p in spectral if p),F(0))
    I=sum((p*s.bit_count() for s,p in enumerate(spectral)),F(0))
    check(H==2*a); check(I==1+F(a,2))
    tables.append(dict(a=a,n=n,rows=size,atoms=len(expected),H=str(H),I=str(I),influences=influence))

models=[]
for a in range(7):
    N=1<<a; I=1+F(a,2)
    mass=F(1,N*N)
    total=F(0); repeated=F(0); optimal=F(0)
    for u in range(N):
        for t in range(N):
            # Actual decoder: read a mask bits, then s address words in canonical coordinate order.
            mask=f'{t:0{a}b}' if a else ''
            label=f'{u:0{a}b}' if a else ''
            s=1+t.bit_count()
            bad=mask+label*s
            good=label+mask
            check(len(bad)==a*(s+1)); check(len(good)==2*a)
            check((int(good[:a],2),int(good[a:],2))==(u,t) if a else good=='')
            total+=mass; repeated+=mass*len(bad); optimal+=mass*len(good)
    check(total==1); check(repeated==a*(I+1)); check(optimal==2*a)
    pressure=F(7,2)*a*a+F(11,5)*a if a else F(0)
    models.append(dict(a=a,H=str(2*a),I=str(I),repeated_label_only=str(a*I),repeated_complete=str(repeated),optimal_complete=str(optimal),fractional_pressure=str(pressure)))

ranks=[]
for a in [0,1,2,4,8,16,32]:
    # R_a = E sum_{j in A} log2(rank/(selected predecessors+1)); each selector occurs with probability 1/2.
    lo=F(0); hi=F(0)
    for r in range(1,a+2):
        inclusion=F(1,2) if r<=a else F(1)
        weights=[F(comb(r-1,k),2**(r-1)) for k in range(r)]
        check(sum(weights)==1)
        reciprocal=sum((w/F(k+1) for k,w in enumerate(weights)),F(0))
        check(reciprocal==F(2,r)*(1-F(1,2**r)))
        for k,w in enumerate(weights):
            l,h=log2_interval(F(r,k+1))
            lo+=inclusion*w*l; hi+=inclusion*w*h
    I=1+F(a,2)
    check(lo>=0); check(hi<=I)
    ranks.append(dict(a=a,R_lower=str(lo),R_upper=str(hi),R_interval_decimal=[float(lo),float(hi)],I=str(I)))

result=dict(helper_version='A016-addressing-check/1',assertions=checks,failed=0,truth_tables=tables,symbolic_models=models,rank_certificates=ranks,elapsed_seconds=time.perf_counter()-start,arithmetic='exact integer/Fraction; rigorously bounded logarithms',full_fei='OPEN')
(RUN/'out'/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['helper_version','assertions','failed','elapsed_seconds','full_fei']}))
