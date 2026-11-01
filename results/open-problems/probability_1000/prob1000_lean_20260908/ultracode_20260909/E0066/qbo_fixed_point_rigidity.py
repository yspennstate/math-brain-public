"""E0066: is the identity the only QBO fixing an interior point with pairwise distinct coordinates?
LP feasibility (qbo_periodic_lp machinery) with two random objectives; 'unique' means both LP vertices coincide
with the identity operator (max entry deviation < 1e-7).  Controls: a point with two equal coordinates and a
boundary point, where non-identity solutions are expected."""
import numpy as np, time
import qbo_periodic_lp as L
rng = np.random.default_rng(3)

def identity_op(m):
    P = np.zeros((m, m, m))
    for k in range(m):
        for j in range(m):
            P[k, j, k] += 0.5; P[j, k, k] += 0.5
    return P

def farthest_from_identity(m, y, base):
    """maximise / minimise random objectives; return the max deviation from the identity over the vertices found"""
    A_eq, b_eq, A_ub, b_ub, nv = base
    R, rhs = L.orbit_rows(m, [y])
    I = identity_op(m)
    worst = 0.0; example = None
    for trial in range(6):
        c = rng.standard_normal(nv)
        for cc in (c, -c):
            res = L.linprog(cc, A_ub=A_ub, b_ub=b_ub, A_eq=np.vstack([A_eq, R]), b_eq=np.concatenate([b_eq, rhs]),
                            bounds=[(0, 1)] * nv, method='highs')
            if res.status != 0:
                return None, None
            P = L.build_P(m, res.x)
            dev = float(np.max(np.abs(P - I)))
            if dev > worst:
                worst = dev; example = P
    return worst, example

t0 = time.time()
for m in (3, 4, 5):
    base = L.polytope_constraints(m)
    devs = []
    for r in range(20):
        while True:
            y = np.sort(rng.random(m))[::-1]; y /= y.sum()
            if np.min(np.diff(y[::-1])) > 0.02 and y.min() > 0.02:
                break
        d, P = farthest_from_identity(m, y, base)
        devs.append(d)
    print('m=%d distinct-coordinate interior y: max deviation from identity over 20 y x 12 LP vertices = %.2e' % (m, max(devs)), '%.0fs' % (time.time() - t0))
    # controls
    y = np.array([0.5] + [0.5 / (m - 1)] * (m - 1))
    d, P = farthest_from_identity(m, y, base)
    print('   control, two-or-more equal coordinates y=%s: deviation %.3f' % (np.round(y, 3), d))
    y = np.sort(rng.random(m))[::-1]; y[-1] = 0; y /= y.sum()
    d, P = farthest_from_identity(m, y, base)
    print('   control, boundary y=%s: deviation %.3f' % (np.round(y, 3), d))
