# Check the chain recursion D' = D/2 + psi(p') and D(P) = sum_k 2^-k psi(T^k P) against exact Walsh sums.
import numpy as np, random
from math import log2
def phi(w): return 0.0 if w <= 0 else w*log2(1/w)
def eps(p): return 4*p*p - phi(p*p) - phi((1-p)**2) + 0.5*phi((1-2*p)**2)
def psi(u): return eps(2*min(u, 1-u))
def walsh(F):
    a = F.astype(np.float64).copy(); h = 1
    while h < len(a):
        a = a.reshape(-1, 2*h); a = np.concatenate([a[:, :h]+a[:, h:], a[:, :h]-a[:, h:]], axis=1).reshape(-1); h *= 2
    return a/len(a)
def HI(F, n):
    c = walsh(F); w = c*c; N = 1 << n
    pc = np.array([bin(i).count("1") for i in range(N)])
    return sum(phi(x) for x in w), float((pc*w).sum())
random.seed(1); worst = 0.0
for trial in range(300):
    m = random.randint(1, 14)
    gates = [random.choice("AO") for _ in range(m-1)]
    n = m; N = 1 << n
    x = ((np.arange(N)[:, None] >> np.arange(n)) & 1).astype(bool)
    f = x[:, 0].copy()                      # dictator on variable 0
    for j, g in enumerate(gates, start=1):
        f = (x[:, j] & f) if g == "A" else (x[:, j] | f)
    F = np.where(f, -1, 1)
    H, I = HI(F, n); D_exact = 4*I - H
    P = f.mean()
    D_tak, s = 0.0, P
    for k in range(m):
        D_tak += psi(s) / 2**k; s = (2*s) % 1.0
    worst = max(worst, abs(D_exact - D_tak))
    if trial < 3: print(m, "".join(gates), "P", P, "D exact", round(D_exact, 12), "Takagi", round(D_tak, 12), "H/I", round(H/I, 6))
print("300 random chains, max |D_exact - D_Takagi| =", worst)
