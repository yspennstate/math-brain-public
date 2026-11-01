"""Independent integer FWHT and edge-pivotal check. Does not import producer."""
from pathlib import Path
from fractions import Fraction as Q
import json,time
R=Path(__file__).resolve().parents[1]
def fw(v):
    w=v[:];h=1
    while h<len(w):
        for i in range(0,len(w),2*h):
            for j in range(i,i+h):a,b=w[j],w[j+h];w[j],w[j+h]=a+b,a-b
        h*=2
    return w
count=0;start=time.perf_counter()
def check(ok):
    global count
    count+=1;assert ok
for k in range(1,9):
    n=k+1;N=1<<n
    values=[-1]+[1]*(N-1);w=fw(values)
    check(w[0]==N-2);check(all(abs(x)==2 for x in w[1:]))
    I=Q(sum(values[x]!=values[x^(1<<i)] for x in range(N) for i in range(n)),N)
    rho=Q(1,1<<k);check(I==n*rho)
    for J in range(1,N):check(Q(n)*(1-Q(w[J]*w[J],N*N))/I==1/rho-rho)
for d in range(2,7):
    for r in range(1,4):
        n=d*r
        if n>12:continue
        N=1<<n;mask=(1<<d)-1
        values=[]
        for x in range(N):
            value=1
            for j in range(r):
                block=(x>>(d*j))&mask
                value*=(-1 if block&1 else 1)*(-1 if block==0 else 1)
            values.append(value)
        w=fw(values);J=sum(1<<(d*j) for j in range(r));a=4*Q(1,1<<d)*(1-Q(1,1<<d))
        check(Q(w[J]*w[J],N*N)==(1-a)**r)
        check(sum(x*x for x in w)==N*N)
        if r*a<=1:check((1-Q(w[J]*w[J],N*N))/a>=Q(r,2))
# Independent all-essential sparse parity ghost witness, using integer FWHT
# and a literal table restriction (not the producer's coefficient channel).
for k in range(1,6):
    n=k+3;N=1<<n;rho=Q(1,1<<k)
    vals=[]
    for x in range(N):
        core=x>>k
        vals.append((-1 if core.bit_count()%2 else 1) if x&((1<<k)-1)==0 else 1)
    w=fw(vals);p=[Q(z*z,N*N) for z in w];q=[Q(0)]*N
    q[0]=(1-rho)**2
    for s in range(1,1<<k):q[s]=rho*rho
    # core frequency7=guard*x1*x2; reference-only frequency3=guard*x1
    for s in range(1<<k):
        q[s|(7<<k)]=rho*rho*Q(5,6)
        q[s|(3<<k)]=rho*rho*Q(1,6)
    check(sum(q)==1)
    pc=[]
    for y in range(2):
        vv=[v for x,v in enumerate(vals) if x%2==y];ww=fw(vv)
        pc.append([Q(z*z,len(vv)**2) for z in ww])
    pb=[p[2*t]+p[2*t+1] for t in range(N//2)]
    qb=[q[2*t]+q[2*t+1] for t in range(N//2)]
    ker=[[pc[y][t]/(2*pb[t]) if pb[t] else Q(1,2) for t in range(N//2)] for y in range(2)]
    rr=[sum(qb[t]*ker[y][t] for t in range(N//2)) for y in range(2)]
    check(rr==[Q(1,2)*(1-rho/6),Q(1,2)*(1+rho/6)])
    inherited_fail_empty=qb[0]*ker[1][0]/rr[1]
    check(inherited_fail_empty==Q(1,2)/rr[1])
    check(inherited_fail_empty<1)
    I=Q(sum(vals[x]!=vals[x^(1<<i)] for x in range(N) for i in range(n)),N)
    check(I==(k+3)*rho)
    check(all(any(vals[x]!=vals[x^(1<<i)] for x in range(N)) for i in range(n)))
# Boundary and common-factor interference checks: source-equal references,
# singleton absorption and tensor-anchor effect of a deterministic parity.
for n in range(1,7):
    for J in [0,1,(1<<n)-1]:
        v=[-1 if (x&J).bit_count()%2 else 1 for x in range(1<<n)]
        w=fw(v);check(w[J]==1<<n);check(sum(z!=0 for z in w)==1)
out=dict(status='PASS',checks=count,seconds=time.perf_counter()-start,arithmetic='integer FWHT; exact pivotal edge counts; Fraction',producer_imported=False)
R.joinpath('out/AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
