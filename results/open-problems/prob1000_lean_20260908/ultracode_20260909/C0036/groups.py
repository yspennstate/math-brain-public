# Small finite groups as multiplication tables (elements 0..n-1, identity 0), plus
# random equivariant positive contractions and the exact determinantal law.
import numpy as np


def cyclic(n):
    return np.array([[(i + j) % n for j in range(n)] for i in range(n)])


def direct_product(T1, T2):
    n1, n2 = len(T1), len(T2)
    n = n1 * n2
    T = np.zeros((n, n), dtype=int)
    for a in range(n1):
        for b in range(n2):
            for c in range(n1):
                for d in range(n2):
                    T[a * n2 + b, c * n2 + d] = T1[a, c] * n2 + T2[b, d]
    return T


def from_perms(gens):
    """closure of permutation generators; identity first"""
    deg = len(gens[0])
    idp = tuple(range(deg))
    elems = [idp]
    seen = {idp}
    frontier = [idp]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                gh = tuple(h[g[i]] for i in range(deg))  # h after g
                if gh not in seen:
                    seen.add(gh)
                    elems.append(gh)
                    new.append(gh)
        frontier = new
    idx = {e: i for i, e in enumerate(elems)}
    n = len(elems)
    T = np.zeros((n, n), dtype=int)
    for i, g in enumerate(elems):
        for j, h in enumerate(elems):
            gh = tuple(h[g[k]] for k in range(deg))
            T[i, j] = idx[gh]
    return T


def S3():
    return from_perms([(1, 0, 2), (1, 2, 0)])


def D4():
    return from_perms([(1, 2, 3, 0), (0, 3, 2, 1)])


def Q8():
    names = ['1', '-1', 'i', '-i', 'j', '-j', 'k', '-k']

    def mul(a, b):
        sa = -1 if a.startswith('-') else 1
        sb = -1 if b.startswith('-') else 1
        ua, ub = a.lstrip('-'), b.lstrip('-')
        tab = {('1', '1'): (1, '1'), ('1', 'i'): (1, 'i'), ('1', 'j'): (1, 'j'), ('1', 'k'): (1, 'k'),
               ('i', '1'): (1, 'i'), ('j', '1'): (1, 'j'), ('k', '1'): (1, 'k'),
               ('i', 'i'): (-1, '1'), ('j', 'j'): (-1, '1'), ('k', 'k'): (-1, '1'),
               ('i', 'j'): (1, 'k'), ('j', 'k'): (1, 'i'), ('k', 'i'): (1, 'j'),
               ('j', 'i'): (-1, 'k'), ('k', 'j'): (-1, 'i'), ('i', 'k'): (-1, 'j')}
        s, u = tab[(ua, ub)]
        s *= sa * sb
        return ('-' if s < 0 else '') + u

    idx = {nm: i for i, nm in enumerate(names)}
    T = np.zeros((8, 8), dtype=int)
    for i, a in enumerate(names):
        for j, b in enumerate(names):
            T[i, j] = idx[mul(a, b)]
    return T


def inverse_table(T):
    n = len(T)
    inv = np.zeros(n, dtype=int)
    for g in range(n):
        inv[g] = int(np.where(T[g] == 0)[0][0])
    return inv


def check_group(T):
    n = len(T)
    assert all(T[0, g] == g and T[g, 0] == g for g in range(n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                assert T[T[a, b], c] == T[a, T[b, c]]
    inverse_table(T)
    return True


def equivariant_matrix(T, q):
    """Q(x,y) = q(x^{-1} y)"""
    n = len(T)
    inv = inverse_table(T)
    Q = np.zeros((n, n), dtype=complex)
    for x in range(n):
        for y in range(n):
            Q[x, y] = q[T[inv[x], y]]
    return Q


def random_equivariant_contraction(T, rng, kind="random"):
    n = len(T)
    inv = inverse_table(T)
    while True:
        q = rng.normal(size=n) + 1j * rng.normal(size=n)
        q = 0.5 * (q + np.conj(q[inv]))
        H = equivariant_matrix(T, q)
        assert np.allclose(H, H.conj().T)
        w = np.linalg.eigvalsh(H)
        lo, hi = w.min(), w.max()
        if hi - lo < 1e-9:
            continue
        H = (H - lo * np.eye(n)) / (hi - lo)   # spectrum in [0,1], touching both ends
        if kind == "random":
            a, b = np.sort(rng.uniform(0, 1, size=2))
            Q = a * np.eye(n) + (b - a) * H
        elif kind == "full":            # spectrum in [eps, 1-eps], both ends touched
            eps = 10 ** rng.uniform(-6, -3)
            Q = eps * np.eye(n) + (1 - 2 * eps) * H
        elif kind == "near0":
            eps = 10 ** rng.uniform(-4, -1)
            Q = eps * np.eye(n) + (rng.uniform(0.2, 1) - eps) * H
        elif kind == "near1":
            eps = 10 ** rng.uniform(-4, -1)
            Q = (1 - eps) * np.eye(n) - (1 - eps - rng.uniform(0, 0.8)) * H
        Q = 0.5 * (Q + Q.conj().T)
        w = np.linalg.eigvalsh(Q)
        if w.min() > 1e-12 and w.max() < 1 - 1e-12:
            return Q


def determinantal_law(Q):
    """exact P_Q(X = A) for all A, indexed by bitmask: P(X=A) = (-1)^{|A^c|} det(Q - 1_{A^c})"""
    n = len(Q)
    P = np.zeros(2 ** n)
    for m in range(2 ** n):
        M = Q.copy()
        comp = [i for i in range(n) if not (m >> i) & 1]
        for i in comp:
            M[i, i] -= 1
        P[m] = ((-1) ** len(comp) * np.linalg.det(M)).real
    return P


def inclusion_exclusion_law(Q):
    """independent computation: P(X = A) = sum over S containing A of (-1)^{|S|-|A|} det Q_S"""
    n = len(Q)
    N = 2 ** n
    up = np.zeros(N)
    for m in range(N):
        S = [i for i in range(n) if (m >> i) & 1]
        up[m] = np.linalg.det(Q[np.ix_(S, S)]).real if S else 1.0
    P = np.zeros(N)
    for A in range(N):
        s = 0.0
        rest = (N - 1) ^ A
        sub = rest
        while True:
            S = A | sub
            s += (-1) ** (bin(sub).count('1')) * up[S]
            if sub == 0:
                break
            sub = (sub - 1) & rest
        P[A] = s
    return P


def product_law(n, p):
    P = np.zeros(2 ** n)
    for m in range(2 ** n):
        k = bin(m).count('1')
        P[m] = p ** k * (1 - p) ** (n - k)
    return P


def FK(Q):
    w = np.linalg.eigvalsh(Q)
    return float(np.exp(np.mean(np.log(w))))
