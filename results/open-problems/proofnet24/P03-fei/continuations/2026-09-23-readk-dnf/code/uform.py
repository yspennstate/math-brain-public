"""Check the identity  P_mu(A) = sigma_A^2 4^{-|A|} (E_{x outside A} d_A g)^2  for the mu-biased spectrum
(g = 1-2f, x in {0,1}^n, q_j = mu(x_j=1), phi_j = (2x_j-1-nu_j)/sigma_j), where d_A g is the |A|-fold mixed
difference sum_{y subset A} (-1)^{|A minus y|} g(1_y, x_{-A}).  Random f, random biases."""
import numpy as np, itertools
rng = np.random.default_rng(7)
def biased_spectrum(g, q):
    n = len(q); N = 1 << n
    X = ((np.arange(N)[:, None] >> np.arange(n)) & 1).astype(float)
    w = np.prod(np.where(X == 1, q, 1 - q), axis=1)
    nu = 2 * q - 1; sig = np.sqrt(1 - nu ** 2)
    Phi = (2 * X - 1 - nu) / sig
    P = np.zeros(N)
    for A in range(N):
        idx = [j for j in range(n) if A >> j & 1]
        phiA = np.prod(Phi[:, idx], axis=1) if idx else np.ones(N)
        P[A] = (w * g * phiA).sum() ** 2
    return P, sig
def u_form(g, q):
    n = len(q); N = 1 << n
    X = ((np.arange(N)[:, None] >> np.arange(n)) & 1)
    sig2 = 4 * q * (1 - q)
    out = np.zeros(N)
    for A in range(N):
        idx = [j for j in range(n) if A >> j & 1]
        rest = [j for j in range(n) if not A >> j & 1]
        tot = 0.0
        for xr in itertools.product([0, 1], repeat=len(rest)):
            pr = np.prod([q[j] if b else 1 - q[j] for j, b in zip(rest, xr)]) if rest else 1.0
            d = 0.0
            for y in itertools.product([0, 1], repeat=len(idx)):
                x = 0
                for j, b in zip(rest, xr): x |= b << j
                for j, b in zip(idx, y): x |= b << j
                d += (-1) ** (len(idx) - sum(y)) * g[x]
            tot += pr * d
        out[A] = np.prod(sig2[idx]) * 4.0 ** (-len(idx)) * tot ** 2
    return out
worst = 0
for trial in range(40):
    n = int(rng.integers(2, 6)); N = 1 << n
    f = rng.integers(0, 2, N); g = 1 - 2 * f.astype(float)
    q = rng.uniform(0.02, 0.98, n)
    P, _ = biased_spectrum(g, q); U = u_form(g, q)
    worst = max(worst, np.abs(P - U).max())
    assert abs(P.sum() - 1) < 1e-9
print("max |P_mu(A) - sigma_A^2 4^-|A| (E d_A g)^2| over 40 random functions:", worst)
