try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
rng = np.random.default_rng(1)

# characteristic functions of laws with density <= 1
def psi_uniform(s):
    s = np.asarray(s, dtype=float)
    out = np.ones_like(s)
    nz = np.abs(s) > 1e-12
    out[nz] = np.sin(s[nz]/2)/(s[nz]/2)
    return out

def make_spread(k, spread, rng):
    # uniform on union of k intervals of length 1/k, left ends random in [-spread, spread]
    lefts = np.sort(rng.uniform(-spread, spread, size=k))
    # force disjointness by shifting
    for m in range(1, k):
        if lefts[m] < lefts[m-1] + 1.0/k:
            lefts[m] = lefts[m-1] + 1.0/k
    L = 1.0/k
    def psi(s):
        s = np.asarray(s, dtype=float)
        base = psi_uniform(s*L)  # ch.f. of uniform on [0,L] up to phase: |.| = sinc(sL/2)
        ph = np.zeros(s.shape, dtype=complex)
        for a in lefts:
            ph += np.exp(1j*s*(a + L/2))
        return base*ph/k
    def sample(size):
        idx = rng.integers(0, k, size=size)
        return lefts[idx] + rng.uniform(0, L, size=size)
    return psi, sample

def EF2(M, t, psis, samplers, N=200000):
    # E_W prod_i |psi_i(2t (M W)_i)|^2, W_j = X_j - X_j'
    nI, nJ = M.shape
    W = np.empty((N, nJ))
    for j in range(nJ):
        W[:, j] = samplers[j](N) - samplers[j](N)
    Y = W @ M.T  # N x nI
    val = np.ones(N)
    for i in range(nI):
        val *= np.abs(psis[i](2*t*Y[:, i]))**2
    return val.mean(), val.std()/np.sqrt(N)

def bound(M, t):
    return np.sqrt(2*np.e)*np.pi/(abs(t)*np.linalg.norm(M))

cases = []
cases.append(("single row, 30 spread", rng.normal(size=(1, 30))/np.sqrt(30)))
cases.append(("single column 30", rng.normal(size=(30, 1))/np.sqrt(30)))
cases.append(("gauss 10x10 /sqrt(10)", rng.normal(size=(10, 10))/np.sqrt(10)))
cases.append(("gauss 20x5 /sqrt(20)", rng.normal(size=(20, 5))/np.sqrt(20)))
row = np.zeros((10, 10)); row[0, :] = 1/np.sqrt(10); row[1:, :] = 0.02*rng.normal(size=(9, 10))
cases.append(("one heavy row + noise", row))
cases.append(("rank one 15x15 spread", np.outer(np.ones(15), np.ones(15))/15))
cases.append(("1x1 entry 0.3", np.array([[0.3]])))

print("law=uniform", flush=True)
for name, M in cases:
    nI, nJ = M.shape
    psis = [psi_uniform]*nI
    samplers = [lambda n: rng.uniform(-0.5, 0.5, size=n)]*nJ
    worst = 0
    for t in [0.5, 1, 2, 5, 10, 30, 100]:
        m, se = EF2(M, t, psis, samplers, N=100000)
        r = m/bound(M, t)
        worst = max(worst, r)
    print(f"{name:28s} max ratio EF2/bound over t = {worst:.4f}", flush=True)

print("law=spread sets (k intervals)", flush=True)
for name, M in cases:
    nI, nJ = M.shape
    psis = []; 
    for i in range(nI):
        p, _ = make_spread(int(rng.integers(1, 8)), 5.0, rng); psis.append(p)
    samplers = []
    for j in range(nJ):
        _, sm = make_spread(int(rng.integers(1, 8)), 5.0, rng); samplers.append(sm)
    worst = 0
    for t in [0.5, 1, 2, 5, 10, 30, 100]:
        m, se = EF2(M, t, psis, samplers, N=100000)
        r = m/bound(M, t)
        worst = max(worst, r)
    print(f"{name:28s} max ratio EF2/bound over t = {worst:.4f}", flush=True)
