"""Independent referee routines; no imports from the submitted code."""
from fractions import Fraction as F


def inverse(a):
    n = len(a)
    q = [[F(x) for x in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for j in range(n):
        k = next(k for k in range(j, n) if q[k][j])
        q[j], q[k] = q[k], q[j]
        pivot = q[j][j]
        q[j] = [v / pivot for v in q[j]]
        for k in range(n):
            if k != j:
                c = q[k][j]
                q[k] = [x - c*y for x, y in zip(q[k], q[j])]
    return [row[n:] for row in q]


def exact_chain(w):
    """Grounded conductance inverse, rather than the authors' hitting solves.

    If K is inverse grounded Laplacian, extended by a zero root row/column,
    H_ij=(Kd)_i-(Kd)_j-total*(K_ij-K_jj).
    """
    w = [[F(v) for v in row] for row in w]
    n = len(w)
    d = list(map(sum, w))
    total = sum(d)
    pi = [v/total for v in d]
    lap = [[(d[i] if i == j else F(0))-w[i][j]
            for j in range(n-1)] for i in range(n-1)]
    ki = inverse(lap)
    k = [row + [F(0)] for row in ki] + [[F(0)]*n]
    kd = [sum(x*y for x,y in zip(row, d)) for row in k]
    h = [[kd[i]-kd[j]-total*(k[i][j]-k[j][j]) for j in range(n)]
         for i in range(n)]
    means = [sum(pi[i]*h[i][j] for i in range(n)) for j in range(n)]
    deviations = [[h[i][j]-means[j] for j in range(n)] for i in range(n)]
    times = list(map(max, deviations))
    # Independently certify the occupation LP and an attaining stopping rule.
    # v(I-P)=delta_i-pi, v>=0; stop at x on each arrival with
    # probability pi_x/(v_x+pi_x). A zero v_j certifies optimality.
    for start in range(n):
        v = [pi[j]*(times[start]-deviations[start][j]) for j in range(n)]
        assert min(v) == 0 and sum(v) == times[start]
        assert all(x >= 0 for x in v)
        for j in range(n):
            assert v[j]-sum(v[i]*w[i][j]/d[i] for i in range(n)) == F(start == j)-pi[j]
    t0s = [sum(pi[j]*h[i][j] for j in range(n)) for i in range(n)]
    assert len(set(t0s)) == 1
    return dict(pi=pi, d=d, H=h, D=deviations, starts=times,
                tmix=max(times), tau0=t0s[0])


def lump(w, labels):
    m = max(labels)+1
    v = [[F(0)]*m for _ in range(m)]
    for i, row in enumerate(w):
        for j, x in enumerate(row):
            v[labels[i]][labels[j]] += x
    return v


def comb(n, h, alpha, r, heavy=True, ell=None):
    h, alpha, r = map(F, (h, alpha, r))
    size = 2*n+2
    w = [[F(0)]*size for _ in range(size)]
    def edge(a,b,c):
        w[a][b] = w[b][a] = c
    for j in range(n):
        edge(j, j+1, r**j)
        edge(n+1+j, j+1, alpha*r**j)
        w[n+1+j][n+1+j] = (h-1)*alpha*r**j
    edge(n,size-1,r**n)
    if ell is None:
        rest = sum(map(sum,w))-r**n
        ell = (n+2)*h**2*rest-r**n if heavy else F(0)
    w[-1][-1] = F(ell)
    labels = list(range(n+1))+list(range(n))+[n+1]
    return w, labels


def exact_hit(w, target):
    outside = [i for i in range(len(w)) if i not in target]
    d = list(map(sum,w))
    l = [[F(d[i] if i == j else 0)-w[i][j] for j in outside]
         for i in outside]
    k = inverse(l)
    g = [[k[i][j]*d[y] for j,y in enumerate(outside)] for i in range(len(outside))]
    times = [F(0)]*len(w)
    for i,x in enumerate(outside):
        times[x] = sum(g[i])
    return outside, times, g, k


def display(x):
    return {'exact': str(x), 'decimal': float(x)}
