"""T392: DDPM leakage P(y < 0) at larger separation m, by a Crank-Nicolson Fokker-Planck solve in log-safe form.

Reverse SDE in the class-+ guided model (see DOSSIER, 18 Oct): dy = b_w(y, s) ds + sqrt2 dB, s in [0, T],
b_w = -y + 2 w a + 2 (1 - w) a tanh(a y), a = a(s) = e^{-(T - s)} m / 2, y(0) ~ N(0, 1).
The question: is log P(y_T < 0) = -m^2/8 + o(m^2) (the conditional's exponent) or is the exponent larger?
Prints P_DDPM, the conditional's Phi(-m/2) and log(P_DDPM / Phi(-m/2)); w = 1 is the control (ratio 1).
Central differences + CN on a uniform grid; the mass left of 0 is integrated with the trapezoid rule.
argv: w m-list T h dt
"""
import sys, math
import numpy as np
from scipy.linalg import solve_banded
from scipy.special import log_ndtr

w = float(sys.argv[1]); ms = [float(x) for x in sys.argv[2].split(",")]
T = float(sys.argv[3]); h = float(sys.argv[4]); dt = float(sys.argv[5])

def run(m):
    lo, hi = -8.0, m * (2 * w - 1) / 2 + 8.0
    y = np.arange(lo, hi + h / 2, h); n = len(y)
    p = np.exp(-y ** 2 / 2) / math.sqrt(2 * math.pi)
    nsteps = int(round(T / dt))
    def op(s):
        a = math.exp(-(T - s)) * m / 2
        b = -y + 2 * w * a + 2 * (1 - w) * a * np.tanh(a * y)
        # L p = -(b p)_y + p_yy, central: (L p)_i = -(b_{i+1} p_{i+1} - b_{i-1} p_{i-1})/(2h) + (p_{i+1} - 2 p_i + p_{i-1})/h^2
        up = -b[1:] / (2 * h) + 1 / h ** 2        # coefficient of p_{i+1} in row i (length n-1)
        dn = b[:-1] / (2 * h) + 1 / h ** 2        # coefficient of p_{i-1} in row i
        md = np.full(n, -2 / h ** 2)
        return up, md, dn
    for k in range(nsteps):
        s0, s1 = k * dt, (k + 1) * dt
        u0, m0, d0 = op(s0); u1, m1, d1 = op(s1)
        rhs = p + 0.5 * dt * (m0 * p + np.concatenate([u0 * p[1:], [0]]) + np.concatenate([[0], d0 * p[:-1]]))
        ab = np.zeros((3, n))
        ab[0, 1:] = -0.5 * dt * u1
        ab[1, :] = 1 - 0.5 * dt * m1
        ab[2, :-1] = -0.5 * dt * d1
        p = solve_banded((1, 1), ab, rhs)
    mass = np.trapezoid(p, y)
    i0 = np.searchsorted(y, 0.0)
    leak = np.trapezoid(p[:i0 + 1], y[:i0 + 1]) - 0.5 * h * p[i0] * 0  # y[i0] ~ 0
    neg = p.min()
    return leak, mass, neg

print(f"w={w} T={T} h={h} dt={dt}")
for m in ms:
    leak, mass, neg = run(m)
    lphi = log_ndtr(-m / 2)
    print(f"m={m:5.2f} P_DDPM={leak:.4e} Phi(-m/2)={math.exp(lphi):.4e} log ratio={math.log(max(leak, 1e-300)) - lphi:+.4f} "
          f"logP/m^2={math.log(max(leak, 1e-300)) / m ** 2:+.4f} mass={mass:.6f} min p={neg:.1e}", flush=True)
