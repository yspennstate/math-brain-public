#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, comb
import itertools

CHECKS = 0

def check(cond, msg="check failed"):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1

def fall(n, r):
    if r < 0:
        return 0
    if r == 0:
        return 1
    if n < r:
        return 0
    out = 1
    for t in range(r):
        out *= n - t
    return out

def B(i, j):
    return Fraction(factorial(i-1) * factorial(j-1), factorial(i+j-1))

def H(n):
    return sum((Fraction(1, r) for r in range(1, n+1)), Fraction(0))

def c(N, s):
    return Fraction(N * (N-1), 2 * s * (N-s))

# A. Full S_N orbit equals exact without-replacement sampling.
for N in range(3, 8):
    perms = list(itertools.permutations(range(1, N+1)))
    for b in range(2, N+1):
        for i in range(1, b):
            j = b - i
            A = set(range(i))
            for s in range(1, N):
                red = set(range(1, s+1))
                count = 0
                for p in perms:
                    col = [p[r] in red for r in range(b)]
                    ori1 = all(col[r] for r in A) and all(not col[r] for r in range(b) if r not in A)
                    ori2 = all(not col[r] for r in A) and all(col[r] for r in range(b) if r not in A)
                    count += int(ori1 or ori2)
                lhs = Fraction(count, factorial(N))
                rhs = Fraction(fall(s, i) * fall(N-s, j) + fall(s, j) * fall(N-s, i), fall(N, b))
                check(lhs == rhs, ("orbit/hypergeom", N, b, i, s, lhs, rhs))

# B. Exact beta generator identity at every finite N.
for N in range(3, 15):
    for b in range(2, N+1):
        for i in range(1, b):
            j = b - i
            q = Fraction(0)
            for s in range(1, N):
                w = Fraction(N, 2 * s * (N-s))
                h = Fraction(fall(s, i) * fall(N-s, j) + fall(s, j) * fall(N-s, i), fall(N, b))
                q += w * h
            check(q == B(i, j), ("beta kernel", N, b, i, q, B(i, j)))

# C. Falling-factorial Vandermonde identity.
for N in range(3, 30):
    for b in range(2, N+1):
        for i in range(1, b):
            j = b - i
            lhs = sum(fall(s-1, i-1) * fall(N-s-1, j-1) for s in range(1, N))
            rhs = factorial(i-1) * factorial(j-1) * comb(N-1, b-1)
            check(lhs == rhs, ("Vandermonde", N, b, i, lhs, rhs))

