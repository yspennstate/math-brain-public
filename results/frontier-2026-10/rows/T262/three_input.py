"""T262 Target 2, three inputs (agent A, 19 Oct). Three inputs at pairwise angle phi0/n (equilateral) through a critical
He ReLU net, width n, depth t n. Compared with the MESOSCOPIC model that the two-input analysis suggests: positions p1 = 0, p2,
p3 in the tangent plane (phi units); per layer (a) the Wishart action Q -> P^T S P, S = Y^T Pi Y / |x|^2 * (K-1)... no rescale:
S = (Y^T Pi_x Y) / |x|^2 with x (K) and Y (K x 2) iid N(0,1) on the K active units, Pi_x the projection off x; (b) the
infinite-width kernel contraction applied to each pairwise distance, phi -> phi (1 - phi/(3 pi n)); then rebuild the triangle.
Statistics at each t: quantiles of the flatness r = (a + b - c)/c (a <= b <= c the three phi_ij; 0 = collinear) and of log c.
usage: python three_input.py n1,n2 t1,t2 reps phi0"""
import sys, numpy as np
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
ns = [int(v) for v in sys.argv[1].split(",")]; ts = [float(v) for v in sys.argv[2].split(",")]
reps = int(sys.argv[3]); phi0 = float(sys.argv[4]); rng = np.random.default_rng(2621)

def stats(D):
    s = np.sort(D, axis=1); a, b, c = s[:, 0], s[:, 1], s[:, 2]; r = (a + b - c) / c
    return np.quantile(r, [.1, .25, .5, .75, .9]), np.quantile(np.log(c), [.1, .5, .9])

def tri(D):   # distances (reps, 3) = (d12, d13, d23) -> positions of p2, p3 (p1 = 0)
    d12, d13, d23 = D.T; cx = (d12 ** 2 + d13 ** 2 - d23 ** 2) / (2 * d12); cy = np.sqrt(np.maximum(d13 ** 2 - cx ** 2, 0))
    P = np.zeros((len(D), 2, 2)); P[:, 0, 0] = d12; P[:, 0, 1] = cx; P[:, 1, 1] = cy; return P   # columns p2, p3

def dists(P):
    p2, p3 = P[:, :, 0], P[:, :, 1]
    return np.stack([np.linalg.norm(p2, axis=1), np.linalg.norm(p3, axis=1), np.linalg.norm(p2 - p3, axis=1)], 1)

for n in ns:
    L = int(round(max(ts) * n)); marks = {int(round(t * n)): t for t in ts}
    # exact network: coordinates of the three unit outputs in their own QR frame, plus norms
    th = phi0 / n; c = np.cos(th); u = np.zeros((reps, 3, 3))
    u[:, 0, 0] = 1; u[:, 1, :2] = [c, np.sin(th)]
    c3x = c; c3y = (c - c * c) / np.sin(th); u[:, 2, :] = [c3x, c3y, np.sqrt(max(1 - c3x ** 2 - c3y ** 2, 0))]
    R = u   # rows = inputs, in an orthonormal frame
    D_meso = np.full((reps, 3), phi0); out = {}
    for l in range(1, L + 1):
        G = rng.standard_normal((reps, 3, n))                       # frame coordinates -> preactivations (rows: inputs)
        H = np.maximum(np.einsum('rij,rjn->rin', R, G), 0)          # (reps, 3, n); common norm scale irrelevant for angles
        Hn = H / np.linalg.norm(H, axis=2, keepdims=True)
        Q, Rr = np.linalg.qr(np.transpose(Hn, (0, 2, 1)))           # n x 3 -> coordinates of each unit output, rows of R^T
        R = np.transpose(Rr, (0, 2, 1))
        # mesoscopic model
        x = rng.standard_normal((reps, n)); Y = rng.standard_normal((reps, n, 2)); act = rng.random((reps, n)) < 0.5
        x = x * act; Y = Y * act[:, :, None]; xx = np.einsum('rn,rn->r', x, x)
        xY = np.einsum('rn,rnk->rk', x, Y); YY = np.einsum('rnk,rnm->rkm', Y, Y)
        S = (YY - xY[:, :, None] * xY[:, None, :] / xx[:, None, None]) / xx[:, None, None]
        P = tri(D_meso); Qm = np.einsum('rki,rkm,rmj->rij', P, S, P)
        d12 = np.sqrt(Qm[:, 0, 0]); d13 = np.sqrt(Qm[:, 1, 1]); d23 = np.sqrt(np.maximum(Qm[:, 0, 0] + Qm[:, 1, 1] - 2 * Qm[:, 0, 1], 0))
        D_meso = np.stack([d12, d13, d23], 1) * n / n; D_meso = D_meso * (1 - D_meso / (3 * np.pi * n))
        if l in marks:
            Dn = np.zeros((reps, 3))
            for k, (i, j) in enumerate([(0, 1), (0, 2), (1, 2)]):
                a, b = R[:, i, :], R[:, j, :]
                Dn[:, k] = n * 2 * np.arctan2(np.linalg.norm(a - b, axis=1), np.linalg.norm(a + b, axis=1))
            out[marks[l]] = (stats(Dn), stats(D_meso))
    for t in ts:
        (rn, cn), (rm, cm) = out[t]
        print(f"n {n} t {t}: flatness r q10/25/50/75/90 net {' '.join('%.3f' % v for v in rn)} | meso {' '.join('%.3f' % v for v in rm)}"
              f" || log c q10/50/90 net {' '.join('%.2f' % v for v in cn)} | meso {' '.join('%.2f' % v for v in cm)}", flush=True)
print("DONE", flush=True)
