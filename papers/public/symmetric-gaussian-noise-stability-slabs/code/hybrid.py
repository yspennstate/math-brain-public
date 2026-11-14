"""In R^2: at the measure a* where the strip and the ball tie, do shapes between them beat both?
Families (all of Gaussian measure a*): ellipses x1^2/s^2 + s^2 x2^2 <= c (s = 1 is the ball, s -> 0 the strip),
truncated strips {|x1| <= t, |x| <= R}, and the rounded strip {dist(x, segment [-h e2, h e2]) <= t}.
Values on an N x N grid with the PSD cell kernel (same discretization for every shape, so differences are fair),
with sub-cell sampling of the indicator for smooth boundaries."""
import math, sys
import numpy as np
from scipy.optimize import brentq
from scipy.special import ndtr
sys.path.insert(0, '.')
from cyl2d import ball, interval

rho = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
L, N, Q, SUB = 6.5, int(sys.argv[2]) if len(sys.argv) > 2 else 600, 6, 4
astar = brentq(lambda a: interval(a, rho) - ball(a, rho), 0.5, 0.97)
print(f'rho={rho} tie a*={astar:.6f} exact strip={interval(astar, rho):.10f} ball={ball(astar, rho):.10f}')

edges = np.linspace(-L, L, N + 1)
gx, gw = np.polynomial.legendre.leggauss(Q)
s = math.sqrt(1 - rho * rho)
lo, hi = edges[:-1], edges[1:]
xs = (lo + hi)[:, None] / 2 + (hi - lo)[:, None] / 2 * gx[None, :]
wx = (hi - lo)[:, None] / 2 * gw[None, :] * np.exp(-xs ** 2 / 2) / math.sqrt(2 * math.pi)
e = edges.copy(); e[0], e[-1] = -40, 40
c = ndtr((e[None, :] - rho * xs.ravel()[:, None]) / s)
K = (wx.ravel()[:, None] * np.diff(c, axis=1)).reshape(N, Q, N).sum(1); K = (K + K.T) / 2
w1 = ndtr(edges[1:]) - ndtr(edges[:-1]); w1[0] += ndtr(-L); w1[-1] += ndtr(-L)
# sub-cell sample points, Gaussian-weighted within each cell
h = (2 * L) / N
off = (np.arange(SUB) + 0.5) / SUB * h
P = (lo[:, None] + off[None, :])                     # N x SUB
pw = np.exp(-P ** 2 / 2); pw /= pw.sum(1, keepdims=True)

def frac(ind):
    """ind(X1, X2) on the sub-sample grid -> Gaussian-weighted cell fractions (N x N)."""
    X1 = P.reshape(N, SUB, 1, 1); X2 = P.reshape(1, 1, N, SUB)
    v = np.clip(ind(X1, X2), 0.0, 1.0)
    return np.einsum('aibj,ai,bj->ab', v, pw, pw)

def stab(f):
    return float((f * (K @ f @ K)).sum())

def mass(f):
    return float((f * np.outer(w1, w1)).sum())

HS = h / SUB                                          # smoothing width of the boundary
def lvl(g, gn, c):                                    # smoothed indicator of {g <= c}
    return 0.5 + (c - g) / (np.maximum(gn, 1e-12) * HS)
def solve(make, lo_, hi_):
    """find the parameter giving mass a* (make(p) increasing in p); mass is continuous in p."""
    p = brentq(lambda p: mass(frac(make(p))) - astar, lo_, hi_, xtol=1e-12)
    f = frac(make(p)); m = mass(f)
    assert abs(m - astar) < 1e-9, m
    return p, stab(f), m

_, Sb, _ = solve(lambda r: (lambda x, y: lvl(np.sqrt(x * x + y * y), 1.0, r)), 0.5, 6)
_, Ss, _ = solve(lambda t: (lambda x, y: lvl(np.abs(x) + 0 * y, 1.0, t)), 0.2, 6)
ref = max(Sb, Ss)
print(f'grid: ball={Sb:.10f} strip={Ss:.10f}  (grid error vs exact: ball {Sb - ball(astar, rho):+.1e}, strip {Ss - interval(astar, rho):+.1e})')
best = ('cyl', ref)
print('ellipses x1^2/s^2 + s^2 x2^2 <= c^2')
for sc in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]:
    c_, S_, m_ = solve(lambda cc, sc=sc: (lambda x, y: lvl(np.sqrt(x * x / sc ** 2 + sc ** 2 * y * y), np.sqrt(x * x / sc ** 4 + sc ** 4 * y * y) / np.maximum(np.sqrt(x * x / sc ** 2 + sc ** 2 * y * y), 1e-12), cc)), 0.3, 30)
    print(f'  s={sc:<5} S={S_:.10f} rel_vs_best_cyl={S_ / ref - 1:+.2e}')
    if S_ > best[1]: best = (f'ellipse s={sc}', S_)
print('truncated strips |x1|<=t, |x|<=R')
for R in [2.6, 2.8, 3.0, 3.2, 3.5, 4.0, 4.5]:
    try:
        t_, S_, m_ = solve(lambda t, R=R: (lambda x, y: np.minimum(np.clip(lvl(np.abs(x) + 0 * y, 1.0, t), 0, 1), np.clip(lvl(np.sqrt(x * x + y * y), 1.0, R), 0, 1))), 0.2, R - 1e-6)
    except ValueError:
        print(f'  R={R} no t'); continue
    print(f'  R={R:<4} t={t_:.4f} S={S_:.10f} rel_vs_best_cyl={S_ / ref - 1:+.2e}')
    if S_ > best[1]: best = (f'trunc R={R}', S_)
print('stadiums: within t of the segment [-H, H] on the x2 axis')
for H in [0.5, 1.0, 1.5, 2.0, 3.0, 4.0]:
    t_, S_, m_ = solve(lambda t, H=H: (lambda x, y: lvl(np.sqrt(x * x + np.maximum(np.abs(y) - H, 0) ** 2), 1.0, t)), 0.1, 6)
    print(f'  H={H:<4} t={t_:.4f} S={S_:.10f} rel_vs_best_cyl={S_ / ref - 1:+.2e}')
    if S_ > best[1]: best = (f'stadium H={H}', S_)
print('best:', best[0], f'{best[1]:.10f}', f'rel {best[1] / ref - 1:+.2e}')
