# T115: numerical test of the steps in "Average sensitivity of polynomial threshold functions" (OpenAI, 25 Sep 2026):
# Lemma 2 (one-sided coupling), the weighted grading of Section 3, Lemma 3 (edges from the anticommutator),
# and the assembly of Section 5. Floating point; small n only, where the final bound 8 d sqrt(n) exceeds n and
# only the intermediate inequalities carry information.
import itertools, math
import numpy as np

def out(*a):
    print(*a, flush=True)

rng = np.random.default_rng(11)

def cube(n):
    X = np.array(list(itertools.product([-1, 1], repeat=n)), dtype=float)
    subsets = sorted(itertools.chain.from_iterable(itertools.combinations(range(n), k) for k in range(n + 1)), key=len)
    deg = np.array([len(S) for S in subsets])
    Chi = np.ones((2**n, len(subsets)))
    for j, S in enumerate(subsets):
        for i in S:
            Chi[:, j] *= X[:, i]
    return X, subsets, deg, Chi

def grading(w, Chi, deg, n):
    """orthonormal basis adapted to E_0, ..., E_n for the weight w, and M = sum (k - n/2) Pi_k"""
    Q, R = np.linalg.qr(np.sqrt(w)[:, None]*Chi)
    M = (Q*(deg - n/2)) @ Q.T
    return Q, M

def hamming(X):
    return ((X[:, None, :] != X[None, :, :]).sum(axis=2))

worst = dict(edge=0.0, FA=-1e9, lem3=-1e9, blocks=0.0, marg=0.0, lem2=-1e9, final=-1e9, ratio_lem3=0.0, ratio_lem2=0.0, ratio_all=0.0)
cases = 0
for n in range(2, 9):
    X, subsets, deg, Chi = cube(n)
    N = 2**n
    rho = hamming(X)
    # unweighted: M = -A/2
    Q, M = grading(np.ones(N), Chi, deg, n)
    A = (rho == 1).astype(float)
    out("n=%d  unweighted: |M + A/2| = %.1e ; ||M||_HS^2 - nN/4 = %.1e" % (n, np.abs(M + A/2).max(), (M**2).sum() - n*N/4))
    parity = Chi[:, -1]
    reps = 60 if n <= 6 else 12
    for rep in range(reps):
        d = int(rng.integers(1, min(n, 4) + 1))
        kind = rep % 4
        # a polynomial of degree at most d
        coef = np.zeros(N)
        low = deg <= d
        if kind == 0:
            coef[low] = rng.normal(size=low.sum())
        elif kind == 1:                       # sparse
            idx = rng.choice(np.where(low)[0], size=min(low.sum(), 3 + rep % 5), replace=False)
            coef[idx] = rng.normal(size=len(idx))
        elif kind == 2:                       # symmetric, roots between central levels
            t = (n + X.sum(axis=1))/2
            J = sorted(range(n), key=lambda j: abs(j - (n - 1)/2))[:d]
            p = np.ones(N)
            for j in J:
                p *= (t - j - 0.5)
            coef = Chi.T @ p / N
        else:                                 # integer coefficients, zeros of p on the cube likely
            coef[low] = rng.integers(-2, 3, size=low.sum())
        p = Chi @ coef
        assert np.abs((Chi.T @ p / N)[deg > d]).max(initial=0.0) < 1e-9
        f = np.where(p >= 0, 1.0, -1.0)
        # the perturbation of Section 5
        neg = p < 0
        eps = 0.5*np.abs(p[neg]).min() if neg.any() else 1.0
        p2 = p + eps
        if np.abs(p2).min() < 1e-9:
            continue
        assert (np.where(p2 >= 0, 1.0, -1.0) == f).all()
        w = np.abs(p2)
        h = parity*f
        Q, M = grading(w, Chi, deg, n)
        cases += 1
        off = M - np.diag(np.diag(M))
        worst['edge'] = max(worst['edge'], np.abs(off).max())            # claim: <= 1/2
        A0 = (np.diag(M)**2).sum()
        F = (M[rho >= 2]**2).sum()
        worst['FA'] = max(worst['FA'], F - A0)                           # claim: <= 0
        Eh = (rho == 1) & (h[:, None] == h[None, :])
        T = M*h[None, :] + h[:, None]*M
        T2 = (T**2).sum()
        nE = Eh.sum()
        worst['lem3'] = max(worst['lem3'], nE - 2*T2)                    # claim: <= 0
        if T2 > 0:
            worst['ratio_lem3'] = max(worst['ratio_lem3'], nE/(2*T2))
        # influence directly
        I = 0.0
        for i in range(n):
            flip = X.copy(); flip[:, i] *= -1
            idx = ((flip + 1)/2) @ (2**np.arange(n - 1, -1, -1))
            I += (f != f[idx.astype(int)]).mean()
        assert abs(I - nE/N) < 1e-9
        # grade blocks of H
        HQ = Q.T @ (h[:, None]*Q)
        P = np.zeros((n + 1, n + 1))
        for r in range(n + 1):
            for s in range(n + 1):
                P[s, r] = (HQ[np.ix_(deg == s, deg == r)]**2).sum()/N
        zero = max((P[s, r] for r in range(n + 1) for s in range(n + 1) if r + s < n - d), default=0.0)
        worst['blocks'] = max(worst['blocks'], zero)                     # claim: 0
        binom = np.array([math.comb(n, k) for k in range(n + 1)])/N
        worst['marg'] = max(worst['marg'], np.abs(P.sum(axis=0) - binom).max(), np.abs(P.sum(axis=1) - binom).max())
        second = sum(P[s, r]*(s + r - n)**2 for r in range(n + 1) for s in range(n + 1))
        assert abs(second - T2/N) < 1e-8
        worst['lem2'] = max(worst['lem2'], second - 4*d*math.sqrt(n))    # claim: <= 0
        worst['ratio_lem2'] = max(worst['ratio_lem2'], second/(4*d*math.sqrt(n)))
        worst['final'] = max(worst['final'], I - 8*d*math.sqrt(n))
        worst['ratio_all'] = max(worst['ratio_all'], I/(2*second))
