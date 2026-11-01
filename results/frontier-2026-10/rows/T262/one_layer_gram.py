"""T262 Target 2 (agent A, 20 Oct): one-layer law of the tangent Gram for three inputs. Inputs at small angles (tangent
positions p1 = 0, p2, p3 in units of 1/n); one critical He ReLU layer of width n. G (2 x 2) is the Gram of the tangent positions
of points 2, 3 relative to point 1, built from the three exact pairwise angles (chord formula, times n). M = G^(-1/2) G' G^(-1/2).
Prediction of the mesoscopic model (S = W / |x|^2, W ~ Wishart_2(K-1), K ~ n/2 active units):
  n Var log(M11/M22) = 8,  n Var M12/sqrt(M11 M22) = 2,  n Var log det M = 24,  all cross covariances 0.
usage: python one_layer_gram.py n1,n2 reps phi2x,phi3x,phi3y"""
import sys, numpy as np
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
ns = [int(v) for v in sys.argv[1].split(",")]; reps = int(sys.argv[2])
p2x, p3x, p3y = (float(v) for v in sys.argv[3].split(",")); rng = np.random.default_rng(2622)

def gram(U, n):   # U (..., 3, dim) unit rows -> tangent Gram (..., 2, 2) in units of 1/n
    def ang(a, b): c = np.linalg.norm(U[..., a, :] - U[..., b, :], axis=-1); return 2 * np.arcsin(c / 2) * n
    d12, d13, d23 = ang(0, 1), ang(0, 2), ang(1, 2)
    G = np.empty(d12.shape + (2, 2)); G[..., 0, 0] = d12 ** 2; G[..., 1, 1] = d13 ** 2
    G[..., 0, 1] = G[..., 1, 0] = (d12 ** 2 + d13 ** 2 - d23 ** 2) / 2; return G

for n in ns:
    # inputs on the sphere in R^3: point 1 at the pole, others at geodesic tangent coordinates q/n
    def pt(qx, qy):
        r = np.hypot(qx, qy) / n
        return np.array([np.cos(r), np.sin(r) * qx / max(np.hypot(qx, qy), 1e-300), np.sin(r) * qy / max(np.hypot(qx, qy), 1e-300)])
    X = np.stack([np.array([1.0, 0, 0]), pt(p2x, 0.0), pt(p3x, p3y)])
    G0 = gram(X, n); w, V = np.linalg.eigh(G0); Gm = V @ np.diag(w ** -0.5) @ V.T
    out = []
    B = max(1, min(reps, int(2e7 // (3 * n))))
    done = 0
    while done < reps:
        b = min(B, reps - done)
        H = np.maximum(np.einsum('ij,rjn->rin', X, rng.standard_normal((b, 3, n))), 0)
        U = H / np.linalg.norm(H, axis=2, keepdims=True)
        M = Gm @ gram(U, n) @ Gm
        out.append(np.stack([np.log(M[:, 0, 0] / M[:, 1, 1]), M[:, 0, 1] / np.sqrt(M[:, 0, 0] * M[:, 1, 1]),
                             np.log(M[:, 0, 0] * M[:, 1, 1] - M[:, 0, 1] ** 2)], 1)); done += b
    Z = np.concatenate(out)
    # the mesoscopic model for the same step: tangent positions P (columns p2, p3), S = Y^T Pi_x Y / |x|^2, then side contraction
    d0 = np.array([np.sqrt(G0[0, 0]), np.sqrt(G0[1, 1]), np.sqrt(G0[0, 0] + G0[1, 1] - 2 * G0[0, 1])])
    cx = G0[0, 1] / d0[0]; P = np.array([[d0[0], cx], [0.0, np.sqrt(G0[1, 1] - cx ** 2)]])
    Zm = []
    for _ in range(len(Z)):
        K = rng.binomial(n, 0.5); x = rng.standard_normal(K); Y = rng.standard_normal((K, 2))
        Y = Y - np.outer(x, x @ Y) / (x @ x); S = Y.T @ Y / (x @ x); Q = P.T @ S @ P
        D = np.array([np.sqrt(Q[0, 0]), np.sqrt(Q[1, 1]), np.sqrt(max(Q[0, 0] + Q[1, 1] - 2 * Q[0, 1], 0))])
        D = D * (1 - D / (3 * np.pi * n)); G1 = np.array([[D[0] ** 2, (D[0] ** 2 + D[1] ** 2 - D[2] ** 2) / 2], [0, D[1] ** 2]]); G1[1, 0] = G1[0, 1]
        Mm = Gm @ G1 @ Gm; Zm.append([np.log(Mm[0, 0] / Mm[1, 1]), Mm[0, 1] / np.sqrt(Mm[0, 0] * Mm[1, 1]), np.log(Mm[0, 0] * Mm[1, 1] - Mm[0, 1] ** 2)])
    Zm = np.array(Zm); Cm = np.cov(Zm.T) * n
    print(f"   model: n Var {Cm[0,0]:.3f} / {Cm[1,1]:.3f} / {Cm[2,2]:.3f} | n mean logdet {n*Zm[:,2].mean():+.3f} (net {n*Z[:,2].mean():+.3f}, se {np.sqrt(n*Cm[2,2]/len(Z)):.3f})", flush=True)
    C = np.cov(Z.T) * n; mu = Z.mean(0)
    se = lambda v: v * np.sqrt(2 / (len(Z) - 1))
    print(f"n {n} reps {len(Z)} p2 ({p2x},0) p3 ({p3x},{p3y}): n Var log(M11/M22) {C[0,0]:.3f} +/- {se(C[0,0]):.3f} (pred 8) | "
          f"n Var M12n {C[1,1]:.3f} +/- {se(C[1,1]):.3f} (pred 2) | n Var logdet {C[2,2]:.3f} +/- {se(C[2,2]):.3f} (pred 24) | "
          f"n Cov 01 {C[0,1]:+.3f} 02 {C[0,2]:+.3f} 12 {C[1,2]:+.3f} | n mean logdet {n*mu[2]:+.3f}", flush=True)
