"""arXiv 2611.06117, Lemmas 4.7 and 4.8: numerical check of the identities and inequalities of the sign weight.

W_tau(r) = r tau^-2 exp(-r^2/(4 tau)),  zeta = r^2/(4 tau),  chi0 = e - 2,
g(zeta) = (e^zeta - 1 - zeta)/zeta,  mG(zeta) = (g(zeta) - chi0)/(zeta - 1)   (removable at 0 and 1),
C_tau = W' - W/r,  B_tau = W' + W/r,  Omega_tau = W/r,
K_hist(tau, r) = (8/r^2)(1 - (1 + zeta) e^-zeta).

Checked on a grid, 40 digits:
 1. C_tau = -(r^2/(2 tau^3)) e^-zeta                                   (4.45)
 2. -2 int_0^inf C_{tau+2h}(r) dh = K_hist(tau, r)                     (4.49)
 3. K_hist = (-B_tau) tau mG + 2 chi0 tau Omega_tau                    (4.53)
 4. 0 <= K_hist <= 2/tau
 5. mG >= chi0, mG increasing, mG <= chi0 e^zeta
 6. (1 - zeta) mG' + zeta mG'' <= mG       (so (d_t + d_r^2 + d_r/r) m_G <= 2 m_G / tau)
 7. int_{te}^inf W_{1+2t-te}(r) dt = (2/r)(1 - exp(-r^2/(4(1+te))))
"""
from mpmath import mp, mpf, exp, quad, diff, e, inf

mp.dps = 40
chi0 = e - 2


def g(z):
    if abs(z) < mpf("1e-8"):
        return z / 2 + z * z / 6
    return (exp(z) - 1 - z) / z


def mG(z):
    if abs(z - 1) < mpf("1e-6"):
        # g'(1) + g''(1)(z-1)/2: g' = (z e^z - e^z + 1)/z^2 -> 1 at z = 1; g''(1) = e - 2
        return 1 + (e - 2) * (z - 1) / 2
    return (g(z) - chi0) / (z - 1)


def W(tau, r):
    return r * tau ** -2 * exp(-r * r / (4 * tau))


def K(tau, r):
    z = r * r / (4 * tau)
    return 8 / (r * r) * (1 - (1 + z) * exp(-z))


worst = {k: mpf(0) for k in "1237"}
ok4 = ok5 = ok6 = True
m6 = None
for tau in [mpf(1), mpf("1.7"), mpf(5), mpf(40)]:
    for r in [mpf("0.05"), mpf("0.5"), mpf(1), mpf(2), mpf("3.3"), mpf(7), mpf(15)]:
        z = r * r / (4 * tau)
        Wp = diff(lambda x: W(tau, x), r)
        C = Wp - W(tau, r) / r
        B = Wp + W(tau, r) / r
        Om = W(tau, r) / r
        worst["1"] = max(worst["1"], abs(C + r * r / (2 * tau ** 3) * exp(-z)))
        Cf = lambda s: -(r * r / (2 * s ** 3)) * exp(-r * r / (4 * s))
        lhs = -2 * quad(lambda h: Cf(tau + 2 * h), [0, 1, 10, 100, inf])
        worst["2"] = max(worst["2"], abs(lhs - K(tau, r)) / K(tau, r))
        worst["3"] = max(worst["3"], abs(K(tau, r) - (-B * tau * mG(z) + 2 * chi0 * tau * Om)) / K(tau, r))
        ok4 = ok4 and 0 <= K(tau, r) <= 2 / tau
        te = tau - 1
        lhs7 = quad(lambda t: W(1 + 2 * t - te, r), [te, te + 1, te + 10, te + 100, inf])
        worst["7"] = max(worst["7"], abs(lhs7 - 2 / r * (1 - exp(-r * r / (4 * (1 + te))))))
prev = None
z = mpf(0)
while z <= 80:
    zz = z if abs(z - 1) > mpf("0.01") else z + mpf("0.013")
    v = mG(zz)
    ok5 = ok5 and v >= chi0 - mpf("1e-30") and v <= chi0 * exp(zz) + mpf("1e-30") and (prev is None or v >= prev)
    prev = v
    d1 = diff(mG, zz); d2 = diff(mG, zz, 2)
    margin = (v - ((1 - zz) * d1 + zz * d2)) / v
    ok6 = ok6 and margin >= 0
    m6 = margin if m6 is None else min(m6, margin)
    z += mpf("0.05")
for k in "1237":
    print("check %s: largest error %s" % (k, mp.nstr(worst[k], 5)))
print("check 4 (0 <= K <= 2/tau):", ok4)
print("check 5 (chi0 <= mG increasing <= chi0 e^zeta), zeta in [0, 80]:", ok5)
print("check 6 ((1-zeta) mG' + zeta mG'' <= mG), zeta in [0, 80]:", ok6, " smallest relative margin", mp.nstr(m6, 6))
print("mG(0) =", mp.nstr(mG(mpf(0)), 10), " chi0 =", mp.nstr(chi0, 10), " mG(1) =", mp.nstr(mG(mpf(1)), 10))
for zz in [mpf(5), mpf(20), mpf(80)]:
    v = mG(zz); d1 = diff(mG, zz); d2 = diff(mG, zz, 2)
    print("zeta %s: mG %s  ((1-z)mG'+z mG'')/mG %s  mG/(chi0 e^z) %s" % (mp.nstr(zz, 3), mp.nstr(v, 6), mp.nstr(((1 - zz) * d1 + zz * d2) / v, 8), mp.nstr(v / (chi0 * exp(zz)), 6)))
