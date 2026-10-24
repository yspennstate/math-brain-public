from fractions import Fraction
from collections import Counter
from math import gcd, factorial

ASSERTIONS = 0
def ck(cond, msg=""):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def de_bruijn(q, K):
    # Fredricksen-Kessler-Maiorana / Lyndon-style generator.
    a = [0] * (q*K + 1)
    seq = []
    def db(t, p):
        if t > K:
            if K % p == 0:
                seq.extend(a[1:p+1])
        else:
            a[t] = a[t-p]
            db(t+1, p)
            for j in range(a[t-p] + 1, q):
                a[t] = j
                db(t+1, t)
    db(1, 1)
    return seq

def params(N):
    # q_N = max(2, ceil(log_2 N)), computed exactly.
    q = max(2, (N-1).bit_length())
    K = 2
    while q**K < N:
        K += 1
    L = q**K
    M = (q-1)*L
    return q, K, L, M

def c_rate(q, u):
    x = Fraction(u, q)
    return Fraction(1, 2*x*(1-x))

def grid_rate(q, i, j):
    return sum(
        Fraction(u, q)**(i-1) * (1-Fraction(u, q))**(j-1)
        for u in range(1, q)
    ) / (q-1)

def beta_rate(i, j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def matches_unordered(z, A, B):
    return (
        all(z[a] == 1 for a in A) and all(z[b] == 0 for b in B)
    ) or (
        all(z[a] == 0 for a in A) and all(z[b] == 1 for b in B)
    )

# 1. Parameter repair: L_N >= N, legal gate, and exact mesh relations.
for N in range(4, 501):
    q, K, L, M = params(N)
    ck(L >= N, ("L>=N", N, q, K, L))
    ck(gcd(L, q-1) == 1, ("coprime", N, q, K))
    Delta = Fraction(1, M**3)
    tau = M * Delta
    ck(tau == Fraction(1, M**2), ("tau", N))
    for u in range(1, q):
        ck(Delta * c_rate(q,u) < 1, ("gate", N, q, u))

# 2. Exact de Bruijn window counts and minimal period.
for q in range(2, 6):
    for K in range(2, 6):
        w = de_bruijn(q, K)
        L = q**K
        ck(len(w) == L, ("length", q, K))
        Kwords = [tuple(w[(s+r) % L] for r in range(K)) for s in range(L)]
        ck(len(set(Kwords)) == L, ("Kwords", q, K))
        # exact r-window multiplicities
        for r in range(1, K+1):
            C = Counter(tuple(w[(s+j)%L] for j in range(r)) for s in range(L))
            ck(len(C) == q**r, ("r words", q, K, r))
            for cnt in C.values():
                ck(cnt == q**(K-r), ("mult", q, K, r, cnt))
        # no nontrivial cyclic period
        for d in range(1, L):
            if L % d == 0:
                ck(any(w[s] != w[(s+d)%L] for s in range(L)),
                   ("period", q, K, d))

# 3. CRT diagonal rotor visits every (phase,threshold-index) pair exactly once.
for q in range(2, 8):
    for K in range(2, 6):
        L = q**K
        M = (q-1)*L
        pairs = [(t % L, t % (q-1)) for t in range(M)]
        ck(len(set(pairs)) == M, ("CRT", q, K))
        ck(set(pairs) == {(s,r) for s in range(L) for r in range(q-1)},
           ("CRT full", q, K))

# 4. Exact averaged split generator = harmonic-grid generator.
for q in range(2, 7):
    for K in range(2, 6):
        w = de_bruijn(q, K)
        L = len(w)
        M = (q-1)*L
        for i in range(1, K):
            for j in range(1, K-i+1):
                A = set(range(i))
                B = set(range(i, i+j))
                total = Fraction(0)
                for t in range(M):
                    s = t % L
                    u = 1 + (t % (q-1))
                    z = [1 if w[(s+ell) % L] < u else 0 for ell in range(i+j)]
                    if matches_unordered(z, A, B):
                        total += c_rate(q, u)
                direct = total / M
                formula = grid_rate(q, i, j)
                ck(direct == formula, ("generator", q, K, i, j, direct, formula))
        ck(grid_rate(q,1,1) == 1, ("pair normalization", q,K))

# 5. Every pair of distinct leaf positions <= L is separated by some rotor pair.
for q in range(2, 5):
    for K in range(2, 5):
        w = de_bruijn(q, K)
        L = len(w)
        n = min(L, 24)
        for a in range(n):
            for b in range(a+1, n):
                found = False
                for s in range(L):
                    va = w[(s+a)%L]
                    vb = w[(s+b)%L]
                    if va != vb:
                        lo, hi = sorted((va, vb))
                        # some u in 1,...,q-1 separates va<u from vb<u
                        if lo + 1 <= hi:
                            found = True
                            break
                ck(found, ("pair separation", q,K,a,b))

# 6. Finite N=4 witness distinguishing deterministic CRT rotor from C060 random phase.
q, K, L, M = params(4)
ck((q,K,L,M) == (2,2,4,4), ("N4 params", q,K,L,M))
w = de_bruijn(q,K)
ck(w == [0,0,1,1], ("canonical B22", w))
pairs22 = [
    ({0,1},{2,3}),
    ({0,2},{1,3}),
    ({0,3},{1,2}),
]
# C061 first microstep: s=0,u=1 deterministically.
z0 = [1 if w[ell % L] < 1 else 0 for ell in range(4)]
c061 = [Fraction(int(matches_unordered(z0,*p)),1) for p in pairs22]
ck(sorted(c061) == [Fraction(0),Fraction(0),Fraction(1)], ("C061 witness", c061))
# C060 random phase, conditional on a balanced split.
cnt = [0,0,0]
for s in range(L):
    z = [1 if w[(s+ell)%L] < 1 else 0 for ell in range(4)]
    for r,p in enumerate(pairs22):
        if matches_unordered(z,*p):
            cnt[r] += 1
den = sum(cnt)
c060 = [Fraction(x,den) for x in cnt]
ck(sorted(c060) == [Fraction(0),Fraction(1,2),Fraction(1,2)], ("C060 witness", c060))
ck(sorted(c061) != sorted(c060), "witness collision")

# 7. Exact beta identities and representative convergence values.
for i in range(1, 6):
    for j in range(1, 6):
        B = beta_rate(i,j)
        ck(B > 0, ("beta",i,j))
        ck(B == beta_rate(j,i), ("beta symmetry",i,j))

print("R11-I0054-U040-C061 exact self-check")
print("ASSERTIONS", ASSERTIONS)
print("N4_params", q, K, L, M)
print("N4_word", ''.join(map(str,w)))
print("C061_first_microstep_2v2_conditional_multiset",
      ",".join(str(x) for x in sorted(c061)))
print("C060_random_phase_2v2_conditional_multiset",
      ",".join(str(x) for x in sorted(c060)))
for q0 in (3,5,11,31):
    vals = []
    for i,j in ((1,1),(1,3),(2,2),(2,3)):
        vals.append(f"{i},{j}:{grid_rate(q0,i,j)}->{beta_rate(i,j)}")
    print("grid", q0, " ".join(vals))
print("ALL_EXACT_CHECKS_PASS")
