"""T250 lemma (ii) (agent A, 18 Oct): the deterministic facts the written proof uses, checked on a fine grid.
k(t) = (sin t + (pi - t) cos t)/pi, F(t) = arccos k(t) (the ReLU angle map). With a = |r1|^2/n, b = |d|^2/(n t^2), m = <d, r1>/(n t):
E a = 1/2, E b = (1 - k)/t^2, E m = (k - 1)/(2 t), and (Eb - (Em)^2/Ea) = sin^2 F / (2 t^2), q(means) = sin F / t.
Also: one Monte Carlo check that sin theta' = t q(a, b, m) holds exactly sample by sample."""
import numpy as np
t = np.linspace(1e-4, np.pi / 2, 200001)
k = (np.sin(t) + (np.pi - t) * np.cos(t)) / np.pi; F = np.arccos(np.clip(k, -1, 1))
dF = np.gradient(F, t); d2F = np.gradient(dF, t)
print('F concave on (0, pi/2]: max F\'\' =', d2F[5:-5].max())
print('t F\'/F in', (t * dF / F)[5:-5].min(), (t * dF / F)[5:-5].max())
r = np.sin(F) / t
print('sin F / t: monotone decreasing', bool(np.all(np.diff(r) <= 1e-12)), ' range', r.min(), r.max(), ' delta0 = min sin^2F/(2t^2) =', (r ** 2 / 2).min())
print('sup sin F =', np.sin(F).max(), ' F(pi/2) =', F[-1])
rng = np.random.default_rng(1); n = 50
for th in (1e-3, 0.3, 1.5):
    x, w = rng.standard_normal(n), rng.standard_normal(n); y = np.cos(th) * x + np.sin(th) * w
    r1, r2 = np.maximum(x, 0), np.maximum(y, 0); d = r2 - r1
    a, b, m = r1 @ r1 / n, d @ d / (n * th * th), d @ r1 / (n * th)
    q = np.sqrt(b - m * m / a) / np.sqrt(a + 2 * th * m + th * th * b)
    s_direct = np.sqrt(max(0.0, 1 - (r1 @ r2 / np.linalg.norm(r1) / np.linalg.norm(r2)) ** 2))
    print(f'theta {th}: sin theta\' direct {s_direct:.12f}  t*q {th * q:.12f}')
