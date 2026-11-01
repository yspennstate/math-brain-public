# Audit of cert_renyi_qp_arb.py (agent A, 19 Oct 2026): raw-definition mpmath check + ball inclusion check.
import sys; sys.path.insert(0, '.')
import mpmath as mp, cert_renyi_qp_arb as R
from flint import arb
mp.mp.dps = 40
def Nm(z, mu): return mp.exp(-(z - mu) ** 2 / 2) / mp.sqrt(2 * mp.pi)
def raw(g, al):  # J = int q^al p^(1-al) from the undivided weights
    g = mp.mpf(g); wa, w0, wc = Nm(g, -1) / 2, Nm(g, 0) / 2, Nm(g, 1) / 2
    S = mp.quad(lambda z: (w0 * Nm(z, 1) + wc * Nm(z, 0)) ** al * ((wa + wc) * Nm(z, 1)) ** (1 - al), [-mp.inf, -5, 0, 5, mp.inf])
    A = mp.quad(lambda z: (w0 * Nm(z, -1) + wc * Nm(z, 0)) ** al * (wa * Nm(z, -1) + wc * Nm(z, 1)) ** (1 - al), [-mp.inf, -5, 0, 5, mp.inf])
    return S, A
for al, g in [(2, -0.5), (2, -0.6), (3, 0.5), (3, 0.4), (3, -1.0)]:
    s, t = R.J(arb(g), al, True), R.J(arb(g), al, False); S, A = raw(g, al)
    print(f"alpha {al} g {g}: arb S {s.str(10)} A {t.str(10)} | raw S {mp.nstr(S, 10)} A {mp.nstr(A, 10)}")
for al, lo, hi in [(2, -0.6, -0.595), (3, 0.4, 0.405)]:
    gb = arb((lo + hi) / 2, (hi - lo) / 2)
    for same in (True, False):
        B = R.J(gb, al, same)
        for gp in (lo, (lo + hi) / 2, hi):
            P = R.J(arb(gp), al, same); assert B.contains(P), (al, same, gp)
    d = R.J(gb, al, True) - R.J(gb, al, False); print(f"alpha {al} ball [{lo},{hi}] diff lower {d.lower().str(6)} upper {d.upper().str(6)}; endpoint enclosures contained")
