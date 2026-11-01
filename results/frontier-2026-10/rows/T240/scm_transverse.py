"""Growth of the specialization mode along the symmetric trajectory of the Saad-Solla ODE (K=M=2, erf, noiseless).

The trajectory that starts from the SGD initial state (Q = q0 I, R = 0) stays in the symmetric subspace; a small
perturbation in the specializing direction (R_11 - R_12 - R_21 + R_22) grows by a factor G(t). Finite-N SGD starts
that direction at size ~ N^{-1/2} and keeps feeding it noise of the same order, so tau_N solves log G(tau) = 1/2 log N
+ O(1): the slope of tau_N against log N is 1/(2 g(tau)), g = d log G / dt, which equals 1/(2 lambda) only once the
symmetric part has reached the plateau. Prints t, distance of the symmetric part to the fixed point, log G and g.
usage: python -X utf8 scm_transverse.py eta [tmax]"""
import sys
import os
import numpy as np
from scipy.integrate import solve_ivp

src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "scm_plateau.py"), encoding="utf-8").read()
exec(src[:src.index("for eta in")])          # I3, I4, rhs, unpack, sym_rhs, eg (not the driver loop)

eta = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
tmax = float(sys.argv[2]) if len(sys.argv) > 2 else 600.0
q0 = 0.2
z0 = np.array([q0, 0.0, q0, 1e-9, 1e-9, 1e-9, 1e-9])   # symmetric start (R = 0 is itself a fixed point of the ODE)
eps = 1e-7
pert = np.array([0, 0, 0, 1, -1, -1, 1.0]) / 2.0


def f(t, z):
    return rhs(z, eta)


ts = np.arange(0, tmax + 1e-9, 2.0)
base = solve_ivp(f, (0, tmax), z0, t_eval=ts, rtol=1e-11, atol=1e-14, method="DOP853")
# fixed point
s = base.y[[0, 1, 3], -1]
from scipy.optimize import fsolve
sp = fsolve(sym_rhs, s, args=(eta,), xtol=1e-13)
# variational growth by finite differences, restarted every 20 time units so the perturbation stays linear
logG = np.zeros(len(ts))
acc = 0.0
zt = z0.copy()
for i in range(1, len(ts)):
    a = solve_ivp(f, (ts[i - 1], ts[i]), zt + eps * pert, rtol=1e-11, atol=1e-16, method="DOP853").y[:, -1]
    b = solve_ivp(f, (ts[i - 1], ts[i]), zt - eps * pert, rtol=1e-11, atol=1e-16, method="DOP853").y[:, -1]
    zt = base.y[:, i]
    dv = (a - b) / (2 * eps)
    gain = np.dot(dv, pert) / np.dot(pert, pert)     # component along the specializing direction
    acc += np.log(abs(gain))
    logG[i] = acc
g = np.gradient(logG, ts)
print("eta %.3f fixed point Q=%.6f C=%.6f R=%.6f" % (eta, sp[0], sp[1], sp[2]))
print("   t   |Q-q*|      |C-c*|      |R-r*|      logG     g(t)")
for i in range(0, len(ts), 10):
    q, c, r = base.y[0, i], base.y[1, i], base.y[3, i]
    print("%5.0f  %.3e  %.3e  %.3e  %8.3f  %.5f" % (ts[i], abs(q - sp[0]), abs(c - sp[1]), abs(r - sp[2]), logG[i], g[i]))
np.savetxt(os.path.join(os.path.dirname(os.path.abspath(__file__)), "transverse_eta%.2f.tsv" % eta),
           np.c_[ts, base.y.T, logG, g], header="t Q11 Q12 Q22 R11 R12 R21 R22 logG g", fmt="%.8g")
