import math
import numpy as np

rng = np.random.default_rng(20260923)

def orth(n, d):
    x = rng.normal(size=(n, d))
    q, _ = np.linalg.qr(x)
    return q[:, :d]

def complement(u):
    p = u @ u.T
    vals, vecs = np.linalg.eigh(np.eye(u.shape[0]) - p)
    return vecs[:, vals > 0.5]

def scale_sym(m, norm):
    m = (m + m.T) / 2
    op = np.max(np.abs(np.linalg.eigvalsh(m)))
    return m * (norm / op) if op else m

def projector_abs(a_mat, a):
    vals, vecs = np.linalg.eigh(a_mat)
    sel = np.abs(vals) >= a
    return vecs[:, sel] @ vecs[:, sel].T if np.any(sel) else np.zeros_like(a_mat)

violations = 0
tests = 0
worst_angle_ratio = 0.0
worst_leverage_ratio = 0.0
for n in (12, 16, 24):
    for d in (3, 5, 7):
        if d >= n:
            continue
        for _ in range(200):
            u = orth(n, d)
            w = complement(u)
            beta = float(rng.uniform(0, 0.2))
            a = float(rng.uniform(beta + 0.15, beta + 0.8))
            inside = u @ np.diag(rng.uniform(-50, 50, size=d)) @ u.T
            outside = w @ np.diag(rng.uniform(-beta, beta, size=n-d)) @ w.T
            b = inside + outside
            delta = float(rng.uniform(0, 0.05 * (a-beta)))
            t = scale_sym(rng.normal(size=(n, n)), delta)
            afinal = b + t
            pi = projector_abs(afinal, a)
            p = u @ u.T
            q = np.eye(n) - p
            lhs = np.linalg.norm(q @ pi, 2)
            rhs = math.sqrt(2) * delta / (a-beta)
            worst_angle_ratio = max(worst_angle_ratio, lhs / (rhs + 1e-30))
            if lhs > rhs + 1e-9:
                violations += 1
            mu = float(np.max(np.diag(p)))
            lev = float(np.max(np.diag(pi)))
            lev_rhs = (math.sqrt(mu) + rhs)**2
            worst_leverage_ratio = max(worst_leverage_ratio, lev / (lev_rhs + 1e-30))
            if lev > lev_rhs + 1e-9:
                violations += 1
            tests += 1

print({
    'tests': tests,
    'violations': violations,
    'worst_angle_ratio': worst_angle_ratio,
    'worst_leverage_ratio': worst_leverage_ratio,
    'constants': {
        'a': 1/64,
        'mu': 1/256,
        'delta': 1/1024,
        'angle_bound': math.sqrt(2)/16,
        'leverage_bound': (1/16 + math.sqrt(2)/16)**2,
        'leverage_threshold': 1/32,
        'ridge_cap': 288*math.sqrt(3*math.e)/13,
        'd5_cap': 5*math.sqrt(2*math.e)/(2-1/1024),
        'partner_core_cap': 2*math.sqrt(48*math.pi)/(13/8),
    }
})
