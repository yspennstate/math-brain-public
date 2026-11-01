try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
from itertools import combinations
from scipy import integrate, optimize

np.random.seed(1)
print("=== N1: Lemma 1, int |g^|^p <= 4 pi / sqrt p (also twisted) ===", flush=True)
# f = indicator of a union of intervals of total length 1 (density 1); g = e^{i s x^2} f
def ft(intervals, s, Xi=300.0, nxi=30001, nx=1201):
    xi = np.linspace(-Xi, Xi, nxi)
    tot = np.zeros_like(xi, dtype=complex)
    for (a, b) in intervals:
        x = np.linspace(a, b, nx)
        w = np.full(nx, (b - a) / (nx - 1)); w[0] *= 0.5; w[-1] *= 0.5
        g = np.exp(1j * s * x**2) * w
        for k in range(0, nxi, 3000):
            tot[k:k+3000] += np.exp(1j * np.outer(xi[k:k+3000], x)) @ g
    return xi, np.abs(tot)
laws = {
    "uniform": [(-0.5, 0.5)],
    "3 intervals spread": [(0.0, 0.3), (5.0, 5.4), (-17.0, -16.7)],
    "10 small intervals": [(3.0*k, 3.0*k + 0.1) for k in range(10)],
}
for name, iv in laws.items():
    for s in [0.0, 3.0]:
        xi, a = ft(iv, s)
        for p in [2.0, 2.5, 3.0, 4.5, 7.0]:
            v = a**p
            I = np.trapezoid(v, xi)
            m = len(xi) // 20
            tail = 2 * np.mean(v[-m:]) * xi[-1] / (p - 1)
            print(f"  {name:20s} s={s:4.1f} p={p:4.1f}: int|g^|^p = {I:8.4f} (+tail~{tail:.1e})  bound 4pi/sqrt p = {4*np.pi/np.sqrt(p):7.4f}", flush=True)

print("=== N2: Theorem D determinant / AM-GM inequality, including beta_j = 1 ===", flush=True)
def vol_marginals(M):
    nI, nJ = M.shape
    Z = 0.0; al = np.zeros(nI); be = np.zeros(nJ); W = []
    for S in combinations(range(nI), 3):
        for T in combinations(range(nJ), 3):
            d2 = np.linalg.det(M[np.ix_(S, T)])**2
            Z += d2; W.append((S, T, d2))
            for i in S: al[i] += d2
            for j in T: be[j] += d2
    return Z, al / Z, be / Z, W
def logratio(M, Z, al, be, logd, loge):
    d = np.exp(logd); e = np.exp(loge)
    mask = be < 1 - 1e-12
    e = np.where(mask, e, 0.0)
    Mat = np.diag(e) + M.T @ np.diag(d) @ M
    sign, ld = np.linalg.slogdet(Mat)
    num = np.log(Z) + np.sum(al * logd) + np.sum(np.where(mask, (1 - be) * loge, 0.0))
    return num - ld
worst = -np.inf
for trial in range(30):
    nI = np.random.randint(4, 7); nJ = np.random.randint(3, 6)
    M = np.random.randn(nI, nJ)
    if trial % 3 == 0:
        M[0] *= 10.0   # a heavy row
    Z, al, be, W = vol_marginals(M)
    # marginal formula check
    U, sv, Vt = np.linalg.svd(M, full_matrices=False)
    s2 = sv**2
    def e_k(x, k):
        return sum(np.prod([x[i] for i in c]) for c in combinations(range(len(x)), k))
    e3 = e_k(s2, 3)
    pm = np.array([s2[m] * e_k(np.delete(s2, m), 2) / e3 for m in range(len(s2))])
    al_formula = (U**2) @ pm
    err = np.max(np.abs(al_formula - al))
    # maximise log ratio over (log d, log e)
    f = lambda z: -logratio(M, Z, al, be, z[:nI], z[nI:])
    best = -np.inf
    for rep in range(6):
        z0 = np.random.randn(nI + nJ) * 2
        res = optimize.minimize(f, z0, method="BFGS")
        best = max(best, -res.fun)
    worst = max(worst, best)
    if trial < 8 or best > -1e-3:
        print(f"  trial {trial}: {nI}x{nJ} Z={Z:9.3e} max alpha={al.max():.3f} #beta=1: {int(np.sum(be>1-1e-12))} "
              f"marginal-formula err={err:.1e}  sup log(ratio) found = {best:+.4f} (must be <= 0)", flush=True)
print(f"  worst sup log ratio over all trials: {worst:+.5f}", flush=True)

print("=== N3: constants of Theorem 2.1 and Lemma 1.6/C1 ===", flush=True)
c0 = 6.2 + np.log(16) + np.exp(-1)
print(f"  6.2 + log16 + 1/e = {c0:.5f} (file uses 9.34)", flush=True)
for c in [9.34, c0]:
    g = lambda v: min(1.0, 2 * v**-2 * (c + 2 * max(np.log(v), 0.0)))
    val = integrate.quad(g, 0, 50, limit=200, points=[1, 5])[0] + integrate.quad(g, 50, np.inf)[0]
    print(f"  int_0^inf min(1, 2v^-2({c:.4f} + 2 log_+ v)) dv = {val:.5f}; /sqrt(0.3) = {val/np.sqrt(0.3):.4f}", flush=True)
