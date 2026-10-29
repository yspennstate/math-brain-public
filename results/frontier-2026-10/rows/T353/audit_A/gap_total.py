"""T353 audit: the size of the adaptive gain, from the closed-form inner integrals of rigorous_point.py, integrated over g1 < -2 in
mpmath at 30 digits (1-D quad, split at the ANTI discriminant zero). gain = D(policy) - D(P_S||Q_S) = int_{-inf}^{-2} (I_SAME - I_ANTI) dg1.
Also D(P_S||Q_S) itself = int I_ANTI over all g1."""
import mpmath as mp
mp.mp.dps = 30
E = mp.e ** mp.mpf("0.5"); phi = mp.npdf; Phi = mp.ncdf
def parts(g1): return (phi(g1 + 2) - E * phi(g1 + 1)) / 2, phi(g1) / 2
def disc(g1):
    u, v = parts(g1); A = v * mp.e ** -2; B = -v * E * mp.e ** mp.mpf("-0.5"); return B * B - 4 * A * u, A, B, u, v
def I_anti(g1):
    d, A, B, u, v = disc(g1); F = lambda x: u * Phi(x) + v * Phi(x - 2) - v * E * Phi(x - 1); tot = u + v - v * E
    if d < 0: return tot
    yl, yh = (-B - mp.sqrt(d)) / (2 * A), (-B + mp.sqrt(d)) / (2 * A)
    if u < 0: return tot - F(mp.log(yh))
    return F(mp.log(yl)) + tot - F(mp.log(yh))
def I_same(g1):
    u, v = parts(g1)
    if u + v <= 0: return mp.mpf(0)
    x0 = mp.mpf("-0.5") - mp.log((u + v) / (v * E)); return (u + v) * (1 - Phi(x0)) - v * E * (1 - Phi(x0 + 1))
gz = mp.findroot(lambda t: disc(t)[0], -2.1)        # ANTI discriminant zero on g1 < -2
# u + v = 0 <=> e^-2 z^2 - z + 1 = 0 with z = e^-g1 (E e^-1/2 = 1): SAME is empty on g1 in (zl, zh)
r = mp.sqrt(1 - 4 * mp.e ** -2); zl, zh = -mp.log((1 + r) / (2 * mp.e ** -2)), -mp.log((1 - r) / (2 * mp.e ** -2)); ub = zl
gain = mp.quad(lambda t: I_same(t) - I_anti(t), [-mp.inf, -12, -6, gz, -2])
DPQ = mp.quad(I_anti, [-mp.inf, -12, -6, gz, -2, zl, zh, 4, 12, mp.inf])
print(f"ANTI discriminant zero at g1 = {mp.nstr(gz, 15)}; SAME empty on ({mp.nstr(zl, 12)}, {mp.nstr(zh, 12)})")
print(f"D(P_S||Q_S) = {mp.nstr(DPQ, 20)}\ngain       = {mp.nstr(gain, 20)}\nD(policy)  = {mp.nstr(DPQ + gain, 20)}")
