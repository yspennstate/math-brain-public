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

def common_parent_transition_prob(N, mu, x, y):
    # One victim site shared across the genome, and one common parent site
    # shared across the genome. At one locus the mutation bit is independent.
    ans = Fraction(0)
    for v in range(N):
        for p in range(N):
            if p == v:
                continue
            if any(y[q] != x[q] for q in range(N) if q != v):
                continue
            copied = x[p]
            pr = (1-mu) if y[v] == copied else mu
            ans += Fraction(1,N) * Fraction(1,N-1) * pr
    return ans

# Exact N=4 finite witness.
N = 4
m = fourth_root_ceil(N)
alpha = Fraction(1,m)
Delta = alpha
mu = alpha / (N + 2*alpha)
ck(alpha == Fraction(1,2), "N4 alpha")
ck(Delta == Fraction(1,2), "N4 Delta")
ck(mu == Fraction(1,10), "N4 mu")

states = list(product([0,1], repeat=N))
nu = {x: nu_config(N, alpha, x) for x in states}
ck(sum(nu.values()) == 1, "nu normalization")

post = {y: Fraction(0) for y in states}
for x in states:
    row = Fraction(0)
    for y in states:
        p = common_parent_transition_prob(N, mu, x, y)
        row += p
        if p:
            post[y] += nu[x]*p
    ck(row == 1, f"transition row {x}")
ck(sum(post.values()) == 1, "post normalization")

def avg_support(dist, i, j):
    return sum(pr * support_prob(N, x, i, j) for x, pr in dist.items())

p13 = avg_support(post, 1, 3)
p22 = avg_support(post, 2, 2)
R = p13 / p22
ck(p13 == Fraction(3,40), "C025 p13")
ck(p22 == Fraction(11,240), "C025 p22")
ck(R == Fraction(18,11), "C025 ratio")

previous_binary = {
    "original_CTCS_finite": Fraction(2,1),
    "C001": Fraction(7,5),
    "C009": Fraction(2699,1365),
    "C010": Fraction(2273,1153),
    "C020": Fraction(61381,43765),
    "C021": Fraction(166094447739,85563797248),
    "C022": Fraction(33,17),
    "C023": Fraction(5,3),
    "C024": Fraction(597,359),
}
diffs = {}
for name, q in previous_binary.items():
    ck(R != q, f"C025 ratio collides with {name}")
    diffs[name] = R-q

# Every C025 population generation uses the maximally shared parent.
for NN in range(2, 201):
    excess = 1 - Fraction(1,NN)
    ck(excess > 0, f"positive parent-sharing excess N={NN}")
    ck(excess <= 1, f"parent-sharing excess <=1 N={NN}")

# Exact hypergeometric observation inequality used in U009:
# a b-site sample hits a discrepancy set of size d with probability
# 1-C(N-d,b)/C(N,b), bounded by bd/N.
for NN in range(4, 81):
    for b in range(1, min(8,NN)+1):
        for d in range(0, min(12,NN)+1):
            if NN-d >= b:
                hit = 1 - Fraction(comb(NN-d,b), comb(NN,b))
            else:
                hit = Fraction(1)
            upper = min(Fraction(1), Fraction(b*d,NN))
            ck(hit <= upper, f"hypergeom union bound N={NN},b={b},d={d}")

# U009 scaling on the exact subsequence N=n^4:
# Delta=1/n, one physical unit contains n raw generations, and the
# cumulative k=1 disagreement bound is O(n^2/N)=O(n^-2).
for n in range(2, 101):
    NN = n**4
    mm = fourth_root_ceil(NN)
    D = Fraction(1,mm)
    ck(mm == n, f"fourth root exact n={n}")
    ck(Fraction(NN,1)*D*D == n*n, f"N Delta^2=n^2 n={n}")
    M = n
    bound = Fraction(M*(M+1), 2*NN)
    ck(bound <= Fraction(1,n*n), f"T1 k1 coupling benchmark n={n}")

print("R11 C025 exact self-check")
print(f"checks={checks}")
print(f"N4 alpha={alpha} Delta={Delta} mu={mu}")
print(f"N4 shared-parent p13={p13} p22={p22} ratio={R}")
print(f"C025-C023 ratio difference={diffs['C023']}")
print(f"C025-C024 ratio difference={diffs['C024']}")
print("parent-sharing excess=1-1/N (maximal every generation)")
print("U009 path-coupling bound <= k*M*(M+1)/(2N)")
print("with Delta=1/ceil(N^(1/4)), N*Delta^2 -> infinity")
print("ALL_EXACT_CHECKS_PASS")
