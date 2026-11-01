"""Sanity checks of fei_lib against known values (AND_n, majority, F5's L1)."""
import numpy as np, time
from fei_lib import *
setup_process()
t0 = time.time()
# AND_10 : H/I = 3.88418 (F5 table)
n = 10
X = coords(n)
f = sgn(X.sum(1) - (n - 1.5))       # true only at all-ones -> AND with output +1 rare
c = wht(f)
H, I = HI(c, n)
print("AND_10 H/I = %.5f (F5: 3.88418)" % (H / I))
# majority 17 : H/I = 2.3989
n = 17
X = coords(n)
f = sgn(X.sum(1))
c = wht(f)
H, I = HI(c, n)
print("MAJ_17 H/I = %.4f (F5: 2.3989)" % (H / I))
val, order = phi_min(c, n)
print("MAJ_17 Phi = min_r Sigma_r / I = %.4f" % (val / I))
# check sigma_of_order equals val for optimal order
print("sigma(opt order)/I = %.4f" % (sigma_of_order(c, n, order) / I))
# a random LTF: Lemma 3 Q_i <= L1
rng = np.random.default_rng(1)
n = 14
X = coords(n)
w = np.sort(np.abs(rng.standard_normal(n)))[::-1]
f = sgn(X @ w - 0.7)
c = wht(f)
H, I = HI(c, n)
Q = lemma3_Q(c, n, list(range(n)))
print("random LTF n=14: H/I=%.4f, max Q_i = %.4f (L1 = %.4f)" % (H / I, np.nanmax(Q), L1))
v, o = phi_min(c, n)
print("  Phi = %.4f, Sigma(weight order)/I = %.4f" % (v / I, sigma_of_order(c, n, list(range(n))) / I))
print("constants: B=%.10f L1=%.10f C(L1)=%.10f" % (B_LTF, L1, fei_constant(L1)))
print("time %.1fs" % (time.time() - t0))
