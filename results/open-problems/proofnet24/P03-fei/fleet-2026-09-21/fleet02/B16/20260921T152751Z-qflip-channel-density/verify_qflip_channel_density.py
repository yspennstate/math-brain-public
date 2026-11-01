#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import json, random

def parity(x): return x.bit_count() & 1

def walsh_int(vals):
    a=list(vals)
    h=1
    n=len(a)
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return a

def influences(vals,n):
    N=1<<n
    out=[]
    for i in range(n):
        out.append(Fraction(sum(vals[x]!=vals[x^(1<<i)] for x in range(N)),N))
    return out

def deriv(vals,n,i):
    N=1<<n
    return [vals[x]*vals[x^(1<<i)] for x in range(N)]

def K_direct(n,k):
    # m=n-1 coordinates; use the first k as a representative Fourier support
    m=n-1
    smask=(1<<k)-1
    tot=Fraction()
    for w in range(1<<m):
        tot += Fraction(1 - (-1 if parity(w&smask) else 1), w.bit_count()+1)
    return tot

def K_integral_combinatorial(n,k):
    # exact integral expanded by binomial coefficients
    from math import comb
    m=n-1
    # first integral
    A=Fraction((1<<(m+1))-1,m+1)
    # integral (1-t)^k (1+t)^(m-k)
    B=Fraction()
    for a in range(k+1):
        ca=comb(k,a)*((-1)**a)
        for b in range(m-k+1):
            cb=comb(m-k,b)
            B += Fraction(ca*cb,a+b+1)
    return A-B

def q_direct(vals,n):
    N=1<<n
    total=Fraction()
    for v in range(1,N):
        kv=v.bit_count()
        if kv<2: continue
        for i in range(n):
            if not ((v>>i)&1): continue
            active=sum(vals[a]*vals[a^(1<<i)]*vals[a^v]*vals[(a^v)^(1<<i)] == -1 for a in range(N))
            total += Fraction(active, N*kv)
    return total

def q_spectral(vals,n):
    N=1<<n
    total=Fraction()
    for i in range(n):
        d=deriv(vals,n,i)
        W=walsh_int(d)
        for S,z in enumerate(W):
            if S==0 or ((S>>i)&1) or z==0: continue
            # derivative invariance makes coefficients with i in S zero
            k=S.bit_count()
            total += Fraction(1,2)*Fraction(z*z,N*N)*K_direct(n,k)
    return total

def bounds(vals,n):
    ps=influences(vals,n)
    s=sum((p*(1-p) for p in ps),Fraction())
    J=sum((min(p,1-p) for p in ps),Fraction())
    N=1<<n
    alpha=Fraction(2*((1<<(n-1))*(n-2)+1),n*(n-1))
    beta=Fraction(N-2,n)
    return alpha,beta,2*alpha*s,2*beta*s,alpha*J,2*beta*J,J

def vals_from_mask(mask,n):
    N=1<<n
    return [-1 if ((mask>>x)&1) else 1 for x in range(N)]

def char_twist(vals,n,A):
    return [vals[x]*(-1 if parity(A&x) else 1) for x in range(1<<n)]

def q_pair(n):
    assert n%2==0
    vals=[]
    for x in range(1<<n):
        b=0
        for i in range(0,n,2):
            b ^= ((x>>i)&1)&((x>>(i+1))&1)
        vals.append(-1 if b else 1)
    return vals

def q_complete(n):
    assert n%2==0
    vals=[]
    for x in range(1<<n):
        b=0
        for i in range(n):
            for j in range(i+1,n):
                b ^= ((x>>i)&1)&((x>>j)&1)
        vals.append(-1 if b else 1)
    return vals

checks=0
# multiplier identity and monotonicity
for n in range(2,11):
    ks=[K_direct(n,k) for k in range(1,n)]
    assert ks==sorted(ks)
    for k,Kv in enumerate(ks,1):
        assert Kv==K_integral_combinatorial(n,k)
        checks+=1
    alpha=Fraction(2*((1<<(n-1))*(n-2)+1),n*(n-1))
    beta=Fraction((1<<n)-2,n)
    assert ks[0]==alpha and ks[-1]==beta

# exhaustive Boolean functions n<=3
function_checks=0
for n in (2,3):
    for mask in range(1<<(1<<n)):
        vals=vals_from_mask(mask,n)
        q1=q_direct(vals,n); q2=q_spectral(vals,n)
        assert q1==q2
        alpha,beta,lo,hi,loJ,hiJ,J=bounds(vals,n)
        assert lo <= q1 <= hi
        assert loJ <= q1 <= hiJ
        # all character twists preserve q-flip activity count
        for A in range(1<<n):
            assert q_direct(char_twist(vals,n,A),n)==q1
        function_checks += 1

# deterministic exact n=4 sample
rng=random.Random(20260921)
sample_checks=0
for _ in range(512):
    mask=rng.getrandbits(16)
    vals=vals_from_mask(mask,4)
    q1=q_direct(vals,4); q2=q_spectral(vals,4)
    assert q1==q2
    alpha,beta,lo,hi,loJ,hiJ,J=bounds(vals,4)
    assert lo <= q1 <= hi and loJ <= q1 <= hiJ
    sample_checks += 1

extremals={}
for n in (2,4,6,8):
    for name,make in (("matching_quadratic",q_pair),("complete_quadratic",q_complete)):
        vals=make(n)
        qv=q_spectral(vals,n)
        alpha,beta,lo,hi,loJ,hiJ,J=bounds(vals,n)
        target=(alpha*J if name=="matching_quadratic" else beta*J)
        assert qv==target
        extremals[f"{name}_n{n}"]={
            "Q":str(qv),"J":str(J),"Q_over_J":str(qv/J) if J else None,
            "alpha":str(alpha),"beta":str(beta)
        }
        checks+=1

out={
    "status":"PASS",
    "scope":"self_check_only",
    "multiplier_exact_checks":checks,
    "exhaustive_boolean_function_checks":function_checks,
    "deterministic_n4_sample_checks":sample_checks,
    "extremals":extremals,
}
print(json.dumps(out,indent=2,sort_keys=True))
