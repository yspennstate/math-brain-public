from fractions import Fraction as F
from math import comb, factorial
from itertools import combinations


def beta(a, b):
    assert a >= 1 and b >= 1
    return F(factorial(a - 1) * factorial(b - 1), factorial(a + b - 1))


def pi(N, k):
    assert 2 <= k <= N
    return F(N, (N - 1) * k * (k - 1))


checks = {
    "k_law_normalization": 0,
    "kernel_identity": 0,
    "hidden_merger_projection": 0,
    "anchor_full_split": 0,
    "beta_binomial_restriction": 0,
    "scale_bounds": 0,
}

# K-law normalization.
for N in range(2, 41):
    assert sum((pi(N, k) for k in range(2, N + 1)), F(0)) == 1
    checks["k_law_normalization"] += 1

# pi_N(k)/C(N,k) = B(k-1,N-k+1)/(N-1).
for N in range(2, 31):
    for k in range(2, N + 1):
        lhs = pi(N, k) / comb(N, k)
        rhs = beta(k - 1, N - k + 1) / (N - 1)
        assert lhs == rhs
        checks["kernel_identity"] += 1

# A fixed r-subset T of a hidden m-block is the intersection of one active
# global sweep with probability B(r-1,m-r+1)/(N-1).
for N in range(2, 17):
    for m in range(2, N + 1):
        for r in range(2, m + 1):
            lhs = F(0)
            for x in range(0, N - m + 1):
                k = r + x
                lhs += pi(N, k) * F(comb(N - m, x), comb(N, k))
            rhs = beta(r - 1, m - r + 1) / (N - 1)
            assert lhs == rhs
            checks["hidden_merger_projection"] += 1

# Uniform-anchor deletion turns the shifted merger kernel into exactly
# B(i,m-i)/(N-1) for a particular unordered split A|A^c.
for N in range(2, 17):
    for m in range(2, N + 1):
        for i in range(1, m):
            merger = beta(i, m - i) / (N - 1)
            lhs = F(m - i, m) * merger + F(i, m) * merger
            rhs = beta(i, m - i) / (N - 1)
            assert lhs == rhs
            checks["anchor_full_split"] += 1

# Hidden labels cancel exactly under restriction.
for m in range(2, 26):
    for b in range(2, m + 1):
        for i in range(1, b):
            lhs = sum(
                (
                    F(comb(m - b, s - i)) * beta(s, m - s)
                    for s in range(i, m - b + i + 1)
                ),
                F(0),
            )
            rhs = beta(i, b - i)
            assert lhs == rhs
            checks["beta_binomial_restriction"] += 1

# Exact scaling: p_N=1/(2N^2), Delta_N=2p_N/(N-1)=1/(N^2(N-1)).
# The nonlinear two-active-event error per physical unit is
# p_N^2/Delta_N=(N-1)/(4N^2), hence tends to zero.
for N in range(2, 501):
    p = F(1, 2 * N * N)
    delta = F(2) * p / F(N - 1)
    ratio = p * p / delta
    assert ratio == F(N - 1, 4 * N * N)
    assert ratio < F(1, 4 * N)
    checks["scale_bounds"] += 1


# Full exact N=4 two-opportunity enumeration.
def event_dist(N, p):
    d = {None: 1 - p}
    for k in range(2, N + 1):
        mass = p * pi(N, k) / comb(N, k)
        for S in combinations(range(N), k):
            d[S] = mass
    assert sum(d.values(), F(0)) == 1
    return d


def components(n, events):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for S in events:
        if S is None or len(S) < 2:
            continue
        a = S[0]
        for b in S[1:]:
            union(a, b)

    ans = {}
    for x in range(n):
        ans.setdefault(find(x), set()).add(x)
    return list(ans.values())


def canon_split(A, n):
    A = frozenset(A)
    Ac = frozenset(set(range(n)) - set(A))
    if not A or not Ac:
        return None
    return tuple(sorted((tuple(sorted(A)), tuple(sorted(Ac)))))


N = 4
p = F(1, 2 * N * N)
d = event_dist(N, p)
out = {}
for e1, w1 in d.items():
    for e2, w2 in d.items():
        comps = components(N, [e1, e2])
        c_of = {}
        for c in comps:
            for x in c:
                c_of[x] = c
        for anchor in range(N):
            M = c_of[anchor]
            if len(M) == 1:
                key = "none"
            else:
                key = canon_split(set(M) - {anchor}, N)
            out[key] = out.get(key, F(0)) + w1 * w2 * F(1, N)

assert sum(out.values(), F(0)) == 1
p_none = out["none"]
p_13 = out[canon_split({0}, N)]
p_22 = out[canon_split({0, 1}, N)]
ratio = p_13 / p_22
assert p_none == F(319225, 331776)
assert p_13 == F(2273, 331776)
assert p_22 == F(1153, 331776)
assert ratio == F(2273, 1153)

# Frozen-equivalence comparisons against the previous binary classes.
assert ratio != F(2, 1)          # original CTCS
assert ratio != F(7, 5)          # C001 harmonic-grid paintbox
assert ratio != F(2699, 1365)    # C009 RRT anchor-lift

total = sum(checks.values())
print("R11 I0054 C010 exact checker")
for k, v in checks.items():
    print(f"{k}={v}")
print(f"N4_no_visible={p_none}")
print(f"N4_particular_1v3={p_13}")
print(f"N4_particular_2v2={p_22}")
print(f"N4_ratio={ratio}")
print(f"recorded_identity_checks={total}")
print("ALL_EXACT_CHECKS_PASS")
