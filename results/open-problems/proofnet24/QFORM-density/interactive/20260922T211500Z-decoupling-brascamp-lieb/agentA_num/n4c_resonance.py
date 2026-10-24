try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# (c) F2 construction: X uniform (density 1) on {x in [0,R] : cos(s x^2) >= 0}, measure 1.
# Single coordinate resonates (|E e^{isX^2}| ~ 2/pi); the sum X+X' of two such variables does not,
# consistent with Theorem F / Cauchy-Schwarz: |E e^{is(X+X')^2}| <= sqrt(pi/s).
import numpy as np
from math import sqrt, pi
rng = np.random.default_rng(3)
def make_sampler(s):
    xs = np.linspace(0, 4, 4_000_001); good = np.cos(s*xs*xs) >= 0
    cum = np.cumsum(good)*(xs[1]-xs[0]); R = xs[np.searchsorted(cum, 1.0)]
    pts = xs[(xs <= R) & good]
    return lambda N: rng.choice(pts, N) + rng.uniform(0, xs[1]-xs[0], N)
for s in [20.0, 80.0, 320.0, 1280.0]:
    samp = make_sampler(s); N = 2_000_000
    x = samp(N); y = samp(N)
    single = abs(np.mean(np.exp(1j*s*x*x)))
    pair = abs(np.mean(np.exp(1j*s*(x+y)**2)))
    # the pair bound applies to the direction (e1+e2)/sqrt2 with lambda=2: s(X+Y)^2
    print(f"s={s:7.1f}: single |E e^(isX^2)| = {single:.3f} (2/pi={2/pi:.3f});  pair |E e^(is(X+Y)^2)| = {pair:.4f};"
          f"  bound sqrt(pi/s) = {sqrt(pi/s):.4f}")
