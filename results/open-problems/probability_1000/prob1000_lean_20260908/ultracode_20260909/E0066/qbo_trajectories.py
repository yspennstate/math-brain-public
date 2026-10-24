"""E0066 numeric check: trajectories of quadratic bistochastic operators.

Claims checked
  (A) an operator built to satisfy Ganikhodzhaev's condition (c) (sum_{i,j in I} P_{ij,k} <= |I|)
      is bistochastic: V(x) is majorised by x on random x (independent of the proof of (c) => bistochastic);
  (B) along every trajectory the partial sums of the decreasing rearrangement are nonincreasing;
  (C) the tail of every trajectory clusters on finitely many points, all coordinate permutations of one
      vector, and the trajectory cycles through them with a fixed period (the structural theorem);
  (D) which periods occur, for m = 2,3,4, on boundary points of the polytope B_m, on permutation
      compositions, and on convex mixtures with permutation operators.
Single process, numpy only.
"""
import itertools, time
import numpy as np
rng = np.random.default_rng(20260909)


def apply(P, x):
    # V(x)_k = sum_{ij} P[i,j,k] x_i x_j
    # V is homogeneous of degree 2, so the mass sum V(x) = (sum x)^2 drifts doubly-exponentially under rounding;
    # renormalising keeps the iterate on the simplex (the same map there).
    v = np.einsum('ijk,i,j->k', P, x, x)
    return v / v.sum()


def sorted_partial(x):
    return np.cumsum(np.sort(x)[::-1])


def majorised(v, x, tol=1e-12):
    return np.all(sorted_partial(v) <= sorted_partial(x) + tol)


def center_op(m):
    return np.full((m, m, m), 1.0 / m)


def perm_op(sigma):
    # V(x)_k = x_{sigma(k)} = sum_j x_{sigma(k)} x_j : P[i,j,k] = (d(i,sigma k) + d(j,sigma k))/2
    m = len(sigma)
    P = np.zeros((m, m, m))
    for k in range(m):
        for j in range(m):
            P[sigma[k], j, k] += 0.5
            P[j, sigma[k], k] += 0.5
    return P


def random_balanced(m):
    # symmetric in (i,j), sum_k P = 1, sum_{ij} P[.,.,k] = m  (Sinkhorn on the m^2 x m matrix)
    A = rng.random((m * m, m)) ** 3 + 1e-9
    for _ in range(500):
        A /= A.sum(axis=1, keepdims=True)
        A *= m / A.sum(axis=0, keepdims=True)
    P = A.reshape(m, m, m)
    P = 0.5 * (P + P.transpose(1, 0, 2))
    return P


def subsets(m):
    for t in range(1, m + 1):
        for I in itertools.combinations(range(m), t):
            yield list(I), t


def cond_c_slack(P):
    m = P.shape[0]
    worst = np.inf
    for I, t in subsets(m):
        s = P[np.ix_(I, I)].sum(axis=(0, 1))  # over k
        worst = min(worst, float(np.min(t - s)))
    return worst  # >= -tol means (c) holds


def boundary_op(m):
    """largest lambda with lam*P + (1-lam)*P0 satisfying (c): a boundary point of B_m."""
    P = random_balanced(m)
    P0 = center_op(m)
    lam = 1.0
    for I, t in subsets(m):
        s = P[np.ix_(I, I)].sum(axis=(0, 1))
        s0 = t * t / m
        for sk in s:
            if sk > s0 + 1e-15:
                lam = min(lam, (t - s0) / (sk - s0))
    return lam * P + (1 - lam) * P0, lam


def compose_perm(P, sigma):
    # (Q o V)(x)_k = V(x)_{sigma(k)}
    return P[:, :, list(sigma)]


