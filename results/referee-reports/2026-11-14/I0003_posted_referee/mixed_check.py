# Exact P^n(0,0) for the field e = g (e_y = sign, y>=0 -> +1), f alternating (f_x = (-1)^x): the case outside
# Theorems 1.1-1.4 of the I0003 paper. Heuristic: x_n ~ n (arcsine-type), y_n ~ sqrt(n), so P^n(0,0) ~ n^{-3/2}
# (transient). Prints n^{1.5} P and the partial Green sum G. numpy, CPU. Evidence only.
import sys, numpy as np
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
L = 2 * N + 3; c = N + 1
k = np.arange(L) - c
e = np.where(k >= 0, 1, -1); f = (-1) ** np.abs(k)
E = (e[:, None] == 1); F = (f[None, :] == 1)
p = np.zeros((L, L)); p[c, c] = 1.0; G = 1.0
marks = {50, 100, 200, 400, 600, 800, N}
for n in range(1, N + 1):
    h = 0.5 * p
    q = np.zeros_like(p)
    q[:, 1:] += np.where(E, h, 0)[:, :-1]
    q[:, :-1] += np.where(~E, h, 0)[:, 1:]
    q[1:, :] += np.where(F, h, 0)[:-1, :]
    q[:-1, :] += np.where(~F, h, 0)[1:, :]
    p = q; G += p[c, c]
    if n in marks:
        print(f"n={n} P={p[c,c]:.3e} nP={n*p[c,c]:.4f} n^1.5P={n**1.5*p[c,c]:.4f} G={G:.5f}", flush=True)
print("mass", round(p.sum(), 12))
