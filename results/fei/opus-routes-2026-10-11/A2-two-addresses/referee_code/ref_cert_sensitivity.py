"""Sensitivity of the scenario-B certificate to the constant c (non-vacuity check, my closed-form method).
All constants (kappa, delta, psi, GA, GB) are recomputed from c; the certificate is minimised over mu by golden
section and evaluated rigorously at the rounded optimum.  If the certificate is meaningful it must FAIL for c below
the rho = 3 relaxation value (route: 2.914374) and pass at c*."""
import sys
from mpmath import iv, mpf
import ref_certificate as RC

def set_c(cval):
    RC.C = iv.mpf(cval)
    RC.KAP = RC.C / 2 - 1
    RC.DEL = 2 - RC.C / 2
    RC.PSI = RC.log2(1 + iv.mpf(2) ** (-RC.C))
    RC.GA = RC.G(2, 1) / RC.SA
    RC.GB = (RC.KAP * (RC.L10 - 2) - RC.PSI) / (RC.L10 - 1)

for cval in ("2.88", "2.90", "2.91", "2.92", "2.93", "2.94"):
    set_c(cval)
    res = []
    for rho, e_odd in ((2, True), (3, True), (3, False)):
        m_ = RC.best_mu(rho, e_odd, it=40)
        tot, M, nodd = RC.bound(rho, e_odd, mpf(round(m_, 4)))
        res.append(f"rho={rho} e {'odd' if e_odd else 'even'}: {float(tot):+.5f}")
    print(f"c = {cval}:  " + ";  ".join(res), flush=True)
