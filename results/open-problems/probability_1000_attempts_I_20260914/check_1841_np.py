# Theorem B check in double precision via probability-space convolutions (all terms positive, no cancellation).
import numpy as np, math, sys
def run(J, lam_minus_nu, cliff):
    def g(j):
        v=3*j
        if cliff and j>=J: v=max(v,6*J+4)
        return v
    maxk = 2**(J+9)
    w = np.array([1.0]+[math.exp(-g(int(math.floor(math.log2(k))))) for k in range(1,maxk+1)])
    Phi = w.sum(); pi = w/Phi; nu = (np.arange(len(w))*pi).sum()
    B = 2**(J-1); K = 3*B; n = int(math.ceil(K/lam_minus_nu)); m = K + int(math.floor(nu*n))
    assert m < maxk
    def power(p, N, L):
        # p^{*N} truncated to degree L
        res = np.zeros(L+1); res[0]=1.0; base = p[:L+1].copy()
        while N:
            if N&1: res = np.convolve(res, base)[:L+1]
            N >>= 1
            if N: base = np.convolve(base, base)[:L+1]
        return res
    total = power(pi, n, m)[m]
    for y in [B//4, B//2, B]:
        py = pi.copy(); py[y:] = 0.0
        W0 = power(py, n, m)[m]
        Pn1 = power(py, n-1, m)
        W1 = n*sum(pi[k]*Pn1[m-k] for k in range(y, m+1))
        print(f"J={J} cliff={cliff} lam-nu={lam_minus_nu} n={n} m={m} nu={nu:.4f} K={K} y={y}: P(Y2>=y)={1-(W0+W1)/total:.4g}  [P0={W0/total:.3g} P1={W1/total:.3g} Pm={total:.3g}]")
for J in [7,8,9,10]:
    for cl in [True, False]:
        run(J, float(sys.argv[1]), cl)
