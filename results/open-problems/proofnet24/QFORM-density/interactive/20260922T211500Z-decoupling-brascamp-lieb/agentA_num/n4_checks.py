try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
from math import gamma, sqrt, pi, log
rng = np.random.default_rng(11)
# (a) constants
ca = lambda a: 2**(1-a)*gamma((1-a)/2)/(2*sqrt(pi)*gamma(a/2))
y = np.linspace(1e-6, 50, 2_000_001); kap = np.max(np.log1p(y)/np.sqrt(y))
print(f"(a) c_1/2={ca(0.5):.6f} (1/sqrt(2pi)={1/sqrt(2*pi):.6f})  c_1/4={ca(0.25):.6f}  kappa={kap:.5f}")
# (b) coordinate hyperbola: p_{Y1Y2}(u) vs 4 log(1+1/(2 sqrt|u|)) for several densities <=1 (exact quadrature)
def p_prod(u, f1, f2, lo=1e-7, hi=60, N=400_001):
    ys = np.concatenate([-np.geomspace(hi, lo, N), np.geomspace(lo, hi, N)])
    w = np.gradient(ys)
    return np.sum(f1(ys)*f2(u/ys)/np.abs(ys)*w)
unif = lambda x: ((x > -0.5) & (x < 0.5)).astype(float)
shift = lambda c: (lambda x: ((x > c-0.5) & (x < c+0.5)).astype(float))
def bath(a):  # the extremal density near |y|=a from the proof
    return lambda x: (((np.abs(x) > a) & (np.abs(x) < a+0.5))).astype(float)
worst = 0
for u in [1e-4, 1e-3, 1e-2, 0.1, 0.5, 1, 3]:
    b = 4*log(1+1/(2*sqrt(u)))
    vals = [p_prod(u, unif, unif), p_prod(u, shift(0.7), shift(-0.3)), p_prod(u, bath(sqrt(u)), bath(sqrt(u))),
            p_prod(u, shift(sqrt(u)), shift(sqrt(u)))]
    worst = max(worst, max(vals)/b)
    print(f"(b) u={u:7.4f}  densities: " + "  ".join(f"{v:.3f}" for v in vals) + f"   bound {b:.3f}")
print("(b) worst ratio density/bound =", round(worst, 3))
# (c) per-direction pointwise decay: single X can resonate (F2); X+X' cannot
def chf_sq(sampler, s, N=2_000_000):
    x = sampler(N); return abs(np.mean(np.exp(1j*s*x*x)))
for s in [20.0, 80.0, 320.0]:
    h = sqrt(2*pi/s)    # lattice with s*h^2 = 2 pi
    latt = lambda N, h=h: h*rng.integers(-int(0.5/0.02), int(0.5/0.02), N) + rng.uniform(-0.01, 0.01, N)
    # density of latt: bumps of width 0.02 carrying mass 1/50 each -> density 1 (valid)
    single = chf_sq(latt, s)
    pair = chf_sq(lambda N: latt(N)+latt(N), s)
    print(f"(c) s={s:6.1f}: |E e^(isX^2)| lattice-resonant single = {single:.3f};  for X+X' (same law) = {pair:.4f};"
          f"  C-S bound sqrt(pi/s) = {sqrt(pi/s):.4f}")
