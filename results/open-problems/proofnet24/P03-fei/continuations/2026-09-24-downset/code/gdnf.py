# Spectral quantities of monotone DNFs given by their terms (lists of variable indices), exact via the fast
# Walsh-Hadamard transform. Used for graph DNFs f_G = OR_{uv in E} x_u x_v (width 2), with optional singleton terms.
# Conventions: f in {+1,-1} with -1 = true; P(S) = fhat(S)^2; H in bits; Delta_v = H(f) - (H(f|x_v=0)+H(f|x_v=1))/2;
# B_v = H(S) - H(S minus v) (erasure term); Inf_v = sum_{S ni v} P(S).
import numpy as np

def truth_table(n, terms):
    N = 1 << n
    x = np.arange(N, dtype=np.int64)
    f = np.zeros(N, dtype=bool)
    for t in terms:
        m = 0
        for v in t:
            m |= 1 << v
        f |= (x & m) == m
    return f

def fwht(a):
    a = a.astype(np.float64).copy()
    N = a.shape[0]
    h = 1
    while h < N:
        a = a.reshape(-1, 2, h)
        u = a[:, 0, :].copy(); w = a[:, 1, :]
        a[:, 0, :] = u + w; a[:, 1, :] = u - w
        a = a.reshape(N)
        h *= 2
    return a

def phi(p):
    p = np.asarray(p, dtype=np.float64)
    out = np.zeros_like(p)
    nz = p > 1e-300
    out[nz] = -p[nz] * np.log2(p[nz])
    return out

def popcounts(N):
    x = np.arange(N, dtype=np.int64)
    c = np.zeros(N, dtype=np.int64)
    while x.any():
        c += x & 1
        x >>= 1
    return c

def analyse(n, f):
    """f: bool truth table (True = true).  Returns dict with H, I, Var and per-coordinate Inf, Delta, B, JS."""
    N = 1 << n
    G = fwht(np.where(f, -1.0, 1.0)) / N
    P = G * G
    H = float(phi(P).sum())
    pc = popcounts(N)
    I = float((P * pc).sum())
    Var = float(1.0 - P[0])
    Inf = np.zeros(n); Delta = np.zeros(n); B = np.zeros(n); JS = np.zeros(n)
    idx = np.arange(N, dtype=np.int64)
    for v in range(n):
        m0 = (idx >> v) & 1 == 0
        a = G[m0]; b = G[idx[m0] | (1 << v)]
        Inf[v] = float((b * b).sum())
        Her = float(phi(a * a + b * b).sum())
        hch = 0.5 * float((phi((a + b) ** 2) + phi((a - b) ** 2)).sum())
        Delta[v] = H - hch; B[v] = H - Her; JS[v] = Her - hch
    return dict(H=H, I=I, Var=Var, Inf=Inf, Delta=Delta, B=B, JS=JS, P=P)

def graph_terms(edges, singles=()):
    return [tuple(e) for e in edges] + [(s,) for s in singles]

def summary(n, edges, singles=(), name=''):
    f = truth_table(n, graph_terms(edges, singles))
    r = analyse(n, f)
    rel = r['Inf'] > 1e-15
    ratio = np.where(rel, r['Delta'] / np.where(rel, r['Inf'], 1), np.inf)
    deg = np.zeros(n, dtype=int)
    for u, v in edges:
        deg[u] += 1; deg[v] += 1
    vmin = int(np.argmin(ratio))
    out = dict(name=name, n=n, m=len(edges), Var=r['Var'], H=r['H'], I=r['I'],
               HI=r['H'] / r['I'] if r['I'] > 0 else 0.0,
               avgstep=float(r['Delta'].sum() / r['I']) if r['I'] > 0 else 0.0,
               erasure=float(r['B'].sum() / r['I']) if r['I'] > 0 else 0.0,
               rho0=float(ratio[vmin]), rho0_vertex=vmin, rho0_deg=int(deg[vmin]),
               ratio_maxdeg=float(ratio[int(np.argmax(deg))]), ratio_mindeg=float(ratio[int(np.argmin(deg))]),
               ratio_max=float(ratio[rel].max()) if rel.any() else 0.0)
    return out, r
