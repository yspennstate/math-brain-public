from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, time

START=time.monotonic()
COUNT=0
def ck(x):
    global COUNT
    COUNT+=1
    assert x
    assert time.monotonic()-START<55, 'frozen runtime cap'
def add(x,y): return x[0]+y[0],x[1]+y[1]
def scale(c,x): return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def sub(x,y): return add(x,scale(-1,y))
def lnsmall(x):
    z=(x-1)/(x+1)
    assert 0<=z<=F(1,3)
    s=sum((z**(2*j+1)/F(2*j+1) for j in range(44)),F(0))*2
    tail=2*z**89/(89*(1-z*z))
    return s,s+tail
LN2=lnsmall(F(2))
@lru_cache(None)
def logint(v):
    e=v.bit_length()-1
    # Tiny entropy terms at k=32 need absolute precision beyond 2^-63.
    # The first pilot's 56-bit enclosure was too wide; retain 128 bits.
    shift=max(0,e-128)
    lo=F(v>>shift,1<<(e-shift))
    hi=lo if not shift or v==(v>>shift)<<shift else lo+F(1,1<<(e-shift))
    l=lnsmall(lo)[0]/LN2[1]+e
    h=lnsmall(hi)[1]/LN2[0]+e
    return l,h
@lru_cache(None)
def lg(x):
    assert x>0
    lo,hi=sub(logint(x.numerator),logint(x.denominator))
    unit=1<<80
    return F((lo*unit).__floor__(),unit),F((hi*unit).__ceil__(),unit)
def H(p):
    ans=(F(0),F(0))
    for x in p:
        if x: ans=add(ans,scale(-x,lg(x)))
    return ans
def KL(p,q):
    ans=(F(0),F(0))
    for x,y in zip(p,q):
        if x: ans=add(ans,scale(x,lg(x/y)))
    return ans
def occ(s,k): return sum(bool(s&(3<<(2*j)))<<j for j in range(k))
def fwht(a):
    a=a[:]; h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a
rows=[]
for k in [2,3,4]:
    n=2*k; N=1<<n; d=F(2,N); t=3*d/2
    W=fwht([-1]+[1]*(N-1)); p=[F(w*w,N*N) for w in W]
    ck(sum(p)==1); ck(p[0]==(1-d)**2); ck(all(x==d*d for x in p[1:]))
    for i in range(n):
        ck(sum(p[s] for s in range(N) if s>>i&1)==d)
        physical=F(sum((s==0)!=((s^(1<<i))==0) for s in range(N)),N)
        ck(physical==d)
    Q=[d**s.bit_count()*(1-d)**(n-s.bit_count()) for s in range(N)]
    rz=[sum(p[s] for s in range(N) if occ(s,k)==z) for z in range(1<<k)]
    a=2*d-d*d
    qz=[a**z.bit_count()*(1-a)**(k-z.bit_count()) for z in range(1<<k)]
    ck(rz[0]==(1-d)**2)
    ck(all(rz[z]==d*d*3**z.bit_count() for z in range(1,1<<k)))
    R=[rz[occ(s,k)]*Q[s]/qz[occ(s,k)] for s in range(N)]
    ck(sum(R)==1); ck(all(x>0 for x in R))
    prodR=[F(1)]*N; local=(F(0),F(0))
    for j in range(k):
        pj=[sum(p[s] for s in range(N) if (s>>(2*j))&3==v) for v in range(4)]
        rj=[sum(R[s] for s in range(N) if (s>>(2*j))&3==v) for v in range(4)]
        qj=[(1-d)**2,d*(1-d),d*(1-d),d*d]
        ck(pj[0]==1-t); ck(pj[0]>=qj[0]); ck(rj[0]==pj[0])
        ck(all(rj[v]/t==qj[v]/a for v in [1,2,3]))
        for s in range(N): prodR[s]*=rj[(s>>(2*j))&3]
        # T_j is computed independently from four source atoms.
        tj=sub(KL(pj,qj),KL(pj,rj))
        bj=KL([1-t,t],[1-a,a])
        ck(tj[0]<=bj[1] and bj[0]<=tj[1])
        local=add(local,tj)
    globalT=sub(KL(p,Q),KL(p,R)); sector=KL(rz,qz)
    coupling=(F(0),F(0))
    for s in range(N): coupling=add(coupling,scale(p[s],lg(R[s]/prodR[s])))
    tc=sub(scale(k,H([1-t,t])),H(rz))
    ck(globalT[0]<=sector[1] and sector[0]<=globalT[1])
    ck(coupling[0]<=tc[1] and tc[0]<=coupling[1])
    rhs=add(local,coupling)
    ck(globalT[0]<=rhs[1] and rhs[0]<=globalT[1])
    # Falsification controls: replacing R by the product of its actual block
    # marginals MUST remove the large coupling, without changing local terms.
    productT=sub(KL(p,Q),KL(p,prodR))
    ck(productT[0]<=local[1] and local[0]<=productT[1])
    ck(productT[1] < F(3,2)*n*d)
    # R=p (the known arbitrary-reference obstruction) does NOT have the
    # required lambda=1 pair-conditional shape: our reference is different.
    ck(pj[3]/t != qj[3]/a)
    I=n*d
    lb=F(3*k,2)-F(9,2)-F(1,2*k)
    ck(tc[0]>lb*I)
    rows.append({'kind':'full_boolean','k':k,'atoms':N,'C_over_I_interval':[str(v/I) for v in tc],'T_over_I_interval':[str(v/I) for v in globalT]})
for k in [2,3,4,8,16,32]:
    n=2*k; d=F(1,1<<(n-1)); t=3*d/2; rho=2*d-d*d; p0=(1-d)**2
    hz=add(add(scale(-p0,lg(p0)),scale(-2*rho,lg(d))),scale(-k*t,lg(F(3))))
    tc=sub(scale(k,H([1-t,t])),hz)
    T=sub(scale(-k,add(scale(1-t,lg(p0)),scale(t,lg(rho)))),hz)
    I=n*d; bound=F(3*k,2)-F(9,2)-F(1,2*k)
    ck(tc[0]>bound*I); ck(T[1]>=tc[0]); ck(1-t>=p0)
    rows.append({'kind':'compressed_exact','k':k,'C_over_I_interval':[str(v/I) for v in tc],'T_over_I_interval':[str(v/I) for v in T],'proved_analytic_lower_bound':str(bound)})
out={'status':'PASS','assertions':COUNT,'runtime_seconds':time.monotonic()-START,'rows':rows,'arithmetic':'Fraction; rational logarithm intervals with explicit atanh remainder, normalized integer mantissa enclosure, outward dyadic rounding'}
dest=Path(__file__).resolve().parents[1]/'out'/'checks.json'
dest.parent.mkdir(exist_ok=True)
dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'assertions':COUNT,'runtime_seconds':out['runtime_seconds'],'output':str(dest)}))
