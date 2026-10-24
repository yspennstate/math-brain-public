#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, comb

def beta_int(i,j):
    assert i>=1 and j>=1
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def target_specific_unordered_rate(m,i):
    # Aldous--Janson Part III eq. (4.6)/(4.13): q_pi = B(i,m-i)
    return beta_int(i,m-i)

def harmonic_grid_specific_unordered_rate(N,m,i):
    # x_j=j/N, raw oriented intensity w_j=(1/N)/(2*x_j*(1-x_j)).
    # Summing the two orientations and using grid symmetry yields
    # (1/N) sum x_j^(i-1)(1-x_j)^(m-i-1).
    ans=Fraction(0)
    for j in range(1,N):
        x=Fraction(j,N)
        ans += x**(i-1) * (1-x)**(m-i-1)
    return ans/Fraction(N,1)

def harmonic_grid_rate_direct(N,m,i):
    ans=Fraction(0)
    for j in range(1,N):
        x=Fraction(j,N)
        w=Fraction(1,N) / (2*x*(1-x))
        ans += w*(x**i*(1-x)**(m-i)+x**(m-i)*(1-x)**i)
    return ans

def target_total_split_rate(m):
    # Sum over unordered bipartitions of an m-label block.
    # Use half of the sum over nonempty proper subsets.
    ans=Fraction(0)
    for i in range(1,m):
        ans += Fraction(comb(m,i),2)*target_specific_unordered_rate(m,i)
    return ans

def harmonic_number(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))

def flat_bias_limit_specific_unordered_rate(m,i):
    # Candidate without the singular harmonic weight:
    # nu(dx)=dx on (0,1); unordered Bernoulli split rate.
    return 2*beta_int(i+1,m-i+1)

print("ProofNet15 R11 I0054 exact checker")
print("FINITE CLAIMS ONLY; no asymptotic convergence is inferred from enumeration.")

# 1. Source algebra: q_pi beta integral and total h_{m-1}.
for m in range(2,21):
    for i in range(1,m):
        q=target_specific_unordered_rate(m,i)
        assert q == Fraction(factorial(i-1)*factorial(m-i-1), factorial(m-1))
    assert target_total_split_rate(m) == harmonic_number(m-1)
print("source beta-rate / harmonic-total identities: PASS m=2..20")

# 2. Direct-vs-symmetrized grid formula.
for N in range(2,21):
    for m in range(2,min(N,8)+1):
        for i in range(1,m):
            assert harmonic_grid_specific_unordered_rate(N,m,i) == harmonic_grid_rate_direct(N,m,i)
print("harmonic-grid direct/symmetrized rate identity: PASS")

# 3. Frozen-equivalence witness at N=4.
r13=harmonic_grid_specific_unordered_rate(4,4,1)
r22=harmonic_grid_specific_unordered_rate(4,4,2)
t13=target_specific_unordered_rate(4,1)
t22=target_specific_unordered_rate(4,2)
assert r13 == Fraction(7,32)
assert r22 == Fraction(5,32)
assert r13/r22 == Fraction(7,5)
assert t13 == Fraction(1,3)
assert t22 == Fraction(1,6)
assert t13/t22 == 2
assert r13/r22 != t13/t22
print("N=4 non-equivalence witness: grid rates 1|3 =",r13,", 2|2 =",r22,
      ", ratio =",r13/r22,"; CTCS ratio =",t13/t22,"PASS")

# 4. Negation-first bad candidate: flat bias has wrong limiting shape invariant.
f13=flat_bias_limit_specific_unordered_rate(4,1)
f22=flat_bias_limit_specific_unordered_rate(4,2)
assert f13 == Fraction(1,10)
assert f22 == Fraction(1,15)
assert f13/f22 == Fraction(3,2)
assert f13/f22 != t13/t22
print("flat-bias limiting invariant: 1|3 =",f13,", 2|2 =",f22,
      ", ratio =",f13/f22,"!= CTCS 2: PASS")

# 5. Exact rate tables showing approach. These are diagnostics only.
for N in (4,8,16,32,64,128):
    a=harmonic_grid_specific_unordered_rate(N,4,1)
    b=harmonic_grid_specific_unordered_rate(N,4,2)
    print(f"N={N:3d}: q_N(1|3)={a} err={a-t13}; q_N(2|2)={b} err={b-t22}")

# 6. Pair/triple necessary invariants: exact visible split rates.
# For m=2 there is one bipartition; for m=3 there are three singleton|pair partitions.
for N in range(2,101):
    pair=harmonic_grid_specific_unordered_rate(N,2,1)
    triple=3*harmonic_grid_specific_unordered_rate(N,3,1)
    assert pair == Fraction(N-1,N)
    assert triple == Fraction(3*(N-1),2*N)
print("pair/triple rate invariants: PASS N=2..100")

print("PASS")