# D. Total CTCS exit rate of one b-block is H_{b-1}; hence any
# partition of [N] has total exit rate <= N-1.
for b in range(2, 30):
    lam = Fraction(0)
    for i in range(1, b//2 + 1):
        j = b - i
        number_of_unordered_supports = comb(b, i) if i < j else comb(b, i)//2
        lam += number_of_unordered_supports * B(i, j)
    check(lam == H(b-1), ("exit rate", b, lam, H(b-1)))
    check(lam <= b-1, ("exit rate bound", b, lam))

# E. A cyclic-shift subgroup is not enough: at N=4,s=2 it visits only
# adjacent 2-subsets, so opposite supports never occur.
N = 4
red = {1, 2}

def shift_perm(t):
    return tuple(((x-1+t) % N) + 1 for x in range(1, N+1))

def red_support(p):
    return frozenset(x for x in range(1, N+1) if p[x-1] in red)

cyclic_supports = [red_support(shift_perm(t)) for t in range(N)]
check(frozenset({1, 3}) not in cyclic_supports, "opposite support unexpectedly hit")
check(frozenset({1, 2}) in cyclic_supports, "adjacent support missing")

# F. Quenched seed identity: for every fixed seed sigma, {g o sigma:g in S_N}=S_N.
for N in range(3, 7):
    perms = list(itertools.permutations(range(1, N+1)))
    target = set(perms)
    def compose(g, sigma):
        return tuple(g[sigma[x]-1] for x in range(N))
    seeds = perms if N <= 5 else perms[:20]
    for sigma in seeds:
        orbit = {compose(g, sigma) for g in perms}
        check(orbit == target, ("seeded orbit", N, sigma))

# G. C030 finite tree-visible separation from C029.
# Rotor entries are duplicated. At N=4 the first entry is (s=1,g=id),
# repeated twice. If the root splits in step 1, its 3-child is entirely
# blue under the identical second map and cannot split in step 2.
N = 4
red = {1}
for sigma in itertools.permutations(range(1, N+1)):
    red_labels = {l for l in range(1, N+1) if sigma[l-1] in red}
    check(len(red_labels) == 1, ("one red label", sigma))
    child = [l for l in range(1, N+1) if l not in red_labels]
    check(all(sigma[l-1] not in red for l in child), ("child not all blue", sigma))

Delta_C029 = Fraction(1, 16)
a1_C029 = Delta_C029 * c(4, 1)
a2_C029 = Delta_C029 * c(4, 2)
check(a1_C029 == Fraction(1, 8), a1_C029)
check(a2_C029 == Fraction(3, 32), a2_C029)
E_C029 = a1_C029 * a2_C029
check(E_C029 == Fraction(3, 256), E_C029)
E_C030 = Fraction(0)
check(E_C030 != E_C029, ("finite separation", E_C030, E_C029))

# H. C030 scaling. Each (s,g) appears twice in one cycle.
for N in range(3, 30):
    M = 2 * (N-1) * factorial(N)
    tau = Fraction(1, N**3)
    delta = tau / M
    max_c = max(c(N, s) for s in range(1, N))
    check(delta * max_c < 1, ("activation probability", N))
    check(tau * N * N == Fraction(1, N), ("cycle error scale", N))

N = 4
M = 2 * (N-1) * factorial(N)
tau = Fraction(1, N**3)
delta = tau / M
a1_C030 = delta * c(N, 1)
check(M == 144, M)
check(tau == Fraction(1, 64), tau)
check(delta == Fraction(1, 9216), delta)
check(a1_C030 == Fraction(1, 4608), a1_C030)

# I. First-visible root particular-support ratio at N=4. The rotor order
# groups all duplicated (s=1,g), then s=2, then s=3. Root survival is
# seed-independent. Repeating whole cycles does not change this ratio.
u = 1 - a1_C030
a2_C030 = delta * c(4, 2)
v = 1 - a2_C030
nphase = 2 * factorial(4)
U1 = 1 - u**nphase
U2 = u**nphase * (1 - v**nphase)
U3 = (u*v)**nphase * (1 - u**nphase)
R_C030 = Fraction(3, 4) * (U1 + U3) / U2
check(u == Fraction(4607, 4608), u)
check(v == Fraction(6143, 6144), v)
check(R_C030 > 2, ("R_C030 <= 2", R_C030))
check(R_C030 < Fraction(459, 224), ("R_C030 >= C029 witness", R_C030))
prior_binary = [
    Fraction(2,1), Fraction(7,5), Fraction(2699,1365), Fraction(2273,1153),
    Fraction(61381,43765), Fraction(166094447739,85563797248), Fraction(33,17),
    Fraction(5,3), Fraction(597,359), Fraction(18,11), Fraction(9,5),
    Fraction(5,4), Fraction(459,224),
]
for q in prior_binary:
    check(R_C030 != q, ("binary witness collision", q))

print("C030 seeded permutation rotor exact checker")
print("exact_checks =", CHECKS)
print("N=4 C030 first-step activation =", a1_C030)
print("N=4 witness P_C030(root split step1 and 3-child split step2) =", E_C030)
print("N=4 C029 comparison event =", E_C029)
print("cyclic_shift_failure_supports_N4_s2 =", sorted(map(sorted, cyclic_supports)))
print("N=4 first-visible particular-support ratio R_C030 =", float(R_C030))
print("exact bracket: 2 < R_C030 < 459/224")
print("ALL_EXACT_CHECKS_PASS")
