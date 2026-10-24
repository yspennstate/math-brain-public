# Independent check (written separately from F5's code) of F5 Lemma 3 and Theorem 1 on linear threshold functions.
# Lemma 3: sum_{T not i} fhat(T+i)^2 ln(N_i/(|T cap U_i|+1)) <= L1 * Inf_i, L1 = 2 ln(3 sqrt(3/pi)) + 2.
import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import numpy as np, math
L1 = 2*math.log(3*math.sqrt(3/math.pi)) + 2
C_THM = 14.2141880860
def walsh(t):
    a = t.astype(np.float64).copy(); h = 1
    while h < len(a):
        b = a.reshape(-1, 2*h); x = b[:, :h].copy(); y = b[:, h:].copy(); b[:, :h] = x+y; b[:, h:] = x-y; h *= 2
    return a/len(t)
def ltf(w, theta):
    n = len(w); N = 1 << n
    X = 1 - 2*((np.arange(N)[:, None] >> np.arange(n)) & 1)     # x_i = +1 if bit 0, -1 if bit 1
    s = X @ w - theta
    return np.where(s > 0, 1, -1), n
def check(w, theta):
    f, n = ltf(np.asarray(w, float), theta); N = 1 << n
    fh = walsh(f); p = fh*fh
    pc = np.array([bin(s).count('1') for s in range(N)])
    I = float((p*pc).sum()); nz = p > 0
    H = float(-(p[nz]*np.log2(p[nz])).sum())
    aw = np.abs(np.asarray(w, float)); worst = 0.0
    for i in range(n):
        U = [j for j in range(n) if j != i and aw[j] >= aw[i]]; Ni = len(U)+1
        Umask = sum(1 << j for j in U)
        T = np.arange(N); sel = (T >> i) & 1 == 0
        wts = p[T[sel] | (1 << i)]
        Inf = wts.sum()
        if Inf <= 1e-15: continue
        k = np.array([bin(t & Umask).count('1') for t in T[sel]])
        lhs = float((wts*np.log(Ni/(k+1))).sum())
        worst = max(worst, lhs/(L1*Inf))
    return H, I, worst
rng = np.random.default_rng(20260923)
worst_l3 = 0.0; worst_thm = 0.0; cnt = 0
fams = []
for n in (8, 10, 12, 14):
    for _ in range(30):
        fams.append((rng.normal(size=n), rng.normal()*math.sqrt(n)*0.5))
        fams.append((rng.exponential(size=n)**3, rng.normal()))
        fams.append((2.0**np.arange(n) * rng.uniform(0.9, 1.1, n), rng.uniform(-1, 1)*2**n))
    fams.append((np.ones(n), 0.5)); fams.append((np.arange(1, n+1)**-0.5, 0.0)); fams.append((np.r_[n*1.0, np.ones(n-1)], 1.0))
for w, th in fams:
    H, I, wl3 = check(w, th)
    if I <= 1e-12: continue
    cnt += 1
    worst_l3 = max(worst_l3, wl3); worst_thm = max(worst_thm, H/(C_THM*I))
print(f"LTFs checked: {cnt}; worst Lemma-3 ratio lhs/(L1*Inf_i) = {worst_l3:.4f}; worst H/(14.2142 I) = {worst_thm:.4f}; L1 = {L1:.10f}")
