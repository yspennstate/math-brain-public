"""T262 Target 3 (agent A, 20 Oct): one critical tanh layer at small q, the Fisher z increment. Prediction (linear Wishart
chain, sample correlation of n iid pairs): n E dz -> tanh(z)/2, n Var dz -> 1, as q -> 0; the tanh correction to E dz is O(q^2).
Also checks the infinite-width small-q expansion E tanh u tanh v = q c (1 - 2q + 5q^2 + (2/3) q^2 c^2) + O(q^4).
The linear twin (same Gaussians, identity activation) is the exact Wishart chain; tanh - linear isolates the nonlinearity.
usage: python tanh_one_layer.py n reps"""
import sys, numpy as np
n, R = int(sys.argv[1]), int(sys.argv[2]); rng = np.random.default_rng(7)
xg, wg = np.polynomial.hermite_e.hermegauss(80); wg /= wg.sum(); X, Y = np.meshgrid(xg, xg, indexing='ij'); W = np.outer(wg, wg)
for q in [0.05, 0.02]:
    for c in [0.3, 0.8]:
        u = np.sqrt(q) * X; v = np.sqrt(q) * (c * X + np.sqrt(1 - c * c) * Y)
        ex = (W * np.tanh(u) * np.tanh(v)).sum(); pr = q * c * (1 - 2 * q + 5 * q * q + 2 / 3 * q * q * c * c)
        print(f"expansion q {q} c {c}: exact {ex:.10f} predicted {pr:.10f} rel err {(ex - pr) / ex:.2e} (q^3 = {q ** 3:.1e})")
for q in [1e-2, 1e-3]:
    for c in [0.3, 0.8]:
        z0 = np.arctanh(c); s = 0.0; s2 = 0.0; sl = 0.0; sd = 0.0; sd2 = 0.0; B = max(1, int(4e6 // n)); done = 0
        while done < R:
            b = min(B, R - done); g = rng.standard_normal((b, n)); gp = rng.standard_normal((b, n))
            a = np.tanh(np.sqrt(q) * g); bb = np.tanh(np.sqrt(q) * (c * g + np.sqrt(1 - c * c) * gp))
            cc = (a * bb).sum(1) / np.sqrt((a * a).sum(1) * (bb * bb).sum(1)); dz = np.arctanh(cc) - z0
            lb = c * g + np.sqrt(1 - c * c) * gp; cl = (g * lb).sum(1) / np.sqrt((g * g).sum(1) * (lb * lb).sum(1)); dl = np.arctanh(cl) - z0
            s += dz.sum(); s2 += (dz * dz).sum(); sl += dl.sum(); sd += (dz - dl).sum(); sd2 += ((dz - dl) ** 2).sum(); done += b
        m = s / R; var = s2 / R - m * m
        md = sd / R; vd = sd2 / R - md * md
        print(f"n {n} q {q} c {c}: n E dz {n * m:.4f} +/- {n * np.sqrt(var / R):.4f} (tanh(z)/2 = {c / 2:.4f}) | n Var dz {n * var:.4f} (1) | linear twin n E dz {n * sl / R:.4f} | tanh - linear: n E {n * md:.5f} +/- {n * np.sqrt(vd / R):.5f}", flush=True)
