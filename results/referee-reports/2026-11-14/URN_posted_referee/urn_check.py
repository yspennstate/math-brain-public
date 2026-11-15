# Independent check of the numbers in "On a contractivity question of Neri and Pinto", from the paper's statements only.
import numpy as np
def Rd(d):
    R = np.zeros((d, d)); R[0,0]=5; R[0,1]=1; R[1,0]=5; R[1,2]=1
    R[d-1,d-1]=5; R[d-1,d-2]=1; R[d-2,d-1]=5; R[d-2,d-3]=1
    for i in range(2, d-2): R[i,i-1]=3; R[i,i+1]=3
    return R
def basisH(d):  # orthonormal basis of the sum-zero hyperplane
    M = np.eye(d) - 1.0/d; u, s, vt = np.linalg.svd(M); return u[:, :d-1]
def readings(R, lam):
    d = len(R); A = R - lam*np.eye(d)
    Ld = np.linalg.eigvalsh((A + A.T)/2).max()
    B = basisH(d); S = B.T @ ((A + A.T)/2) @ B; LH = np.linalg.eigvalsh(S).max()
    ks = []
    for k in range(d):
        # max of Q_(k)(w) over w in H with sum_{i != k} w_i^2 = 1; parametrise w by the other coordinates v, w_k = -sum v
        idx = [i for i in range(d) if i != k]
        C = np.zeros((d-1, d)); C[np.arange(d-1), idx] = 1; C[:, k] = -1
        J = np.eye(d); J[k, k] = 0
        M = C @ J @ A.T @ C.T; ks.append(np.linalg.eigvalsh((M + M.T)/2).max())
    ev = np.sort_complex(np.linalg.eigvals(R)); re = sorted(ev.real)
    # gamma: remove one copy of lam
    lst = list(ev); j = int(np.argmin(abs(np.array(lst) - lam))); lst.pop(j); g = max(x.real for x in lst)
    return Ld, LH, min(ks), max(ks), ks, g
for d in range(4, 11):
    Ld, LH, mn, mx, ks, g = readings(Rd(d), 6)
    print("d=%2d Lambda_d=%.5f Lambda_H=%.5f min_k=%.5f max_k=%.5f gamma=%.4f" % (d, Ld, LH, mn, mx, g))
print("3sqrt2-4 =", 3*np.sqrt(2)-4)
R3 = np.array([[0,1,99],[1,99,0],[36,0,64]], float)
Ld, LH, mn, mx, ks, g = readings(R3, 100); print("Ex3: Lambda_d=%.5f Lambda_H=%.5f k-readings=%s gamma=%.4f" % (Ld, LH, np.round(ks, 5), g))
R6 = np.array([[0,1,0,5,0,0],[0,0,0,6,0,0],[1,0,5,0,0,0],[0,0,0,5,1,0],[0,0,5,0,0,1],[0,0,6,0,0,0]], float)
Ld, LH, mn, mx, ks, g = readings(R6, 6); print("Ex6: Lambda_H=%.5f k-readings=%s gamma=%.4f gamma/lam=%.4f" % (LH, np.round(ks, 4), g, g/6))
print("Ex6 charpoly", np.round(np.poly(R6), 6), " expected", np.round(np.polymul(np.polymul([1,-6],[1,1,1]),[1,-5,5,6]), 6))
for w, k in [((0,-1,2,-2,0,1), None), ((-1,0,1,-1,0,1), 0), ((0,-1,1,-1,0,1), 1), ((0,-1,3,-2,0,0), 2), ((0,0,-2,3,0,-1), 3), ((-1,0,1,-1,1,0), 4), ((-1,0,1,-1,0,1), 5)]:
    w = np.array(w, float); r = w @ R6 - 6*w; terms = w*r
    print("  Ex6 w=%s sum=%g Q_(%s)=%g" % (w.astype(int), w.sum(), k, terms.sum() - (0 if k is None else terms[k])))
# Lyapunov construction with A = 0.999(lam - gamma) on R^(5): check the adapted inequality on random w in H
from scipy.linalg import solve_continuous_lyapunov
for R, lam in [(Rd(4), 6), (Rd(5), 6), (Rd(8), 6), (R3, 100), (R6, 6)]:
    d = len(R); g = readings(R, lam)[5]; A = 0.999*(lam - g)
    C = np.hstack([np.eye(d-1), -np.ones((d-1, 1))])
    # K: (vK)C = vC(R - lam I) + A vC  ->  K = C(R - lam I + A I) restricted (first d-1 columns of vC(...) determine v')
    M = C @ (R - lam*np.eye(d) + A*np.eye(d)); K = M[:, :d-1]
    assert np.allclose(K @ C, M)
    G = solve_continuous_lyapunov(K, -np.eye(d-1))   # K G + G K^T = -I
    P = np.zeros((d, d)); P[:d-1, :d-1] = G
    rng = np.random.default_rng(1); worst = -1e9
    for _ in range(20000):
        v = rng.standard_normal(d-1); w = v @ C
        worst = max(worst, (w @ (R - lam*np.eye(d))) @ P @ w + A * (w @ P @ w))
    print("Lyapunov d=%d lam=%d gamma=%.4f A=%.4f max <L(w)+Aw,w>_P over 20000 w = %.3e (should be <= 0)" % (d, lam, g, A, worst))
