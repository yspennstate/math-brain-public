from fractions import Fraction


def theta_graph(a, k):
    """Two terminals 0,1; k internally-disjoint length-a unit paths."""
    edges = []
    next_v = 2
    for _ in range(k):
        if a == 1:
            edges.append((0, 1))
            continue
        prev = 0
        for _ in range(a - 1):
            w = next_v
            next_v += 1
            edges.append((prev, w))
            prev = w
        edges.append((prev, 1))
    return next_v, edges


def components(n, edges, mask):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x, y = find(x), find(y)
        if x == y:
            return False
        parent[y] = x
        return True

    for i, (x, y) in enumerate(edges):
        if (mask >> i) & 1:
            if not union(x, y):
                return None
    return find(0) == find(1)


theta_cases = 0
theta_examples = []
for a in range(1, 5):
    for k in range(1, 5):
        n, edges = theta_graph(a, k)
        m = len(edges)
        if m > 12:
            continue
        disconnected = connected = 0
        for mask in range(1 << m):
            state = components(n, edges, mask)
            if state is None:
                continue
            if state:
                connected += 1
            else:
                disconnected += 1
        expected_d = (2**a - 1) ** k
        expected_c = k * (2**a - 1) ** (k - 1)
        assert (disconnected, connected) == (expected_d, expected_c)
        theta_cases += 1
        theta_examples.append(
            (a, k, disconnected, connected, Fraction(connected, disconnected))
        )

# Exact rational regression for the straddling mixture lemma.
# q=(1-p)q0+p q1, q0<=ell<q<u<=q1.
# Verify Cov(X,Y)>=((q-ell)(u-q))/(u-ell) and the two p bounds.
mix_cases = 0
min_slack = None
for denominator in (8, 12):
    N = denominator
    for i0 in range(N + 1):
        q0 = Fraction(i0, N)
        for i1 in range(i0 + 1, N + 1):
            q1 = Fraction(i1, N)
            for jp in range(1, N):
                p = Fraction(jp, N)
                q = (1 - p) * q0 + p * q1
                for il in range(i0, N + 1):
                    ell = Fraction(il, N)
                    if not (q0 <= ell < q):
                        continue
                    for iu in range(il + 1, N + 1):
                        u = Fraction(iu, N)
                        if not (q < u <= q1):
                            continue
                        cov = p * (1 - p) * (q1 - q0)
                        kappa = (q - ell) * (u - q) / (u - ell)
                        assert cov >= kappa
                        lower = (q - ell) / (1 - ell)
                        upper = q / u
                        assert p >= lower
                        assert p <= upper
                        slack = cov - kappa
                        min_slack = slack if min_slack is None else min(min_slack, slack)
                        mix_cases += 1

print("THETA_FORMULA_CASES", theta_cases)
for row in theta_examples:
    print("THETA", *row)
print("MIXTURE_GRID_CASES", mix_cases)
print("MIXTURE_MIN_SLACK", min_slack)
print("STATUS=PASS")
