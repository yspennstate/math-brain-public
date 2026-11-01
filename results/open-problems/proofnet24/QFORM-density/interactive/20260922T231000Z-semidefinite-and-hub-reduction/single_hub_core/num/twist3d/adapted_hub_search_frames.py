# Random search over frames as well as laws for the hub that sees P. m = 4, 5 or 6 light coordinates; for m = 4 the pair
# (w, v) is a tight frame (w_i^2 + v_i^2 = 1/2 for every i, the only way the leverage condition holds on four
# coordinates) and q^ is a random unit vector orthogonal to it; for m = 5, 6 the triple is the Q-factor of a Gaussian
# matrix, redrawn until w_i^2 + v_i^2 <= 1/2. Each coordinate is uniform on [0, 1] (probability 1/3) or uniform on T
# teeth of width 1/T at random positions in [0, R], T = 2..8, R = T, 4T or 16T. lambda = 1, s uniform in [-2, 2] and
# beta = -(E L + u) with u uniform in [-1, 1]; with the argument 'centre' the square is lambda (V - v_c)^2 with
# v_c = E V + u', u' uniform in [-1, 1] (v_c is free in (SP)), otherwise v_c = 0. Net Phi = Phi - (shuffled - bathtub), as in adapted_hub_search.py.
import sys, math, time
import numpy as np

def draw_frame(rng, m):
    if m == 4:
        a = rng.uniform(0, math.pi / 2)
        th = np.array([0.0, a, math.pi / 2, math.pi / 2 + a]) + rng.uniform(0, math.pi)
        w = np.cos(th) / math.sqrt(2); v = np.sin(th) / math.sqrt(2)
        M = np.stack([w, v]).T
        Qf, _ = np.linalg.qr(np.concatenate([M, rng.standard_normal((4, 2))], axis=1))
        c = rng.standard_normal(2); c /= np.linalg.norm(c)
        q = Qf[:, 2] * c[0] + Qf[:, 3] * c[1]
        return np.stack([w, v, q], axis=1)
    while True:
        Qf, _ = np.linalg.qr(rng.standard_normal((m, 3)))
        if np.max(Qf[:, 0] ** 2 + Qf[:, 1] ** 2) <= 0.5:
            return Qf

def draw_law(rng):
    if rng.random() < 1 / 3:
        return ("u", np.array([0.0]), 1)
    T = int(rng.integers(2, 9)); R = float(rng.choice([1, 4, 16])) * T
    while True:
        p = np.sort(rng.uniform(0, R - 1.0 / T, T))
        if np.all(np.diff(p) > 1.0 / T):
            return ("c", p, T)

def sample_law(rng, law, size):
    kind, p, T = law
    if kind == "u":
        return rng.random(size)
    return p[rng.integers(0, T, size)] + rng.random(size) / T

def estimate(E, laws, s, beta, n, seed, b0=0.02, bp=0.05, xmax=6.0, chunk=1_000_000, vc=0.0):
    rng = np.random.default_rng(seed); m = E.shape[0]
    q = E[:, 2]
    ext = [(lw[1][0], lw[1][-1] + 1.0 / lw[2]) for lw in laws]
    lo = sum(min(q[i] * ext[i][0], q[i] * ext[i][1]) for i in range(m)) - 0.2
    hi = sum(max(q[i] * ext[i][0], q[i] * ext[i][1]) for i in range(m)) + 0.2
    nx = int(round(2 * xmax / b0)); npb = int(math.ceil((hi - lo) / bp))
    rg = ((-xmax, xmax), (lo, lo + npb * bp))
    H = np.zeros((nx, npb)); H0 = np.zeros((nx, npb))
    for _ in range(max(1, n // chunk)):
        X = np.stack([sample_law(rng, laws[i], chunk) for i in range(m)], axis=1)
        Y = X @ E; T = Y[:, 0] + beta; V = Y[:, 1] - vc; P = Y[:, 2]
        xs = (s - V * V) / (2 * T); wt = 1.0 / (2 * np.abs(T))
        H += np.histogram2d(xs, P, bins=(nx, npb), range=rg, weights=wt)[0]
        H0 += np.histogram2d(xs, rng.permutation(P), bins=(nx, npb), range=rg, weights=wt)[0]
    top = int(round(1.0 / b0)); nn = max(1, n // chunk) * chunk
    B0 = np.sort(H.sum(axis=1))[::-1][:top].sum() / nn
    Phi = np.sort(H, axis=0)[::-1][:top].sum() / nn
    Sh = np.sort(H0, axis=0)[::-1][:top].sum() / nn
    return B0, Phi, Sh, Phi - (Sh - B0)

def mean_L(E, laws, col=0):
    mu = np.array([np.mean(lw[1]) + 0.5 / lw[2] for lw in laws])
    return float(mu @ E[:, col])

CENTRE = False
if __name__ == "__main__":
    CENTRE = len(sys.argv) > 3 and sys.argv[3] == "centre"
    rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 21)
    draws = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    res = []; t0 = time.time()
    for k in range(draws):
        m = int(rng.choice([4, 5, 6])); E = draw_frame(rng, m)
        laws = [draw_law(rng) for _ in range(m)]
        s = rng.uniform(-2, 2); beta = -(mean_L(E, laws) + rng.uniform(-1, 1))
        vc = mean_L(E, laws, 1) + (rng.uniform(-1, 1) if CENTRE else 0.0) if CENTRE else 0.0
        B0, Phi, Sh, net = estimate(E, laws, s, beta, 4_000_000, 100 + k, vc=vc)
        desc = "".join("u" if lw[0] == "u" else "c%d/%d" % (lw[2], int(round((lw[1][-1] + 1.0 / lw[2])))) for lw in laws)
        res.append((net, B0, Phi, Sh, m, E, laws, s, beta, k, desc, vc))
        print("draw %2d m=%d laws %-28s s=%+.2f  bathtub %.4f  Phi %.4f  shuffled %.4f  net %.4f  ratio %.3f"
              % (k, m, desc, s, B0, Phi, Sh, net, net / B0 if B0 > 0 else float("nan")), flush=True)
    print("(%.0fs) re-estimating the three largest net Phi and the three largest ratios with 3.2e7 samples" % (time.time() - t0), flush=True)
    by_net = sorted(res, key=lambda r: -r[0])[:3]
    by_ratio = sorted([r for r in res if r[1] > 0.05], key=lambda r: -(r[0] / r[1]))[:3]
    for tag, group in (("net", by_net), ("ratio", by_ratio)):
        for net, B0, Phi, Sh, m, E, laws, s, beta, k, desc, vc in group:
            b, P_, S_, n_ = estimate(E, laws, s, beta, 32_000_000, 9000 + k, vc=vc)
            print("[%s] draw %2d m=%d laws %-28s  bathtub %.4f  Phi %.4f  shuffled %.4f  net %.4f  ratio %.3f"
                  % (tag, k, m, desc, b, P_, S_, n_, n_ / b), flush=True)
