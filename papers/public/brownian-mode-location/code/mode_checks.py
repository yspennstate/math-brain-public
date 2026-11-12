"""Checks for the paper on the mode of classical and free Brownian motion with an initial law.

usage: python mode_checks.py out.json

Part 1 (SymPy): the coefficients of the two expansions, derived from the stationarity equations as formal
        series in s = 1/t.
Part 2 (mpmath): the global modes of several initial laws at large t against the two-term expansions.
Part 3 (mpmath): at the thresholds of Theorems 1 and 2, a scan for the global maximizers and the stated bounds.
"""
import json
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 40


# ---------------------------------------------------------------- part 1
def formal():
    s, a, b, r1, r2, v, m3, m4, m5 = sp.symbols('s a b r1 r2 v m3 m4 m5')
    mom = {0: 1, 1: 0, 2: v, 3: m3, 4: m4, 5: m5}

    def trunc(e):
        return sp.series(sp.expand(e), s, 0, 3).removeO()

    # classical: E[(Y-h) exp(-s (Y-h)^2 / 2)] = 0, h = a s + b s^2
    h = a * s + b * s ** 2

    def Ec(k):  # E (Y-h)^k
        return sum(sp.binomial(k, j) * mom[j] * (-h) ** (k - j) for j in range(0, min(k, 5) + 1))

    eq = trunc(Ec(1) - s / 2 * Ec(3) + s ** 2 / 8 * Ec(5))
    a_c = sp.solve(eq.coeff(s, 1), a)[0]
    b_c = sp.solve(eq.coeff(s, 2).subs(a, a_c), b)[0]

    # free: E[1/(r + s q^2)] = 1, E[q/(r + s q^2)^2] = 0, q = u - Y, mode = u + E[q/(r + s q^2)]
    u = a * s + b * s ** 2
    r = 1 + r1 * s + r2 * s ** 2

    def Ef(k):  # E (u-Y)^k
        return sum(sp.binomial(k, j) * u ** (k - j) * (-1) ** j * mom[j] for j in range(0, min(k, 5) + 1))

    e1 = trunc(r ** 2 * (1 / r - s * Ef(2) / r ** 2 + s ** 2 * Ef(4) / r ** 3 - 1))
    r1_f = sp.solve(e1.coeff(s, 1), r1)[0]
    r2_f = sp.solve(e1.coeff(s, 2).subs(r1, r1_f), r2)[0]
    e2 = trunc((Ef(1) - 2 * s * Ef(3) / r + 3 * s ** 2 * Ef(5) / r ** 2).subs({r1: r1_f, r2: r2_f}))
    a_f = sp.solve(e2.coeff(s, 1), a)[0]
    b_f = sp.solve(e2.coeff(s, 2).subs(a, a_f), b)[0]
    mode = trunc((u + Ef(1) / r - s * Ef(3) / r ** 2 + s ** 2 * Ef(5) / r ** 3).subs(
        {r1: r1_f, r2: r2_f, a: a_f, b: b_f}))
    out = {
        'classical_c1': str(sp.factor(a_c)), 'classical_c2': str(sp.factor(b_c)),
        'free_r1': str(sp.factor(r1_f)), 'free_r2': str(sp.factor(r2_f)),
        'free_u1': str(sp.factor(a_f)), 'free_u2': str(sp.factor(b_f)),
        'free_c1': str(sp.factor(mode.coeff(s, 1))), 'free_c2': str(sp.factor(mode.coeff(s, 2))),
    }
    ok = (sp.simplify(a_c + m3 / 2) == 0 and sp.simplify(b_c - (m5 - 6 * v * m3) / 8) == 0
          and sp.simplify(mode.coeff(s, 1) + 3 * m3) == 0
          and sp.simplify(mode.coeff(s, 2) - (5 * m5 - 22 * v * m3)) == 0)
    # the same coefficients in cumulants (k2 = t + v, k3 = m3, k5 = m5 - 10 v m3) and in free cumulants
    # (r2 = t + v, r3 = m3, r5 = m5 - 5 v m3)
    t = 1 / s
    cl = sp.series(-m3 / (2 * (t + v)) + (m5 - 10 * v * m3) / (8 * (t + v) ** 2), s, 0, 3).removeO()
    fr = sp.series(-3 * m3 / (t + v) + 5 * (m5 - 5 * v * m3) / (t + v) ** 2, s, 0, 3).removeO()
    ok = ok and sp.simplify(cl - (a_c * s + b_c * s ** 2)) == 0 and sp.simplify(fr - mode) == 0
    out['all_identities_hold'] = bool(ok)
    return out


