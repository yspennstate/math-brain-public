# Second, independent check of the chi2 gain (agent B, 19 Oct 2026): mpmath at 30 digits, J_SAME - J_ANTI at
# single g1 points, and the integrated gain over the SAME set by mp.quad with the crossing found by findroot.
import mpmath as mp
mp.mp.dps = 30
s = mp.mpf(1)
def J(g1, a2, v2):
    wa, w0, wc = mp.npdf(g1, -1, s) / 2, mp.npdf(g1, 0, s) / 2, mp.npdf(g1, 1, s) / 2
    p = lambda y: wa * mp.npdf(y, v2, s) + wc * mp.npdf(y, a2, s)
    q = lambda y: w0 * mp.npdf(y, v2, s) + wc * mp.npdf(y, 0, s)
    return mp.quad(lambda y: p(y) ** 2 / q(y), [-mp.inf, -2, 0, 2, mp.inf])
d = lambda g: J(g, 1, 1) - J(g, 1, -1)
for g in (-4, -3, -2, -1.6, -1.45, -1.3, -1, 0, 1):
    print("g1 %6s  J_SAME - J_ANTI = %s" % (g, mp.nstr(d(mp.mpf(g)), 12)), flush=True)
c = mp.findroot(d, (-1.6, -1.3), solver='anderson')
print("crossing g1 =", mp.nstr(c, 15))
conj = mp.quad(lambda g: J(g, 1, -1), [-mp.inf, -2, 0, 2, mp.inf]) - 1
gain = mp.quad(d, [-mp.inf, -6, -3, c])
print("chi2 conj %s (van Dijk-Ertan 1.5895)  gain %s  adaptive %s" % (mp.nstr(conj, 12), mp.nstr(gain, 12), mp.nstr(conj + gain, 12)))
