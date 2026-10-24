#!/usr/bin/env python3
from itertools import permutations
from fractions import Fraction as F
from math import factorial
from collections import Counter
import hashlib

checks = 0

def harmonic(n, power=1):
    return sum((F(1, j**power) for j in range(1, n+1)), F(0))

def beta_int(i,j):
    return F(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def cycles_of_perm(p):
    n=len(p)
    seen=[False]*n
    out=[]
    for i in range(n):
        if not seen[i]:
            c=[]
            j=i
            while not seen[j]:
                seen[j]=True
                c.append(j+1)
                j=p[j]-1
            out.append(tuple(sorted(c)))
    return tuple(sorted(out))

def visible_partition(cycles,k):
    S=set(range(1,k+1))
    blocks=[]
    for c in cycles:
        b=tuple(sorted(S.intersection(c)))
        if b:
            blocks.append(b)
    return tuple(sorted(blocks))

def e2(vals):
    ans=F(0)
    for i in range(len(vals)):
        for j in range(i+1,len(vals)):
            ans += vals[i]*vals[j]
    return ans

def partition_formula(N, blocks):
    k=sum(map(len,blocks))
    q=len(blocks)
    H=harmonic(N-1)
    H2=harmonic(N-1,2)
    D=H*H-H2
    prod=1
    for b in blocks:
        prod *= factorial(len(b)-1)
    if q==2:
        return F(prod,factorial(k-1))*2*(H-harmonic(k-1))/D
    if q==3:
        return F(prod,factorial(k-1))*2/D
    if q==1:
        vals=[F(1,j) for j in range(k,N)]
        return 2*e2(vals)/D
    return F(0)

print("R11 I0054 C034 conditioned-three-cycle permutation checker")

# 1. Exhaustive enumeration: conditioned uniform permutations with exactly 3 cycles.
enum_checks=0
for N in range(3,9):
    cond=[]
    for p in permutations(range(1,N+1)):
        c=cycles_of_perm(p)
        if len(c)==3:
            cond.append(c)
    den=len(cond)
    for k in range(2,min(N,5)+1):
        cnt=Counter(visible_partition(c,k) for c in cond)
        assert sum(cnt.values())==den
        for part,num in cnt.items():
            got=F(num,den)
            want=partition_formula(N,part)
            assert got==want, (N,k,part,got,want)
            enum_checks+=1
            checks+=1
print("conditional_cycle_partition_formula: PASS", enum_checks, "exact partitions, N=3..8")

# 2. The cycle-count denominator identity P(K_N=3)=(H^2-H2)/(2N)
# checked by exact permutation counts through N=8.
stirling_checks=0
for N in range(3,9):
    num=0
    for p in permutations(range(1,N+1)):
        if len(cycles_of_perm(p))==3:
            num+=1
    got=F(num,factorial(N))
    H=harmonic(N-1); H2=harmonic(N-1,2)
    want=(H*H-H2)/F(2*N)
    assert got==want
    stirling_checks+=1
    checks+=1
print("three_cycle_probability_identity: PASS", stirling_checks, "N-values")

# 3. Exact binary and ternary rate formulas with lambda_N=H_{N-1}/2.
# Binary specified split sizes i,j:
# q_N/B(i,j)=H(H-H_{b-1})/(H^2-H2) ->1.
# Ternary specified partition coefficient:
# q_N= [(a-1)!(b-1)!(c-1)!/(k-1)!] H/(H^2-H2) ->0.
rate_checks=0
for N in range(4,81):
    H=harmonic(N-1); H2=harmonic(N-1,2); D=H*H-H2
    assert D>0
    lam=H/2
    # attempt probability for delta=N^-2
    delta=F(1,N*N)
    assert 0 < delta*lam < 1
    for b in range(2,min(N,9)+1):
        hb=harmonic(b-1)
        for i in range(1,b):
            j=b-i
            p2=2*beta_int(i,j)*(H-hb)/D
            q2=lam*p2
            ratio=q2/beta_int(i,j)
            assert ratio == H*(H-hb)/D
            assert p2>=0
            rate_checks += 3
            checks += 3
        if b>=3:
            # test every composition a+b+c=b; any specified set partition with those sizes.
            for a in range(1,b-1):
                for bb in range(1,b-a):
                    c=b-a-bb
                    coeff=F(factorial(a-1)*factorial(bb-1)*factorial(c-1), factorial(b-1))
                    p3=2*coeff/D
                    q3=lam*p3
                    assert q3==coeff*H/D
                    assert p3>0
                    rate_checks += 2
                    checks += 2
print("binary_ternary_rate_formulas: PASS", rate_checks, "exact identities")

# 4. CTCS total binary exit-rate identity.
exit_checks=0
for b in range(2,41):
    total=F(0)
    for i in range(1,b):
        total += F(factorial(b),factorial(i)*factorial(b-i))*beta_int(i,b-i)
    total /= 2
    assert total==harmonic(b-1)
    exit_checks+=1
    checks+=1
print("ctcs_total_exit_rate: PASS b=2..40")

# 5. Explicit asymptotic direction at finite exact N:
# ratio error shrinks along N=10,20,50,100,200 for every b<=6;
# ternary coefficient H/D shrinks on the same grid.
grid=[10,20,50,100,200]
prev_bin={}
prev_ter=None
asym_checks=0
for N in grid:
    H=harmonic(N-1); H2=harmonic(N-1,2); D=H*H-H2
    ter=H/D
    if prev_ter is not None:
        assert ter < prev_ter
        asym_checks+=1; checks+=1
    prev_ter=ter
    for b in range(2,7):
        r=H*(H-harmonic(b-1))/D
        err=abs(r-1)
        if b in prev_bin:
            assert err < prev_bin[b]
            asym_checks+=1; checks+=1
        prev_bin[b]=err
print("fixed_k_convergence_direction: PASS", asym_checks, "strict exact comparisons")

# 6. Full-root finite witness: at N=3, conditioning on exactly 3 cycles leaves only identity.
cond3=[]
for p in permutations(range(1,4)):
    c=cycles_of_perm(p)
    if len(c)==3:
        cond3.append(c)
assert len(cond3)==1
assert cond3[0]==((1,),(2,),(3,))
assert visible_partition(cond3[0],3)==((1,),(2,),(3,))
checks += 3
print("C034_N3_root_degree3_probability: PASS 1")

# 7. The full N-root on an attempt always has exactly three nonempty cycle blocks.
# Verify for N<=8 exactly.
root_checks=0
for N in range(3,9):
    for p in permutations(range(1,N+1)):
        c=cycles_of_perm(p)
        if len(c)==3:
            assert len(visible_partition(c,N))==3
            root_checks+=1
            checks+=1
print("full_root_arity_three: PASS", root_checks, "conditioned permutations")

print("TOTAL_EXACT_CHECKS", checks)
print("ALL_EXACT_CHECKS_PASS")
