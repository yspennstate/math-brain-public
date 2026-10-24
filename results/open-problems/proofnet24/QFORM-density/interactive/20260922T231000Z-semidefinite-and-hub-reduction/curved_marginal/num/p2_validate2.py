import numpy as np
from p2_adversary import frame, Evaluator, random_pos
rng = np.random.default_rng(3)
m, N = 6, 4
D = frame(m, rng)
pos, gaps = random_pos(m, N, rng, 1.0)
n = 8_000_000
X = np.zeros((n, m))
for i in range(m):
    k = rng.integers(0, N, size=n)
    X[:, i] = pos[i][k] + rng.uniform(0, 1.0/N, size=n)
U = X @ D[0]; V = X @ D[1]
for (G, delta) in [(512, 0.05), (1024, 0.025), (2048, 0.0125)]:
    ev = Evaluator(D, N, G, delta, cs=[0.1], nb=5)
    rho = ev.density(pos)
    d = ev.delta
    ugrid = ev.x0u + d*np.arange(G); vgrid = ev.x0v + d*np.arange(G)
    for (c, b) in [(0.1, -0.8687), (0.01, 0.0)]:
        acc = np.zeros(G)
        for j in range(G):
            acc += np.interp(ugrid - c*(vgrid[j]-b)**2, ugrid, rho[j], left=0, right=0)
        acc *= d
        Y = U + c*(V - b)**2
        # MC histogram on the same grid (bin centred at grid points)
        edges = np.concatenate([ugrid - d/2, [ugrid[-1] + d/2]])
        h = np.histogram(Y, bins=edges)[0]/(n*d)
        i0 = np.argmax(acc)
        print("G=%4d d=%.4f c=%.2f b=%+.3f  FFT max %.4f at %.3f | MC bin there %.4f | MC max %.4f | max|FFT-MC| %.4f | rho min %.2e" %
              (G, d, c, b, acc.max(), ugrid[i0], h[i0], h.max(), np.max(np.abs(acc - h)), rho.min()))
