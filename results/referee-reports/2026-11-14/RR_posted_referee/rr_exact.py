# Independent check of "The logarithmic factor in the tuned constant-step rate of random reshuffling",
# written from the paper's statements only (not from code/rr_check.py). L = s = D = 1.
import sys, itertools, math
import numpy as np
from scipy.optimize import minimize_scalar

def epoch_moments(n, n1, g):
    """E B and E B^2 for one epoch by a backward DP over (stiff seen, flat seen); B = sum c_t (r^q_t - 1)."""
    n2 = n - n1; lr = math.log1p(-g) if g < 1 else -np.inf
    em1 = [math.expm1(q*lr) if g < 1 else (0.0 if q == 0 else -1.0) for q in range(n1+1)]  # r^q - 1
    cs, cf = g, -g*n1/n2
    P = np.zeros((n1+1, n2+1)); M1 = np.zeros_like(P); M2 = np.zeros_like(P); P[0, 0] = 1.0
    for tot in range(n):            # states with j+i = tot
        for j in range(max(0, tot-n2), min(n1, tot)+1):
            i = tot - j; p = P[j, i]
            if p == 0: continue
            left = n - tot; ps = (n1-j)/left; pf = (n2-i)/left
            for (dj, di, pr, c) in ((1, 0, ps, cs), (0, 1, pf, cf)):
                if pr == 0: continue
                d = c*em1[j]                       # q_t = number of stiff steps after t = j
                P[j+dj, i+di] += p*pr
                M1[j+dj, i+di] += pr*(M1[j, i] + p*d)
                M2[j+dj, i+di] += pr*(M2[j, i] + 2*d*M1[j, i] + p*d*d)
    return M1[n1, n2], M2[n1, n2]

def brute(n, n1, g):
    r = 1-g; n2 = n-n1; vals = []
    for S in itertools.combinations(range(n), n1):
        S = set(S); B = 0.0
        for t in range(n):
            q = sum(1 for u in S if u > t)
            B += (g if t in S else -g*n1/n2)*r**q
        vals.append(B)
    v = np.array(vals); return v.mean(), (v**2).mean()

def phi(r, n1):
    k = np.arange(n1); w = r**k
    return 2/(n1+1)*np.sum((k+1)*w)/np.sum(w)

def err(n, n1, K, g, x0=1.0):
    EB, EB2 = epoch_moments(n, n1, g); VB = EB2 - EB**2
    A = (1-g)**n1; AK = A**K
    m = EB/(-math.expm1(n1*math.log1p(-g))) if g < 1 else EB
    EX = AK*x0 + (1-AK)*m
    VX = VB*(-math.expm1(2*K*n1*math.log1p(-g)))/(-math.expm1(2*n1*math.log1p(-g))) if g < 1 else VB
    mu = n1/n
    return mu/2*(EX**2 + VX), EX, VX, VB, m

print("== DP vs brute force over all arrangements")
for (n, n1, g) in [(8, 3, 0.3), (9, 4, 0.9), (7, 1, 0.5), (10, 5, 1.0), (10, 2, 0.01)]:
    a = epoch_moments(n, n1, g); b = brute(n, n1, g)
    print(n, n1, g, "EB %.15e %.15e  EB2 %.15e %.15e" % (a[0], b[0], a[1], b[1]))
print("== Monte Carlo of RR itself, n=12 n1=3 g=0.2 K=5 x0=1 (4e5 runs)")
rng = np.random.default_rng(1); n, n1, g, K = 12, 3, 0.2, 5; R = 400000
x = np.ones(R)
for k in range(K):
    perm = np.argsort(rng.random((R, n)), axis=1) < n1   # True = stiff
    for t in range(n):
        st = perm[:, t]; x = np.where(st, (1-g)*x + g, x - g*n1/(n-n1))
e, EX, VX, VB, m = err(n, n1, K, g)
print("MC E X %.5f +- %.5f exact %.5f | MC E X^2 %.6f exact %.6f" % (x.mean(), x.std()/math.sqrt(R), EX, (x**2).mean(), EX**2+VX))

