"""T250 (agent A, 18 Oct 2026): p = 2 inputs, critical ReLU MLP (W ~ N(0, 2/n)). The coupling bound
W2(h_L/sqrt n, GP/sqrt n) <= sqrt(E ||G_(L-1)^(1/2) - Gbar_(L-1)^(1/2)||_F^2), with G the exact 2 x 2 Gram chain (unnormalized) and
Gbar its deterministic arc-cosine iterate. Prints the bound times sqrt(n/(L-1)) to test whether it is O(sqrt(L/n)) uniformly in L.
usage: two_input_w2.py n paths theta0"""
import sys, numpy as np
n, P, th0 = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
rng = np.random.default_rng(250 + n)
def sqrtm2(G):
    w, V = np.linalg.eigh(G); return (V * np.sqrt(np.maximum(w, 0))[..., None, :]) @ np.swapaxes(V, -1, -2)
G0 = np.array([[1, np.cos(th0)], [np.cos(th0), 1]]); G = np.repeat(G0[None], P, 0); Gb = G0.copy()
def kappa(G):  # infinite-width map for ReLU with weight variance 2: E[2 relu(u) relu(v)]
    a, b = np.sqrt(G[0, 0]), np.sqrt(G[1, 1]); c = np.clip(G[0, 1] / (a * b), -1, 1); t = np.arccos(c)
    off = a * b * (np.sin(t) + (np.pi - t) * c) / np.pi; return np.array([[G[0, 0], off], [off, G[1, 1]]])
print(f"n {n} paths {P} theta0 {th0}", flush=True)
for l in range(1, 4 * n + 1):
    if l in (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048) and l <= 4 * n:
        d = sqrtm2(G) - sqrtm2(Gb)[None]; b = np.sqrt(np.mean(np.sum(d * d, axis=(1, 2))))
        print(f"  L {l:5d} (L/n {l / n:6.3f}): bound {b:.5f}  bound*sqrt(n/(L-1)) {b * np.sqrt(n / max(l - 1, 1)):.4f}", flush=True)
    a = np.sqrt(G[:, 0, 0]); c = G[:, 0, 1] / a; bb = np.sqrt(np.maximum(G[:, 1, 1] - c ** 2, 0))
    xi = rng.standard_normal((P, n, 2)); z1 = a[:, None] * xi[:, :, 0]; z2 = c[:, None] * xi[:, :, 0] + bb[:, None] * xi[:, :, 1]
    r1, r2 = np.maximum(z1, 0), np.maximum(z2, 0); s12 = (r1 * r2).sum(1)
    G = np.stack([np.stack([(r1 * r1).sum(1), s12], 1), np.stack([s12, (r2 * r2).sum(1)], 1)], 1) * (2 / n)
    Gb = kappa(Gb)
