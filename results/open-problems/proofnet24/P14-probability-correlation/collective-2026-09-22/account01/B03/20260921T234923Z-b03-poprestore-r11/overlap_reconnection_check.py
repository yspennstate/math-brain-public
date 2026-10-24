from itertools import combinations


def forest(n, es):
    p = list(range(n))

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    for a, b in es:
        a, b = find(a), find(b)
        if a == b:
            return False
        p[b] = a
    return True


def roots(n, es):
    p = list(range(n))

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    for a, b in es:
        a, b = find(a), find(b)
        if a != b:
            p[b] = a
    return [find(i) for i in range(n)]


def stats(n, E, e, f):
    R = [g for g in E if g not in (e, f)]
    n00 = n10 = n01 = n11 = q = 0
    for mask in range(1 << len(R)):
        H = [R[j] for j in range(len(R)) if (mask >> j) & 1]
        if not forest(n, H):
            continue
        c = roots(n, H)
        X = c[e[0]] != c[e[1]]
        Y = c[f[0]] != c[f[1]]
        Q = X and Y and {c[e[0]], c[e[1]]} == {c[f[0]], c[f[1]]}
        if X and Y:
            n11 += 1
        elif X:
            n10 += 1
        elif Y:
            n01 += 1
        else:
            n00 += 1
        q += int(Q)
    N = n00 + n10 + n01 + n11
    B = n10 + n11
    C = n01 + n11
    D = n11 - q
    delta = B * C - N * D
    rhs = n10 * n01 - n00 * n11 + N * q
    assert delta == rhs
    return (N, n00, n10, n01, n11, q, delta)


# Minimal witness to failure of the tempting overlap-free covariance bound.
E = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)]  # K4 minus edge (2,3)
print("witness", stats(4, E, (0, 1), (0, 2)))

# Exhaust all simple graphs on at most five vertices and all distinguished edge pairs.
pairs = 0
identity_failures = 0
first_naive = None
for n in range(2, 6):
    K = list(combinations(range(n), 2))
    for gmask in range(1 << len(K)):
        E = [K[i] for i in range(len(K)) if (gmask >> i) & 1]
        for e, f in combinations(E, 2):
            N, n00, n10, n01, n11, q, delta = stats(n, E, e, f)
            pairs += 1
            if delta != n10 * n01 - n00 * n11 + N * q:
                identity_failures += 1
            if first_naive is None and n10 * n01 - n00 * n11 < 0:
                first_naive = (n, E, e, f, (N, n00, n10, n01, n11, q, delta))
print("pairs_checked", pairs)
print("identity_failures", identity_failures)
print("first_naive_failure", first_naive)
