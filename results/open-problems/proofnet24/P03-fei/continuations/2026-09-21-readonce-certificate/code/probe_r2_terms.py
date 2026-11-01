"""Where does the region-2 bound's width come from? Decompose phi2_over_v_lower term by term on the failing
depth-0 node cells of a candidate, and report each term's width (the amount of slack it costs).
usage: probe_r2_terms.py <npz> <c> [stride]"""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fei_cert23 as C2
from fei_cert import Iv, Cert, exp2neg, ell_iv, LN2, psi_iv
from fei_cert23 import psi_prime_iv, psit_over_z_iv, Ghat_prime_range, build_slope_tables, BSTAR

src, c = sys.argv[1], float(sys.argv[2]); stride = int(sys.argv[3]) if len(sys.argv) > 3 else 7
d = np.load(src); xs, G = d["xs"], d["G"]; K = float(xs[-1])
cert = Cert(xs, G, c, tail_slope=(G[-1] - BSTAR) / K); build_slope_tables(cert)
n = len(xs) - 1
I, J = np.meshgrid(np.arange(n), np.arange(n), indexing="ij"); I = I.ravel()[::stride]; J = J.ravel()[::stride]
X = Iv(xs[I], xs[I + 1]); Yp = Iv(xs[J], xs[J + 1])
lo, wx, wy = C2.phi2_over_v_lower(cert, X, Yp)
bad = lo < 0
print("%d cells sampled (stride %d); %d fail at depth 0 (%.1f%%); worst %.3e" % (len(I), stride, int(bad.sum()), 100.0*bad.mean(), lo.min()))
# term-by-term widths on the failing cells
p = exp2neg(X); v = exp2neg(Yp); ellv = ell_iv(v); lam = v * ellv / LN2
Xl = Iv(X.lo, np.nextafter(X.hi + lam.hi, np.inf))
A_mv = -(ellv / LN2) * Ghat_prime_range(cert, Xl)
A_dir = (cert.Ghat_range(X) - cert.Ghat_range(X + lam)) / v
B = cert.Ghat_range(Yp) / (1 - v)
Cc = (-8) * p * X
D = (-8) * (1 - v) * (1 - p) * ellv / LN2
Ee = (-8) * (1 - p)
zlo = np.maximum(np.nextafter(p.lo * (1 - v.hi), -np.inf), 1e-300); Z = Iv(zlo, p.hi)
F_mv = p * psi_prime_iv(Z)
F_dir = (psi_iv(p) - psi_iv(p * (1 - v))) / v
Gg = psit_over_z_iv(v)
terms = {
    "A (the G difference, mean-value form)": A_mv.width(),
    "A (the G difference, direct form)": A_dir.width(),
    "B = Ghat(y')/(1-v)": B.width(),
    "C = -8 p x": Cc.width(),
    "D": D.width(),
    "E = -8(1-p)": Ee.width(),
    "F (Psi difference, mean-value)": F_mv.width(),
    "F (Psi difference, direct)": F_dir.width(),
    "G = Psi(1-v)/v": Gg.width(),
}
m = bad if bad.any() else np.ones(len(I), bool)
print("\nwidth on the %d failing cells (median, and the 90th percentile):" % int(m.sum()))
for k, w in sorted(terms.items(), key=lambda kv: -np.median(kv[1][m])):
    print("  %-40s %10.3e   %10.3e" % (k, np.median(w[m]), np.percentile(w[m], 90)))
useA = np.where(A_mv.lo >= A_dir.lo, "mean-value", "direct")
useF = np.where(F_mv.lo >= F_dir.lo, "mean-value", "direct")
print("\nform actually used on the failing cells: A mean-value %.0f%%, F mean-value %.0f%%"
      % (100*(useA[m] == "mean-value").mean(), 100*(useF[m] == "mean-value").mean()))
usedA = np.where(A_mv.lo >= A_dir.lo, A_mv.width(), A_dir.width())
usedF = np.where(F_mv.lo >= F_dir.lo, F_mv.width(), F_dir.width())
tot = usedA + B.width() + Cc.width() + D.width() + Ee.width() + usedF + Gg.width()
print("total width of the used forms: median %.3e" % np.median(tot[m]))
for k, w in (("A used", usedA), ("B", B.width()), ("C", Cc.width()), ("D", D.width()), ("E", Ee.width()), ("F used", usedF), ("G", Gg.width())):
    print("  %-10s %5.1f%% of the total" % (k, 100*np.median(w[m])/np.median(tot[m])))
