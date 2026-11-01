# Audit of cert_renyi_real_arb_sigma.py, orders 3/2 and 5/2, sigma 1, PQ and QP (agent A, 19 Oct 2026): mpmath J from the raw
# densities (dps 40) against the arb J at the certified intervals' ends and centre and at the scan points; ball inclusion on an
# exact-cover sub-ball; gain arithmetic min-lower x width. Tail bound checked by hand (convexity of x^alpha, monotone q^(1-alpha),
# the Gaussian product identity, Mills), see AUDIT_REAL_ORDERS_agent_A.md.
import sys, importlib; sys.path.insert(0, 'agent_B')
import mpmath as mp
from flint import arb
mp.mp.dps = 40
def raw(g, same, qp, al, s):
    s = mp.mpf(s); Nm = lambda z, mu: mp.exp(-(z - mu) ** 2 / (2 * s * s)) / (mp.sqrt(2 * mp.pi) * s)
    g = mp.mpf(g); wa, w0, wc = Nm(g, -1) / 2, Nm(g, 0) / 2, Nm(g, 1) / 2
    if same: p = lambda z: (wa + wc) * Nm(z, 1); q = lambda z: w0 * Nm(z, 1) + wc * Nm(z, 0)
    else:    p = lambda z: wa * Nm(z, -1) + wc * Nm(z, 1); q = lambda z: w0 * Nm(z, -1) + wc * Nm(z, 0)
    if qp: p, q = q, p
    return mp.quad(lambda z: p(z) ** al * q(z) ** (1 - al), [-mp.inf, -15, -8, -4, -2, 0, 2, 4, 8, 15, mp.inf])
CASES = [('3/2', 'PQ', -1.51, -1.49, (-1.2, -1.8, -2.4), 0.00045372, 9.20947e-6),
         ('5/2', 'PQ', -2.11, -2.09, (-1.2,), 0.0035292, 7.14287e-5),
         ('3/2', 'QP', -0.51, -0.49, (-1.0, 0.0), 0.0010951, 2.30495e-5),
         ('5/2', 'QP', -0.01, 0.01, (-0.5, 0.5), 0.089638, 0.00180232)]
mod = None; bad = 0
for als, d, a, b, pts, lo, gain in CASES:
    sys.argv = ['x', '1', als, d]; mod = importlib.reload(mod) if mod else importlib.import_module('cert_renyi_real_arb_sigma')
    qp = d == 'QP'; al = mp.mpf(als.split('/')[0]) / mp.mpf(als.split('/')[1])
    for g in (a, (a + b) / 2, b) + pts:
        As, Aa = mod.J(arb(g), True, qp), mod.J(arb(g), False, qp); S_, T_ = raw(g, True, qp, al, 1), raw(g, False, qp, al, 1)
        dA, dR = As - Aa, S_ - T_
        ok = abs(float(As.mid()) - float(S_)) < 1e-12 and abs(float(Aa.mid()) - float(T_)) < 1e-12 and abs(float(dA.mid()) - float(dR)) < 1e-12
        bad += not ok
        print(f"order {als} {d} g {g:+.3f}: arb S {As.str(10)} A {Aa.str(10)} | mpmath S {mp.nstr(S_, 10)} A {mp.nstr(T_, 10)} diff {mp.nstr(dR, 8)} {'agree' if ok else 'MISMATCH'}", flush=True)
    sub = arb(a).union(arb(a + (b - a) / 80))
    for same in (True, False):
        V = mod.J(sub, same, qp)
        for gp in (a, a + (b - a) / 160, a + (b - a) / 80): assert V.contains(mod.J(arb(gp), same, qp))
    print(f"  first sub-ball inclusion ok; gain check {lo:g} x {b - a:.17g} = {lo * (b - a):.5e} vs reported {gain:.5e}", flush=True)
print("mismatches:", bad)
