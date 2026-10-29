# Audit of the sigma 0.5 certificates (agent A, 19 Oct 2026). For KL (cert_kl_arb_sigma.py) and Renyi orders 2, 3
# (cert_renyi_arb_sigma.py), PQ and QP: mpmath values of S, A and S - A from the raw densities at dps 50, against the arb values,
# at the certified point and a few scan points; ball inclusion at the certified ball (the cert's own width); the gain
# arithmetic min-lower-end x width. The certified intervals are 2e-7 (KL), 2e-10 / 2e-12 (Renyi PQ) and 2e-8 (Renyi QP) wide.
import sys, importlib; sys.path.insert(0, 'agent_B')
import mpmath as mp
from flint import arb
mp.mp.dps = 50
def raw(g, same, qp, al, s):
    s = mp.mpf(s); Nm = lambda z, mu: mp.exp(-(z - mu) ** 2 / (2 * s * s)) / (mp.sqrt(2 * mp.pi) * s)
    g = mp.mpf(g); wa, w0, wc = Nm(g, -1) / 2, Nm(g, 0) / 2, Nm(g, 1) / 2
    if same: p = lambda z: (wa + wc) * Nm(z, 1); q = lambda z: w0 * Nm(z, 1) + wc * Nm(z, 0)
    else:    p = lambda z: wa * Nm(z, -1) + wc * Nm(z, 1); q = lambda z: w0 * Nm(z, -1) + wc * Nm(z, 0)
    if qp: p, q = q, p
    f = (lambda z: p(z) * mp.log(p(z) / q(z))) if al == 'KL' else (lambda z: p(z) ** al * q(z) ** (1 - al))
    br = [-mp.inf] + [mp.mpf(x) / 4 for x in range(-24, 25)] + [mp.inf]      # breaks every s/2 on [-6, 6]
    return mp.quad(f, br)
# (order, dir, certified centre, half width, scan points, reported min lower end)
CASES = [('KL', 'PQ', -1.4, 1e-7, (-1.5, -1.45, -1.35, -2.0), 9.3520e-8, 1.87040e-14),
         ('KL', 'QP', -1.0, 1e-7, (-1.2, -0.8), 5.5837e-7, 1.11673e-13),
         (2, 'PQ', -1.9, 1e-10, (-2.0, -1.6, -2.2), 3.3736e-7, 6.74720e-17),
         (3, 'PQ', -2.35, 1e-12, (-3.0, -2.0), 1.2981e-5, 2.59658e-17),
         (2, 'QP', -0.5, 1e-8, (-1.0, -1.4), 0.0014407, 2.88137e-11),
         (3, 'QP', -0.5, 1e-8, (-1.0, -1.4), 0.23973, 4.79457e-9)]
km = rm = None; bad = 0
for al, d, ctr, hw, pts, lo, gain in CASES:
    qp = d == 'QP'
    if al == 'KL':
        sys.argv = ['x', '0.5']; km = importlib.reload(km) if km else importlib.import_module('cert_kl_arb_sigma'); F = lambda g, same: km.K(g, same, qp)
    else:
        sys.argv = ['x', '0.5', str(al), d]; rm = importlib.reload(rm) if rm else importlib.import_module('cert_renyi_arb_sigma'); F = lambda g, same: rm.J(g, same, qp)
    for g in (ctr,) + pts:
        As, Aa = F(arb(g), True), F(arb(g), False); S_, T_ = raw(g, True, qp, al, 0.5), raw(g, False, qp, al, 0.5)
        dA = As - Aa; dR = S_ - T_
        ok = dA.contains(arb(mp.nstr(dR, 30))) or abs(float(dA.mid()) - float(dR)) <= 1e-9 * max(1.0, abs(float(dR)))
        rel = abs(float(dA.mid()) - float(dR)) / max(abs(float(dR)), 1e-300)
        bad += not ok
        print(f"{al} {d} g {g}: arb diff {dA.str(8)} | mpmath diff {mp.nstr(dR, 10)} rel.err {rel:.1e} {'agree' if ok else 'MISMATCH'}", flush=True)
    B = arb(ctr, hw)
    for same in (True, False):
        V = F(B, same)
        for gp in (ctr - hw, ctr, ctr + hw): assert V.contains(F(arb(gp), same))
    Dlo = (F(B, True) - F(B, False)).lower()
    print(f"  ball [{ctr}+-{hw:g}] inclusion ok; one-ball lower end of S - A {arb(Dlo).str(5)} (cert min over its balls {lo:g}); "
          f"gain check {lo:g} x {2 * hw:g} = {lo * 2 * hw:.5e} vs reported {gain:.5e}", flush=True)
print("mismatches:", bad)