# ---------------------------------------------------------------- laws
class Atomic:
    def __init__(self, name, xs, ps):
        self.name = name
        ps = [mp.mpf(p) for p in ps]
        tot = sum(ps)
        ps = [p / tot for p in ps]
        mean = sum(mp.mpf(x) * p for x, p in zip(xs, ps))
        self.mean = mean
        self.ys = [mp.mpf(x) - mean for x in xs]
        self.ps = ps

    def E(self, f):
        return sum(p * f(y) for y, p in zip(self.ys, self.ps))

    def mom(self, k):
        return self.E(lambda y: y ** k)

    def absmom(self, k):
        return self.E(lambda y: abs(y) ** k)


class CenteredExponential:
    """Y = Z - 1 with Z standard exponential: all moments finite, no Gaussian tail."""
    name = 'centered exponential'
    mean = mp.mpf(0)

    def E(self, f):
        return mp.quad(lambda z: f(z - 1) * mp.exp(-z), [0, 1, 4, 16, 64, mp.inf])

    def mom(self, k):
        return mp.mpf([1, 0, 1, 2, 9, 44, 265, 1854][k])

    def absmom(self, k):
        return self.E(lambda y: abs(y) ** k)


LAWS = [
    Atomic('two atoms -1 (2/3), 2 (1/3)', [-1, 2], [2, 1]),
    Atomic('three atoms -1, 1/2, 3', [-1, mp.mpf(1) / 2, 3], [mp.mpf('0.5'), mp.mpf('0.35'), mp.mpf('0.15')]),
    Atomic('rare outlier 0, 1, 50', [0, 1, 50], [800, 199, 1]),
    Atomic('zero third moment', [-2, -1, 1, 3], [mp.mpf(4) / 30, mp.mpf(15) / 30, mp.mpf(5) / 30, mp.mpf(6) / 30]),
    Atomic('symmetric -1, 1', [-1, 1], [1, 1]),
]


# ---------------------------------------------------------------- modes
def classical_mode(law, t):
    H = lambda h: law.E(lambda y: (y - h) * mp.exp(-(y - h) ** 2 / (2 * t)))
    return mp.findroot(H, -law.mom(3) / (2 * t))


def free_mode(law, t):
    def eqs(u, r):
        return (law.E(lambda y: 1 / (r + (u - y) ** 2 / t)) - 1,
                law.E(lambda y: (u - y) / (r + (u - y) ** 2 / t) ** 2))
    u, r = mp.findroot(eqs, (-2 * law.mom(3) / t, 1 - law.mom(2) / t))
    return u + law.E(lambda y: (u - y) / (r + (u - y) ** 2 / t)), u, r * t


