from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, random

ROOT=Path(__file__).resolve().parent
def solve(a,b):
    n=len(b); a=[[F(x) for x in row]+[F(y)] for row,y in zip(a,b)]
    for i in range(n):
        j=next(j for j in range(i,n) if a[j][i])
        a[i],a[j]=a[j],a[i]
        z=a[i][i]; a[i]=[x/z for x in a[i]]
        for j in range(n):
            if j!=i and a[j][i]:
                z=a[j][i]; a[j]=[x-z*y for x,y in zip(a[j],a[i])]
    return [row[-1] for row in a]

def expected(A):
    A=set(A); n=len(next(iter(A)))
    states=sorted({w[:i] for w in A for i in range(n)},key=lambda x:(len(x),x))
    index={w:i for i,w in enumerate(states)}
    a=[[F(int(i==j)) for j in range(len(states))] for i in range(len(states))]
    for i,s in enumerate(states):
        for bit in '01':
            t=s+bit
            if len(t)>=n and t[-n:] in A: continue
            u=max((x for x in states if t.endswith(x)),key=len)
            a[i][index[u]]-=F(1,2)
    return solve(a,[1]*len(states))[index['']]

def enlarged_density(A):
    n=len(next(iter(A))); A=set(A)
    count=sum(any(w[i:i+n] in A for i in range(n)) for w in words(2*n-1))
    return F(count,2**(2*n-1))

def words(n): return [''.join(x) for x in product('01',repeat=n)]

def matching_mean(A):
    n=len(A[0])
    # Source orientation: prefix of row word = suffix of column word.
    M=[[sum((F(1,2**l) for l in range(n) if u[:n-l]==v[l:]),F(0)) for v in A] for u in A]
    return F(2**n,1)/sum(solve(M,[1]*len(A)))

def run_stats(n,k):
    counts=[0]*k; counts[0]=1; survival=[]
    for t in range(n):
        survival.append(F(sum(counts),2**t))
        counts=[sum(counts)]+counts[:-1]
    p=1-F(sum(counts),2**n)
    et=F(2**(k+1)-2+n)-sum(survival)
    return p,et

def main():
    rng=random.Random(81); checked=0; matrix_checked=0
    report=[]
    for n in range(1,7):
        W=words(n)
        if n<=3:
            families=[[W[j] for j in range(len(W)) if mask>>j&1] for mask in range(1,2**len(W))]
        else:
            families=[W,[W[0]],[W[-1]],W[:len(W)//2]]
            for _ in range({4:80,5:25,6:8}[n]):
                families.append(rng.sample(W,rng.randint(1,min(len(W),20))))
        for A in families:
            p=F(len(A),2**n); q=enlarged_density(A); et=expected(A)
            assert max(F(n),1/(2*p))<=et<=n/p,(n,A,et,p)
            assert n/(2*q)<=et<=F(2*n-1)/q,(n,A,et,q)
            s=len(A).bit_length()-1
            assert q>=n*p/F(2*s+5),(n,A,p,q)
            assert et<=(4*s+10)/p,(n,A,et,p)
            if n<=4:
                assert et==matching_mean(A),(n,A,et)
                matrix_checked+=1
            checked+=1
        report.append({'n':n,'families_checked':len(families)})
    for n in range(1,9):
        W=words(n)
        for k in range(1,n+1):
            A=[w for w in W if '1'*k in w]
            p,et=run_stats(n,k)
            assert p==F(len(A),2**n)
            mu=F(n-k+2,2**(k+1))
            assert mu-mu*mu/2<=p<=mu
            if n<=6: assert expected(A)==et
            # Exhaustive finite histories check pathwise max(n,R_k).
            for w in words(n+3):
                r=next((t for t in range(k,len(w)+1) if w[t-k:t]=='1'*k),None)
                t=next((t for t in range(n,len(w)+1) if w[t-n:t] in A),None)
                assert t==(max(n,r) if r is not None and max(n,r)<=len(w) else None)
    equal=[]
    for n in range(4,11):
        k=min(n,(n*n-1).bit_length()); W=words(n)
        A=[w for w in W if '1'*k in w]; m=len(A)
        d=next(d for d in range(n+1) if 2**(n-d)<=m)
        C=[w for w in W if w.startswith('1'*d)]
        B=C+sorted(set(W)-set(C),reverse=True)[:m-len(C)]
        assert len(set(B))==m
        eb=expected(B); pa,ea=run_stats(n,k)
        assert n<=eb<=2**(d+1)-2+n-d
        equal.append({'n':n,'k':k,'m':m,'d':d,'E_A':str(ea),'E_B':str(eb)})
    asympt=[]
    for r in range(4,11):
        n=2**r; k=2*r; p,ea=run_stats(n,k)
        asympt.append({'n':n,'k':k,'n_p':float(n*p),'E_A_over_n2':float(ea/(n*n)),
                       'fast_bound_over_n':float((4/p+n)/n)})
    extremal_constructions=0
    for n in range(1,6):
        W=words(n)
        runs={k:set(w for w in W if '1'*k in w) for k in range(1,n+1)}
        for m in range(1,2**n+1):
            p=F(m,2**n); ceil_log=(m-1).bit_length()
            if m>=len(runs[1]):
                B=W[:m]
            else:
                k=next(k for k in range(1,n+1) if len(runs[k])<=m)
                B=sorted(runs[k])+sorted(runs[k-1]-runs[k])[:m-len(runs[k])]
                assert runs[k]<=set(B)<=runs[k-1]
            eb=expected(B)
            assert len(set(B))==m
            assert eb>=F(1+ceil_log,24)/p,(n,m,eb)
            d=next(d for d in range(n+1) if 2**(n-d)<=m)
            C=[w for w in W if w.startswith('1'*d)]
            Bmin=C+sorted(set(W)-set(C))[:m-len(C)]
            emin=expected(Bmin)
            assert len(set(Bmin))==m and emin<=n+4/p
            extremal_constructions+=1
    result={'all_assertions_passed':True,'total_families':checked,'matching_formula_checks':matrix_checked,
            'prescribed_cardinality_extremal_constructions_checked':extremal_constructions,
            'family_counts':report,'equal_cardinality_small_cases':equal,'asymptotics':asympt}
    ROOT.joinpath('checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
