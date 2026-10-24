#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations
from math import factorial, isqrt

A = 0

def check(cond, msg=""):
    global A
    A += 1
    if not cond:
        raise AssertionError(msg or f"assertion {A} failed")

def H(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))

def harmonic_clocks(N):
    return [Fraction(N, 2*s*(N-s)) for s in range(1,N)]

def q_from_biases(N, biases, i, j):
    cs = harmonic_clocks(N)
    check(len(cs) == N-1)
    check(len(biases) == N-1)
    return sum((lam*(p**i*(1-p)**j + p**j*(1-p)**i)
                for lam,p in zip(cs,biases)), Fraction(0))

def c084_tau(x):
    # Pullback of the swap [0,log2) <-> [log2,2log2) in logit coordinates.
    if x < Fraction(1,2):
        return x
    if x < Fraction(2,3):
        return 2*x/(1+x)
    if x < Fraction(4,5):
        return x/(2-x)
    return x

def beta_int(i,j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

# 1. Harmonic clock normalization and identity-compiler algebra.
for N in range(2, 31):
    cs = harmonic_clocks(N)
    check(sum(cs, Fraction(0)) == H(N-1), f"clock normalization N={N}")
    idbias = [Fraction(s,N) for s in range(1,N)]
    for b in range(2, min(7,N+1)):
        for i in range(1,b):
            j=b-i
            q = q_from_biases(N,idbias,i,j)
            # Grid symmetry collapses the two orientations exactly.
            rhs = sum((Fraction(1,N) * Fraction(s,N)**(i-1)
                       * (1-Fraction(s,N))**(j-1)
                       for s in range(1,N)), Fraction(0))
            check(q == rhs, f"identity Riemann identity N={N},i={i},j={j}")
            check(q > 0)
            check(beta_int(i,j) > 0)

# 2. Abstract exact interval-exchange finite core:
# every cell permutation is a bijection preserving equal-cell counting measure.
for M in range(2,8):
    count = 0
    for pi in permutations(range(M)):
        count += 1
        check(sorted(pi) == list(range(M)), f"not permutation M={M}")
        inv = [0]*M
        for r,s in enumerate(pi):
            inv[s] = r
        for r in range(M):
            check(inv[pi[r]] == r)
            check(pi[inv[r]] == r)
        # On normalized cells [r/M,(r+1)/M), the image cell length is exactly 1/M.
        total_domain = sum((Fraction(1,M) for _ in range(M)), Fraction(0))
        total_image  = sum((Fraction(1,M) for _ in range(M)), Fraction(0))
        check(total_domain == 1)
        check(total_image == 1)
        # Every target cell is covered exactly once.
        for t in range(M):
            check(sum(1 for s in pi if s == t) == 1)
    check(count == factorial(M), f"permutation count M={M}")

# 3. Concrete C085 N=4: environment is identity or C084 swap, each with weight 1/2.
N = 4
cs = harmonic_clocks(N)
check(cs == [Fraction(2,3), Fraction(1,2), Fraction(2,3)])

idbias = [Fraction(s,N) for s in range(1,N)]
swbias = [c084_tau(Fraction(s,N)) for s in range(1,N)]
check(idbias == [Fraction(1,4), Fraction(1,2), Fraction(3,4)])
check(swbias == [Fraction(1,4), Fraction(2,3), Fraction(3,5)])

q13_id = q_from_biases(N,idbias,1,3)
q22_id = q_from_biases(N,idbias,2,2)
q13_sw = q_from_biases(N,swbias,1,3)
q22_sw = q_from_biases(N,swbias,2,2)

check(q13_id == Fraction(7,32))
check(q22_id == Fraction(5,32))
check(q13_sw == Fraction(722693,3240000))
check(q22_sw == Fraction(560707,3240000))

lam_id = 4*q13_id + 3*q22_id
lam_sw = 4*q13_sw + 3*q22_sw
check(lam_id == Fraction(43,32))
check(lam_sw == Fraction(4572893,3240000))
check(lam_id != lam_sw)

# Annealed one-time split rates are the arithmetic mean, but the root holding time is
# a mixture of exponentials because the environment is sampled once and then frozen.
q13_ann = (q13_id + q13_sw)/2
q22_ann = (q22_id + q22_sw)/2
lam_ann_rate_average = (lam_id + lam_sw)/2
check(4*q13_ann + 3*q22_ann == lam_ann_rate_average)

a = 1/lam_id
b = 1/lam_sw
ET = (a+b)/2
ET2 = a*a + b*b  # half*(2a^2)+half*(2b^2)
moment_defect = ET2 - 2*ET*ET
check(moment_defect == (a-b)**2/2)
check(moment_defect == Fraction(24588111077888,38665086870091201))
check(moment_defect > 0)

# Scale-free exponentiality invariant: exponential iff E[T^2]/E[T]^2=2 here;
# positive common time scaling leaves this ratio unchanged.
std_ratio = ET2/(ET*ET)
check(std_ratio > 2)
for c in [Fraction(1,7), Fraction(1,3), Fraction(2,1), Fraction(11,4), Fraction(100,1)]:
    scaled_ET = c*ET
    scaled_ET2 = c*c*ET2
    check(scaled_ET2/(scaled_ET*scaled_ET) == std_ratio)
    check(scaled_ET2 - 2*scaled_ET*scaled_ET == c*c*moment_defect)

# CTCS(4) has a single exponential root holding rate: 4*(1/3)+3*(1/6)=11/6.
lam_ctcs4 = 4*Fraction(1,3) + 3*Fraction(1,6)
check(lam_ctcs4 == Fraction(11,6))
ctcs_ET = 1/lam_ctcs4
ctcs_ET2 = 2/(lam_ctcs4*lam_ctcs4)
check(ctcs_ET2 == 2*ctcs_ET*ctcs_ET)

# The C085 annealed root topology probability is also an exact scale-free witness.
# Conditional topology probabilities are normalized by each environment's own total root rate;
# annealed unconditional root topology is their 1/2 mixture because the environment is chosen first.
pbal_id = 3*q22_id/lam_id
pbal_sw = 3*q22_sw/lam_sw
pbal_ann = (pbal_id+pbal_sw)/2
check(pbal_id == Fraction(15,43))
check(pbal_sw == Fraction(1682121,4572893))
check(pbal_ann != Fraction(3,11))

# 4. The concrete growth schedule M_N=floor(sqrt N) has M_N/N -> 0.
# Exact perfect-square identities give an explicit subsequence certificate.
for m in range(2,101):
    N = m*m
    M = max(2,isqrt(N))
    check(M == m)
    check(Fraction(M,N) == Fraction(1,m))
# And for a broad exact finite range M_N <= sqrt(N) <= N/M_N up to rounding.
for N in range(4,2001):
    M = max(2,isqrt(N))
    check(M*M <= N)
    check(M <= N)
    check(Fraction(M,N) <= Fraction(1,M))

print("R11-I0054-U067/C085 quenched-logit-shuffle exact self-check")
print(f"ASSERTIONS={A}")
print("N4_identity_biases=" + ",".join(str(x) for x in idbias))
print("N4_swap_biases=" + ",".join(str(x) for x in swbias))
print(f"N4_q13_identity={q13_id}")
print(f"N4_q22_identity={q22_id}")
print(f"N4_lambda_identity={lam_id}")
print(f"N4_q13_swap={q13_sw}")
print(f"N4_q22_swap={q22_sw}")
print(f"N4_lambda_swap={lam_sw}")
print(f"N4_root_moment_defect={moment_defect}")
print(f"N4_root_secondmoment_ratio={std_ratio}")
print(f"N4_balanced_prob_identity={pbal_id}")
print(f"N4_balanced_prob_swap={pbal_sw}")
print(f"N4_balanced_prob_annealed={pbal_ann}")
print("STATUS=ALL_EXACT_CHECKS_PASS")
