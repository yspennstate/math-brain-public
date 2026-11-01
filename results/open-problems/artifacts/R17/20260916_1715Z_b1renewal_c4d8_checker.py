#!/usr/bin/env python3
"""
R17 exact self-check for C008 (bounded-span B=1 renewal saturation).

No Monte Carlo.

Analytic theorem checked:
For every integer m>=2, if Q_{m,1} is the bounded-span primal from R17-C006,
then q_{m,1}=lim_r E Q_{m,1}(X_1^{mr},Y_1^{mr})/(mr)=1/m.

The proof uses:
- pathwise dual/capacity bound Q_{m,1}<=r;
- greedy all-block matching lower bound;
- iid waiting times W with
  P(block mixed)=1-2^(1-m), W=1;
  P(block constant)=2^(1-m), W~Geom(1/2) on {1,2,...};
- exact Chernoff point x=4/3:
  rho_m=E[x^(W-m)]=(3/4)^(m-1)*(1+2^(-m))<1.
Then
  0 <= 1/m - E Q_{m,1}/(mr) <= rho_m^r/m.

Finite checks:
- exact Q DP versus brute packing for small m,r;
- greedy success implies Q=r;
- exact finite failure probabilities satisfy the claimed Chernoff bound.
"""
from itertools import product
from fractions import Fraction
from functools import lru_cache

def lcs(x,y):
    d=[0]*(len(y)+1)
    for a in x:
        prev=0
        for j,b in enumerate(y,1):
            old=d[j]
            d[j]=prev+1 if a==b else max(d[j],d[j-1])
            prev=old
    return d[-1]

def q_dp_b1(x,y,m):
    assert len(x)%m==0
    r=len(x)//m
    n=len(y)
    D=[[0]*(n+1) for _ in range(r+1)]
    for j in range(1,r+1):
        block=x[(j-1)*m:j*m]
        aset=set(block)
        for t in range(1,n+1):
            w=1 if y[t-1] in aset else 0
            D[j][t]=max(D[j][t-1], D[j-1][t], D[j-1][t-1]+w)
    return D[r][n]

def q_brute_b1(x,y,m):
    assert len(x)%m==0
    r=len(x)//m
    n=len(y)
    @lru_cache(None)
    def rec(j,start):
        if j==r:
            return 0
        aset=set(x[j*m:(j+1)*m])
        best=rec(j+1,start)
        for t in range(start,n):
            best=max(best, (1 if y[t] in aset else 0)+rec(j+1,t+1))
        return best
    return rec(0,0)

def greedy_all_success(x,y,m):
    assert len(x)%m==0
    pos=0
    r=len(x)//m
    for j in range(r):
        aset=set(x[j*m:(j+1)*m])
        while pos<len(y) and y[pos] not in aset:
            pos+=1
        if pos==len(y):
            return False
        pos+=1
    return True

checks=0
for m,r in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3)]:
    n=m*r
    for x in product((0,1),repeat=n):
        for y in product((0,1),repeat=n):
            q=q_dp_b1(x,y,m)
            if n<=6:
                assert q==q_brute_b1(x,y,m)
            assert q<=r
            if greedy_all_success(x,y,m):
                assert q==r
            checks+=1
print("C008 finite structure PASS")
print("  exact (x,y,m,r) instances:", checks)

for m in range(2,41):
    c=Fraction(1,2**(m-1))
    x=Fraction(4,3)
    mgf=(1-c)*x + c*x/(2-x)
    rho=mgf/(x**m)
    closed=(Fraction(3,4)**(m-1))*(1+Fraction(1,2**m))
    assert rho==closed
    assert rho<1
print("C008 Chernoff factor PASS for m=2..40")
print("  rho_2 =", Fraction(15,16))

def fail_prob(m,r):
    n=m*r
    bad=0
    total=2**(2*n)
    for x in product((0,1),repeat=n):
        for y in product((0,1),repeat=n):
            bad += int(not greedy_all_success(x,y,m))
    return Fraction(bad,total)

finite=[]
for m,rmax in [(2,4),(3,3)]:
    rho=(Fraction(3,4)**(m-1))*(1+Fraction(1,2**m))
    for r in range(1,rmax+1):
        p=fail_prob(m,r)
        assert p<=rho**r
        finite.append((m,r,p,rho**r))
print("C008 exact finite failure-vs-Chernoff PASS")
for m,r,p,b in finite:
    print(f"  m={m}, r={r}: P_fail={p}, bound={b}")

print("PASS")
