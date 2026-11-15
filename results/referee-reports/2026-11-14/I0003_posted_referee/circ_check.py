# Exact return probabilities P^n(0,0) of the discrete Manhattan walk for three deterministic fields
# (numerical sanity check of the posted I0003 paper; numpy, CPU).
# circulating (g,-g): recurrent by Lemma 6.1 -> sum_n P^n(0,0) should grow without bound (like log n if P^n ~ c/n)
# alternating ((-1)^y,(-1)^x): bounded primitives, recurrent by Theorem 1.2
# saddle (g,g): P^n(0,0)=0 for n>0
import sys, numpy as np
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
L = 2 * N + 3; c = N + 1
k = np.arange(L) - c
g = np.where(k >= 0, 1, -1)
fields = {"circulating": (g, -g), "alternating": ((-1) ** np.abs(k), (-1) ** np.abs(k)), "saddle": (g, g)}
for name, (e, f) in fields.items():
    E = (e[:, None] == 1)  # e_y indexed by row y (axis 0 = y), f_x by column x (axis 1 = x)
    F = (f[None, :] == 1)
    p = np.zeros((L, L)); p[c, c] = 1.0
    G = 1.0; out = []
    for n in range(1, N + 1):
        h = 0.5 * p
        q = np.zeros_like(p)
        q[:, 1:] += np.where(E, h, 0)[:, :-1]      # move x+1 where e_y=+1
        q[:, :-1] += np.where(~E, h, 0)[:, 1:]     # move x-1 where e_y=-1
        q[1:, :] += np.where(F, h, 0)[:-1, :]      # move y+1 where f_x=+1
        q[:-1, :] += np.where(~F, h, 0)[1:, :]     # move y-1 where f_x=-1
        p = q; G += p[c, c]
        if n in (100, 200, 400, 800, N): out.append(f"n={n} P={p[c,c]:.3e} nP={n*p[c,c]:.4f} G={G:.4f}")
    print(name, "mass", round(p.sum(), 12), " | ".join(out), flush=True)
