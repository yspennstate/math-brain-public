try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, sys
# Hub + L^2 + leakage:  Q = 2k S1 Z + p S1^2 + s S2^2 + m0 Z^2,  Z = sqrt(l) Xh + eps W,  eps^2 = 1 - l
# (S1,S2,W) orthonormal projections of X_L (n light coords). Fibre estimator in X_h:
# given X_L, Q = a x^2 + b x + c with a = m0 l, b = 2 sqrt(l)(k S1 + m0 eps W), c = rest.
# p_Q(y) = E sum_{roots} f_h(x)/|2 a x + b|.
rng = np.random.default_rng(1)
def frame(n):
    G = rng.standard_normal((n,3)); Qm,_ = np.linalg.qr(G); return Qm
def sample_law(kind, size):
    if kind == 'unif':
        return rng.random(size) - 0.5
    if kind == 'comb':   # uniform on 8 teeth of width 1/8 spread over [0,40)
        t = rng.integers(0,8,size); return 5.0*t + rng.random(size)/8.0
def fh(x, kind):
    if kind == 'unif':
        return ((x >= -0.5) & (x < 0.5)).astype(float)
    if kind == 'comb':
        t = np.floor(x/5.0); r = x - 5.0*t
        return ((t >= 0) & (t < 8) & (r < 1/8.0)).astype(float)
def density(y, n, eps, k, p, s, m0, lawL, lawh, N=400000):
    l = 1 - eps**2
    F = frame(n); s1, s2, w = F[:,0], F[:,1], F[:,2]
    tot = np.zeros_like(y)
    B = 50000
    for _ in range(N//B):
        XL = sample_law(lawL, (B, n))
        S1, S2, W = XL@s1, XL@s2, XL@w
        # centre laws: subtract mean of the law so that S's are near 0 (linear terms matter only via shifts)
        a = m0*l; b = 2*np.sqrt(l)*(k*S1 + m0*eps*W)
        c = 2*k*S1*eps*W + p*S1**2 + s*S2**2 + m0*eps**2*W**2
        for j, yy in enumerate(y):
            if abs(a) < 1e-14:
                x = (yy - c)/b; tot[j] += np.sum(fh(x, lawh)/np.abs(b))
            else:
                disc = b*b - 4*a*(c - yy)
                ok = disc > 0; sq = np.sqrt(np.where(ok, disc, 0))
                for sg in (1, -1):
                    x = (-b + sg*sq)/(2*a)
                    tot[j] += np.sum(np.where(ok, fh(x, lawh)/np.maximum(np.abs(2*a*x + b),1e-300), 0))
    return tot/((N//B)*B)
if __name__ == '__main__':
    y = np.linspace(-1.5, 1.5, 61)
    for (k,p,s,m0) in [(1.0,1.0,1.0,0.0),(1.0,3.0,1.0,0.0),(1.0,1.0,-1.0,0.0),(1.0,3.0,-1.0,0.2)]:
        for eps in [0.0, 0.05, 0.2, 0.5]:
            for lawL, lawh in [('unif','unif'), ('unif','comb')]:
                d = density(y, 40, eps, k, p, s, m0, lawL, lawh, N=200000)
                j = np.argmax(d)
                print(f"k={k} p={p} s={s} m0={m0} eps={eps} L={lawL} h={lawh}: max {d[j]:.3f} at y={y[j]:.2f}; d(-0.5)={d[20]:.3f} d(0)={d[30]:.3f} d(0.5)={d[40]:.3f}", flush=True)