def analyse(P, x0, n_iter=3000, tail=400):
    x = x0.copy()
    traj = []
    prev = sorted_partial(x)
    mono_ok = True
    for n in range(n_iter):
        x = apply(P, x)
        if not np.all(np.isfinite(x)):
            raise RuntimeError('non-finite iterate at step %d, P entries min %g max %g, k-sums %s' % (n, P.min(), P.max(), P.sum(axis=2)))
        cur = sorted_partial(x)
        if np.any(cur > prev + 1e-12):
            mono_ok = False
        prev = cur
        if n >= n_iter - tail:
            traj.append(x.copy())
    traj = np.array(traj)
    srt = np.sort(traj, axis=1)
    sorted_spread = float(np.max(np.abs(srt - srt[-1])))
    period = None
    for p in range(1, tail // 2):
        if np.max(np.abs(traj[p:] - traj[:-p])) < 1e-6:
            period = p
            break
    pts = []
    for y in traj[-200:]:
        if not any(np.max(np.abs(y - z)) < 1e-6 for z in pts):
            pts.append(y)
    return dict(mono_ok=mono_ok, sorted_spread=sorted_spread, period=period, n_clusters=len(pts),
                interior=bool(np.min(traj[-1]) > 1e-6), final=traj[-1])


def rand_simplex(m):
    x = rng.exponential(size=m)
    return x / x.sum()


def check_operator(P, name, n_x=600, n_traj=8, **kw):
    m = P.shape[0]
    assert np.allclose(P, P.transpose(1, 0, 2)) and np.allclose(P.sum(axis=2), 1) and np.all(P >= -1e-15)
    slack = cond_c_slack(P)
    maj_fail = sum(not majorised(apply(P, x), x) for x in (rand_simplex(m) for _ in range(n_x)))
    for i in range(m):
        e = np.zeros(m)
        e[i] = 1
        if not majorised(apply(P, e), e):
            maj_fail += 1
    res = [analyse(P, rand_simplex(m), **kw) for _ in range(n_traj)]
    periods = sorted(set(r['period'] for r in res), key=lambda p: (p is None, p or 0))
    return dict(name=name, m=m, slack=slack, maj_fail=maj_fail,
                mono_fail=sum(not r['mono_ok'] for r in res),
                max_sorted_spread=max(r['sorted_spread'] for r in res),
                periods=periods, clusters=sorted(set(r['n_clusters'] for r in res)),
                interior_periodic=[(r['period'], r['n_clusters']) for r in res if r['interior'] and (r['period'] or 0) > 1])


def main():
    t0 = time.time()
    rows = []
    # explicit examples
    P2 = np.array([[[0.0, 1.0], [1.0, 0.0]], [[1.0, 0.0], [0.0, 1.0]]])  # V=(2x1x2, x1^2+x2^2)
    rows.append(check_operator(P2, 'm2: V=(2x1x2, x1^2+x2^2)'))
    rows.append(check_operator(compose_perm(P2, [1, 0]), 'm2: swap o (2x1x2, x1^2+x2^2)'))
    rows.append(check_operator(perm_op([1, 2, 0]), 'm3: 3-cycle permutation operator'))
    rows.append(check_operator(perm_op([1, 0, 3, 2]), 'm4: (12)(34) permutation operator'))
    # linear example P o W on S^3: W averages coords 1,2; P = (34) -> period 2 interior orbit
    B = np.array([[.5, .5, 0, 0], [.5, .5, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1.0]])
    W = np.zeros((4, 4, 4))
    for k in range(4):
        for i in range(4):
            for j in range(4):
                W[i, j, k] = 0.5 * (B[k, i] + B[k, j])
    rows.append(check_operator(compose_perm(W, [0, 1, 3, 2]), 'm4: (34) o average(1,2)  [linear]'))
    # random boundary operators, permutation compositions, and mixtures
    for m in (2, 3, 4):
        n_ops = {2: 12, 3: 30, 4: 20}[m]
        for r in range(n_ops):
            P, lam = boundary_op(m)
            rows.append(check_operator(P, 'm%d: boundary op #%d (lam=%.3f)' % (m, r, lam), n_traj=6))
            sigma = rng.permutation(m)
            rows.append(check_operator(compose_perm(P, sigma), 'm%d: perm%s o boundary op #%d' % (m, tuple(sigma), r), n_traj=6))
            mu = rng.random()
            rows.append(check_operator(mu * P + (1 - mu) * perm_op(sigma),
                                       'm%d: %.2f*boundary#%d + %.2f*perm%s' % (m, mu, r, 1 - mu, tuple(sigma)), n_traj=6))
    print('%d operators, %.0fs' % (len(rows), time.time() - t0))
    print('min (c)-slack over all ops (must be >= -1e-9):', min(r['slack'] for r in rows))
    print('majorisation failures (must be 0):', sum(r['maj_fail'] for r in rows))
    print('monotone partial-sum failures (must be 0):', sum(r['mono_fail'] for r in rows))
    print('max spread of the sorted vector over the tail (must be small):', max(r['max_sorted_spread'] for r in rows))
    print('operators whose tail did not lock to a period within tolerance:', sum(None in r['periods'] for r in rows))
    for m in (2, 3, 4):
        ps = {}
        for r in rows:
            if r['m'] == m:
                for p in r['periods']:
                    ps[p] = ps.get(p, 0) + 1
        print('m=%d: periods observed (period: #operators) =' % m, dict(sorted(ps.items(), key=lambda kv: (kv[0] is None, kv[0] or 0))))
        ip = [(r['name'], r['interior_periodic']) for r in rows if r['m'] == m and r['interior_periodic']]
        print('   non-permutation ops with an interior periodic limit (period>1):',
              [(n, sorted(set(v))) for n, v in ip if 'permutation operator' not in n][:12])
    print('--- explicit examples')
    for r in rows[:5]:
        print(r['name'], '| periods', r['periods'], '| clusters', r['clusters'], '| sorted spread %.2e' % r['max_sorted_spread'])
    for r in rows:
        if None in r['periods']:
            print('  slow/unlocked:', r['name'], 'spread %.2e' % r['max_sorted_spread'], 'clusters', r['clusters'])


if __name__ == '__main__':
    main()
