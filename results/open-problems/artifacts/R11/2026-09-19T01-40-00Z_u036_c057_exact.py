from fractions import Fraction
from itertools import product, combinations

ASSERTS = 0

def check(cond, msg=""):
    global ASSERTS
    ASSERTS += 1
    if not cond:
        raise AssertionError(msg)


def split_poly(k, i):
    A = set(range(i))
    B = set(range(i, k))
    poly = {}
    Bl = list(B)
    for r in range(len(Bl) + 1):
        for D in combinations(Bl, r):
            S = frozenset(A | set(D))
            poly[S] = poly.get(S, 0) + (-1) ** r
    Al = list(A)
    for r in range(len(Al) + 1):
        for E in combinations(Al, r):
            S = frozenset(B | set(E))
            poly[S] = poly.get(S, 0) + (-1) ** r
    return {S: c for S, c in poly.items() if c}


# U036: exact split-indicator degree and sharp first detector.
for k in range(2, 13):
    for i in range(1, k):
        p = split_poly(k, i)
        deg = max(map(len, p))
        check(deg == (k if k % 2 == 0 else k - 1), (k, i, deg))
        if k % 2 == 0:
            check(p[frozenset(range(k))] == 2 * ((-1) ** i))
        else:
            check(frozenset(range(k)) not in p)
            check(any(len(S) == k - 1 for S in p))

for d in range(2, 11):
    K = d + 1 if d % 2 else d + 2
    for k in range(2, K):
        for i in range(1, k):
            check(max(map(len, split_poly(k, i))) <= d, (d, k, i))
    for i in range(1, K):
        check(max(map(len, split_poly(K, i))) > d, (d, K, i))


# Walsh/parity perturbation is (k-1)-wise independent and changes every
# specified split at the first even detector size.
eps = Fraction(1, 2)
for k in [4, 6, 8, 10]:
    states = list(product([0, 1], repeat=k))
    probs = {
        z: Fraction(1, 2**k) * (1 + eps * ((-1) ** sum(z)))
        for z in states
    }
    check(sum(probs.values()) == 1)
    check(all(p >= 0 for p in probs.values()))
    for r in range(0, k):
        for S in combinations(range(k), r):
            for pat in product([0, 1], repeat=r):
                got = sum(
                    p for z, p in probs.items()
                    if all(z[S[t]] == pat[t] for t in range(r))
                )
                check(got == Fraction(1, 2**r), (k, r, S, pat, got))
    for i in range(1, k):
        A = set(range(i))
        B = set(range(k)) - A
        got = sum(
            p for z, p in probs.items()
            if (
                all(z[a] == 1 for a in A) and all(z[b] == 0 for b in B)
            ) or (
                all(z[a] == 0 for a in A) and all(z[b] == 1 for b in B)
            )
        )
        want = Fraction(1, 2 ** (k - 1)) * (1 + eps * ((-1) ** i))
        check(got == want, (k, i, got, want))


def prod_bern_prob(x, z):
    s = sum(z)
    return (x**s) * ((1 - x) ** (len(z) - s))


def tilted_prob(x, z, T):
    K = len(T)
    M = max(x, 1 - x)
    h = Fraction(1, 1)
    for t in T:
        h *= Fraction(z[t], 1) - x
    return prod_bern_prob(x, z) * (1 + h / (M**K))


def mixed_tilt_dist(N, x):
    K = 2 * (N // 2)
    Ts = list(combinations(range(N), K))
    out = {}
    for z in product([0, 1], repeat=N):
        out[z] = sum((tilted_prob(x, z, T) for T in Ts), Fraction(0)) / len(Ts)
    return out


# C057: exact positivity/normalization and (K_N-1)-wise Bernoulli marginals.
for N in range(4, 8):
    K = 2 * (N // 2)
    for j in range(1, N):
        x = Fraction(j, N)
        dist = mixed_tilt_dist(N, x)
        check(sum(dist.values()) == 1, (N, j, sum(dist.values())))
        check(all(p >= 0 for p in dist.values()), (N, j))
        for r in range(1, K):
            for S in combinations(range(N), r):
                for pat in product([0, 1], repeat=r):
                    got = sum(
                        p for z, p in dist.items()
                        if all(z[S[t]] == pat[t] for t in range(r))
                    )
                    want = prod_bern_prob(x, pat)
                    check(got == want, (N, j, r, S, pat, got, want))


def mixed_split_prob(N, x, A):
    dist = mixed_tilt_dist(N, x)
    A = set(A)
    B = set(range(N)) - A
    z1 = tuple(1 if i in A else 0 for i in range(N))
    z2 = tuple(1 if i in B else 0 for i in range(N))
    return dist[z1] + dist[z2]


# Exact N=4 finite non-equivalence witness against the harmonic-grid iid paintbox.
N = 4
xs = [Fraction(j, N) for j in range(1, N)]
weights = [Fraction(1, N) * Fraction(1, 2 * x * (1 - x)) for x in xs]
q_pair = sum(w * (2 * x * (1 - x)) for x, w in zip(xs, weights))
q_13 = sum(w * mixed_split_prob(4, x, {0}) for x, w in zip(xs, weights))
q_22 = sum(w * mixed_split_prob(4, x, {0, 1}) for x, w in zip(xs, weights))
check(q_pair == Fraction(3, 4), q_pair)
check(q_13 == Fraction(7, 48), q_13)
check(q_22 == Fraction(11, 48), q_22)
check(q_13 / q_pair == Fraction(7, 36))
check(q_22 / q_pair == Fraction(11, 36))

print("ALL_EXACT_CHECKS_PASS")
print(f"assertions={ASSERTS}")
print(f"N4_pair={q_pair}")
print(f"N4_1|3={q_13}; normalized={q_13 / q_pair}")
print(f"N4_2|2={q_22}; normalized={q_22 / q_pair}")
