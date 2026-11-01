import json,time
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from search import spectrum,restrict

ROOT=Path(__file__).resolve().parents[1]

@lru_cache(None)
def factors(n):
    out=[];d=2
    while d*d<=n:
        k=0
        while n%d==0: n//=d;k+=1
        if k:out.append((d,k))
        d+=1
    if n>1:out.append((n,1))
    return tuple(out)

def alternative_spectrum(table,ms):
    # Tensor transform in the unnormalized centered basis, not weighted sums.
    a=list(map(F,table));n=len(ms)
    for i,m in enumerate(ms):
        p=F(m,8)
        for x in range(1<<n):
            if not x>>i&1:
                y=x|(1<<i);u,v=a[x],a[y]
                a[x]=(1-p)*u+p*v;a[y]=v-u
    return tuple(a[s]**2*__import__('math').prod(F(ms[i]*(8-ms[i]),64) for i in range(n) if s>>i&1) for s in range(1<<n))

def run():
    start=time.perf_counter();data=json.loads((ROOT/'out/search.json').read_text());certs=[];remaining=[]
    for row in data['unresolved']:
        ms=tuple(row['bias_numerators_over_8']);code=row['code'];mask=row['block_mask']
        table=tuple(1 if x==0 or not(code>>(x-1)&1) else -1 for x in range(8))
        parent=spectrum(table,ms);assert parent==alternative_spectrum(table,ms)
        A=[i for i in range(3) if mask>>i&1];B=[i for i in range(3) if not mask>>i&1]
        q=tuple(sum(parent[s] for s in range(8) if sum(((s>>i)&1)<<j for j,i in enumerate(B))==t) for t in range(1<<len(B)))
        logs=defaultdict(F)
        def log(p,c):
            if p and c:logs[p]+=c
        def ent(dist,c):
            for p in dist:log(p,-c*p)
        ent(parent,F(1));ent(q,F(-2))
        for z in range(1<<len(A)):
            w=F(__import__('math').prod(ms[i] if z>>j&1 else 8-ms[i] for j,i in enumerate(A)),8**len(A))
            ent(restrict(table,ms,A,z),w)
        for i in A:
            p=F(ms[i],8);ent((p,1-p),F(1));log(max(p,1-p),F(1))
        primes=defaultdict(F)
        for p,c in logs.items():
            for r,k in factors(p.numerator):primes[r]+=c*k
            for r,k in factors(p.denominator):primes[r]-=c*k
        nonzero={str(r):str(c) for r,c in primes.items() if c}
        receipt={'code':code,'bias_numerators_over_8':ms,'block_mask':mask,'nonzero_prime_log_coefficients':nonzero,'alternative_spectrum_matched':True}
        (remaining if nonzero else certs).append(receipt)
        if time.perf_counter()-start>55:raise RuntimeError('55 second cap')
    result={'input_cases':len(data['unresolved']),'exact_zero_certificates':len(certs),'remaining':remaining,'certificates':certs,'runtime_seconds':time.perf_counter()-start,'method':'D=sum_r c_r log2(r); every prime coefficient exactly zero; alternate centered tensor transform matches original parent spectrum'}
    (ROOT/'out/zero_certificates.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='certificates'},indent=2))

if __name__=='__main__':run()
