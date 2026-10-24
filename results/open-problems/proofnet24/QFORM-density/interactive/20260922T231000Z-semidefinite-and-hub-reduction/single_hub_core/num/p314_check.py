# Exact push-forward density of dt/(2|t|) on 0<|t|<1 under x(t) = alpha/(2t) - sigma t/2, then the bathtub
# (integral of the density over its top set of measure 1), against 3.5 log(1+2/|a|) + 0.5 log(1+2|s|)
# (and log(1+1/|a|) for sigma = 0).
import numpy as np
rng = np.random.default_rng(11)
def dens(x, a, s):
    d = np.zeros_like(x)
    if s == 0:
        t = a/(2*x); ok = (np.abs(t) < 1) & (t != 0)
        d[ok] = 1/(2*np.abs(x[ok]))
        return d
    disc = x*x + s*a
    for sg in (1, -1):
        with np.errstate(invalid="ignore", divide="ignore"):
            t = (-x + sg*np.sqrt(disc))/s
            xp = -a/(2*t*t) - s/2
            c = 1/(2*np.abs(t)*np.abs(xp))
        ok = (disc >= 0) & np.isfinite(c) & (np.abs(t) < 1) & (t != 0)
        d[ok] += c[ok]
    return d
worst = 0.0; worst0 = 0.0; rows = []
for trial in range(300):
    a = 10**rng.uniform(-4, 1) * rng.choice([-1, 1])
    s = 0.0 if trial % 3 == 0 else 10**rng.uniform(-3, 3) * rng.choice([-1, 1])
    W = max(10.0, 2*np.sqrt(abs(a*s)) + 10, abs(a) + 10)
    h = 2e-5
    x = np.arange(-W, W, h) + h/2
    d = dens(x, a, s)
    k = int(round(1/h))
    top = np.partition(d, len(d)-k)[len(d)-k:]
    I = top.sum()*h
    b = np.log(1+1/abs(a)) if s == 0 else 3.5*np.log(1+2/abs(a)) + 0.5*np.log(1+2*abs(s))
    if s == 0: worst0 = max(worst0, I/b)
    else: worst = max(worst, I/b)
print("worst I/bound: sigma != 0 ->", round(worst, 4), "; sigma = 0 ->", round(worst0, 4))
