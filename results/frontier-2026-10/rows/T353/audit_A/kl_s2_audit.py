# Audit of cert_kl_arb_sigma.py at sigma 2 (agent A, 19 Oct 2026): mpmath K from raw densities with N(., mu, 2)
# against the arb K, both directions; ball inclusion on [-2.01,-1.99]; sigma 1 of the new file reproduces cert_kl_arb.py.
import sys; sys.path.insert(0, 'agent_B')
import mpmath as mp
sys.argv = ['x', '2']; import cert_kl_arb_sigma as R2
from flint import arb
mp.mp.dps = 40; s = mp.mpf(2)
def Nm(z, mu): return mp.exp(-(z - mu) ** 2 / (2 * s * s)) / (mp.sqrt(2 * mp.pi) * s)
def raw(g, same, qp):
    g = mp.mpf(g); wa, w0, wc = Nm(g, -1) / 2, Nm(g, 0) / 2, Nm(g, 1) / 2
    if same: p = lambda z: (wa + wc) * Nm(z, 1); q = lambda z: w0 * Nm(z, 1) + wc * Nm(z, 0)
    else:    p = lambda z: wa * Nm(z, -1) + wc * Nm(z, 1); q = lambda z: w0 * Nm(z, -1) + wc * Nm(z, 0)
    if qp: p, q = q, p
    return mp.quad(lambda z: p(z) * mp.log(p(z) / q(z)), [-mp.inf, -10, 0, 10, mp.inf])
for qp in (False, True):
    for g in (-2.01, -2.0, -1.99, 0.3):
        a_s, a_a = R2.K(arb(g), True, qp), R2.K(arb(g), False, qp); S, A = raw(g, True, qp), raw(g, False, qp)
        print(f"{'QP' if qp else 'PQ'} g {g}: arb S {a_s.str(10)} A {a_a.str(10)} | raw S {mp.nstr(S, 10)} A {mp.nstr(A, 10)} diff {mp.nstr(S - A, 6)}", flush=True)
    gb = arb(-2.0, 0.00025)
    for same in (True, False):
        B = R2.K(gb, same, qp)
        for gp in (-2.00025, -2.0, -1.99975): assert B.contains(R2.K(arb(gp), same, qp))
    print("ball inclusion ok", "QP" if qp else "PQ", flush=True)
    # tail coefficient at the worst end, to show it is negligible
    print("tail bound at g -2:", R2.tail(arb(-2.0), True, qp).str(3), R2.tail(arb(-2.0), False, qp).str(3))
