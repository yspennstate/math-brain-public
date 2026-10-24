# Two coordinates, rotated frame: (U, V) = R_theta (Y_1, Y_2), Phi = U + c (V - b)^2, Y_i with densities <= 1.
# The density of Phi at s is approximated by the thickened level set: p(s) ~ (2 eta)^{-1} P(|Phi - s| <= eta), which on
# a grid is f_1^T M f_2 dx^2 with M_kl = 1[|Phi(x_k, x_l) - s| <= eta]/(2 eta). Best responses are exact for this
# functional: f_1 = top level set (measure 1) of M f_2, f_2 = top level set of M^T f_1.
# Question: is the largest value attained by laws uniform on intervals? (eta is kept at least twice the grid spacing
# times the largest gradient of Phi on the grid, so the band is resolved.)
import sys, math, json
import numpy as np

def band_matrix(x, th, c, b, s, eta):
    Y1, Y2 = np.meshgrid(x, x, indexing='ij')           # M[k, l] <-> (y1 = x_k, y2 = x_l)
    U = math.cos(th)*Y1 + math.sin(th)*Y2
    V = -math.sin(th)*Y1 + math.cos(th)*Y2
    return (np.abs(U + c*(V - b)**2 - s) <= eta).astype(np.float32)/(2*eta)

def value(M, f1, f2, dx):
    return float(f1 @ (M @ f2))*dx*dx

def top_set(h, ncell):
    f = np.zeros_like(h); f[np.argpartition(-h, ncell)[:ncell]] = 1.0
    return f

def ascend(M, f1, f2, dx, ncell, sweeps=60):
    best = value(M, f1, f2, dx)
    for _ in range(sweeps):
        f1 = top_set(M @ f2, ncell)
        f2 = top_set(M.T @ f1, ncell)
        v = value(M, f1, f2, dx)
        if v <= best + 1e-9:
            best = max(best, v); break
        best = v
    return best, f1, f2

def runs(f, x):
    idx = np.flatnonzero(f > 0)
    parts = np.split(idx, np.flatnonzero(np.diff(idx) > 1) + 1)
    return [(round(float(x[p[0]]), 3), round(len(p)*(x[1] - x[0]), 3)) for p in parts]

if __name__ == "__main__":
    try:
        import psutil, os
        psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        psutil.Process().cpu_affinity(list(range(2, os.cpu_count())))
    except Exception:
        pass
    rng = np.random.default_rng(1)
    dx = 1/200; x = np.arange(-4, 4, dx) + dx/2; ncell = int(round(1/dx))
    for th in (0.0, math.pi/8, math.pi/4, 3*math.pi/8, math.pi/2):
        for c in (0.03, 0.1, 0.3, -0.1):
            gmax = 1 + 2*abs(c)*(4*math.sqrt(2) + 2)
            eta = max(0.02, 2*dx*gmax)
            best_int = (0.0, None)
            best_any = (0.0, None)
            for s in (-1.0, 0.0, 1.0):
                for b in (-1.0, 0.0, 1.0):
                    M = band_matrix(x, th, c, b, s, eta)
                    # interval laws: every pair of offsets on a 0.05 grid inside [-3, 2]
                    offs = np.arange(-3.0, 2.0, 0.05)
                    F1 = np.array([((x >= a) & (x < a + 1)).astype(np.float32) for a in offs])
                    vals = (F1 @ M) @ F1.T*dx*dx
                    k1, k2 = np.unravel_index(np.argmax(vals), vals.shape)
                    if vals[k1, k2] > best_int[0]:
                        best_int = (float(vals[k1, k2]), (round(float(offs[k1]), 2), round(float(offs[k2]), 2), s, b))
                    for trial in range(4):
                        f1 = np.zeros_like(x); f1[rng.choice(len(x)//2, ncell, replace=False) + len(x)//4] = 1
                        f2 = np.zeros_like(x); f2[rng.choice(len(x)//2, ncell, replace=False) + len(x)//4] = 1
                        v, g1, g2 = ascend(M, f1.astype(np.float32), f2.astype(np.float32), dx, ncell)
                        if v > best_any[0]:
                            best_any = (v, (runs(g1, x)[:4], runs(g2, x)[:4], s, b))
            print(json.dumps(dict(theta=round(th, 4), c=c, eta=round(eta, 4), interval_best=round(best_int[0], 4),
                                  interval_at=best_int[1], bestresp_best=round(best_any[0], 4),
                                  bestresp_laws=best_any[1])), flush=True)
