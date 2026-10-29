# T354 vector case (agent B, 20 Oct 2026). f_i(x) = x'Hx/2 + b_i'x in R^d, sum b_i = 0, argmin 0, coordinatewise Adam
# (beta1, beta2, eps 0) with random reshuffling (or iid), vanishing step -> x* solves D(x*) = 0, D_k = stationary mean of
# m_k/sqrt(v_k) at frozen x. First-order claim: each coordinate sees only its own lag covariance of m_k with v_k, so
#   H x* = (1 - beta2) K c,   c_k = E[b_k^3] / (2 E[b_k^2])   (no cross moments), K from kfactor.py (same for every coordinate).
# Test: D at a few x with common random numbers, fit D(x) = J x + D0 (D is near-linear on this scale), solve x* = -J^-1 D0,
# then one refinement step at x*. Compare with the prediction and with the cross-moment-free claim.
import numpy as np, sys, json
from kfactor import K_rr, K_iid
def drift(x, H, B, b1, b2, chains, seed, iid=False):
    rng = np.random.default_rng(seed); n, d = B.shape
    G_all = B + (H @ x)[None, :]                       # per-sample gradient at frozen x, (n, d)
    W = 1 / (1 - b2); burn = int(np.ceil(8 * W / n)) + 2; meas = max(40, int(np.ceil(4 * W / n)))
    m = np.zeros((chains, d)); v = np.tile(np.mean(G_all ** 2, 0), (chains, 1)); acc = np.zeros(d); cnt = 0
    for e in range(burn + meas):
        perm = rng.integers(0, n, size=(chains, n)) if iid else np.argsort(rng.random((chains, n)), axis=1)
        G = G_all[perm]                                # (chains, n, d)
        for k in range(n):
            g = G[:, k, :]; m = b1 * m + (1 - b1) * g; v = b2 * v + (1 - b2) * g * g
            if e >= burn: acc += np.sum(m / np.sqrt(v), 0); cnt += chains
    return acc / cnt
if __name__ == "__main__":
    b2 = float(sys.argv[1]); b1 = float(sys.argv[2]); chains = int(sys.argv[3]); iid = len(sys.argv) > 4 and sys.argv[4] == "iid"
    H = np.array([[1.0, 0.5], [0.5, 2.0]])
    B = np.array([[9, -4], [-1, -4], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 0]], float)
    n = len(B); assert np.allclose(B.sum(0), 0)
    c = np.mean(B ** 3, 0) / (2 * np.mean(B ** 2, 0))
    K = K_iid(n, b1, b2) if iid else K_rr(n, b1, b2)
    pred = np.linalg.solve(H, (1 - b2) * K * c)
    s = 1.5 * np.abs(pred).max(); seed = 7
    D0 = drift(np.zeros(2), H, B, b1, b2, chains, seed, iid)
    J = np.column_stack([(drift(s * e, H, B, b1, b2, chains, seed, iid) - D0) / s for e in np.eye(2)])
    xs = -np.linalg.solve(J, D0)
    D1 = drift(xs, H, B, b1, b2, chains, seed, iid); xs2 = xs - np.linalg.solve(J, D1)
    D2 = drift(xs2, H, B, b1, b2, chains, seed + 1, iid)   # fresh seed: residual drift at the answer
    print(json.dumps(dict(beta2=b2, beta1=b1, sampling="iid" if iid else "RR", K=K, c=c.tolist(), pred=pred.tolist(),
        xstar=xs2.tolist(), ratio=(xs2 / pred).tolist(), D_at_xstar_freshseed=D2.tolist(), D0=D0.tolist())), flush=True)
