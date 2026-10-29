# K = E[m_k dv_k] / ((1 - beta2) C) under random reshuffling, first order in dv (agent B, 20 Oct 2026).
# m_k = (1-b1) sum_i b1^i g_{k-i}; dv_k = (1-b2) sum_j b2^j (g^2_{k-j} - V). For lags i, j: E[g_{k-i}(g^2_{k-j} - V)] is C if
# i = j, -C/(n-1) if k-i, k-j are different positions of the same epoch, 0 if they are in different epochs (independent
# permutations, E g^2 - V = 0). Average over the position p of k in its epoch.
import numpy as np
def K_rr(n, b1, b2, epochs=None):
    W = 1 / (1 - b2); E = epochs or int(np.ceil(40 * max(W, 1 / (1 - b1 + 1e-300)) / n)) + 2
    L = E * n; tot = 0.0
    lag = np.arange(L)
    for p in range(n):
        ep = np.where(lag <= p, 0, (lag - p - 1) // n + 1)   # epoch index of position k - lag
        wm = (1 - b1) * b1 ** lag; wv = b2 ** lag
        S = np.bincount(ep, weights=wv)                   # sum of b2^j over each epoch
        tot += np.sum(wm * (wv - (S[ep] - wv) / (n - 1)))
    return tot / n
def K_iid(n, b1, b2): return (1 - b1) / (1 - b1 * b2)  # corrected by agent A audit 20 Oct (was 1.0)
if __name__ == "__main__":
    import json
    for l in open("sweep_n10.jsonl"):
        r = json.loads(l); n, b1, b2 = r["n"], r["beta1"], r["beta2"]
        K = K_rr(n, b1, b2) if r["sampling"] == "RR" else 1.0
        V0, m3 = (n - 1) ** 2 / n + (n - 1) / n, ((n - 1) ** 3 - (n - 1)) / n
        x = 0.0
        for _ in range(50): x = K * (1 - b2) * (m3 + 2 * x * V0) / (2 * (V0 + x * x))
        print("%s b1 %.1f b2 %.4f n(1-b2) %5.2f K %.4f  x*_sim %.6f  x*_firstorder %.6f  sim/fo %.4f" % (r["sampling"], b1, b2, r["n1mb2"], K, r["xstar"], x, r["xstar"] / x))
