#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import comb

ASSERTS = 0

def check(cond, msg=""):
    global ASSERTS
    ASSERTS += 1
    if not cond:
        raise AssertionError(msg or f"assertion {ASSERTS} failed")

def falling(n, k):
    out = 1
    for r in range(k):
        out *= n-r
    return out

def isprime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def primes_lt(N):
    return [p for p in range(2, N) if isprime(p)]

def proposal_probs(N):
    ps = primes_lt(N)
    Z = sum((Fraction(1,p) for p in ps), Fraction(0))
    return {p: Fraction(1,p)/Z for p in ps}

def split_prob(N, i, j):
    den = falling(N, i+j)
    ans = Fraction(0)
    for m, pm in proposal_probs(N).items():
        num = falling(m,i)*falling(N-m,j) + falling(m,j)*falling(N-m,i)
        ans += pm * Fraction(num, den)
    return ans

def lam(N):
    return 1 / split_prob(N,1,1)

def pair_weight(N, m):
    return Fraction(m*(N-m), N*(N-1))

def h_exact(N, m, i, j):
    return Fraction(
        N*(N-1)*falling(m-1,i-1)*falling(N-m-1,j-1),
        falling(N,i+j)
    )

def rho_moment(N, r):
    probs = proposal_probs(N)
    L = lam(N)
    out = Fraction(0)
    for m, pm in probs.items():
        w = L * pm * pair_weight(N,m)
        out += w * (Fraction(m,N)**r + Fraction(N-m,N)**r)
    return out

# Prime-harmonic proposal, exact transformed-measure identity,
# and probability normalization over a broad finite range.
for N in range(4, 301):
    probs = proposal_probs(N)
    check(sum(probs.values(), Fraction(0)) == 1, f"proposal normalization N={N}")
    L = lam(N)

    # rho_N is exactly a probability measure.
    mass = sum((L*pm*pair_weight(N,m)*2 for m,pm in probs.items()), Fraction(0))
    check(mass == 1, f"rho mass N={N}")

    # closed-form pair normalization
    Z = sum(Fraction(1,p) for p in primes_lt(N))
    S = sum(N-p for p in primes_lt(N))
    check(L == Fraction(Z*N*(N-1), 2*S), f"lambda formula N={N}")

    # Exact transformed-measure representation of all tested split rates.
    for i in range(1, 7):
        for j in range(1, 7):
            if i+j > N:
                continue
            lhs = L * split_prob(N,i,j)
            rhs = Fraction(0)
            for m,pm in probs.items():
                w = L * pm * pair_weight(N,m)
                rhs += w * (h_exact(N,m,i,j) + h_exact(N,N-m,i,j))
            check(lhs == rhs, f"transform identity N={N}, split={i}|{j}")

    # exact symmetry consequences of rho_N
    check(rho_moment(N,0) == 1, f"moment0 N={N}")
    check(rho_moment(N,1) == Fraction(1,2), f"moment1 N={N}")
    check(split_prob(N,1,2) / split_prob(N,1,1) == Fraction(1,2),
          f"1|2 ratio N={N}")

# Independent subset enumeration in small N.
for N in range(4, 10):
    probs = proposal_probs(N)
    for i in range(1, 4):
        for j in range(1, 4):
            b = i+j
            if b > N:
                continue
            target_A = set(range(i))
            target_B = set(range(i,b))
            brute = Fraction(0)
            for m,pm in probs.items():
                total = comb(N,m)
                good = 0
                for tup in combinations(range(N),m):
                    S = set(tup)
                    vis = S.intersection(range(b))
                    if vis == target_A or vis == target_B:
                        good += 1
                brute += pm * Fraction(good,total)
            check(brute == split_prob(N,i,j),
                  f"subset enumeration mismatch N={N}, split={i}|{j}")

# Exact non-equivalence witness at N=7.
check(proposal_probs(7) == {
    2: Fraction(15,31),
    3: Fraction(10,31),
    5: Fraction(6,31),
})
check(split_prob(7,1,1) == Fraction(110,217))
check(split_prob(7,2,2) == Fraction(26,217))
check(split_prob(7,1,3) == Fraction(29,217))
check(split_prob(7,2,2) / split_prob(7,1,1) == Fraction(13,55))
check(split_prob(7,1,3) / split_prob(7,1,1) == Fraction(29,110))

print(f"EXACT_ASSERTIONS={ASSERTS}")
print("N7_PROPOSAL=2:15/31,3:10/31,5:6/31")
print("N7_SPLITS=P11:110/217,P22:26/217,P13:29/217")
print("N7_INVARIANT_RATIOS=P22/P11:13/55,P13/P11:29/110")
print("ALL_EXACT_CHECKS_PASS")
