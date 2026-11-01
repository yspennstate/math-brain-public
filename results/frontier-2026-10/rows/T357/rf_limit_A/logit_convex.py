"""T357, RF sign lemma. g(s) = E sigma(b s + tau Z). With D(s) = sigma(k s) - g(s), both odd about 1/2: if D changes sign once on
(0, inf), + then -, then FM = int_0^inf D s phi = 0 forces OC = 2 int_0^inf D phi = 2 int D (1 - s/s0) phi > 0 (D (1 - s/s0) >= 0).
D has that shape whenever L(s)/s is increasing on (0, inf), L = logit g; a sufficient condition is L convex on (0, inf).
By scaling L(s) = Lam(b s) with Lam(x) = logit E sigma(x + tau Z), so only tau matters. This checks Lam'' > 0 on x in (0, 40]
for tau in [0.02, 12], in log space (trapezoid in z, step 1e-3 on [-40, 40]; logsumexp keeps 1 - h exact in the tail)."""
import numpy as np
z = np.arange(-40, 40, 1e-3); lphi = -z ** 2 / 2
def lam(x, tau):
    t = x[:, None] + tau * z[None, :]
    lh = np.logaddexp.reduce(-np.logaddexp(0, -t) + lphi, axis=1); l1h = np.logaddexp.reduce(-np.logaddexp(0, t) + lphi, axis=1)
    return lh - l1h
worst = []
for tau in [0.02, 0.05, 0.1, 0.2, 0.5, 1, 1.5, 2, 3, 4, 6, 8, 12]:
    x = np.linspace(0, 40, 2001); h = x[1] - x[0]; L = np.concatenate([lam(x[i:i + 200], tau) for i in range(0, len(x), 200)])
    d2 = (L[2:] - 2 * L[1:-1] + L[:-2]) / h ** 2; d1 = np.gradient(L, h)
    star = np.diff(L[1:] / x[1:])
    worst.append((tau, d2.min(), x[1 + int(np.argmin(d2))], d1[0], d1[-1], star.min()))
    print(f"tau {tau:5}: min Lam'' {d2.min():+.3e} at x {x[1 + int(np.argmin(d2))]:.2f}   Lam'(0) {d1[0]:.4f}  Lam'(40) {d1[-1]:.4f}"
          f"  min diff(Lam/x) {star.min():+.3e}  Lam(40) - 40 + tau^2/2 {L[-1] - 40 + tau ** 2 / 2:+.2e}", flush=True)
