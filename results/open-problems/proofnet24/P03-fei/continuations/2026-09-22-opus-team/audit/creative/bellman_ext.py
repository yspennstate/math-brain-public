# Mixed AND/OR extensions. With fresh variables, D(g') = D(g)/2 + psi(p') where p' = p/2 (AND) or (1+p)/2 (OR).
# M(p) := least defect at bias p such that no finite extension goes negative:
#   M(p) = max(0, 2(M(p/2) - psi(p/2)), 2(M((1+p)/2) - psi((1+p)/2))).
# M_L = depth-L unrolling with leaves Lambda (pure runs to infinity), so Lambda <= M_L <= M.
# H <= 4I on threshold functions forces D(g) >= M(p_g) for every threshold function g.
import numpy as np, random, sys, psutil
psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); psutil.Process().cpu_affinity(list(range(2, psutil.cpu_count())))
LN2 = np.log(2.0)
def eps(p):
    p = np.asarray(p, dtype=np.float64); out = np.zeros_like(p)
    m = p > 0; q = p[m]
    with np.errstate(divide="ignore", invalid="ignore"):
        l2 = np.where(q < 0.5, np.log1p(-2*np.minimum(q, 0.4999999999)), np.where(q > 0.5, np.log(np.maximum(2*q - 1, 1e-300)), 0.0))
        l1 = np.where(q < 1, np.log1p(-np.minimum(q, 1 - 1e-16)), 0.0)
        phi_q2 = np.where(q > 0, -q*q*np.log2(q*q), 0.0)
        out[m] = 4*q*q - phi_q2 + (2*(1-q)**2*l1 - (1-2*q)**2*l2)/LN2
    return out
def psi(u): u = np.asarray(u, dtype=np.float64); return eps(2*np.minimum(u, 1-u))
def E(p):
    p = np.asarray(p, dtype=np.float64); tot = np.zeros_like(p)
    for i in range(70): tot += 2.0**i * eps(p / 2.0**i)
    return tot
def Lam(p): return np.maximum(0.0, np.maximum(-2*E(p), -2*E(1-p)))
def M_L(p, L):
    p = np.asarray(p, dtype=np.float64)
    if L == 0: return Lam(p)
    a, b = p/2, (1+p)/2
    m = M_L(np.concatenate([a, b]), L-1); n = len(p)
    return np.maximum(0.0, np.maximum(2*(m[:n] - psi(a)), 2*(m[n:] - psi(b))))
if __name__ == "__main__":
    grid = np.array([0.5, 0.25, 0.75, 0.125, 0.375, 0.40625, 0.66656494140625, 0.9, 0.99])
    for L in (0, 4, 8, 12):
        print("L=%2d" % L, " ".join("%.4f" % v for v in M_L(grid, L)))
