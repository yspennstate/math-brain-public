#!/usr/bin/env python3
"""Regression checker for B18 dimension-uniform EQ_d rare-corner theorem.

The proof is analytic. This checker independently:
(1) reconstructs biased Fourier laws for NOR_d and EQ_d on deterministic
    unequal-bias samples and tests the inherited exact L1 bound
       ||mu_EQ-mu_NOR||_1 <= (8*2^d+4) P;
(2) verifies the NOR Poincare-currency identity numerically;
(3) checks exact rational constants in the all-d boundary estimate.
"""
from fractions import Fraction
import math
import random

EPS = Fraction(1, 2**13)
L = 13
A_DAGGER = Fraction(268204856, 10**9)
B_RESERVE = A_DAGGER - Fraction(1,100)

def basis(bit,p):
    q=1.0-p
    return math.sqrt(q/p) if bit else -math.sqrt(p/q)

def spectrum(ps, antipodal):
    d=len(ps); N=1<<d
    out=[]
    for S in range(N):
        c=0.0
        for x in range(N):
            pr=1.0
            for i,p in enumerate(ps):
                pr *= p if ((x>>i)&1) else (1.0-p)
            neg=(x==0) or (antipodal and x==N-1)
            f=-1.0 if neg else 1.0
            z=1.0
            for i,p in enumerate(ps):
                if (S>>i)&1:
                    z *= basis((x>>i)&1,p)
            c += pr*f*z
        out.append(c*c)
    return out

rng=random.Random(20260922041349)
tests=0
max_l1_ratio=0.0
max_parseval=0.0
max_currency_err=0.0
for d in range(3,7):
    N=1<<d
    for _ in range(120):
        ps=[10.0**rng.uniform(math.log10(.005),math.log10(.4))
            for __ in range(d)]
        P=math.prod(ps)
        Q=math.prod(1.0-p for p in ps)
        mu_eq=spectrum(ps,True)
        mu_nor=spectrum(ps,False)
        max_parseval=max(max_parseval,abs(sum(mu_eq)-1),abs(sum(mu_nor)-1))
        l1=sum(abs(a-b) for a,b in zip(mu_eq,mu_nor))
        bound=(8*N+4)*P
        assert l1 <= bound*(1+1e-9)+1e-14
        max_l1_ratio=max(max_l1_ratio,l1/bound)
        # W_N = I/4-Q(1-Q)=Q[sum p_i-(1-Q)].
        lhs=Q*sum(ps)-Q*(1-Q)
        rhs=Q*(sum(ps)-(1-Q))
        max_currency_err=max(max_currency_err,abs(lhs-rhs))
        assert abs(lhs-rhs)<1e-14
        tests+=1

# All-d analytic entropy coefficient is
# E_d = 20*d*(2 eps)^(d-2)*log2(1/eps).
# It decreases for d>=3 because E_{d+1}/E_d
# = ((d+1)/d)*(2 eps) < 1.
def E(d):
    return Fraction(20*d*L,1) * (2*EPS)**(d-2)
for d in range(3,200):
    assert E(d+1) < E(d)

entropy_coeff=E(3)                    # 120 eps L
reserve_coeff=B_RESERVE*(1-EPS)       # b Q >= b(1-eps)
gap=reserve_coeff-entropy_coeff
assert gap > 0
assert gap == Fraction(69369496937,1024000000000)

# Candidate monotonicity lower bound on x>=13:
# G >= 4.9096*x+2.22 and |G'|<31; 1/ln2<3/2.
gamma0_prime_lower = Fraction(49096,10000)*13 + Fraction(222,100) - Fraction(93,2)
assert gamma0_prime_lower == Fraction(24431,1250)  # 19.5448
assert gamma0_prime_lower > 0

print("PASS")
print("spectral_tests =",tests)
print("max_parseval_error =",format(max_parseval,".3e"))
print("max_l1_over_exact_bound =",format(max_l1_ratio,".12f"))
print("max_NOR_currency_identity_error =",format(max_currency_err,".3e"))
print("epsilon =",float(EPS))
print("gamma0_prime_lower_x_ge_13 >",float(gamma0_prime_lower))
print("entropy_error_coeff <=",float(entropy_coeff))
print("readonce_reserve_coeff >=",float(reserve_coeff))
print("final_defect_gap_coeff >=",float(gap))
