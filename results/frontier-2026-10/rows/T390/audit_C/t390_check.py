"""T390 review, agent C, 4 Nov 2026. Independent check of the next-order term in
ARE(m) = sqrt(2 pi) e^(-m^2/2)/m (1 - c/m^2) for 1/2 N(-m,1) + 1/2 N(m,1), weight parameter at eta = 0.

Exact rewrite in y = m x (no approximation): p(x) = phi(x) e^(-m^2/2) cosh(m x), so with eps = 1/m^2
  H = phi0 e^(-m^2/2) m   * A,  A = int sech^3(y) e^(-eps y^2/2) dy
  V = phi0 e^(-m^2/2) m^3 * B,  B = int sech^3(y) (tanh y + eps y)^2 e^(-eps y^2/2) dy
  ratio(m) = ARE / asymptotic = A^2 / (B * 2 pi * I),  I = E tanh^2(m x) (1 - I is O(e^(-m^2/2))).
First order in eps: ratio = 1 + eps[2 dA/A0 - dB/B0] = 1 - c eps with c = 8/3 - (2/pi) J3 + (4/pi) J5,
with J3 = int y^2 sech^3, J5 = int y^2 sech^5, using int y tanh sech^3 = (1/3) int sech^3 = pi/6.
"""
import json
import mpmath as mp
mp.mp.dps = 40
sech = mp.sech
inf = mp.inf
J3 = mp.quad(lambda y: y**2 * sech(y)**3, [-inf, 0, inf])
J5 = mp.quad(lambda y: y**2 * sech(y)**5, [-inf, 0, inf])
c_formula = 8 / mp.mpf(3) - 2 / mp.pi * J3 + 4 / mp.pi * J5   # ratio ~ 1 - c/m^2
lead = 4 / mp.mpf(3) + mp.pi**2 / 8


def ratio(m):
    m = mp.mpf(m); e = 1 / m**2
    A = mp.quad(lambda y: sech(y)**3 * mp.e**(-e * y**2 / 2), [-inf, 0, inf])
    B = mp.quad(lambda y: sech(y)**3 * (mp.tanh(y) + e * y)**2 * mp.e**(-e * y**2 / 2), [-inf, 0, inf])
    # I = E tanh^2(m x) under the mixture = 1 - E sech^2(m x); E sech^2 = phi0 e^(-m^2/2) (1/m) int sech(y) e^(-eps y^2/2)
    Es = mp.e**(-m**2 / 2) / mp.sqrt(2 * mp.pi) / m * mp.quad(lambda y: sech(y) * mp.e**(-e * y**2 / 2), [-inf, 0, inf])
    return A**2 / (B * 2 * mp.pi * (1 - Es))


def ratio_direct(m):
    """Independent path: integrate in x with the score-matching formulas as written in the source."""
    m = mp.mpf(m)
    p = lambda x: (mp.npdf(x, -m, 1) + mp.npdf(x, m, 1)) / 2
    g = lambda x: m * sech(m * x)**2
    dl = lambda x: -m * sech(m * x)**2 * (x + m * mp.tanh(m * x))
    pts = [-inf, -m, -1 / m, 0, 1 / m, m, inf]
    H = mp.quad(lambda x: g(x)**2 * p(x), pts)
    V = mp.quad(lambda x: dl(x)**2 * p(x), pts)
    I = mp.quad(lambda x: mp.tanh(m * x)**2 * p(x), pts)
    return (H**2 / (V * I)) / (mp.sqrt(2 * mp.pi) * mp.e**(-m**2 / 2) / m)


rows = []
for m in [1, 2, 3, 4, 5, 6, 8, 10, 15, 20, 40, 100]:
    r = ratio(m)
    rd = ratio_direct(m) if m <= 8 else None
    rows.append({"m": m, "ratio": float(r), "ratio_direct": (float(rd) if rd is not None else None),
                 "m2_one_minus_ratio": float(m**2 * (1 - r))})
out = {"J3": float(J3), "J5": float(J5), "c_closed_form": float(c_formula),
       "lead_4_3_plus_pi2_8": float(lead), "difference": float(c_formula - lead), "rows": rows}
json.dump(out, open("t390_check.json", "w"), indent=1)
print(json.dumps(out, indent=1))
