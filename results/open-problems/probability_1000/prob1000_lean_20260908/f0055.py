"""F0055 / Janson Conjecture 18.4, exact check (mpmath, 30 digits).
Z_{k,n} = [t^k] Phi(t)^n.  P(Y_1 = j) = w_j Z_{m-j,n-1}/Z_{m,n};  P(Y(1) >= k) = 1 - Z^{(<k)}_{m,n}/Z_{m,n}.
Bound under test (w_1 > 0, m <= n/4, 1 <= j <= m):  P(Y_1 = j) <= (w_j/w_0) (2m/(gamma n))^j,  gamma = min(1, w_1/w_0)."""
import mpmath as mp
from math import log, factorial
mp.mp.dps = 30
def polypow_trunc(w, n, m):
    """coefficients 0..m of (sum_k w_k t^k)^n"""
    base = [mp.mpf(x) for x in w[:m+1]] + [mp.mpf(0)]*(m+1-len(w[:m+1]))
    def mul(a, b):
        c = [mp.mpf(0)]*(m+1)
        for i, ai in enumerate(a):
            if ai == 0: continue
            for j in range(0, m+1-i):
                if b[j] != 0: c[i+j] += ai*b[j]
        return c
    res = [mp.mpf(1)] + [mp.mpf(0)]*m; cur = base; p = n
    while p:
        if p & 1: res = mul(res, cur)
        p >>= 1
        if p: cur = mul(cur, cur)
    return res
def run(name, w, n, m, ks, general=False):
    Zn = polypow_trunc(w, n, m); Zn1 = polypow_trunc(w, n-1, m)
    gamma = min(1.0, float(w[1]/w[0])) if w[1] > 0 else None
    worst = 0.0
    if gamma:
        for j in range(1, m+1):
            if j >= len(w) or w[j] == 0: continue
            p = w[j]*Zn1[m-j]/Zn[m]; b = (mp.mpf(w[j])/w[0])*(mp.mpf(2*m)/(gamma*n))**j
            worst = max(worst, float(p/b))
    out = []
    for k in ks:
        wk = list(w[:k]) + [0]*(len(w)-k)
        Zk = polypow_trunc(wk, n, m); out.append((k, float(1 - Zk[m]/Zn[m])))
    print(f"{name:16s} n={n:6d} m={m:4d}: max_j P(Y_1=j)/bound = {('%.4f'%worst) if gamma else '  n/a'} ; P(Y(1)>=k): " + ", ".join(f"k={k}:{p:.3g}" for k,p in out), flush=True)
M = 200
fams = [("poisson 1/k!", [mp.mpf(1)/mp.factorial(k) for k in range(M)]),
        ("uniform w=1", [1.0]*M),
        ("geometric 2^-k", [2.0**-k for k in range(M)]),
        ("w=k+1", [float(k+1) for k in range(M)]),
        ("w1=0: 1,0,1,1,..", [1.0, 0.0] + [1.0]*(M-2))]
for name, w in fams:
    for n, m in [(2000, 44), (20000, 141), (100000, 316)]:
        L = int(round(log(n))); run(name, w, n, m, [max(2, L//4), max(2, L//2), L])
