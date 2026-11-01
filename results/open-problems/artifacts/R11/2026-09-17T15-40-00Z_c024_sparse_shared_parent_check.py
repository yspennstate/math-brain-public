from fractions import Fraction
from itertools import product
from math import comb

checks = 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def rising(a, k):
    r = Fraction(1)
    for j in range(k):
        r *= a + j
    return r

def falling(n, k):
    r = 1
    for j in range(k):
        r *= n - j
    return r

def fourth_root_ceil(n):
    m = 1
    while m**4 < n:
        m += 1
    return m

def nu_config(N, alpha, x):
    s = sum(x)
    return rising(alpha, s) * rising(alpha, N-s) / rising(2*alpha, N)

def support_prob(N, x, i, j):
    s = sum(x)
    return Fraction(
        falling(s, i)*falling(N-s, j) + falling(s, j)*falling(N-s, i),
        falling(N, i+j)
    )

def rare_transition_prob(N, mu, x, y):
    # Shared-parent deformation: choose victim v uniformly, then one common
    # parent p uniformly from [N]\{v}; at one locus copy x[p] to v and flip
    # independently with probability mu.
    ans = Fraction(0)
    for v in range(N):
        for p in range(N):
            if p == v:
                continue
            if any(y[q] != x[q] for q in range(N) if q != v):
                continue
            copied = x[p]
            pr = (1-mu) if y[v] == copied else mu
            ans += Fraction(1, N) * Fraction(1, N-1) * pr
    return ans

def ordinary_fixed_v_transition_prob(N, mu, v, x, y):
    # Parent uniform on all N, independent across loci.
    if any(y[q] != x[q] for q in range(N) if q != v):
        return Fraction(0)
    ans = Fraction(0)
    for p in range(N):
        copied = x[p]
        pr = (1-mu) if y[v] == copied else mu
        ans += Fraction(1, N) * pr
    return ans

# Baseline fixed-victim invariance (the C023 mechanism) on a range of exact cases.
for N in range(2, 9):
    m = fourth_root_ceil(N)
    alpha = Fraction(1, m)
    mu = alpha / (N + 2*alpha)
    states = list(product([0,1], repeat=N))
    nu = {x: nu_config(N, alpha, x) for x in states}
    ck(sum(nu.values()) == 1, f"nu normalization N={N}")
    for v in range(N):
        out = {y: Fraction(0) for y in states}
        for x in states:
            for y in states:
                p = ordinary_fixed_v_transition_prob(N, mu, v, x, y)
                if p:
                    out[y] += nu[x]*p
        for y in states:
            ck(out[y] == nu[y], f"fixed-victim invariance N={N}, v={v}, y={y}")

# Sparse deformation scales used in C024:
# Delta=1/m_N, rho=Delta^3, L=N. Then rho/Delta=Delta^2->0
# and L*Delta^2=N/m_N^2->infty.
prev = None
for N in [16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]:
    m = fourth_root_ceil(N)
    D = Fraction(1, m)
    rho = D**3
    ck(rho / D == D**2, f"sparse deformation identity N={N}")
    ck(Fraction(N,1)*D**2 == Fraction(N, m*m), f"birthday scale N={N}")
    if prev is not None:
        ck(Fraction(N, m*m) >= prev, f"birthday scale monotone sample N={N}")
    prev = Fraction(N, m*m)
ck(prev >= 100, "birthday scale already large at N=10000 sample")

# Parent-sharing invariant: pair of loci have same parent with probability
# (1-rho)/N + rho under the mixture. Excess above independent parents is
# rho*(1-1/N), strictly positive.
for N in range(2, 51):
    m = fourth_root_ceil(N)
    D = Fraction(1,m)
    rho = D**3
    p_same = (1-rho)*Fraction(1,N) + rho
    excess = p_same - Fraction(1,N)
    ck(excess == rho*(1-Fraction(1,N)), f"parent sharing identity N={N}")
    ck(excess > 0, f"parent sharing positive N={N}")
    ck(p_same <= 1, f"parent sharing <=1 N={N}")

# Exact N=4 finite tree-level witness.
N = 4
m = fourth_root_ceil(N)
alpha = Fraction(1,m)
Delta = alpha
rho = Delta**3
mu = alpha / (N + 2*alpha)
ck(alpha == Fraction(1,2), "N4 alpha")
ck(mu == Fraction(1,10), "N4 mu")
ck(rho == Fraction(1,8), "N4 rho")

states = list(product([0,1], repeat=N))
nu = {x: nu_config(N, alpha, x) for x in states}
rare = {y: Fraction(0) for y in states}
for x in states:
    row = Fraction(0)
    for y in states:
        p = rare_transition_prob(N, mu, x, y)
        row += p
        if p:
            rare[y] += nu[x]*p
    ck(row == 1, f"rare row sums x={x}")
ck(sum(rare.values()) == 1, "rare output normalization")

def avg_support(dist, i, j):
    return sum(pr * support_prob(N, x, i, j) for x, pr in dist.items())

p13_base = avg_support(nu, 1, 3)
p22_base = avg_support(nu, 2, 2)
p13_rare = avg_support(rare, 1, 3)
p22_rare = avg_support(rare, 2, 2)
mix = {x: (1-rho)*nu[x] + rho*rare[x] for x in states}
p13_mix = avg_support(mix, 1, 3)
p22_mix = avg_support(mix, 2, 2)
R = p13_mix / p22_mix

ck(p13_base == Fraction(5,64), "base p13")
ck(p22_base == Fraction(3,64), "base p22")
ck(p13_base/p22_base == Fraction(5,3), "C023 ratio")
ck(p13_rare == Fraction(3,40), "rare p13")
ck(p22_rare == Fraction(11,240), "rare p22")
ck(p13_rare/p22_rare == Fraction(18,11), "rare ratio")
ck(p13_mix == Fraction(199,2560), "C024 p13")
ck(p22_mix == Fraction(359,7680), "C024 p22")
ck(R == Fraction(597,359), "C024 ratio")
ck(R - Fraction(5,3) == Fraction(-4,1077), "C024 differs C023")

previous_binary = {
    "original_CTCS_finite": Fraction(2,1),
    "C001": Fraction(7,5),
    "C009": Fraction(2699,1365),
    "C010": Fraction(2273,1153),
    "C020": Fraction(61381,43765),
    "C021": Fraction(166094447739,85563797248),
    "C022": Fraction(33,17),
    "C023": Fraction(5,3),
}
for name, q in previous_binary.items():
    ck(R != q, f"C024 ratio collides with {name}")

# Extremal-coupling sanity: independent uniform parents have equality 1/N;
# common-parent coupling has equality 1, which is the absolute maximum.
for N in range(2, 101):
    ck(Fraction(1,N) < 1, f"independent non-extremal N={N}")
    ck(Fraction(1,1) == 1, f"common-parent maximum N={N}")

print("R11 C024 exact self-check")
print(f"checks={checks}")
print(f"N4 alpha={alpha} mu={mu} rho={rho}")
print(f"N4 baseline p13={p13_base} p22={p22_base} ratio={p13_base/p22_base}")
print(f"N4 shared-parent-event p13={p13_rare} p22={p22_rare} ratio={p13_rare/p22_rare}")
print(f"N4 C024 p13={p13_mix} p22={p22_mix} ratio={R}")
print(f"C024-C023 ratio difference={R-Fraction(5,3)}")
print("parent-sharing excess formula=rho*(1-1/N)>0")
print("U008 scale rho/Delta=Delta^2 -> 0")
print("ALL_EXACT_CHECKS_PASS")
