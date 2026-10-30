"""T392 (agent A, 18 Oct 2026): Target 1. Classifier-free guidance, one dimension, p0 = (N(-m/2,1) + N(m/2,1))/2, class c = +.
OU forward dX = -X dt + sqrt2 dW keeps every marginal at variance 1: p_t = mixture of N(+-a_t, 1), a_t = e^(-t) m/2. Exact scores:
s_c = -(y - a), s_u = -y + a tanh(a y), guided s_w = -y + w a + (1 - w) a tanh(a y).
DDPM (reverse SDE): dy = [-y + 2 w a + 2 (1 - w) a tanh(a y)] ds + sqrt2 dB, started at time T from N(0,1); endpoint law by an implicit
finite-volume Fokker-Planck solve. DDIM (probability flow): dy/ds = w a + (1 - w) a tanh(a y) (reverse time), endpoint law from the
monotone flow map of the N(0,1) quantiles. Reported: mean and variance of the endpoint given y > 0, leakage P(y < 0), differential
entropy, TV to the tilted law p0^(1-w) p_c^w, and the same for the tilted law itself. Validation: w = 1 must return p_c = N(m/2, 1).
argv: T nx_per_unit nsteps"""
import sys, numpy as np
from scipy.linalg import solve_banded
from scipy.integrate import solve_ivp
T, nxu, ns = float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
def stats(y, p):
    dy = y[1] - y[0]; p = np.maximum(p, 0); p = p / (p.sum() * dy); r = y > 0; pr = p[r] / (p[r].sum() * dy)
    mu = (y[r] * pr).sum() * dy; var = ((y[r] - mu) ** 2 * pr).sum() * dy
    H = -(p[p > 0] * np.log(p[p > 0])).sum() * dy
    return mu, var, p[~r].sum() * dy, H, p
def ddpm(w, m):
    L = max(w, 1) * m + 12; y = np.arange(-L, L + 1e-9, 1 / nxu); dy = y[1] - y[0]; n = len(y)
    p = np.exp(-y * y / 2) / np.sqrt(2 * np.pi); ds = T / ns; yf = 0.5 * (y[1:] + y[:-1])
    for k in range(ns):
        t = T - (k + 1) * ds; a = np.exp(-t) * m / 2           # implicit: drift at the new time
        b = -yf + 2 * w * a + 2 * (1 - w) * a * np.tanh(a * yf)  # drift on faces
        # flux F = b p_up - (p_(i+1) - p_i)/dy (upwind advection, central diffusion); dp_i/ds = -(F_(i+1/2) - F_(i-1/2))/dy
        bp, bm = np.maximum(b, 0), np.minimum(b, 0); D = 1 / dy
        # F_f = bp p_i + bm p_(i+1) - D (p_(i+1) - p_i) for face f between i, i+1
        cl = bp + D; cr = bm - D                                # F_f = cl p_i + cr p_(i+1)
        main = np.ones(n); up = np.zeros(n); lo = np.zeros(n); r = ds / dy
        main[:-1] += r * cl; up[1:] += r * cr                   # outgoing face to the right of i
        main[1:] -= r * cr; lo[:-1] -= r * cl                   # incoming face to the left of i (sign: -(-F))
        ab = np.vstack([up, main, lo]); p = solve_banded((1, 1), ab, p)
    return y, p
def ddim(w, m, nq=200001):
    u = (np.arange(nq) + 0.5) / nq; from scipy.special import ndtri; y0 = ndtri(u)
    f = lambda s, y: w * (np.exp(-(T - s)) * m / 2) + (1 - w) * (np.exp(-(T - s)) * m / 2) * np.tanh(np.exp(-(T - s)) * m / 2 * y)
    sol = solve_ivp(f, (0, T), y0, rtol=1e-10, atol=1e-10, method="RK45"); yT = sol.y[:, -1]
    L = max(w, 1) * m + 12; grid = np.arange(-L, L + 1e-9, 1 / nxu); dy = grid[1] - grid[0]
    cdf = np.interp(grid, yT, u, left=0, right=1); p = np.gradient(cdf, dy); return grid, p
def tilted(y, w, m):
    lp = np.logaddexp(-(y + m / 2) ** 2 / 2, -(y - m / 2) ** 2 / 2) - np.log(2); lc = -(y - m / 2) ** 2 / 2
    l = (1 - w) * lp + w * lc; return np.exp(l - l.max())
print(__doc__.splitlines()[0], flush=True); print("argv:", sys.argv[1:], flush=True)
print("  w    m  | law    | mean|y>0  var|y>0  P(y<0)     entropy  TV(tilted)", flush=True)
for w in (1.0, 1.5, 2.0, 4.0, 8.0):
    for m in (1.0, 2.0, 4.0):
        y, pd = ddpm(w, m); yg, pi_ = ddim(w, m); q = tilted(y, w, m)
        for name, yy, pp in (("ddpm", y, pd), ("ddim", yg, pi_), ("tilt", y, q)):
            mu, var, leak, H, pn = stats(yy, pp); qn = stats(yy, tilted(yy, w, m))[4]
            tv = 0.5 * np.abs(pn - qn).sum() * (yy[1] - yy[0])
            print(f" {w:3.1f}  {m:3.1f}  | {name}   | {mu:8.4f}  {var:8.4f}  {leak:9.2e}  {H:8.4f}  {tv:8.4f}", flush=True)
print("DONE", flush=True)
