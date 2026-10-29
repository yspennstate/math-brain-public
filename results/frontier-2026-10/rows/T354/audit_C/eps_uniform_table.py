"""Tables for AUDIT_EPS_agent_C.md (agent C, 20 Oct 2026).

1. psi(y) = (s+eps)/(s sqrt(y)+eps): its derivatives at 1 (sympy), and sup |psi''''| over y in [gamma/V, max g^2/V] for a grid of
   eps, to see that the Taylor remainder constant of step 1 does not grow with eps (the model, |x| <= 0.5).
2. The eps > 0 roots of rre_out/: (x*/(r x0) - 1)/d by n d and d, with r = 3/(3+eps), and the linear extrapolation to d = 0.
3. The E2 values at x = 0.1, n d = 1: fit E2 = a x d + c d^2, against (p2/2) E eta^2/d (E eta^2 from the permutation formula,
   uniform_check2.eeta2; eta does not depend on eps).
"""
import glob
import re

import numpy as np
import sympy as sp

y, s, e = sp.symbols("y s eps", positive=True)
psi = (s + e) / (s * sp.sqrt(y) + e)
for k in (1, 2, 3):
    print("psi^(%d)(1) =" % k, sp.factor(sp.simplify(sp.diff(psi, y, k).subs(y, 1))))
d4 = sp.lambdify((y, s, e), sp.diff(psi, y, 4), "numpy")
for X in (0.0, 0.5):
    V = X * X + 9.0
    g2 = np.array([(X + 9) ** 2, (X - 1) ** 2, (9.5) ** 2])  # g = x + 9 or x - 1, |x| <= 0.5
    lo, hi = (1 - 0.5) ** 2 / V, g2.max() / V
    ys = np.linspace(lo, hi, 4001)
    row = []
    for ep in (0, 0.3, 1, 3, 10, 100, 1e4):
        row.append("%g:%.3g" % (ep, np.abs(d4(ys, np.sqrt(V), ep)).max()))
    print("1. x %.1f y in [%.4f, %.3f]: sup |psi''''| by eps  %s" % (X, lo, hi, "  ".join(row)))

rows = {}
for f in glob.glob("rre_out/root_*.txt"):
    t = open(f).read()
    m = re.search(r"n (\d+) beta2 ([\d.]+) nd ([\d.]+) eps ([\d.]+).*\(x\*/\(r x0\)-1\)/d ([-\d.]+)", t)
    if m:
        n, b2, nd, ep, c = int(m[1]), float(m[2]), float(m[3]), float(m[4]), float(m[5])
        rows.setdefault((ep, round(nd)), []).append((1 - b2, n, c))
print("2. (x*/(r x0) - 1)/d")
for key in sorted(rows):
    r = sorted(rows[key], reverse=True)
    cells = "  ".join("d %.3f (n %d) %+.6f" % (d, n, c) for d, n, c in r)
    ext = ""
    if len(r) >= 2:
        (d1, _, c1), (d2, _, c2) = r[-2], r[-1]
        ext = "  -> d=0 %+.4f, slope %.2f" % (c2 - d2 * (c1 - c2) / (d1 - d2), (c1 - c2) / (d1 - d2))
    print("   eps %g n d %d: %s%s" % (key[0], key[1], cells, ext))

from uniform_check2 import eeta2  # noqa: E402  (prints its own tables on import)

print("3. E2 at x = 0.1, n d = 1")
for ep in (1.0, 3.0):
    E2 = {}
    for f in glob.glob("rre_out/e2_*_%g_0.1.txt" % ep):
        m = re.search(r"beta2 ([\d.]+) .*E2 ([-\d.e+]+)", open(f).read())
        if m:
            E2[1 - float(m[1])] = float(m[2])
    if len(E2) < 3:
        print("   eps %g: missing" % ep)
        continue
    x = 0.1
    M = np.array([[x * d, d * d] for d in E2])
    a, c = np.linalg.lstsq(M, np.array(list(E2.values())), rcond=None)[0]
    sv = np.sqrt(x * x + 9.0)
    p2 = sv * (ep + 3 * sv) / (4 * (ep + sv) ** 2)
    pred = [0.5 * p2 * eeta2(int(round(1 / d)), 1 - d, x) / d for d in sorted(E2, reverse=True)]
    print("   eps %g: E2 = %.4f x d + %.3f d^2 (residuals %s); (p2/2) E eta^2/d = %s; (3/8) at eps 0 for scale"
          % (ep, a, c, np.array2string(M @ [a, c] - np.array(list(E2.values())), precision=2),
             ", ".join("%.4f" % v for v in pred)))
