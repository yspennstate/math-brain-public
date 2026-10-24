# Test: for a linear threshold function f with P = Pr[f=1], is D(f) = 4I - H >= Dchain(P) := sum_k 2^-k psi(T^k P)?
# Also: for balanced LTFs, is H <= 4(I-1)?
import numpy as np, random, sys, psutil
psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); psutil.Process().cpu_affinity(list(range(2, psutil.cpu_count())))
from math import log2
def phi(w): return 0.0 if w <= 0 else w*log2(1/w)
def eps(p): return 4*p*p - phi(p*p) - phi((1-p)**2) + 0.5*phi((1-2*p)**2)
def psi(u): return eps(2*min(u, 1-u))
def dchain(P):
    s, d = P, 0.0
    for k in range(64):
        if s == 0: break
        d += psi(s) / 2**k; s = (2*s) % 1.0
    return d
def walsh(F):
    a = F.astype(np.float64).copy(); h = 1
    while h < len(a):
        a = a.reshape(-1, 2*h); a = np.concatenate([a[:, :h]+a[:, h:], a[:, :h]-a[:, h:]], axis=1).reshape(-1); h *= 2
    return a/len(a)
PC = {}
def HI(F, n):
    c = walsh(F); w = c*c
    if n not in PC: PC[n] = np.array([bin(i).count("1") for i in range(1 << n)])
    nz = w[w > 1e-300]
    return float(-(nz*np.log2(nz)).sum()), float((PC[n]*w).sum())
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
worst_gap, worst_bal = (1e9, None), (1e9, None)
cnt = 0
for trial in range(int(sys.argv[2]) if len(sys.argv) > 2 else 4000):
    n = random.randint(3, 14)
    kind = random.choice(["unif", "geom", "heavy", "few", "near_lex"])
    if kind == "unif": w = [random.randint(1, 30) for _ in range(n)]
    elif kind == "geom": r = random.uniform(0.3, 0.95); w = [max(1, int(1000*r**i)) for i in range(n)]
    elif kind == "heavy": w = [random.randint(1, 5) for _ in range(n-1)] + [random.randint(5, 40)]
    elif kind == "few": w = [random.choice([1, 2, 3]) for _ in range(n)]
    else: w = [2**i + random.randint(-1, 1)*(2**i//3) for i in range(n)]
    X = ((np.arange(1 << n)[:, None] >> np.arange(n)) & 1)
    s = X @ np.array(w)
    for theta in random.sample(range(0, sum(w)+2), min(6, sum(w)+2)):
        f = s >= theta
        P = f.mean()
        if P in (0.0, 1.0): continue
        F = np.where(f, -1, 1)
        H, I = HI(F, n); D = 4*I - H
        gap = D - dchain(P); cnt += 1
        if gap < worst_gap[0]: worst_gap = (gap, (n, kind, w, theta, P, D, H/I))
        if abs(P - 0.5) < 1e-12:
            b = 4*(I-1) - H
            if b < worst_bal[0]: worst_bal = (b, (n, kind, w, theta, H/(I-1) if I > 1 else None))
print("functions tested:", cnt)
print("min D(f) - Dchain(P):", worst_gap[0], worst_gap[1])
print("min over balanced of 4(I-1) - H:", worst_bal[0], worst_bal[1])
