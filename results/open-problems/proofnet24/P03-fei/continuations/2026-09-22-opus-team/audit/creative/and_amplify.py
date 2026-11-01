# AND-run amplification test. For any g and fresh variables, D(AND_l & g) = 2^-l [D(g) + 2 S_l(p_g)],
# S_l(p) = sum_{i<l} 2^i eps(2^-i p), decreasing to E(p) for l >= 1. So H <= 4I on a class closed under
# AND/OR with fresh variables forces  D(g) + 2 min(0, E(p_g)) >= 0  and  D(g) + 2 min(0, E(1 - p_g)) >= 0.
# Threshold functions are closed under both operations, so a violation by an LTF g gives an LTF with H > 4I.
import numpy as np, random, sys, psutil
psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); psutil.Process().cpu_affinity(list(range(2, psutil.cpu_count())))
from math import log2
def phi(w): return 0.0 if w <= 0 else w*log2(1/w)
from math import log1p, log
LN2 = log(2)
def eps(p):
    # -phi((1-p)^2) + phi((1-2p)^2)/2 written with log1p so the O(p) parts cancel without losing digits
    if p <= 0: return 0.0
    if p < 0.5: l2 = log1p(-2*p)
    elif p > 0.5: l2 = log(2*p - 1)
    else: l2 = 0.0
    t = (2*(1-p)**2*log1p(-p) - (1-2*p)**2*l2) / LN2
    return 4*p*p - phi(p*p) + t
def E(p): return sum(2**i * eps(p / 2**i) for i in range(200))
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
print("E(1/2) =", E(0.5), " so a balanced g needs 4I - H >=", -2*min(0, E(0.5)))
random.seed(int(sys.argv[1])); worst = (1e9, None); cnt = 0
for trial in range(int(sys.argv[2])):
    n = random.randint(3, 14)
    kind = random.choice(["unif", "geom", "heavy", "few", "near_lex", "maj"])
    if kind == "unif": w = [random.randint(1, 30) for _ in range(n)]
    elif kind == "geom": r = random.uniform(0.3, 0.95); w = [max(1, int(1000*r**i)) for i in range(n)]
    elif kind == "heavy": w = [random.randint(1, 5) for _ in range(n-1)] + [random.randint(5, 40)]
    elif kind == "few": w = [random.choice([1, 2, 3]) for _ in range(n)]
    elif kind == "maj": w = [1]*n
    else: w = [2**i + random.randint(-1, 1)*(2**i//3) for i in range(n)]
    X = ((np.arange(1 << n)[:, None] >> np.arange(n)) & 1)
    s = X @ np.array(w)
    for theta in random.sample(range(0, sum(w)+2), min(8, sum(w)+2)):
        f = s >= theta; P = f.mean()
        if P in (0.0, 1.0): continue
        H, I = HI(np.where(f, -1, 1), n); D = 4*I - H
        for side, q in (("AND", P), ("OR", 1 - P)):
            val = D + 2*min(0.0, E(q)); cnt += 1
            if val < worst[0]: worst = (val, (side, n, kind, w, theta, P, D, H/I))
print("tests:", cnt, " min of D(g) + 2 min(0, E):", worst)
