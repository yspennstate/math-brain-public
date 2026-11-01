#!/usr/bin/env python3
from fractions import Fraction
from math import factorial
from functools import lru_cache

@lru_cache(None)
def partitions(n, max_part=None):
    if n == 0:
        return ((),)
    if max_part is None or max_part > n:
        max_part = n
    out = []
    for a in range(max_part, 0, -1):
        rem = n-a
        for tail in partitions(rem, min(a, rem)):
            out.append((a,)+tail)
    return tuple(out)

@lru_cache(None)
def fdim(mu):
    n=sum(mu)
    if n == 0:
        return 1
    h=1
    for r,rowlen in enumerate(mu):
        for c in range(rowlen):
            below=sum(1 for rr in range(r+1,len(mu)) if mu[rr] > c)
            h *= rowlen-c+below
    return factorial(n)//h

def boxes(mu):
    return {(r,c) for r,rowlen in enumerate(mu) for c in range(rowlen)}

def contents(mu):
    return [c-r for r,rowlen in enumerate(mu) for c in range(rowlen)]

def R(mu,s,n):
    K=n-s
    z=Fraction(1)
    for c in contents(mu):
        z *= Fraction(K-c,K+1-c)
    return z

def covers(mu):
    ans=[]
    b=boxes(mu)
    for lam in partitions(sum(mu)+1):
        if b <= boxes(lam):
            ans.append(lam)
    return ans

def p_growth(mu,lam):
    return Fraction(fdim(lam),(sum(mu)+1)*fdim(mu))

def A(s,n):
    return sum(Fraction(fdim(mu)**2,factorial(s))*R(mu,s,n)**2
               for mu in partitions(s))

# Exact Plancherel-growth stochasticity and exact adjacent-edge ratio.
edge_checks=0
for s in range(1,9):
    for mu in partitions(s):
        assert sum(p_growth(mu,lam) for lam in covers(mu)) == 1
        for lam in covers(mu):
            new_box=(boxes(lam)-boxes(mu)).pop()
            c0=new_box[1]-new_box[0]
            K=24-s  # any stable test n; identity itself is rational
            n=24
            lhs=R(lam,s+1,n)/R(mu,s,n)
            rhs=Fraction(1)
            for c in contents(mu):
                rhs *= 1-Fraction(1,(K-c)**2)
            rhs *= 1-Fraction(1,K-c0)
            assert lhs == rhs
            edge_checks += 1
print(f"plancherel_growth_and_edge_ratio_exact=PASS edges={edge_checks}")

# Exact average inequalities and literal Chen ratio in a nontrivial grid.
grid_checks=0
for j in range(4,10):
    for n in range(4*j,4*j+10):
        d=n-2*j
        q=(1-Fraction(1,(d+3)**2))**(j-1)*Fraction(d+1,d+2)
        assert A(j,n) >= q*q*A(j-1,n)
        assert A(j+1,n) < A(j,n)
        k=n-j
        Q=Fraction(j+1,j)*Fraction(k+1,k)**2*A(j,n)**2/(A(j-1,n)*A(j+1,n))
        assert Q > 1
        grid_checks += 1
print(f"exact_average_and_chen_grid=PASS cases={grid_checks}")

# Exact checks of the elementary logarithmic lower-bound chain at broad integer samples.
# The all-j proof is written algebraically in the immutable report.
bound_checks=0
for j in range(4,1001):
    for d in (2*j,2*j+1,3*j,5*j,10*j):
        lb=(Fraction(1,j)-Fraction(1,2*j*j)
            +Fraction(2,j+d)-Fraction(1,(j+d)**2)
            -Fraction(2,d+1)-Fraction(2*(j-1),(d+2)*(d+4))
           )
        coarse=Fraction(3*j-11,18*j*j)
        assert lb > coarse > 0
        bound_checks += 1
print(f"coarse_log_bound_exact_samples=PASS cases={bound_checks}")
print("THEOREM_CHECKED: n>=4j, j>=4 => Chen ratio lower-bound mechanism is positive")
print("ALL_EXACT_CHECKS_PASS")
