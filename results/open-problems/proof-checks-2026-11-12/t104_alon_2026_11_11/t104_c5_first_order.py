"""First-order behaviour of the margin ratio sum g Q / sum g P at C_5 along the double-top stratum (n = 5).
(a) Chord directions: put weight t on one chord (all five are equivalent under the dihedral group), move the cycle
    weights the least amount that keeps the top double and the total 1, and print ratio(t) - ratio(C_5) and its slope.
(b) Cycle face: weighted 5-cycles with a double top near the uniform one form a 2-dimensional face; walk out along
    12 directions in it and print ratio(s) - ratio(C_5) against s, to see whether C_5 is a strict local maximum there.
Points are pulled exactly onto the stratum (relative top gap below 1e-9) before the ratio is read.
usage: python t104_c5_first_order.py
"""
import sys
import numpy as np
from scipy.optimize import minimize

n = 5
here = __file__.replace("t104_c5_first_order.py", "t104_circulant_ratio.py")
src = open(here, encoding="utf-8").read().split("\nhalf = ")[0]
sys.argv = ["t104_circulant_ratio.py", str(n), "0"]
g = {"__file__": here, "__name__": "cr_mod"}
exec(compile(src, here, "exec"), g)
ratio, circ, Bs, h = g["ratio"], g["circ"], g["Bs"], g["h"]
w0 = circ(np.array([1.0, 0.0])); w0 /= w0.sum()
cyc = np.where(w0 > 0)[0]; chords = np.where(w0 == 0)[0]
r0 = ratio(w0)[2]
L0 = Bs.T @ np.diag(w0) @ Bs
ev0, U0 = np.linalg.eigh(L0)
T0 = U0[:, -2:]


def gap(w):
    ev = np.linalg.eigvalsh(Bs.T @ np.diag(w) @ Bs)
    return (ev[-1] - ev[-2]) / ev[-1]


def offscalar(w):
    A = T0.T @ (Bs.T @ np.diag(w) @ Bs) @ T0
    return np.array([A[0, 0] - A[1, 1], 2 * A[0, 1]])


def onto(wfix, free, x0):
    """Solve for the free weights near x0 so that the top is double and the total is 1."""
    def build(x):
        w = wfix.copy(); w[free] = x; return w
    def F(x):
        w = build(x)
        return np.concatenate([offscalar(w), [w.sum() - 1.0]])
    # Gauss-Newton on the smooth first-order conditions, minimum-norm steps
    x = x0.copy()
    for _ in range(50):
        f = F(x)
        J = np.array([(F(x + 1e-7 * e) - f) / 1e-7 for e in np.eye(len(x))]).T
        x = x - np.linalg.pinv(J) @ f
    w = build(x)
    # exact polish: minimise the true relative gap, staying close
    obj = lambda y: gap(build(y)) ** 2 * 1e6 + np.sum((y - x) ** 2) + (build(y).sum() - 1) ** 2 * 1e6
    y = minimize(obj, x, method="Nelder-Mead", options={"xatol": 1e-14, "fatol": 1e-20, "maxiter": 20000}).x
    w = build(y)
    return w / w.sum()


print("C_5 ratio %.9f" % r0, flush=True)
print("(a) one chord at weight t, cycle weights adjusted", flush=True)
for t in (1e-3, 2e-3, 4e-3, 8e-3, 1.6e-2):
    wfix = np.zeros(h.m); wfix[chords[0]] = t
    w = onto(wfix, cyc, w0[cyc])
    lam, D, r = ratio(w, tol=1e-7)
    print("  t %.4f  gap %.1e  D %d  ratio - C5 %+.3e  slope %+.4f" % (t, gap(w), D, r - r0, (r - r0) / t), flush=True)

print("(b) cycle face", flush=True)
# tangent of the face: null space of the linearised conditions on the cycle weights
f0 = np.concatenate([offscalar(w0), [w0.sum() - 1]])
J = np.array([np.concatenate([offscalar(w0 + 1e-7 * np.eye(h.m)[k]), [w0.sum() + 1e-7 - 1]]) - f0 for k in cyc]).T / 1e-7
_, S, Vt = np.linalg.svd(J)
N = Vt[np.sum(S > 1e-6):]
print("  face dimension %d (singular values %s)" % (N.shape[0], " ".join("%.2e" % s for s in S)), flush=True)
worst = -1.0
for k in range(12):
    th = np.pi * k / 12
    d = np.cos(th) * N[0] + np.sin(th) * N[1] if N.shape[0] >= 2 else N[0]
    row = []
    for s in (0.01, 0.02, 0.04):
        x0 = w0[cyc] + s * d
        if x0.min() <= 0:
            continue
        w = onto(np.zeros(h.m), cyc, x0)
        lam, D, r = ratio(w, tol=1e-7)
        row.append("s %.2f: %+.3e (D %d)" % (s, r - r0, D)); worst = max(worst, r - r0)
    print("  dir %2d  " % k + "  ".join(row), flush=True)
print("largest ratio - C5 on the face %+.3e" % worst, flush=True)
