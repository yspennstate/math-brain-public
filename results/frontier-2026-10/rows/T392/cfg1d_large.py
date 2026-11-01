"""T392 (agent A, 18 Oct 2026): Target 2 checks. DDIM in the variable a = e^(-t) m/2: dy/da = w + (1 - w) tanh(a y), y(0) ~ N(0,1),
endpoint y(m/2). Large-m limit of (endpoint - m/2): mean, variance; leakage P(y(m/2) < 0) against the proved bracket
[Phi(-(2w-1) m/2), Phi(-w m/2)]. DDPM by the implicit Fokker-Planck solve of cfg1d.py at m 6 and 8. argv: nq"""
import sys, numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ndtri, ndtr
nq = int(sys.argv[1]); u = (np.arange(nq) + 0.5) / nq; y0 = ndtri(u)
print(__doc__.splitlines()[0], flush=True)
print("  w     m   | DDIM mean-m/2  var     P(y<0)    Phi(-(2w-1)m/2)  Phi(-w m/2)", flush=True)
for w in (1.5, 2.0, 4.0, 8.0):
    for m in (2.0, 4.0, 8.0, 16.0, 32.0):
        f = lambda a, y: w + (1 - w) * np.tanh(a * y)
        yT = solve_ivp(f, (0, m / 2), y0, rtol=1e-10, atol=1e-10).y[:, -1]
        z = yT - m / 2; leak = np.mean(yT < 0)
        print(f" {w:3.1f}  {m:5.1f}  | {z.mean():9.4f}  {z.var():8.4f}  {leak:9.2e}  {ndtr(-(2*w-1)*m/2):12.2e}  {ndtr(-w*m/2):10.2e}", flush=True)
print("DONE", flush=True)
