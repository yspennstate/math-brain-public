"""Exact certificates for the frozen anchored overlapping-composition family."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import itertools, json, time, argparse

RUN=Path(__file__).resolve().parents[1]
checks=0
def check(cond):
    global checks
    checks+=1
    if not cond: raise AssertionError(checks)

def walsh(a):
    a=list(a); h=1
    while h<len(a):
        for start in range(0,len(a),2*h):
            for j in range(start,start+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def table(t,n): return [1-2*((t>>x)&1) for x in range(1<<n)]
def influence_numer(w): return sum(s.bit_count()*a*a for s,a in enumerate(w))
def factors(n):
    ans={}; p=2
    while p*p<=n:
        while n%p==0: ans[p]=ans.get(p,0)+1; n//=p
        p+=1
    if n>1: ans[n]=ans.get(n,0)+1
    return ans

def mass_entropy(masses,D):
    # H = log2(D) - sum_c (c/D) log2(c), exactly as a prime-log vector.
    check(sum(masses)==D)
    ans=Counter({p:Q(v) for p,v in factors(D).items()})
    for c in masses:
        if c:
            for p,v in factors(c).items(): ans[p]-=Q(c*v,D)
    return {p:v for p,v in ans.items() if v}

def plus(a,b,scale=Q(1)):
    a=dict(a)
    for p,v in b.items():a[p]=a.get(p,Q(0))+scale*v
    return {p:v for p,v in a.items() if v}

def one(F,bs,rows,entropy=True):
    m=(len(F)).bit_length()-1; r=len(bs); n=m+2*r; N=1<<n
    fw=walsh(F); bw=[walsh(b) for b in bs]
    u=[sum(((T&row).bit_count()%2)<<j for j,row in enumerate(rows)) for T in range(1<<m)]
    truth=[]
    for physical in range(N):
        outer=physical&((1<<m)-1)
        for j,row in enumerate(rows):
            if bs[j][(physical>>(m+2*j))&3]==-1:outer^=row
        truth.append(F[outer])
    actual=walsh(truth)
    expected=[0]*N
    for T in range(1<<m):
        active=[j for j in range(r) if (u[T]>>j)&1]
        for support in itertools.product(*[range(4) if j in active else [0] for j in range(r)]):
            a=fw[T]*(1<<(2*(r-len(active))))
            for j in active:a*=bw[j][support[j]]
            physical=T+sum(s<<(m+2*j) for j,s in enumerate(support))
            expected[physical]=a
    for a,e in zip(actual,expected):check(a==e)
    D=N*N; DF=len(F)**2; db=[Q(sum(fw[T]**2 for T in range(1<<m) if (u[T]>>j)&1),DF) for j in range(r)]
    I=Q(influence_numer(actual),D)
    expectedI=Q(influence_numer(fw),DF)+sum(db[j]*Q(influence_numer(bw[j]),16) for j in range(r))
    check(I==expectedI)
    for i in range(n):
        edge=Q(sum(truth[x]!=truth[x^(1<<i)] for x in range(N)),N)
        spec=Q(sum(a*a for s,a in enumerate(actual) if (s>>i)&1),D)
        check(edge==spec)
        if i<m:check(spec==Q(sum(a*a for T,a in enumerate(fw) if (T>>i)&1),DF))
        else:
            j,k=divmod(i-m,2)
            check(spec==db[j]*Q(sum(a*a for S,a in enumerate(bw[j]) if (S>>k)&1),16))
    for j,row in enumerate(rows):
        d_spatial=Q(sum(F[y]!=F[y^row] for y in range(1<<m)),1<<m)
        check(db[j]==d_spatial)
    if entropy:
        H=mass_entropy([a*a for a in actual],D)
        HF=mass_entropy([a*a for a in fw],DF)
        rhs=HF
        for j in range(r):rhs=plus(rhs,mass_entropy([a*a for a in bw[j]],16),db[j])
        check(H==rhs)
        q=[sum(fw[T]**2 for T in range(1<<m) if u[T]==v) for v in range(1<<r)]
        HQ=mass_entropy(q,DF)
        B={}
        for v,c in enumerate(q):
            if c:B=plus(B,mass_entropy([fw[T]**2 for T in range(1<<m) if u[T]==v],c),Q(c,DF))
        check(plus(HQ,B)==HF)
        debt_rhs=plus(HQ,B)
        for j in range(r):debt_rhs=plus(debt_rhs,mass_entropy([a*a for a in bw[j]],16),db[j])
        check(debt_rhs==H)
        # The frozen finite gates have entropies that are rational integers.
        check(set(H).issubset({2}))
        check(H.get(2,0)<=2*I)
    return I

def nonlinear_examples():
    b=table(8,2)
    records=[]
    for k in range(1,5):
        m=2*k; n=m+2; N=1<<n
        def outer(y):
            ans=1
            for j in range(k):ans*=b[(y>>(2*j))&3]
            return ans
        F=[outer(y) for y in range(1<<m)]
        w=walsh([outer((x&((1<<m)-1))^(((1<<m)-1) if b[(x>>m)&3]==-1 else 0)) for x in range(N)])
        H=mass_entropy([a*a for a in w],N*N); I=Q(influence_numer(w),N*N)
        check(H=={2:Q(2*k+1)}); check(I==Q(2*k+1,2))
        fw=walsh(F); q=[sum(a*a for T,a in enumerate(fw) if T.bit_count()%2==v) for v in [0,1]]
        check(q==[2**(4*k-1)]*2)
        records.append({'k':k,'H_bits':2*k+1,'I':str(I),'posterior_bits':2*k-1})
    # Exact cancellation at m=2: outer parity, both children use b.
    one([1,-1,-1,1],[b],[3])
    return records

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',choices=['pilot','main'],required=True); mode=ap.parse_args().mode
    spec=json.loads((RUN/'out/FROZEN_SPEC.json').read_text()); start=time.perf_counter()
    tables=[table(t,2) for t in range(16)]; r=1 if mode=='pilot' else 2; count=0
    for F in tables:
        for bs in itertools.product(tables,repeat=r):
            for rows in itertools.product(range(4),repeat=r):
                one(F,bs,rows); count+=1
        if time.perf_counter()-start>spec[mode]['max_runtime_seconds']:raise RuntimeError('Frozen runtime exceeded')
    check(count==spec[mode]['case_count'])
    examples=nonlinear_examples()
    output={'mode':mode,'case_count':count,'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'integer Walsh, Fraction, exact prime-log vectors','result':'PASS','nonlinear_family':examples}
    (RUN/'out'/f'{mode}_results.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
    print(json.dumps(output))

if __name__=='__main__':main()
