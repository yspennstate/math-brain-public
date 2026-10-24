#!/usr/bin/env python3
from itertools import combinations, product
from fractions import Fraction

PRIMES = [13,17,29,37,41]

def qr_set(p):
    return {x*x % p for x in range(1,p)}

def chi(a,p,Q):
    a %= p
    if a == 0: return 0
    return 1 if a in Q else -1

def max_clique_normalized(p):
    Q=qr_set(p)
    H=[x for x in range(2,p) if x in Q and (x-1)%p in Q]
    adj={x:{y for y in H if y!=x and (x-y)%p in Q} for x in H}
    best=[]
    def rec(cands,cur):
        nonlocal best
        if len(cur)+len(cands)<=len(best): return
        if not cands:
            if len(cur)>len(best): best=cur[:]
            return
        cands=list(cands)
        while cands:
            if len(cur)+len(cands)<=len(best): return
            v=cands.pop()
            rec([u for u in cands if u in adj[v]],cur+[v])
    rec(H,[])
    return [0,1]+best

def check_prime(p):
    Q=qr_set(p)
    C=max_clique_normalized(p)
    k=len(C); q=1<<k; N=p-k

    counts={}
    for x in range(p):
        if x in C: continue
        eps=tuple(chi(x-c,p,Q) for c in C)
        assert all(e in (-1,1) for e in eps)
        counts[eps]=counts.get(eps,0)+1

    A={}; B={}
    for mask in range(q):
        T=[i for i in range(k) if (mask>>i)&1]
        a=b=0
        for x in range(p):
            v=1
            for i in T: v*=chi(x-C[i],p,Q)
            a+=v
            if x not in C: b+=v
        A[mask]=a; B[mask]=b
        assert b == a-(k-len(T))

    for eps in product([-1,1], repeat=k):
        s=0
        for mask in range(q):
            char=1
            for i in range(k):
                if (mask>>i)&1: char*=eps[i]
            s += B[mask]*char
        assert s % q == 0
        assert s//q == counts.get(eps,0)

    assert counts.get((1,)*k,0)==0

    ts=[]
    for x in range(p):
        if x in C: continue
        t=sum(1 for c in C if ((x-c)%p in Q))
        ts.append(t)
    s1=sum(ts)
    s2=sum(t*(t-1) for t in ts)
    rhs1=k*(p-2*k+1)//2
    rhs2=k*(k-1)*(p-4*k+3)//4
    assert s1==rhs1
    assert s2==rhs2

    for i in range(k):
        assert B[1<<i]==-(k-1)
    for i,j in combinations(range(k),2):
        assert B[(1<<i)|(1<<j)]==-(k-1)

    energy=sum(B[m]*B[m] for m in range(1,q))
    lower=Fraction(N*N,q-1)
    assert Fraction(energy,1) >= lower
    low12=(k + k*(k-1)//2)*(k-1)**2
    high=sum(B[m]*B[m] for m in range(1,q) if (m.bit_count()>=3))
    assert high == energy-low12
    high_lower=max(Fraction(0,1), lower-low12)
    assert Fraction(high,1)>=high_lower

    print(f"p={p} k={k} C={','.join(map(str,C))} N={N} "
          f"energy={energy} lower={lower} high={high} high_lower={high_lower} "
          f"S1={s1} S2={s2} PASS")

def check_parity_barrier():
    for k in range(3,9):
        support=[eps for eps in product([-1,1], repeat=k)
                 if __import__('math').prod(eps)==-1]
        assert (1,)*k not in support
        for mask in range(1,(1<<k)-1):
            s=0
            for eps in support:
                v=1
                for i in range(k):
                    if (mask>>i)&1: v*=eps[i]
                s+=v
            assert s==0
        full=sum(__import__('math').prod(eps) for eps in support)
        assert full==-len(support)
        print(f"parity_barrier k={k} support={len(support)} proper_coefficients_zero=PASS")

for p in PRIMES:
    check_prime(p)
check_parity_barrier()
print("ALL_I0099_BOOLEAN_FOURIER_SELF_CHECKS_PASS")