print("== Lemma mean: phi bounds over n1<=200, r grid; stationary mean vs (g/2)phi")
worst_up = -1; worst_lo = 1e9
for n1 in range(1, 201):
    for r in np.linspace(0, 1, 401)[:-1]:
        p = phi(r, n1); worst_up = max(worst_up, p-1); worst_lo = min(worst_lo, p-max(r**(n1-1), 2/(n1+1)))
print("max(phi-1) = %.3e (must be <=0), min(phi - lower) = %.3e (must be >=0)" % (worst_up, worst_lo))
rel = 0
for (n, n1) in [(40, 1), (100, 10), (100, 50), (1000, 100), (13, 6)]:
    for g in [1e-4, 1e-2, 0.1, 0.5, 0.99]:
        m = err(n, n1, 10, g)[4]; rel = max(rel, abs(m/(g/2*phi(1-g, n1)) - 1))
print("max rel diff stationary mean vs (g/2)phi: %.2e" % rel)

print("== Lemma var: exact Var B against the bound and against the first-order term")
viol = 0; ratios = []; ratios_all = []
for (n, n1) in [(4, 1), (40, 1), (20, 5), (100, 10), (100, 50), (1000, 100), (500, 250), (9, 4)]:
    n2 = n-n1
    for g in np.geomspace(1e-5, 1, 60):
        _, _, _, VB, _ = err(n, n1, 2, g)
        first = g**4*n1**3*(n+1)/(12*n2); bound = g**4*(math.sqrt(n1**3*(n+1)/(12*n2)) + g*n1**3)**2
        if VB > bound*(1+1e-9): viol += 1
        ratios_all.append(VB/first)
        if g*n1 <= 0.1: ratios.append(VB/first)
print("violations of Lemma var: %d; Var/first for g*n1<=0.1: %.4f .. %.4f" % (viol, min(ratios), max(ratios)))

print("== The rate")
for (n, n1) in [(40, 1), (100, 10), (100, 50), (1000, 100)]:
    for K in [1000, 10000]:
        mu = n1/n; T = n*K; Lam = math.log(mu*T); unit = Lam**2/(8*mu*T**2)
        f = lambda lg: err(n, n1, K, math.exp(lg))[0]
        grid = np.linspace(math.log(1e-3*Lam/(mu*T)), 0, 400); vals = [f(v) for v in grid]
        i = int(np.argmin(vals)); lo = grid[max(i-1, 0)]; hi = grid[min(i+1, len(grid)-1)]
        res = minimize_scalar(f, bounds=(lo, hi), method="bounded", options={"xatol": 1e-12})
        gmin = math.exp(res.x); emin = res.fun
        gb = Lam/(mu*T); eb = err(n, n1, K, gb)[0]
        bnd = 1/(2*mu*T**2)*((1+Lam/2)**2 + Lam**3*n1/K*(0.5+Lam*math.sqrt(n1)/K)**2)
        lowa = (Lam-math.log(Lam))**2/(512*mu*T**2); conda = K >= n1*(Lam-math.log(Lam))/2
        fm = lambda lg: err(n, n1, K, math.exp(lg), x0=-1.0)[0]
        vm = [fm(v) for v in grid]; j = int(np.argmin(vm))
        rm = minimize_scalar(fm, bounds=(grid[max(j-1, 0)], grid[min(j+1, len(grid)-1)]), method="bounded", options={"xatol": 1e-12})
        print("(%d,%d) K=%d Lam=%.3f min/unit=%.4f at g*mu*T/Lam=%.4f | at tuned step err/bound=%.4f | min/lower(a)=%.1f (a applies: %s) | x0=-D min/unit=%.3e"
              % (n, n1, K, Lam, emin/unit, gmin*mu*T/Lam, eb/bnd, emin/lowa, conda, rm.fun/unit))
sys.stdout.flush()