def expansions(law, times):
    v, m3, m5 = law.mom(2), law.mom(3), law.mom(5)
    rows = []
    for t in times:
        t = mp.mpf(t)
        hc = classical_mode(law, t)
        hf, u, R = free_mode(law, t)
        ec = -m3 / (2 * t) + (m5 - 6 * v * m3) / (8 * t ** 2)
        ef = -3 * m3 / t + (5 * m5 - 22 * v * m3) / t ** 2
        rows.append({'t': mp.nstr(t, 8), 'classical_mode_minus_mean': mp.nstr(hc, 20),
                     'free_mode_minus_mean': mp.nstr(hf, 20),
                     'classical_two_terms': mp.nstr(ec, 20), 'free_two_terms': mp.nstr(ef, 20),
                     'classical_error_times_t3': mp.nstr((hc - ec) * t ** 3, 8),
                     'free_error_times_t3': mp.nstr((hf - ef) * t ** 3, 8)})
    return {'law': law.name, 'variance': mp.nstr(v, 12), 'mu3': mp.nstr(m3, 12), 'mu5': mp.nstr(m5, 12), 'rows': rows}


# ---------------------------------------------------------------- thresholds
def eta_sq(law, u, t):
    """R = v_t(u)^2: the root of E[1/(R + (u-Y)^2)] = 1/t, or 0 when there is none."""
    F = lambda R: law.E(lambda y: 1 / (R + (u - y) ** 2))
    if F(t) > 1 / t:
        raise ValueError('R <= t violated')
    lo, hi = mp.mpf(0), t
    eps = mp.mpf(10) ** (-25)
    if all(abs(u - y) > 0 for y in law.ys) and F(eps) <= 1 / t:
        return mp.mpf(0)
    for _ in range(110):
        mid = (lo + hi) / 2
        if F(mid) > 1 / t:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def thresholds(law, n=1200):
    v, M3 = law.mom(2), law.absmom(3)
    res = {'law': law.name}
    # classical, t = 600 v
    t = 600 * v
    g = lambda h: law.E(lambda y: mp.exp(-(y - h) ** 2 / (2 * t)))
    H = lambda h: law.E(lambda y: (y - h) * mp.exp(-(y - h) ** 2 / (2 * t)))
    span = 4 * mp.sqrt(t) + max(abs(y) for y in law.ys)
    grid = [span * (2 * mp.mpf(i) / n - 1) for i in range(n + 1)]
    vals = [g(h) for h in grid]
    signs = [H(h) > 0 for h in grid]
    crit = sum(1 for i in range(n) if signs[i] != signs[i + 1])
    top = max(range(n + 1), key=lambda i: vals[i])
    hc = classical_mode(law, t)
    minslope = min(
            law.E(lambda y: (1 - (y - h) ** 2 / t) * mp.exp(-(y - h) ** 2 / (2 * t)))
            for h in [mp.sqrt(t) / 2 * (2 * mp.mpf(i) / 200 - 1) for i in range(201)])
    res['classical'] = {
        't': mp.nstr(t, 10), 'critical_points_on_grid': crit,
        'grid_maximizer_within_one_step_of_root': bool(abs(grid[top] - hc) <= 2 * span / n),
        'abs_mode': mp.nstr(abs(hc), 12), 'bound_beta3_over_t': mp.nstr(M3 / t, 12),
        'bound_holds': bool(abs(hc) <= M3 / t),
        'bound_sqrt2_v_over_sqrt_t': mp.nstr(mp.sqrt(2) * v / mp.sqrt(t), 12),
        'variance_bound_holds': bool(abs(hc) <= mp.sqrt(2) * v / mp.sqrt(t)),
        'inside_window': bool(abs(hc) <= mp.sqrt(t) / 2),
        'min_minus_Hprime_on_window': mp.nstr(minslope, 10),
        'slope_bound_holds': bool(minslope > mp.mpf(1) / 2),
    }
    # free, t just above 7 (7 + 4 sqrt 2) v
    A = (7 + 4 * mp.sqrt(2)) * v
    B = (2 + mp.sqrt(2)) * mp.sqrt(v)
    t = 7 * A * (1 + mp.mpf(10) ** (-6))
    span = 2 * mp.sqrt(t) + max(abs(y) for y in law.ys) + 1
    grid = [span * (2 * mp.mpf(i) / n - 1) for i in range(n + 1)]
    Rs = [eta_sq(law, u, t) for u in grid]
    loc = [i for i in range(1, n) if Rs[i] >= Rs[i - 1] and Rs[i] > Rs[i + 1] and Rs[i] > 0]
    top = max(range(n + 1), key=lambda i: Rs[i])
    hf, u, R = free_mode(law, t)
    K = 4 * (B ** 3 + M3)
    conc = max(-2 * law.E(lambda y: (R - 3 * (x - y) ** 2) / (R + (x - y) ** 2) ** 3)
               for x in [B * (2 * mp.mpf(i) / 200 - 1) for i in range(201)])
    res['free'] = {
        't': mp.nstr(t, 12), 'local_maxima_of_density_on_grid': len(loc),
        'grid_maximizer_within_one_step_of_root': bool(abs(grid[top] - u) <= 2 * span / n),
        'u_star': mp.nstr(u, 12), 'B': mp.nstr(B, 12), 'u_star_in_window': bool(abs(u) <= B),
        'R_star_over_t': mp.nstr(R / t, 12), 'R_star_between_t_minus_v_and_t': bool(t - v <= R <= t),
        'max_F_uu_on_window': mp.nstr(conc, 10), 'concave_on_window': bool(conc < 0),
        'abs_u_star_le_2K_over_R': bool(abs(u) <= 2 * K / R),
        'abs_u_star_le_sqrt2_av_over_sqrt_R': bool(abs(u) <= mp.sqrt(2) * A / mp.sqrt(R)),
        'abs_mode': mp.nstr(abs(hf), 12), 'bound_26_over_t': mp.nstr(26 * (B ** 3 + M3) / t, 12),
        'bound_holds': bool(abs(hf) <= 26 * (B ** 3 + M3) / t),
        'bound_4av_over_sqrt_t': mp.nstr(4 * A / mp.sqrt(t), 12),
        'variance_bound_holds': bool(abs(hf) <= 4 * A / mp.sqrt(t)),
    }
    return res


