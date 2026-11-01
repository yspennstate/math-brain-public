"""T255 generator checks. SDE (Noci et al. Thm 4.2), derived 16 Oct (agent Q):
 dV = b(V) dt + sqrt(c) L dH L^T + k (L dN L^T P V + V P L dN^T L^T),  V = L L^T,
 c = g2(2-g2), k = g2/(m tau0), H GOE BM (diag var 2, offdiag var 1), N iid m x m BM, independent.
 b(V) = (g2/tau0^2)[ V |PVP|_F^2/m^2 + (1/2m)(v (VD)^T + (VD) v^T) ],  v = diag V, D = diag(PVP) - tr(PVP)/m.
"""
import numpy as np

def bdrift(V, g2, tau0=1.0):
    m = V.shape[0]; P = np.eye(m) - 1.0/m
    W = P @ V @ P; D = np.diag(W) - np.trace(W)/m; v = np.diag(V); VD = V @ D
    return g2/tau0**2 * (V * np.sum(W*W)/m**2 + (np.outer(v, VD) + np.outer(VD, v))/(2*m))

def noise_basis(V, g2, tau0=1.0, att=True, lin=False):
    """list of matrices E_j such that dV_noise = sum_j E_j dB_j (independent std BMs)"""
    m = V.shape[0]; P = np.eye(m) - 1.0/m; L = np.linalg.cholesky(V); out = []
    if att:
        k = g2/(m*tau0)
        for i in range(m):
            for j in range(m):
                N = np.zeros((m, m)); N[i, j] = 1
                X = L @ N @ L.T @ P @ V; out.append(k*(X + X.T))
    if lin:
        c = g2*(2-g2)
        for i in range(m):
            for j in range(i, m):
                H = np.zeros((m, m))
                if i == j: H[i, i] = np.sqrt(2)
                else: H[i, j] = H[j, i] = 1
                out.append(np.sqrt(c) * L @ H @ L.T)
    return out

def gen_log(F, gradF, hessF, V, g2, att=True, lin=False):
    """drift and quadratic variation of log F(V)"""
    b = bdrift(V, g2); E = noise_basis(V, g2, att=att, lin=lin)
    f = F(V); G = gradF(V)
    drift = np.sum(G*b)/f
    qv = 0.0; ito = 0.0
    for Ej in E:
        gj = np.sum(G*Ej); qv += gj**2
        ito += hessF(V, Ej)
    drift_log = drift + 0.5*ito/f - 0.5*qv/f**2
    return drift_log, qv/f**2
