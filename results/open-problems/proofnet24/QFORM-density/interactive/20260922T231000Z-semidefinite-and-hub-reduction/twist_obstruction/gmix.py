try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
"""Exact twisted characteristic functions for Gaussian-mixture product laws.

X_i ~ sum_p w_ip N(a_ip, s_ip^2), independent.  For a multi-index p the product law is N(mu, S), S diagonal, and
   E_{N(mu,S)} exp(i<b,X> + i X^T E X) = det(I - 2i S E)^{-1/2} exp(i b.mu + i mu^T E mu - beta^T (S^{-1} - 2iE)^{-1} beta / 2),
   beta = b + 2 E mu.
T(u) = E exp(i<Pu, X> + i X^T E X) is the weighted sum over multi-indices.  Exact, no Monte Carlo.
"""
import numpy as np, itertools

def components(laws):
    """laws: list of (w, a, s) arrays per coordinate. Returns arrays W (M,), MU (M,n), S (M,n)."""
    idx = list(itertools.product(*[range(len(l[0])) for l in laws]))
    W = np.array([np.prod([laws[i][0][p[i]] for i in range(len(laws))]) for p in idx])
    MU = np.array([[laws[i][1][p[i]] for i in range(len(laws))] for p in idx], float)
    S = np.array([[laws[i][2][p[i]] ** 2 for i in range(len(laws))] for p in idx], float)
    return W, MU, S

def T_of_u(U, P, E, W, MU, S, chunk=4000):
    """U: (m,k) array of u values. Returns complex array (m,) of T(u)."""
    U = np.atleast_2d(U); m = U.shape[0]; n = P.shape[0]
    out = np.zeros(m, complex)
    # per component precompute: C = (S^{-1} - 2iE)^{-1}, prefactor det(I - 2i S E)^{-1/2}
    pref = np.empty(len(W), complex); Cs = []
    for c in range(len(W)):
        Sd = np.diag(S[c]); A = np.linalg.inv(Sd) - 2j * E
        C = np.linalg.inv(A); Cs.append(C)
        # det(I - 2i S E)^{-1/2} = prod_j (1 - 2i mu_j)^{-1/2}, mu_j = eig(S^{1/2} E S^{1/2}); each factor has
        # positive real part, so the product of principal roots is the analytic continuation from E = 0.
        Sh = np.sqrt(S[c]); mu = np.linalg.eigvalsh(Sh[:, None] * E * Sh[None, :])
        pref[c] = W[c] / np.prod(np.sqrt(1 - 2j * mu))
    Cs = np.array(Cs)
    for c in range(len(W)):
        mu = MU[c]; C = Cs[c]
        for s0 in range(0, m, chunk):
            Ub = U[s0:s0 + chunk]
            b = Ub @ P.T                       # (mb, n)
            beta = b + 2 * (E @ mu)[None, :]
            quad = np.einsum('mi,ij,mj->m', beta, C, beta)
            out[s0:s0 + chunk] += pref[c] * np.exp(1j * (b @ mu) + 1j * (mu @ E @ mu) - 0.5 * quad)
    return out

def J_k1_windowed(v, E, W, MU, S, du, cut=9.0, return_grid=False):
    """k = 1: int_R |T(u)| du on a uniform grid, each component evaluated only where its Gaussian envelope
    exceeds exp(-cut^2/2) of its peak.  The component exponent is quadratic in u:
      Re part  -(1/2)[u^2 Re(v^T C v) + 2u Re(v^T C e) + Re(e^T C e)],  e = 2 E mu."""
    n = len(v); M = len(W)
    cen = np.empty(M); sd = np.empty(M); pref = np.empty(M, complex); Cs = []
    for c in range(M):
        Sd = np.diag(S[c]); C = np.linalg.inv(np.linalg.inv(Sd) - 2j * E); Cs.append(C)
        Sh = np.sqrt(S[c]); mu_ = np.linalg.eigvalsh(Sh[:, None] * E * Sh[None, :])
        pref[c] = W[c] / np.prod(np.sqrt(1 - 2j * mu_))
        e = 2 * E @ MU[c]; a2 = (v @ C @ v).real; a1 = (v @ C @ e).real
        cen[c] = -a1 / a2; sd[c] = 1 / np.sqrt(a2)
    lo = (cen - cut * sd).min(); hi = (cen + cut * sd).max()
    m = int(np.ceil((hi - lo) / du)) + 1
    out = np.zeros(m, complex)
    for c in range(M):
        i0 = max(0, int((cen[c] - cut * sd[c] - lo) / du)); i1 = min(m, int((cen[c] + cut * sd[c] - lo) / du) + 2)
        u = lo + du * np.arange(i0, i1)
        mu = MU[c]; C = Cs[c]; e = 2 * E @ mu
        beta = u[:, None] * v[None, :] + e[None, :]
        quad = np.einsum('mi,ij,mj->m', beta, C, beta)
        out[i0:i1] += pref[c] * np.exp(1j * u * (v @ mu) + 1j * (mu @ E @ mu) - 0.5 * quad)
    J = np.abs(out).sum() * du
    if return_grid:
        return J, lo + du * np.arange(m), out
    return J

def density_max(law, grid):
    w, a, s = law
    f = sum(w[p] * np.exp(-(grid - a[p]) ** 2 / (2 * s[p] ** 2)) / np.sqrt(2 * np.pi * s[p] ** 2) for p in range(len(w)))
    return f.max()

if __name__ == '__main__':
    # self-test against direct 2D quadrature, n = 2, small mixture
    rng = np.random.default_rng(1)
    laws = [(np.array([.5, .5]), np.array([0., 3.]), np.array([.4, .5])),
            (np.array([.3, .7]), np.array([-1., 2.]), np.array([.45, .6]))]
    W, MU, S = components(laws)
    P = np.array([[1.], [1.]]) / np.sqrt(2)
    E = np.array([[0.3, 0.7], [0.7, -0.2]])
    xs = np.linspace(-6, 9, 1501); dx = xs[1] - xs[0]
    def f(law, x):
        w, a, s = law
        return sum(w[p] * np.exp(-(x - a[p]) ** 2 / (2 * s[p] ** 2)) / np.sqrt(2 * np.pi * s[p] ** 2) for p in range(len(w)))
    X1, X2 = np.meshgrid(xs, xs, indexing='ij')
    F = f(laws[0], X1) * f(laws[1], X2)
    for u in [0.0, 0.7, -2.3, 5.0]:
        direct = np.sum(F * np.exp(1j * u * (X1 + X2) / np.sqrt(2) + 1j * (E[0, 0] * X1 ** 2 + 2 * E[0, 1] * X1 * X2 + E[1, 1] * X2 ** 2))) * dx * dx
        exact = T_of_u(np.array([[u]]), P, E, W, MU, S)[0]
        print(f"u={u:5.2f} direct={direct:.6f} exact={exact:.6f} diff={abs(direct-exact):.2e}", flush=True)
