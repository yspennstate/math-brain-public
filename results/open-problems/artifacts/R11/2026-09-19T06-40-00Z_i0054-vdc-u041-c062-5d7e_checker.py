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
    q = max(2, (N-1).bit_length())   # ceil(log_2 N), with floor at 2
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

def vdc_frac(t):
    if t == 0:
        return Fraction(0, 1)
    r = t.bit_length()
    x = t
    rev = 0
    for _ in range(r):
        rev = (rev << 1) | (x & 1)
        x >>= 1
    return Fraction(rev, 1 << r)

def vdc_cell(t, M):
    x = vdc_frac(t)
    j = (M*x.numerator) // x.denominator
    ck(0 <= j < M, ("vdc cell range", t, M, x, j))
    return j

# 1. Repaired finite-tree parameters and micro/macro scales.
for N in range(4, 501):
    q, K, L, M = params(N)
    Delta = Fraction(1, M**3)
    W = M*M
    tau = W*Delta
    ck(L >= N, ("L>=N", N, q, K, L))
    ck(gcd(L, q-1) == 1, ("coprime", N, q, K))
    ck(tau == Fraction(1, M), ("tau", N, tau, M))
    for u in range(1, q):
        ck(Delta*c_rate(q, u) < 1, ("legal gate", N, q, u))

# 2. Exact de Bruijn window multiplicities.
for q in range(2, 6):
    for K in range(2, 6):
        w = de_bruijn(q, K)
        L = q**K
        ck(len(w) == L, ("deBruijn length", q, K))
        for r in range(1, K+1):
            C = Counter(tuple(w[(s+j) % L] for j in range(r)) for s in range(L))
            ck(len(C) == q**r, ("window support", q, K, r))
            for cnt in C.values():
                ck(cnt == q**(K-r), ("window multiplicity", q, K, r, cnt))

# 3. Exact finite checks of the base-2 van der Corput cell discrepancy bound.
# The proof in the report is symbolic; these are finite self-checks.
for M in range(2, 24):
    nmax = 384
    seq = [vdc_cell(t, M) for t in range(nmax)]
    pref = [[0]*(nmax+1) for _ in range(M)]
    for e in range(M):
        c = 0
        for n, x in enumerate(seq, 1):
            if x == e:
                c += 1
            pref[e][n] = c
    for n in range(1, nmax+1, 7):
        R = max(1, n.bit_length())
        B = 2*(R+3)
        for e in range(M):
            err = abs(Fraction(pref[e][n], 1) - Fraction(n, M))
            ck(err <= B, ("prefix discrepancy", M, n, e, err, B))
    for a in range(0, nmax, 19):
        for b in range(a+1, min(nmax, a+127)+1, 17):
            R = max(1, b.bit_length())
            B = 4*(R+3)
            for e in range(M):
                err = abs(
                    Fraction(pref[e][b]-pref[e][a], 1) - Fraction(b-a, M)
                )
                ck(err <= B, ("window discrepancy", M, a, b, e, err, B))

# 4. Environment average is exactly the harmonic-grid generator, independent of order.
for q in range(2, 7):
    for K in range(2, 5):
        w = de_bruijn(q, K)
        L = len(w)
        M = (q-1)*L
        for i in range(1, K):
            for j in range(1, K-i+1):
                A = set(range(i))
                B = set(range(i, i+j))
                total = Fraction(0)
                for s in range(L):
                    for u in range(1, q):
                        z = [
                            1 if w[(s+ell) % L] < u else 0
                            for ell in range(i+j)
                        ]
                        if matches_unordered(z, A, B):
                            total += c_rate(q, u)
                direct = total / M
                formula = grid_rate(q, i, j)
                ck(direct == formula, ("averaged generator", q, K, i, j, direct, formula))
        ck(grid_rate(q, 1, 1) == 1, ("pair normalization", q, K))

# 5. N=4 exact root-split witness: same gates and environment, different schedules only.
q4, K4, L4, M4 = params(4)
w4 = de_bruijn(q4, K4)
ck((q4, K4, L4, M4) == (2, 2, 4, 4), ("N4 params", q4, K4, L4, M4))
ck(w4 == [0, 0, 1, 1], ("canonical B(2,2)", w4))
Delta4 = Fraction(1, M4**3)
p4 = Delta4*c_rate(q4, 1)
ck(p4 == Fraction(1, 32), ("N4 gate", p4))
pairs22 = [
    ({0,1}, {2,3}),
    ({0,2}, {1,3}),
    ({0,3}, {1,2}),
]
def support_for_phase(s):
    z = [1 if w4[(s+ell) % L4] < 1 else 0 for ell in range(4)]
    for idx, pair in enumerate(pairs22):
        if matches_unordered(z, *pair):
            return idx
    return None

phase_support = [support_for_phase(s) for s in range(L4)]
ck(phase_support == [0,2,0,2], ("phase support", phase_support))

c061_phase = [t % L4 for t in range(L4)]
c062_phase = [vdc_cell(t, M4) // (q4-1) for t in range(M4)]
ck(c061_phase == [0,1,2,3], ("C061 phases", c061_phase))
ck(c062_phase == [0,2,1,3], ("C062 phases", c062_phase))
pat61 = [support_for_phase(s) for s in c061_phase]
pat62 = [support_for_phase(s) for s in c062_phase]
ck(pat61 == [0,2,0,2], ("C061 pattern", pat61))
ck(pat62 == [0,0,2,2], ("C062 pattern", pat62))

def geometric_first_gate_support(pattern, p, nsupport=3):
    r = 1-p
    d = len(pattern)
    den = 1-r**d
    out = [Fraction(0) for _ in range(nsupport)]
    for t, s in enumerate(pattern):
        if s is not None:
            out[s] += p*r**t/den
    return out

pr61 = geometric_first_gate_support(pat61, p4)
pr62 = geometric_first_gate_support(pat62, p4)
ck(sum(pr61) == 1, ("C061 total", pr61))
ck(sum(pr62) == 1, ("C062 total", pr62))
ck(pr61 == [Fraction(32,63), 0, Fraction(31,63)], ("C061 root law", pr61))
ck(pr62 == [Fraction(1024,1985), 0, Fraction(961,1985)], ("C062 root law", pr62))
ck(sorted(pr61) != sorted(pr62), ("root-law witness collision", pr61, pr62))

# 6. Representative exact scale inequalities used by U041/C062.
for N in (16, 32, 64, 128, 256, 500, 1000, 5000):
    q, K, L, M = params(N)
    Delta = Fraction(1, M**3)
    W = M*M
    tau = W*Delta
    C = Fraction(q, 1)
    ck(tau*C*C == Fraction(q*q, M), ("tau C^2", N))
    ck(Delta*C*C == Fraction(q*q, M**3), ("Delta C^2", N))
    D = 4*((M**3).bit_length()+3)
    coeff = Fraction(q*D, M)
    ck(coeff > 0, ("discrepancy coefficient", N))

print("R11-I0054-U041-C062 exact self-check")
print("ASSERTIONS", ASSERTIONS)
print("N4_params", q4, K4, L4, M4)
print("N4_word", ''.join(map(str, w4)))
print("N4_gate_p", p4)
print("C061_phase_order", ",".join(map(str, c061_phase)))
print("C062_vdc_phase_order", ",".join(map(str, c062_phase)))
print("C061_root_2v2_probs", ",".join(map(str, pr61)))
print("C062_root_2v2_probs", ",".join(map(str, pr62)))
print("ALL_EXACT_CHECKS_PASS")
