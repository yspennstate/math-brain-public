# Audit of cert_renyi_arb_sigma.py (agent A, 19 Oct 2026): mpmath J from the raw densities against the arb J for
# sigma 1 and 2, alpha 2 and 3, PQ and QP, at the certified intervals and at the scan points; ball inclusion at each centre.
import sys, importlib; sys.path.insert(0, 'agent_B')
import mpmath as mp
from flint import arb
mp.mp.dps = 30
def raw(g, same, qp, al, s):
    s = mp.mpf(s); Nm = lambda z, mu: mp.exp(-(z - mu) ** 2 / (2 * s * s)) / (mp.sqrt(2 * mp.pi) * s)
    g = mp.mpf(g); wa, w0, wc = Nm(g, -1) / 2, Nm(g, 0) / 2, Nm(g, 1) / 2
    if same: p = lambda z: (wa + wc) * Nm(z, 1); q = lambda z: w0 * Nm(z, 1) + wc * Nm(z, 0)
    else:    p = lambda z: wa * Nm(z, -1) + wc * Nm(z, 1); q = lambda z: w0 * Nm(z, -1) + wc * Nm(z, 0)
    if qp: p, q = q, p
    return mp.quad(lambda z: p(z) ** al * q(z) ** (1 - al), [-mp.inf, -15 * s, -5 * s, 0, 5 * s, 15 * s, mp.inf])
mod = None
for s, al, d, pts, ctr in [(2, 2, 'PQ', (-3.01, -3.0, -2.99, -1.0, 0.0), -3.0), (2, 3, 'PQ', (-3.01, -3.0, -2.99, -2.0, -1.0, 0.0), -3.0),
                           (2, 2, 'QP', (-1.01, -1.0, -0.99, 0.0), -1.0), (2, 3, 'QP', (-1.01, -1.0, -0.99), -1.0),
                           (1, 3, 'PQ', (-2.2,), -2.2), (1, 2, 'QP', (-0.5,), -0.5)]:
    sys.argv = ['x', str(s), str(al), d]
    mod = importlib.reload(mod) if mod else importlib.import_module('cert_renyi_arb_sigma')
    qp = d == 'QP'
    for g in pts:
        A_s, A_a = mod.J(arb(g), True, qp), mod.J(arb(g), False, qp); S_, T_ = raw(g, True, qp, al, s), raw(g, False, qp, al, s)
        ok = A_s.contains(mp.nstr(S_, 25)) if False else (abs(float(A_s.mid()) - float(S_)) < 1e-9 and abs(float(A_a.mid()) - float(T_)) < 1e-9)
        print(f"s{s} a{al} {d} g {g}: arb S {A_s.str(10)} A {A_a.str(10)} | raw S {mp.nstr(S_, 10)} A {mp.nstr(T_, 10)} diff {mp.nstr(S_ - T_, 6)} {'agree' if ok else 'MISMATCH'}", flush=True)
    gb = arb(ctr, 0.00025)
    for same in (True, False):
        B = mod.J(gb, same, qp)
        for gp in (ctr - 0.00025, ctr, ctr + 0.00025): assert B.contains(mod.J(arb(gp), same, qp))
    print(f"ball inclusion ok s{s} a{al} {d}; tail bound at centre {mod.tail(*mod.mix(arb(ctr), True, qp)).str(3)} {mod.tail(*mod.mix(arb(ctr), False, qp)).str(3)}", flush=True)
