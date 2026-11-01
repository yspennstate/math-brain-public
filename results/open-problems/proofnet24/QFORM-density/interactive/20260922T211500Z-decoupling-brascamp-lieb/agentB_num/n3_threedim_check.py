try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# n = 3: estimate sup_s p_Q(s) with the route-(i) conditional estimator (no binning):
# p_Q(s) = E_{X2,X3}[ (f1(m+r) + f1(m-r)) / (2 sqrt(a (s-R))) ; (s-R)/a > 0 ],  r = sqrt((s-R)/a).
import numpy as np, sys
rng = np.random.default_rng(11)

def make_set(kind, rng):
    if kind == 'unif':
        return np.array([-0.5]), np.array([1.0])
    m = rng.integers(2, 12); lens = rng.dirichlet(np.ones(m)); spread = 10**rng.uniform(0, 2.5)
    starts = np.sort(rng.uniform(-spread, spread, m))
    for k in range(1, m):          # make disjoint
        starts[k] = max(starts[k], starts[k-1] + lens[k-1])
    return starts, lens

def sample(starts, lens, N, rng):
    k = rng.choice(len(lens), size=N, p=lens/lens.sum()); return starts[k] + rng.random(N)*lens[k]

def dens_fn(starts, lens):
    def f(x):
        out = np.zeros_like(x)
        for a, l in zip(starts, lens): out[(x >= a) & (x < a+l)] = 1.0
        return out
    return f

def estimate(A, b, sets, svals, N, rng):
    # choose pivot i = argmax |a_ii|
    i = int(np.argmax(np.abs(np.diag(A)))); a = A[i, i]; others = [j for j in range(3) if j != i]
    Xo = np.stack([sample(*sets[j], N, rng) for j in others])       # 2 x N
    Aio = A[i, others]; Aoo = A[np.ix_(others, others)]
    beta = 2*Aio @ Xo + b[i]                                         # coefficient of x_i
    m = -beta/(2*a)
    R = np.einsum('in,ij,jn->n', Xo, Aoo, Xo) + b[others] @ Xo - beta**2/(4*a)
    f1 = dens_fn(*sets[i]); out = []
    for s in svals:
        w = (s - R)/a; ok = w > 0; r = np.sqrt(np.where(ok, w, 0.0))
        g = np.where(ok, (f1(m + r) + f1(m - r))/(2*np.sqrt(np.abs(a)*np.abs(s - R)) + 1e-300), 0.0)
        out.append(g.mean())
    return np.array(out)

e = np.ones(3)/np.sqrt(3)
mats = {'I-2ee^T': np.eye(3) - 2*np.outer(e, e),
        'lead_example': np.array([[.5, .5, 1/np.sqrt(2)], [.5, .5, -1/np.sqrt(2)], [1/np.sqrt(2), -1/np.sqrt(2), 0]]),
        '2I-J': 2*np.eye(3) - np.ones((3, 3))}
for name, A in mats.items():
    print(name, 'eig', np.round(np.linalg.eigvalsh(A), 4), 'diag', np.round(np.diag(A), 4), flush=True)
    best = 0; bestinfo = None
    for trial in range(40):
        kinds = ['unif']*3 if trial == 0 else [rng.choice(['unif', 'spread']) for _ in range(3)]
        sets = [make_set(k, rng) for k in kinds]
        b = np.zeros(3) if trial < 2 else rng.normal(0, 3, 3)
        # s grid: coarse scan from a pilot sample of Q, then refine near the max
        Xp = np.stack([sample(*sets[j], 20000, rng) for j in range(3)])
        Qp = np.einsum('in,ij,jn->n', Xp, A, Xp) + b @ Xp
        svals = np.quantile(Qp, np.linspace(0.005, 0.995, 41))
        est = estimate(A, b, sets, svals, 200000, rng)
        s0 = svals[np.argmax(est)]; width = (svals[-1]-svals[0])/40
        sv2 = s0 + np.linspace(-width, width, 21)
        est2 = estimate(A, b, sets, sv2, 400000, rng)
        val = est2.max()
        if val > best: best, bestinfo = val, (kinds, np.round(b, 2), sv2[np.argmax(est2)])
    print(f"  worst sup_s p_Q(s) over 40 configurations: {best:.3f}   info {bestinfo}", flush=True)
