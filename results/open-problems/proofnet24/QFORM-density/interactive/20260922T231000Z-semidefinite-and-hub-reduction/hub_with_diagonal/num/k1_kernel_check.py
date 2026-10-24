try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Check Lemma 2.2: J_a(t,sigma) = sup over densities f<=1 of int f(x) 1{|ax+t|<1} |sigma - a x^2 - 2 x t|^{-1/2} dx
# is <= 9.05 |t^2 + a sigma|^{-1/4}; also check kernel mass identity G_a(sigma) (piece 1, (1.5)(iii)) bound.
import numpy as np
rng = np.random.default_rng(1)

def bathtub(h, dx):
    # sup of int f h over 0<=f<=1, int f <= 1: integrate the largest values of h over total measure 1
    hs = np.sort(h)[::-1]
    k = int(round(1.0/dx))
    return hs[:k].sum()*dx

worst = 0.0; worstG = 0.0
for trial in range(400):
    a = rng.choice([-1,1])*10**rng.uniform(-3, 0)
    t = rng.normal()*10**rng.uniform(-2, 0.5)
    Delta = rng.choice([-1,1])*10**rng.uniform(-6, 1)
    sigma = (Delta - t*t)/a
    # grid over x: slab |a x + t| < 1 -> x in ((-1-t)/a, (1-t)/a); restrict further to a window where h is non-negligible
    lo, hi = sorted([(-1-t)/a, (1-t)/a])
    # the singular points: roots of sigma - a x^2 - 2 x t = 0 -> x = (-t +- sqrt(Delta))/a
    pts = []
    if Delta > 0:
        pts = [(-t + np.sqrt(Delta))/a, (-t - np.sqrt(Delta))/a]
    else:
        pts = [-t/a]
    xs = []
    for p in pts + [lo, hi]:
        # dense geometric grid around each point (both sides)
        g = np.concatenate([p - np.geomspace(1e-12, 5, 4000), p + np.geomspace(1e-12, 5, 4000)])
        xs.append(g)
    xs.append(np.linspace(max(lo, -1e4), min(hi, 1e4), 200001))
    x = np.unique(np.concatenate(xs))
    x = x[(x > lo) & (x < hi)]
    if len(x) < 10:
        continue
    # piecewise measure: use midpoints and cell widths
    xm = 0.5*(x[1:] + x[:-1]); w = np.diff(x)
    phi = sigma - a*xm*xm - 2*xm*t
    h = np.abs(phi)**-0.5
    # weighted bathtub: sort h descending, accumulate widths until 1
    order = np.argsort(-h); hc = h[order]; wc = w[order]
    cw = np.cumsum(wc); k = np.searchsorted(cw, 1.0)
    val = (hc[:k]*wc[:k]).sum() + (hc[k]*(1.0 - (cw[k-1] if k > 0 else 0.0)) if k < len(hc) else 0.0)
    bound = 9.05*abs(Delta)**-0.25
    worst = max(worst, val/bound)
    # G_a(sigma) check with f optimal: G_a(sig) = sup int f 1{|a x^2 + sig| < 2|x|} /(2|x|)
    sig = rng.choice([-1,1])*10**rng.uniform(-4, 1.5)
    xg = np.concatenate([-np.geomspace(1e-9, 1e4, 200000)[::-1], np.geomspace(1e-9, 1e4, 200000)])
    xgm = 0.5*(xg[1:] + xg[:-1]); wg = np.diff(xg)
    hg = np.where(np.abs(a*xgm*xgm + sig) < 2*np.abs(xgm), 1.0/(2*np.abs(xgm)), 0.0)
    order = np.argsort(-hg); hc = hg[order]; wc = wg[order]; cw = np.cumsum(wc); k = np.searchsorted(cw, 1.0)
    G = (hc[:k]*wc[:k]).sum()
    Gb = np.log(1 + (1 + np.sqrt(1 + abs(a*sig)))/(2*abs(sig)))
    worstG = max(worstG, G/Gb)
print("worst ratio J_a / (9.05 |Delta|^{-1/4}) =", round(worst, 4), flush=True)
print("worst ratio G_a / log(1+(1+sqrt(1+|a s|))/(2|s|)) =", round(worstG, 4), flush=True)
