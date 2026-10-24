"""Locate, by bisection in c, where the closed-form scenario-B certificate for (rho, e) changes sign.
Below that c the Lagrangian bound with envelopes cannot certify H <= c I in that scenario; it is therefore an
upper bound for the scenario's relaxation value (route, relax.py: rho=3 e odd 2.914374, rho=2 e odd 2.786517,
rho=3 e even 2.752688).  Float-level search (evidence), rigorous evaluation at the end points."""
from mpmath import iv, mpf
import ref_certificate as RC
from ref_cert_sensitivity import set_c

def val(c, rho, e_odd):
    set_c(str(c))
    m_ = RC.best_mu(rho, e_odd, lo=-6.0, hi=2.0, it=50)
    tot, M, nodd = RC.bound(rho, e_odd, mpf(m_))
    return float(tot)

for rho, e_odd, lo, hi in ((3, True, 2.90, 2.93), (2, True, 2.70, 2.95), (3, False, 2.60, 2.95)):
    a, b = lo, hi
    va, vb = val(a, rho, e_odd), val(b, rho, e_odd)
    for _ in range(18):
        mid = (a + b) / 2
        vm = val(mid, rho, e_odd)
        if vm > 0:
            a = mid
        else:
            b = mid
    print(f"rho={rho} e {'odd' if e_odd else 'even'}: certificate changes sign at c ~ {(a+b)/2:.6f}", flush=True)
