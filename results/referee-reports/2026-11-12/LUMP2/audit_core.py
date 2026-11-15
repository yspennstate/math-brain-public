"""Independent exact audit utilities. No imports from the author's checks.

Hitting times solve (I-P)_killed h=1, not a potential or quotient update.
All arithmetic is fractions.Fraction; no numerical libraries or external writes.
"""
from fractions import Fraction as Q


def solve(a, b):
    """Gaussian elimination with back substitution; empty systems allowed."""
    n = len(b)
    a = [[Q(v) for v in row] for row in a]
    b = list(map(Q, b))
    for k in range(n):
        pivot = next(j for j in range(k, n) if a[j][k])
        a[k], a[pivot] = a[pivot], a[k]
        b[k], b[pivot] = b[pivot], b[k]
        for j in range(k + 1, n):
            f = a[j][k] / a[k][k]
            if not f:
                continue
            for z in range(k + 1, n):
                a[j][z] -= f * a[k][z]
            b[j] -= f * b[k]
            a[j][k] = Q(0)
    x = [Q(0)] * n
    for j in reversed(range(n)):
        x[j] = (b[j] - sum(a[j][k] * x[k] for k in range(j + 1, n))) / a[j][j]
    return x


def inverse(a):
    n = len(a)
    cols = [solve(a, [int(k == j) for k in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def chain(weights):
    w = [[Q(v) for v in row] for row in weights]
    n = len(w)
    d = list(map(sum, w))
    total = sum(d)
    pi = [v / total for v in d]
    p = [[v / d[i] for v in row] for i, row in enumerate(w)]
    lap = [[(d[i] if i == j else 0) - w[i][j] for j in range(n)] for i in range(n)]
    h = [[Q(0)] * n for _ in range(n)]
    for target in range(n):
        keep = [i for i in range(n) if i != target]
        killed = [[int(i == j) - p[i][j] for j in keep] for i in keep]
        sol = solve(killed, [1] * len(keep))
        for i, value in zip(keep, sol):
            h[i][target] = value
    mu = [sum(pi[i] * h[i][j] for i in range(n)) for j in range(n)]
    f = [[h[i][j] - mu[j] for j in range(n)] for i in range(n)]
    kap = list(map(max, f))
    return dict(n=n, w=w, d=d, W=total, pi=pi, P=p, L=lap, H=h, mu=mu, F=f,
                kappa=kap, T=max(kap), phi=[[kap[i] - f[i][j] for j in range(n)] for i in range(n)])


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def mul(a, x):
    return [dot(row, x) for row in a]


def energy(c, x, y):
    return sum(c['w'][i][j] * (x[i] - x[j]) * (y[i] - y[j])
               for i in range(c['n']) for j in range(i))


def quotient(w, blocks):
    return [[sum(w[i][j] for i in a for j in b) for b in blocks] for a in blocks]


def killed(c, targets):
    keep = [i for i in range(c['n']) if i not in targets]
    sol = solve([[int(i == j) - c['P'][i][j] for j in keep] for i in keep], [1] * len(keep))
    result = [Q(0)] * c['n']
    for i, v in zip(keep, sol):
        result[i] = v
    return result


def potentials(c, root):
    keep = [i for i in range(c['n']) if i != root]
    inv = inverse([[c['L'][i][j] for j in keep] for i in keep])
    gamma = [[Q(0)] * c['n'] for _ in range(c['n'])]
    for i, x in enumerate(keep):
        for j, y in enumerate(keep):
            gamma[x][y] = inv[i][j]
    return gamma
