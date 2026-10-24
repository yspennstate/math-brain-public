try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# (a) profile g(x) = p_{Q_x}(s) of the milestone at the hub value x (the bathtub pairs f_h with the top level set of g);
# (b) dense family Q = 2 X_h (L + beta) + lam V^2 + eps X'^T W X' + <b, X'>, uniform and comb laws.
import numpy as np, time, sys
sys.path.insert(0, r'~\AppData\Local\Temp\claude\<project>\9bfb8ed3-a0b8-4b06-94b3-3777f80a6d98\scratchpad\wave2\14_real_variable_hub_dense')
from fibre_density import Law, density
rng = np.random.default_rng(11)
n1 = 48
Qm, _ = np.linalg.qr(rng.normal(size=(n1, 3))); w, v, u = Qm[:, 0], Qm[:, 1], Qm[:, 2]
d = 0.1 * rng.choice([-1, 1], n1) * rng.uniform(0.5, 1, n1)
class Comb(Law):
    def __init__(self, rng, m):
        self.kind = 'comb'; self.m = m; self.rng = rng
        self.pos = (np.arange(m) - (m - 1) / 2) * 1.0          # m teeth of width 1/m at unit spacing (support length ~ m)
    def sample(self, n):
        k = self.rng.integers(0, self.m, n); return self.pos[k] + self.rng.uniform(0, 1.0 / self.m, n)
    def f(self, x):
        out = np.zeros_like(x)
        for p in self.pos:
            out += ((x >= p) & (x < p + 1.0 / self.m))
        return out
print("(a) milestone profile g(x) at s = 0 (uniform leaves), bperp = 0 and 1:", flush=True)
for bperp in (0.0, 1.0):
    xs = np.linspace(-3, 3, 25); gs = []
    for x in xs:
        A = 2 * np.outer(w, w) + 2 * np.outer(v, v) + np.diag(d)
        b = 4 * x * w + bperp * u + 0.3 * v
        laws = [Law('unif', rng) for _ in range(n1)]
        m, sd = density(A, b, laws, np.array([0.0]), 8000)
        gs.append(m[0])
    gs = np.array(gs)
    print(f"  bperp={bperp}: " + " ".join(f"{x:+.1f}:{g:.2f}" for x, g in zip(xs, gs)), flush=True)
    srt = np.sort(gs)[::-1]; dx = xs[1] - xs[0]
    print(f"  int of top level set of measure 1 ~ {srt[:int(round(1/dx))].sum()*dx:.3f};  int over [-1/2,1/2] ~ {gs[np.abs(xs)<=0.5+1e-9].sum()*dx:.3f}", flush=True)
print("(b) dense family: max_s p over s-grid", flush=True)
W = rng.normal(size=(n1, n1)); W = (W + W.T) / 2; np.fill_diagonal(W, 0); W /= np.linalg.norm(W, 2)
for lawname in ('unif', 'comb3'):
    for eps in (0.0, 0.2, 0.5):
        for bperp in (0.0, 1.0):
            t = time.time(); n = n1 + 1
            A = np.zeros((n, n)); A[0, 1:] = w; A[1:, 0] = w
            A[1:, 1:] = 1.0 * np.outer(v, v) + eps * W
            b = np.zeros(n); b[0] = 0.2; b[1:] = bperp * u
            if lawname == 'unif':
                laws = [Law('unif', rng) for _ in range(n)]
            else:
                laws = [Law('unif', rng)] + [Comb(rng, 3) for _ in range(n1)]
            svals = np.linspace(-2, 2, 21)
            m, sd = density(A, b, laws, svals, 12000)
            k = int(np.argmax(m)); s2 = np.linspace(svals[max(k-1,0)], svals[min(k+1,20)], 9)
            m2, sd2 = density(A, b, laws, s2, 20000); k2 = int(np.argmax(m2))
            print(f"  laws={lawname} eps={eps:.1f} bperp={bperp:.1f}: max p ~ {m2[k2]:.3f} +- {sd2[k2]:.3f} at s={s2[k2]:+.2f} ({time.time()-t:.0f}s)", flush=True)
