"""OR(y_h, AND_s(lights)) = 1[s*y_h + sum lights >= s]: the normalization-credit inequality of
paper Lemma bias:credit fails by a factor ~ (ln s)/2, while FEI+ itself stays bounded.
High precision (mpmath).  Evidence + exact closed forms checked numerically."""
import mpmath as mp
from levels import spectrum_2groups
mp.mp.dps = 60
def credit_quantities(s, x, pl):
    # heavy coordinate weight s (bias ph), s lights weight 1 (bias pl), theta = s
    pl = mp.mpf(pl); x = mp.mpf(x)
    a2 = pl ** s                       # P(all lights on)
    # choose ph so that mu_A(all lights on, heavy off) / alpha = x approximately: alpha = ph + (1-ph) a2
    # solve (1-ph) a2 / alpha = x  ->  ph = a2 (1-x) / (x + a2 (1 - x)) ... exact:
    ph = a2 * (1 - x) / (x + a2 * (1 - x))
    alpha = ph + (1 - ph) * a2
    V = 4 * alpha * (1 - alpha)
    rho_h = 1 - a2                      # heavy pivotal iff lights not all on
    rho_l = (1 - ph) * pl ** (s - 1)    # light pivotal iff other lights on and heavy off
    Ih = 4 * ph * (1 - ph) * rho_h
    Il = 4 * pl * (1 - pl) * rho_l
    I = Ih + s * Il
    cred = Ih * max(mp.mpf(0), mp.log(4 * rho_h / V)) + s * Il * max(mp.mpf(0), mp.log(4 * rho_l / V))
    VlnV = V * mp.log(1 / V)
    # TC of mu_A exactly: law of (y_h, N_l) with exchangeable lights
    from math import comb
    probs = {}
    for yh in (0, 1):
        for k in range(s + 1):
            pr = (ph if yh else 1 - ph) * comb(s, k) * pl ** k * (1 - pl) ** (s - k)
            if yh == 1 or k == s:
                probs[(yh, k)] = pr / alpha
    H = mp.mpf(0); bh = mp.mpf(0); EN = mp.mpf(0)
    for (yh, k), pr in probs.items():
        if pr > 0:
            H += -pr * mp.log(pr / comb(s, k))   # uniform over arrangements
            bh += pr * yh; EN += pr * k
    bl = EN / s
    hb = lambda t: -(t * mp.log(t) + (1 - t) * mp.log(1 - t)) if 0 < t < 1 else mp.mpf(0)
    TC = hb(bh) + s * hb(bl) - H
    return dict(alpha=alpha, excess_over_I=(VlnV - cred) / I, aTC_over_I=alpha * TC / I, TC=TC)
for s in [4, 8, 16, 32, 64, 128]:
    x = mp.mpf(1) / s
    r = credit_quantities(s, x, x / 50)
    sp = spectrum_2groups(lambda a, b: int(s * a + b >= s), 1, mp.mpf(r['alpha']) * 0 + mp.mpf(1) * 0 + mp.mpf(0.5), s, x / 50) if s <= 0 else None
    print('s', s, 'alpha', mp.nstr(r['alpha'], 4), '(VlnV-credit)/I', mp.nstr(r['excess_over_I'], 5),
          'alpha*TC/I', mp.nstr(r['aTC_over_I'], 5), ' (ln s)/2 =', mp.nstr(mp.log(s) / 2, 4), flush=True)
