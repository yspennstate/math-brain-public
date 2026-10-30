"""T250 (agent A, 18 Oct 2026): numerical checks of the two lemmas a proof of W2 <= C sqrt(L/n) for p = 2 needs.
(i)  d log F / d log theta = theta F'(theta)/F(theta) lies in [0, 1] on (0, pi/2], F the ReLU arc-cosine angle map.
(ii) uniformly in theta in (0, pi/2]: n |E[log theta' | theta] - log F(theta)| and n Var[log theta' | theta] stay bounded,
     theta' the angle after one finite-width layer (n neurons). Exact one-step sampling.
usage: angle_lemmas.py"""
import numpy as np
F = lambda t: np.arccos(np.clip((np.sin(t) + (np.pi - t) * np.cos(t)) / np.pi, -1, 1))
th = np.linspace(1e-4, np.pi / 2, 20001); h = 1e-7
d = th * (F(th + h) - F(th - h)) / (2 * h) / F(th)
print(f"(i) theta F'/F on (0, pi/2]: min {d.min():.5f} max {d.max():.5f} (at theta {th[d.argmax()]:.4f}); F'(theta) max {((F(th + h) - F(th - h)) / (2 * h)).max():.5f}")
rng = np.random.default_rng(1); P = 20000
for n in (50, 200, 800):
    worst_b, worst_v = 0, 0; rows = []
    for t in (1e-3, 1e-2, 0.05, 0.2, 0.5, 1.0, np.pi / 2):
        x = rng.standard_normal((P, n)); w = rng.standard_normal((P, n))
        r1 = np.maximum(x, 0); r2 = np.maximum(np.cos(t) * x + np.sin(t) * w, 0)
        c = (r1 * r2).sum(1) / np.sqrt((r1 * r1).sum(1) * (r2 * r2).sum(1))
        u1 = r1 / np.linalg.norm(r1, axis=1)[:, None]; u2 = r2 / np.linalg.norm(r2, axis=1)[:, None]
        tp = 2 * np.arcsin(np.linalg.norm(u1 - u2, axis=1) / 2)
        lg = np.log(tp); b = n * (lg.mean() - np.log(F(t))); v = n * lg.var()
        se = n * lg.std() / np.sqrt(P)
        rows.append(f"theta {t:7.4f}: n*bias {b:7.3f} (+-{se:.3f})  n*var {v:6.3f}")
        worst_b = max(worst_b, abs(b)); worst_v = max(worst_v, v)
    print(f"n {n}: max |n*bias| {worst_b:.3f}  max n*var {worst_v:.3f}"); print("   " + "\n   ".join(rows), flush=True)
