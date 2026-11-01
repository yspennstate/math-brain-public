# Audit of cert_kl_arb.py (agent A, 19 Oct 2026): mpmath K from raw densities vs the arb K, both directions, plus ball inclusion.
import sys; sys.path.insert(0, '.')
import mpmath as mp, cert_kl_arb as R
from flint import arb
mp.mp.dps = 40
def Nm(z, mu): return mp.exp(-(z - mu) ** 2 / 2) / mp.sqrt(2 * mp.pi)
def raw(g, same, qp):
    g = mp.mpf(g); wa, w0, wc = Nm(g, -1) / 2, Nm(g, 0) / 2, Nm(g, 1) / 2
    if same: p = lambda z: (wa + wc) * Nm(z, 1); q = lambda z: w0 * Nm(z, 1) + wc * Nm(z, 0)
    else:    p = lambda z: wa * Nm(z, -1) + wc * Nm(z, 1); q = lambda z: w0 * Nm(z, -1) + wc * Nm(z, 0)
    if qp: p, q = q, p
    return mp.quad(lambda z: p(z) * mp.log(p(z) / q(z)), [-mp.inf, -5, 0, 5, mp.inf])
for qp in (False, True):
    for g in (-1.5, -1.49, 0.3):
        s, a = R.K(arb(g), True, qp), R.K(arb(g), False, qp); S, A = raw(g, True, qp), raw(g, False, qp)
        print(f"{'QP' if qp else 'PQ'} g {g}: arb S {s.str(10)} A {a.str(10)} | raw S {mp.nstr(S, 10)} A {mp.nstr(A, 10)} diff {mp.nstr(S - A, 5)}")
    gb = arb(-1.5, 0.00025)
    for same in (True, False):
        B = R.K(gb, same, qp)
        for gp in (-1.50025, -1.5, -1.49975): assert B.contains(R.K(arb(gp), same, qp))
    print("ball inclusion ok", "QP" if qp else "PQ")
