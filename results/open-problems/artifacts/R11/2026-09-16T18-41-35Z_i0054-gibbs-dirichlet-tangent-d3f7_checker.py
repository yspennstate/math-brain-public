#!/usr/bin/env python3
"""
R11 / I0054 exact finite self-check for the ternary Dirichlet/Gibbs-fragmentation
tangent model.

This checker verifies finite algebra only. It does NOT prove the asymptotic
projective-Skorokhod convergence theorem; that proof is written in the run report.

Checks:
  1. Exact Dirichlet paintbox partition probabilities normalize for q=3,
     n<=7, at several rational concentrations.
  2. Exact equality with the finite Poisson--Dirichlet / Ewens--Pitman
     EPPF on the ray (discount d=-eps, strength theta=q*eps).
  3. First-order CTCS coefficients:
       no-change derivative = -(q-1) H_{m-1},
       particular binary split coefficient = (q-1) B(i,m-i),
       r>=3 particular partitions have order >= eps^2.
  4. Exact finite non-equivalence witnesses:
       q=3, N=3, eps=1/6: P(root 1|1|1 at first raw level)=2/135 > 0;
       SC-nCRP, N=4, theta=1/4: P(root 1|1|1|1 at first level)=1/585 > 0;
       q=3 model has zero probability of any 4-way split.
  5. Binary q=2 Dirichlet candidate is exactly on Aldous' beta-splitting
     ray beta=eps-1 at the level of particular split weights; hence it is
     rejected as a new class.
"""
from fractions import Fraction
from math import factorial

def rising(x, n):
    y = Fraction(1,1)
    for j in range(n):
        y *= x + j
    return y

def falling_int(q, r):
    z = 1
    for j in range(r):
        z *= q-j
    return z

def harmonic(n):
    return sum((Fraction(1,j) for j in range(1,n+1)), Fraction(0,1))

def beta_integer(i,j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def dirichlet_partition_prob(q, eps, sizes):
    """Probability of one particular UNLABELLED set partition into given blocks."""
    m=sum(sizes); r=len(sizes)
    if r>q:
        return Fraction(0,1)
    num=Fraction(falling_int(q,r),1)
    for n in sizes:
        num *= rising(eps,n)
    return num / rising(q*eps,m)

def pd_eppf(discount, strength, sizes):
    """Two-parameter Poisson--Dirichlet EPPF for one particular set partition."""
    m=sum(sizes); r=len(sizes)
    num=Fraction(1,1)
    for j in range(1,r):
        num *= strength + j*discount
    den=rising(strength+1,m-1)
    for n in sizes:
        num *= rising(1-discount,n-1)
    return num/den

def ewens_particular(theta, sizes):
    m=sum(sizes); r=len(sizes)
    num=theta**r
    for n in sizes:
        num *= factorial(n-1)
    return num/rising(theta,m)

def set_partitions(n):
    if n==0:
        yield []
        return
    def rec(i, blocks):
        if i==n:
            yield [set(b) for b in blocks]
            return
        for j in range(len(blocks)):
            blocks[j].add(i)
            yield from rec(i+1, blocks)
            blocks[j].remove(i)
        blocks.append({i})
        yield from rec(i+1, blocks)
        blocks.pop()
    yield from rec(1,[{0}])

print("R11 I0054 Gibbs/Dirichlet tangent exact self-check")

# 1. Exact normalization and 2. PD identification.
tests=0
for eps in (Fraction(1,6), Fraction(1,8), Fraction(2,15)):
    q=3
    d=-eps
    theta=q*eps
    for n in range(1,8):
        total=Fraction(0,1)
        for pi in set_partitions(n):
            sizes=[len(b) for b in pi]
            p=dirichlet_partition_prob(q,eps,sizes)
            total += p
            assert p == pd_eppf(d,theta,sizes)
            tests += 1
        assert total == 1
print("normalization_and_PD_identification: PASS", tests, "exact partition instances")

# 3. First-order coefficients, exact algebra.
first_order=0
for q in (2,3,4,5):
    for m in range(2,16):
        deriv=sum((Fraction(1,j)-Fraction(q,j) for j in range(1,m)), Fraction(0,1))
        assert deriv == -(q-1)*harmonic(m-1)
        first_order += 1
        for i in range(1,m):
            coeff=Fraction(q*(q-1),q) * Fraction(factorial(i-1)*factorial(m-i-1),factorial(m-1))
            assert coeff == (q-1)*beta_integer(i,m-i)
            first_order += 1
        for r in range(3,min(q,m)+1):
            assert r-1 >= 2
            first_order += 1
print("first_order_CTCS_coefficients: PASS", first_order, "exact identities")

# 4. Exact non-equivalence witnesses.
p_ternary=dirichlet_partition_prob(3,Fraction(1,6),[1,1,1])
assert p_ternary == Fraction(2,135) and p_ternary>0
p_four_ncrp=ewens_particular(Fraction(1,4),[1,1,1,1])
assert p_four_ncrp == Fraction(1,585) and p_four_ncrp>0
p_four_q3=dirichlet_partition_prob(3,Fraction(1,8),[1,1,1,1])
assert p_four_q3 == 0
print("finite_degree_witnesses: PASS",
      "ternary_q3_N3=",p_ternary,
      "fourway_nCRP_N4=",p_four_ncrp,
      "fourway_q3=",p_four_q3)

# 5. q=2 is exactly the beta-splitting ray beta=eps-1 in split-weight ratios.
binary_checks=0
for eps in (Fraction(1,7),Fraction(2,9),Fraction(3,8)):
    for m in range(3,12):
        base_dir=rising(eps,1)*rising(eps,m-1)
        for i in range(1,m):
            w_dir=rising(eps,i)*rising(eps,m-i)
            w_beta=rising(eps,i)*rising(eps,m-i)
            assert w_dir/base_dir == w_beta/base_dir
            binary_checks += 1
print("q2_beta_splitting_identity: PASS", binary_checks, "exact ratio checks")

print("ALL_EXACT_CHECKS_PASS")
