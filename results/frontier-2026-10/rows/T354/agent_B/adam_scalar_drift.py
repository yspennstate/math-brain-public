# T354 scalar finite-sum model (agent B, 20 Oct 2026). f_i(x) = a_i x^2/2 + b_i x, sum b_i = 0, f = mean f_i, argmin 0.
# Adam (PyTorch form: m, v EMAs, bias correction, eps outside the sqrt) with random reshuffling and a vanishing step: the iterate
# moves on a slower clock than the EMAs, so it follows xdot = -D(x), D(x) = stationary mean over steps of m_k/(sqrt(v_k)+eps) at
# FROZEN x. The limit point x* solves D(x*) = 0; |x*| is the residual. This script computes D by simulating the EMAs at frozen x
# over many independent chains of random permutations, and finds x* by bisection.
# First-order prediction (beta1 = 0, eps = 0, n(1-beta2) small): D(x) ~ V^-1/2 [f'(x) - (1-beta2) C/(4V)], C = mean g^3 - f' V,
# V = mean g^2, so x* ~ (1-beta2) m3 / (4 abar V), m3 = mean b^3, V = mean b^2 (self term (1-beta2)C, the earlier items of the
# same epoch -(1-beta2)C/2 on average because they are drawn without replacement).
import numpy as np, sys, json
def drift(x, a, b, b1, b2, eps, chains=4000, burn=None, meas=None, seed=0, iid=False):
    rng = np.random.default_rng(seed); n = len(a)
    g_all = a * x + b
    W = 1.0 / (1 - b2)
    burn = burn or int(np.ceil(8 * W / n)) + 2; meas = meas or max(20, int(np.ceil(2 * W / n)))
    V = np.mean(g_all ** 2)
    m = np.zeros(chains); v = np.full(chains, V)  # start v at its mean; the burn-in removes the start
    acc = 0.0; cnt = 0
    for e in range(burn + meas):
        perm = rng.integers(0, n, size=(chains, n)) if iid else np.argsort(rng.random((chains, n)), axis=1)
        G = g_all[perm]
        for k in range(n):
            g = G[:, k]
            m = b1 * m + (1 - b1) * g; v = b2 * v + (1 - b2) * g * g
            if e >= burn:
                acc += np.sum(m / (np.sqrt(v) + eps)); cnt += chains
    return acc / cnt
def xstar(a, b, b1, b2, eps, lo, hi, it=30, **kw):
    dlo, dhi = drift(lo, a, b, b1, b2, eps, **kw), drift(hi, a, b, b1, b2, eps, **kw)
    assert dlo < 0 < dhi, (lo, hi, dlo, dhi)
    for _ in range(it):
        mid = (lo + hi) / 2; d = drift(mid, a, b, b1, b2, eps, **kw)
        lo, hi = (mid, hi) if d < 0 else (lo, mid)
    return (lo + hi) / 2
if __name__ == "__main__":
    n = int(sys.argv[1]); b2 = float(sys.argv[2]); b1 = float(sys.argv[3]); eps = float(sys.argv[4]); iid = len(sys.argv) > 5 and sys.argv[5] == "iid"
    b = np.array([n - 1.0] + [-1.0] * (n - 1)); a = np.ones(n)
    V, m3, abar = np.mean(b ** 2), np.mean(b ** 3), np.mean(a)
    pred = (1 - b2) * m3 / (4 * abar * V)
    s = max(4 * abs(pred), 1e-3)
    xs = xstar(a, b, b1, b2, eps, -s, s, it=22, iid=iid)
    out = dict(n=n, beta2=b2, beta1=b1, eps=eps, sampling="iid" if iid else "RR", n1mb2=n * (1 - b2), xstar=xs, pred_first_order=pred, ratio=xs / pred)
    print(json.dumps(out), flush=True)
