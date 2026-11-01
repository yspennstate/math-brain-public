"""H0013/H0014 (intake H), Remark 5.3(ii) of arXiv:2607.07410.

For u = y^delta + V(y) with V a symmetric alpha-stable Levy process, the Muckenhoupt/Opic-Kufner
quantity that decides discreteness of the spectrum near +infinity is

    B(x) = ( int_1^x e^{u(y)} dy ) ( int_x^infty e^{-u(y)} dy ).

The semigroup is compact iff B(x) -> 0; lim sup B = infinity forces lambda_ess = 0 (noncompact).
Deterministic control (V = 0): B(x) -> 1/(delta^2 x^{2 delta - 2}), so compact iff delta > 1 - which is
exactly the benchmark the paper states in Section 2.

Claim under test: for ANY delta, a negative jump of V of size m at x lifts B(x) by e^m, and an
alpha-stable process has jumps of size ~ x^{1/alpha} in [x, 2x] while the requirement is only
(2 delta - 2) log x.  So lim sup B = infinity a.s. and the semigroup is noncompact for every delta.

Everything is computed in logs; B itself overflows immediately.
"""
import numpy as np, sys
from math import log, exp

alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 1.5
delta = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
X = float(sys.argv[3]) if len(sys.argv) > 3 else 20.0
H = float(sys.argv[4]) if len(sys.argv) > 4 else 1e-4
seed = int(sys.argv[5]) if len(sys.argv) > 5 else 11
rng = np.random.default_rng(seed)
n = int(X / H) + 1
y = np.arange(n) * H

def stable_path(n, h, alpha, rng):
    """symmetric alpha-stable increments over steps of width h (Chambers-Mallows-Stuck)"""
    U = (rng.random(n - 1) - 0.5) * np.pi
    W = rng.exponential(size=n - 1)
    inc = (np.sin(alpha * U) / np.cos(U) ** (1 / alpha)) * (np.cos(U - alpha * U) / W) ** ((1 - alpha) / alpha)
    return np.concatenate(([0.0], np.cumsum(inc * h ** (1 / alpha))))

def logB(u, y, h):
    """log of ( int_1^x e^u ) ( int_x^inf e^{-u} ), both by log-sum-exp on the same grid"""
    a = u + log(h)
    m1 = np.maximum.accumulate(a)
    # forward cumulative log-sum-exp of e^{a}
    lo = np.logaddexp.accumulate(a)
    b = -u + log(h)
    hi = np.logaddexp.accumulate(b[::-1])[::-1]
    return lo + hi

for label, V in (("V = 0 (control)", np.zeros(n)), (f"alpha-stable alpha={alpha}", stable_path(n, H, alpha, rng))):
    u = y ** delta + V
    lb = logB(u, y, H)
    i0 = int(1.0 / H)
    xs = np.arange(i0, n, int(0.5 / H))
    print(f"\n{label}, delta={delta}")
    print(f"{'x':>6} {'log B(x)':>11} {'predicted -2log(delta x^(d-1))':>32}")
    for i in xs[::4]:
        pred = -2 * log(delta * y[i] ** (delta - 1)) if y[i] > 0 else float('nan')
        print(f"{y[i]:>6.2f} {lb[i]:>11.3f} {pred:>32.3f}")
    j = int(np.argmax(lb[i0:])) + i0
    print(f"  max over x in [1,{X}]: log B = {lb[j]:.3f} at x = {y[j]:.4f}"
          + (f";  jump there: {V[min(j+1,n-1)] - V[max(j-1,0)]:+.3f}" if V.any() else ""))
    if V.any():
        d = np.diff(V)
        k = int(np.argmin(d))
        print(f"  largest downward jump: {d[k]:+.3f} at x = {y[k]:.4f};  log B there = {lb[k]:.3f}"
              f";  (2delta-2) log x = {(2*delta-2)*log(max(y[k],1.01)):.3f}")
