# Is Lambda(p) = max(0, -2E(p), -2E(1-p)) an inductive lower bound for D = 4I - H on threshold functions?
# For f and a variable i with restrictions f0, f1: D(f) = (D(f0) + D(f1))/2 + step. The induction closes at i if
# Q_i = (Lambda(p0) + Lambda(p1))/2 + step - Lambda(p) >= 0.  Also report D(f) - Lambda(p) itself.
import numpy as np, random, sys, psutil
psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); psutil.Process().cpu_affinity(list(range(2, psutil.cpu_count())))
from math import log2, log1p, log
LN2 = log(2)
def phi(w): return 0.0 if w <= 0 else w*log2(1/w)
def eps(p):
    if p <= 0: return 0.0
    l2 = log1p(-2*p) if p < 0.5 else (log(2*p-1) if p > 0.5 else 0.0)
    l1 = log1p(-p) if p < 1 else 0.0
    return 4*p*p - phi(p*p) + (2*(1-p)**2*l1 - (1-2*p)**2*l2) / LN2
def E(p): return sum(2**i * eps(p / 2**i) for i in range(200))
def Lam(p): return max(0.0, -2*E(p), -2*E(1-p)) if 0 < p < 1 else 0.0
def walsh(F):
    a = F.astype(np.float64).copy(); h = 1
    while h < len(a):
        a = a.reshape(-1, 2*h); a = np.concatenate([a[:, :h]+a[:, h:], a[:, :h]-a[:, h:]], axis=1).reshape(-1); h *= 2
    return a/len(a)
PC = {}
def D_of(f, n):
    if n == 0: return 0.0
    c = walsh(np.where(f, -1, 1)); w = c*c
    if n not in PC: PC[n] = np.array([bin(i).count("1") for i in range(1 << n)])
    nz = w[w > 1e-300]
    return 4*float((PC[n]*w).sum()) + float((nz*np.log2(nz)).sum())
random.seed(int(sys.argv[1])); worstD, worstBest, worstHeavy = (1e9,), (1e9,), (1e9,)
for trial in range(int(sys.argv[2])):
    n = random.randint(2, 12)
    kind = random.choice(["unif", "geom", "heavy", "few", "near_lex", "maj"])
    if kind == "unif": w = [random.randint(1, 30) for _ in range(n)]
    elif kind == "geom": r = random.uniform(0.3, 0.95); w = [max(1, int(1000*r**i)) for i in range(n)]
    elif kind == "heavy": w = [random.randint(1, 5) for _ in range(n-1)] + [random.randint(5, 40)]
    elif kind == "few": w = [random.choice([1, 2, 3]) for _ in range(n)]
    elif kind == "maj": w = [1]*n
    else: w = [2**i + random.randint(-1, 1)*(2**i//3) for i in range(n)]
    X = ((np.arange(1 << n)[:, None] >> np.arange(n)) & 1); s = X @ np.array(w)
    for theta in random.sample(range(0, sum(w)+2), min(5, sum(w)+2)):
        f = s >= theta; p = f.mean()
        if p in (0.0, 1.0): continue
        Df = D_of(f, n); gapD = Df - Lam(p)
        if gapD < worstD[0]: worstD = (gapD, n, kind, w, theta, p, Df)
        Qs = []
        for i in range(n):
            keep = [j for j in range(n) if j != i]
            sub = ((np.arange(1 << (n-1))[:, None] >> np.arange(n-1)) & 1)
            base = sub @ np.array([w[j] for j in keep])
            f0 = base >= theta; f1 = base + w[i] >= theta
            p0, p1 = f0.mean(), f1.mean()
            step = Df - (D_of(f0, n-1) + D_of(f1, n-1))/2
            Qs.append((Lam(p0) + Lam(p1))/2 + step - Lam(p))
        ih = int(np.argmax(w))
        if max(Qs) < worstBest[0]: worstBest = (max(Qs), n, kind, w, theta, p)
        if Qs[ih] < worstHeavy[0]: worstHeavy = (Qs[ih], n, kind, w, theta, p)
print("min D - Lambda(p):", worstD)
print("min over f of max_i Q_i (best variable):", worstBest)
print("min over f of Q at the heaviest variable:", worstHeavy)