def main():
    out = {'formal': formal()}
    print('formal', out['formal'])
    out['expansions'] = [expansions(law, [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]) for law in LAWS]
    mp.mp.dps = 25
    out['expansions'].append(expansions(CenteredExponential(), [10 ** 3, 10 ** 4, 10 ** 5]))
    mp.mp.dps = 40
    for e in out['expansions']:
        print(e['law'], '| t^3 errors classical', [r['classical_error_times_t3'] for r in e['rows']],
              '| free', [r['free_error_times_t3'] for r in e['rows']])
    out['thresholds'] = [thresholds(law) for law in LAWS]
    for th in out['thresholds']:
        print(th['law'], '| classical', th['classical']['critical_points_on_grid'], th['classical']['bound_holds'],
              '| free', th['free']['local_maxima_of_density_on_grid'], th['free']['concave_on_window'],
              th['free']['bound_holds'])
    out['all_threshold_checks_hold'] = all(
        th['classical']['bound_holds'] and th['classical']['inside_window']
        and th['classical']['variance_bound_holds'] and th['free']['variance_bound_holds']
        and th['classical']['slope_bound_holds'] and th['classical']['critical_points_on_grid'] == 1
        and th['free']['abs_u_star_le_sqrt2_av_over_sqrt_R']
        and th['classical']['grid_maximizer_within_one_step_of_root']
        and th['free']['grid_maximizer_within_one_step_of_root'] and th['free']['u_star_in_window']
        and th['free']['R_star_between_t_minus_v_and_t'] and th['free']['concave_on_window']
        and th['free']['abs_u_star_le_2K_over_R'] and th['free']['bound_holds'] for th in out['thresholds'])
    print('all threshold checks hold:', out['all_threshold_checks_hold'])
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'w', encoding='utf-8') as f:
            json.dump(out, f, indent=1)
            f.write('\n')


if __name__ == '__main__':
    main()
