"""Family (d), non-Gaussian multi-scale structure in the hub setting: hub row w and square direction v with entries at
geometrically many scales (w_j ~ r^j, largest entry kept below sqrt(c) so that no 2x2 minor with the hub is a pivot),
uniform laws, E1 exact + window.  Also a hierarchical hub (hub of hubs): root hub coupled to K sub-hubs, each sub-hub
coupled to its own spread leaf direction, plus lam V^2.  And the exact Gaussian value of two orthogonal hubs for
comparison with the bathtub bound 2 sqrt 2 of Proposition S2."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, time
from scipy.integrate import quad
from scipy.stats import norm
from lib import *
rng = np.random.default_rng(77); fh = U(); t0 = time.time()
sv = np.linspace(-0.05, 0.1, 76)


def star_val(w, v, lam=1.0, N=400000):
    n1 = len(w); tot = np.zeros(len(sv)); tot2 = np.zeros(len(sv)); win = np.zeros(len(sv)); done = 0
    while done < N:
        m = min(40000, N - done)
        Xp = rng.uniform(-0.5, 0.5, (m, n1)); T = Xp @ w; V = Xp @ v; R = lam*V*V
        e = hub_cond_values(0.0, T, R, sv, fh); tot += e.sum(0); tot2 += (e*e).sum(0)
        win += hub_window_values(0.0, T, R, sv, fh, 0.002).sum(0)/0.004; done += m
    mean = tot/N; se = np.sqrt(np.maximum(tot2/N - mean**2, 0)/N); win /= N
    j = int(np.argmax(win))
    return mean[j], se[j], win[j], sv[j]


for n1, r in ((60, 0.97), (60, 0.93), (120, 0.97), (200, 0.985)):
    for phase in (0, 1):
        idx = np.arange(n1)
        w = r**idx; w *= rng.choice([-1, 1], n1)
        if phase == 0:
            v = r**idx[::-1]*rng.choice([-1, 1], n1)   # v concentrated where w is small (opposite scales)
        else:
            v = (r**idx)*rng.choice([-1, 1], n1)        # same scales, independent signs
        v -= (v @ w)/(w @ w)*w
        w /= np.linalg.norm(w); v /= np.linalg.norm(v)
        m1, se, wv, s = star_val(w, v)
        print(f"multi-scale n1={n1} r={r} {'opposite' if phase == 0 else 'same'} scales: max |w_j|={np.abs(w).max():.3f} "
              f"max|v_j|={np.abs(v).max():.3f}  E1 {m1:.4f}+-{se:.4f}  window {wv:.4f} at s={s:+.3f}  t={time.time()-t0:.0f}", flush=True)

# hierarchical hub: Q = 2 X0 S/sqrt(K) + 2 rho sum_k X_k L_k + lam V^2,  S = sum X_k, leaves Gaussian-like (spread)
for K in (2, 3, 6):
    for rho in (0.3, 1.0):
        n1 = 40*K + 40
        B, _ = np.linalg.qr(rng.normal(size=(n1, K+1))); Ws = B[:, :K]; v = B[:, K]
        n = 1 + K + n1
        A = np.zeros((n, n))
        for k in range(1, K+1):
            A[0, k] = A[k, 0] = 1/np.sqrt(K)
            A[k, 1+K:] = rho*Ws[:, k-1]; A[1+K:, k] = rho*Ws[:, k-1]
        A[1+K:, 1+K:] = np.outer(v, v)
        m3 = mu3(A)
        # condition on the leaves and on X_1..X_K, integrate X0 exactly (it is a hub of the sub-hubs)
        N = 200000; tot = np.zeros(len(sv)); win = np.zeros(len(sv)); done = 0
        svk = np.linspace(-0.3, 0.3, 61)
        tot = np.zeros(len(svk)); win = np.zeros(len(svk))
        while done < N:
            m = min(20000, N - done)
            Xs = rng.uniform(-0.5, 0.5, (m, K)); Xp = rng.uniform(-0.5, 0.5, (m, n1))
            Lk = Xp @ Ws; V = Xp @ v
            T = Xs.sum(1)/np.sqrt(K)
            R = 2*rho*(Xs*Lk).sum(1) + V*V
            win += hub_window_values(0.0, T, R, svk, fh, 0.003).sum(0)/0.006; done += m
        win /= N; j = int(np.argmax(win))
        print(f"hub of hubs K={K} rho={rho}: mu3={m3:.3f} eig top={np.round(np.sort(np.abs(np.linalg.eigvalsh(A)))[::-1][:4],3)} "
              f"window max {win[j]:.4f} at s={svk[j]:+.3f}  F={m3*win[j]:.4f}  t={time.time()-t0:.0f}", flush=True)

# exact Gaussian value for two orthogonal hubs with nothing else, uniform hub laws, s = 0: E[1/(2 |T|_inf)], T ~ N(0, I/12)
sig = np.sqrt(1/12)
f = lambda r: 4*norm.pdf(r)*(2*norm.cdf(r) - 1)/r
E = quad(f, 0, np.inf)[0]
print(f"two orthogonal hubs, Gaussian leaves, s = 0: p = E[1/(2|T|_inf)] = {E/(2*sig):.4f}  (bathtub bound 2 sqrt2 = {2*np.sqrt(2):.4f})", flush=True)
