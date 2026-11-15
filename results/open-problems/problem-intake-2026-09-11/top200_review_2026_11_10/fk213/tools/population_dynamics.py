"""Population dynamics for the three-state symmetric channel on Galton-Watson trees.

A second look at the 24 Oct three-state argument by a route that shares nothing with the certificates: the law
of the root posterior p_n given the spins at depth n is simulated directly, and three consequences of the
argument are tested on offspring laws with heavy tails.

    (i)   cone:   E H(p_n) >= 0 for every n,  H = y - x^2/2;
    (ii)  drift:  m_{n+1} <= d lambda^2 m_n - c_3 m_n^2,  m_n = E x(p_n),  c_3 = lambda^4 E(D-1)_+ / 1000;
    (iii) at d lambda^2 = 1 the information m_n decreases towards 0.

The population holds posteriors sampled given root colour 0. A new sample draws D children, a colour for each
child through the channel, a member of the population for each child (relabelled so that its true colour is the
child's colour), sends it through the edge and multiplies. The Nishimori identity
E[p_n(root colour)] = E sum_i p_n(i)^2 = (2 m_n + 1)/3 is printed as a check of the simulation itself.

Controls: d lambda^2 = 1.3 (m_n must stay away from 0) and lambda < 0 (E H must become negative, since the edge
multiplies H by lambda^3)."""
import sys, time
import numpy as np


def offspring(name, rng, n):
    if name == "zeta3":            # P(D = k) = k^-3 / zeta(3), mean zeta(2)/zeta(3), infinite variance
        return rng.zipf(3.0, n)
    if name == "rare101":          # D = 1 w.p. 99/100, D = 101 w.p. 1/100, mean 2
        return np.where(rng.random(n) < 0.01, 101, 1)
    if name == "rare10":           # D = 0 w.p. 4/5, D = 10 w.p. 1/5, mean 2
        return np.where(rng.random(n) < 0.2, 10, 0)
    if name == "binary":           # D = 2
        return np.full(n, 2)
    raise ValueError(name)


MEAN = {"zeta3": 1.6449340668482264 / 1.2020569031595942, "rare101": 2.0, "rare10": 2.0, "binary": 2.0}
DELTA = {"zeta3": MEAN["zeta3"] - 1.0, "rare101": 1.0, "rare10": 1.8, "binary": 1.0}   # E (D-1)_+


def stats(P):
    c = 3.0 * P - 1.0
    x = (c ** 2).sum(1) / 6.0
    y = (c ** 3).sum(1) / 6.0
    H = y - x * x / 2.0
    n = len(P)
    return x.mean(), H.mean(), H.std() / np.sqrt(n), P[:, 0].mean(), (P ** 2).sum(1).mean()


def run(name, ratio, sign, N, depth, seed):
    rng = np.random.default_rng(seed)
    d = MEAN[name]
    lam = sign * np.sqrt(ratio / d)
    same = (1.0 + 2.0 * lam) / 3.0
    c3 = abs(lam) ** 4 * DELTA[name] / 1000.0
    P = np.zeros((N, 3)); P[:, 0] = 1.0
    m_prev = 1.0
    print("law %s  d %.4f  lambda %+.4f  d lambda^2 %.3f  N %d" % (name, d, lam, d * lam * lam, N), flush=True)
    print("  n      m_n        E H        se(E H)   drift margin   Nishimori gap", flush=True)
    worst_margin = None; min_H = None
    for n in range(1, depth + 1):
        D = offspring(name, rng, N)
        M = int(D.sum())
        owner = np.repeat(np.arange(N), D)
        r = rng.random(M)
        col = np.where(r < same, 0, np.where(r < same + (1.0 - same) / 2.0, 1, 2))
        Q = P[rng.integers(0, N, M)]
        if CONSISTENT:
            # The population stands for the symmetric law (1/6) sum over relabellings. Given that the child's
            # colour is c, a member p is used with the coordinate j drawn from p itself placed at c (the
            # posterior of a symmetric experiment gives the law of the true colour), the other two in random
            # order. This keeps E p(true colour) = E sum p_i^2 exactly at every step; the plain sampler below
            # lets a deviation from it grow by the factor d lambda per generation.
            u = rng.random(M)
            j = (u > Q[:, 0]).astype(np.int64) + (u > Q[:, 0] + Q[:, 1]).astype(np.int64)
            flip = rng.random(M) < 0.5
            o1 = np.where(flip, (j + 1) % 3, (j + 2) % 3)
            o2 = 3 - j - o1
            rows = np.arange(M)
            c1 = (col + 1) % 3; c2 = (col + 2) % 3
            Q2 = np.empty_like(Q)
            Q2[rows, col] = Q[rows, j]
            Q2[rows, c1] = Q[rows, o1]
            Q2[rows, c2] = Q[rows, o2]
            Q = Q2
        else:
            i1 = col == 1; i2 = col == 2
            Q[i1] = Q[i1][:, [1, 0, 2]]
            Q[i2] = Q[i2][:, [2, 1, 0]]
        L = np.log(lam * Q + (1.0 - lam) / 3.0)
        S = np.zeros((N, 3))
        np.add.at(S, owner, L)
        S -= S.max(1, keepdims=True)
        W = np.exp(S)
        P = W / W.sum(1, keepdims=True)
        m, EH, se, p0, p2 = stats(P)
        margin = (d * lam * lam * m_prev - c3 * m_prev ** 2) - m
        if worst_margin is None or margin < worst_margin: worst_margin = margin
        z = EH / se if se > 0 else 0.0
        if min_H is None or z < min_H[0]: min_H = (z, n, EH)
        if n <= 5 or n % 5 == 0:
            print("%3d  %.6f  %+.3e  %.1e  %+.3e   %+.1e" % (n, m, EH, se, margin, p0 - p2), flush=True)
        m_prev = m
    print("  smallest drift margin %+.3e ; smallest E H in standard errors %+.1f at n = %d (E H %+.3e) ; final m %.5f"
          % (worst_margin, min_H[0], min_H[1], min_H[2], m_prev), flush=True)
    return worst_margin, min_H, m_prev


CONSISTENT = True

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 400000
    depth = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    CONSISTENT = not (len(sys.argv) > 3 and sys.argv[3] == "plain")
    print("sampler:", "consistent" if CONSISTENT else "plain", flush=True)
    t0 = time.time()
    for name in ("zeta3", "rare101", "rare10", "binary"):
        run(name, 1.0, +1, N, depth, 1)
    print("CONTROL above the threshold", flush=True)
    run("zeta3", 1.3, +1, N, depth, 2)
    print("CONTROL antiferromagnetic channel", flush=True)
    run("binary", 0.4, -1, N, min(depth, 20), 3)      # lambda = -0.447, inside [-1/2, 1]
    print("seconds %.0f" % (time.time() - t0), flush=True)