D = 0.365
print(f"  route (ii): D^-1/2 (5.2 + log(16 sqrt D) + 2 log(2 sqrt 2) + 2) at D=0.365: {(5.2+np.log(16*np.sqrt(D))+2*np.log(2*np.sqrt(2))+2)/np.sqrt(D):.4f}", flush=True)
# C1 constant: sup over K>=1 of int min(1, K v^-2 (1 + 2 log_+ v)) dv / sqrt(K(1+log K))
worstc1 = 0
for K in np.exp(np.linspace(0, 12, 200)):
    g = lambda v: min(1.0, K * v**-2 * (1 + 2 * max(np.log(v), 0.0)))
    v0 = optimize.brentq(lambda v: K * v**-2 * (1 + 2*np.log(v)) - 1, 1.0, 1e8)
    val = v0 + integrate.quad(lambda v: K * v**-2 * (1 + 2*np.log(v)), v0, np.inf)[0]
    worstc1 = max(worstc1, val / np.sqrt(K * (1 + np.log(K))))
print(f"  sup_K [int min(1,K v^-2(1+2log_+ v))] / sqrt(K(1+log K)) = {worstc1:.4f} (claimed <= 8)", flush=True)
# 49.6: sup_u min(u^-1/2, (2/sqrt D) u^-1/2 u (6.2 + log_+(16 sqrt D / u))) * D^{1/4}
Dv = 1.0
us = np.exp(np.linspace(-20, 20, 20001))
vals = np.minimum(us**-0.5, 2 * np.sqrt(us) / np.sqrt(Dv) * (6.2 + np.maximum(np.log(16*np.sqrt(Dv)/us), 0)))
print(f"  alpha_1 bound for indefinite 2x2 (D=1): {vals.max():.3f} (claimed 49.6)", flush=True)
# level-2 via 2x2
for Dv in [1e-3, 0.1, 1.0, 10.0, 1e3]:
    print(f"   alpha_2 via 2x2 at D={Dv:g}: 2(6.2+log16+0.5log_+D)/sqrt D * sqrt(min(D,1)) = {2*(6.2+np.log(16)+0.5*max(np.log(Dv),0))/np.sqrt(Dv)*np.sqrt(min(Dv,1)):.3f} (x c^-1/2, claim <= 19)", flush=True)
print(f"  8 sqrt(283) = {8*np.sqrt(283):.3f}, 1 + log 283 = {1+np.log(283):.4f}", flush=True)

print("=== N4: Theorem 5.2 necessity: density of 4(U^2-V^2) vs (1/4) log(1/|z|) ===", flush=True)
def p_UV(z):  # density of U^2 - V^2, U,V uniform[-1/2,1/2]
    z = abs(z)
    if z >= 0.25: return 0.0
    return 2 * np.log((np.sqrt(0.25 - z) + 0.5) / np.sqrt(z))
# MC check of the formula
N = 4_000_000
U = np.random.rand(N) - 0.5; V = np.random.rand(N) - 0.5
Wv = U**2 - V**2
for z in [0.001, 0.01, 0.05, 0.1]:
    h = 0.0005
    mc = np.mean(np.abs(Wv - z) < h) / (2 * h)
    print(f"   z={z}: MC {mc:.4f} formula {p_UV(z):.4f}", flush=True)
mn = min(0.25 * p_UV(z / 4) - 0.25 * np.log(1 / z) for z in np.linspace(1e-6, 0.5, 20000))
print(f"  min over 0<z<=1/2 of [p_4(U2-V2)(z) - (1/4)log(1/z)] = {mn:.4f} (must be >= 0)", flush=True)

print("=== N5: Prop 4.2 matrix Chernoff constant and simulation ===", flush=True)
eps = 1/50
print(f"  3 exp(-0.0767/eps) = {3*np.exp(-0.0767/eps):.4f}; exact 3*(e^-.5/sqrt(.5))^(1/(2eps)) = {3*(np.exp(-0.5)/np.sqrt(0.5))**(1/(2*eps)):.4f}", flush=True)
n = 200
Rm, _ = np.linalg.qr(np.random.randn(n, 3))
lev = np.sum(Rm**2, 1)
print(f"  random frame n={n}: max leverage {lev.max():.4f}", flush=True)
bad = 0; T = 2000; maxal = 0
for tr in range(T):
    mask = np.random.rand(n) < 0.5
    GI = Rm[mask].T @ Rm[mask]; GJ = Rm[~mask].T @ Rm[~mask]
    if min(np.linalg.eigvalsh(GI).min(), np.linalg.eigvalsh(GJ).min()) < 0.25: bad += 1
print(f"  failure frequency (lambda_min < 1/4 on I or J): {bad/T:.4f}", flush=True)