out("cases with a weight built from a polynomial: %d" % cases)
out("largest off-diagonal |M_xy|: %.6f (claim <= 0.5)" % worst['edge'])
out("largest F - A0: %.3e (claim <= 0)" % worst['FA'])
out("largest |E_h| - 2||T||^2: %.3e (claim <= 0); largest ratio |E_h| / (2||T||^2): %.4f" % (worst['lem3'], worst['ratio_lem3']))
out("largest mass on blocks with r + s < n - d: %.1e (claim 0); largest deviation of the marginals from Bin(n,1/2): %.1e" % (worst['blocks'], worst['marg']))
out("largest E(R+S-n)^2 - 4 d sqrt(n): %.3e (claim <= 0); largest ratio: %.4f" % (worst['lem2'], worst['ratio_lem2']))
out("largest I(f) - 8 d sqrt(n): %.3e ; largest I(f) / (2 E(R+S-n)^2): %.4f (claim <= 1)" % (worst['final'], worst['ratio_all']))

# arbitrary positive weights and arbitrary sign functions (Lemma 3 as stated)
w3 = -1e9; r3 = 0.0; e3 = 0.0
for n in range(2, 8):
    X, subsets, deg, Chi = cube(n); N = 2**n; rho = hamming(X)
    for rep in range(40):
        w = np.exp(rng.normal(scale=rng.choice([0.3, 1.5, 4.0]), size=N))
        h = rng.choice([-1.0, 1.0], size=N)
        Q, M = grading(w, Chi, deg, n)
        T = M*h[None, :] + h[:, None]*M
        nE = ((rho == 1) & (h[:, None] == h[None, :])).sum()
        T2 = (T**2).sum()
        w3 = max(w3, nE - 2*T2); r3 = max(r3, nE/(2*T2)); e3 = max(e3, np.abs(M - np.diag(np.diag(M))).max())
out("Lemma 3 with random weights and random signs: largest |E_h| - 2||T||^2 = %.3e, largest ratio %.4f, largest off-diagonal entry %.6f" % (w3, r3, e3))

# Lemma 2: U stationary for a chain whose upward jumps are at most a, V the next state
best = 0.0; viol = -1e9
for rep in range(4000):
    m = int(rng.integers(3, 40)); a = int(rng.integers(0, 6))
    Pm = rng.random((m, m))**rng.choice([1.0, 4.0, 12.0])
    if rep % 3 == 0:
        Pm *= (rng.random((m, m)) < 0.3)
    for i in range(m):
        Pm[i, i + a + 1:] = 0.0
        Pm[i, i] += 1e-6
    Pm /= Pm.sum(axis=1, keepdims=True)
    vals, vecs = np.linalg.eig(Pm.T)
    pi = np.real(vecs[:, np.argmin(np.abs(vals - 1))]); pi = np.abs(pi)/np.abs(pi).sum()
    pos = np.sort(rng.random(m))*rng.choice([1.0, 10.0]) if rep % 2 else np.arange(m, dtype=float)
    gap_up = max((pos[j] - pos[i] for i in range(m) for j in range(i + 1, m) if Pm[i, j] > 0), default=0.0)
    mean = pi @ pos; sig = math.sqrt(max(pi @ (pos - mean)**2, 0.0))
    lhs = sum(pi[i]*Pm[i, j]*(pos[i] - pos[j])**2 for i in range(m) for j in range(m))
    rhs = 8*gap_up*sig
    viol = max(viol, lhs - rhs)
    if rhs > 1e-12:
        best = max(best, lhs/rhs)
out("Lemma 2 on 4000 stationary chains with bounded upward jumps: largest E(U-V)^2 - 8 a sigma = %.3e ; largest ratio %.4f" % (viol, best))
out("done")
