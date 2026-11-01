import sympy as sp
import math
import scipy.integrate as si

p = sp.symbols('p', positive=True)
x = sp.symbols('x', positive=True)
g = (x - 1)**2 / (2 * (1 + x**2))
dg = sp.factor(sp.diff(g, x))
g2 = sp.simplify(g.subs(x, sp.sqrt(2)))
c_unif = sp.simplify(sp.Rational(5, 4) * g2)

print('gprime_factor =', dg)
print('g_sqrt2 =', g2, float(g2))
print('c_unif =', c_unif, float(c_unif))
print('packet_leakage_factor_2_over_c =', float(2 / c_unif))

delta = (3 - p) / 2
b = p - 1
root_explicit = sp.simplify((b + sp.sqrt(2 * b)) / (3 - p))
root_quadratic = sp.simplify((b + sp.sqrt(b**2 + 2 * b * delta)) / (2 * delta))
print('quadratic_root_minus_explicit =', sp.simplify(root_quadratic - root_explicit))

Cq = 2 * (1 + sp.sqrt(2)) * sp.sqrt(sp.E)
print('quantile_constant =', float(Cq), 'pass_lt_8 =', float(Cq) < 8)

for pv in [2, 2.5, 2.9, 2.99]:
    r1 = float(root_explicit.subs(p, pv))
    r2 = 1 / (math.sqrt(2 / (pv - 1)) - 1)
    print(f'p={pv:.2f} root={r1:.12f} exact_Rp={r2:.12f} diff={abs(r1-r2):.3e}')


def defect_two(pv, ratio, theta=0.5):
    coeff = pv * (pv - 2)

    def iu(u):
        s = u / (ratio * ratio)
        x1 = theta * math.exp(-2 * s)
        x2 = (1 - theta) * math.exp(-2 * u)
        rr2 = x1 + x2
        if rr2 == 0:
            return 0.0
        var = (ratio - 1)**2 * x1 * x2 / (rr2**2)
        return coeff * var * (rr2**(pv / 2)) / (ratio * ratio)

    return si.quad(iu, 0, 120, epsabs=1e-12, limit=500)[0]


for pv in [2.5, 2.75, 3.0]:
    for ratio in [math.sqrt(2), 2, 10]:
        d = defect_two(pv, ratio)
        lower = pv * (pv - 2) * float(g2) * 0.25
        print(
            f'two_shell p={pv:.2f} ratio={ratio:.6f} '
            f'defect={d:.12f} lower={lower:.12f} pass={d + 1e-12 >= lower}'
        )

for ell in [6, 30, 300, 3000]:
    pv = 3 - 3 / ell
    kap = ell**(-2 / 3)
    qbound = 8 * ell / (3 + kap * ell)
    print(
        f'ell={ell} p={pv:.9f} kappa={kap:.9e} '
        f'qbound_over_ell23={qbound / (ell**(2 / 3)):.9f}'
    )

print('CHECK_PASS')
