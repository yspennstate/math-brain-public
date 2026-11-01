"""Exact sampler jets and a separately labeled numerical integral check for X047.

The all-parameter sign proof is in agents/X047.md; numerical signs are not inputs.
"""
from pathlib import Path
import json
import sympy as S
import mpmath as mp

OUT = Path(__file__).resolve().parent
checks = 0


def check(value, label):
    global checks
    if not bool(value):
        raise AssertionError(label)
    checks += 1


def simp(value):
    return S.simplify(S.expand_complex(value))


m, r = 3, 2
D = S.Matrix([[S.Rational(2, 5), S.Rational(1, 10) + S.I / 20],
              [S.Rational(1, 10) - S.I / 20, S.Rational(3, 5)]])
u = S.Matrix([1, S.Rational(1, 2)])
U = u * u.conjugate().T
p0, p1 = S.Rational(1, 3), S.Rational(2, 3)
z0, z1 = (2 + S.I) / 20, (3 + 2 * S.I) / 20
p, z = (p0 + p1) / 2, (z0 + z1) / 2
alpha, eta = p1 - p0, z1 - z0
s, eta2 = simp(z * S.conjugate(z)), simp(eta * S.conjugate(eta))
sigma = simp(S.conjugate(z) * eta + z * S.conjugate(eta))

guide_a = simp((u.conjugate().T * D.inv() * u)[0])
guide_b = simp((u.conjugate().T * (S.eye(r) - D).inv() * u)[0])
check(guide_a == S.Rational(240, 91), 'first guide norm')
check(guide_b == S.Rational(20, 7), 'second guide norm')
for mat in (D, S.eye(r) - D):
    check(mat[0, 0] > 0 and simp(mat.det()) > 0, 'strict reservoir')
margins = []
for pp, zz in ((p0, z0), (p1, z1)):
    ss = simp(zz * S.conjugate(zz))
    pair = [simp(pp - m * ss * guide_a), simp(1 - pp - m * ss * guide_b)]
    check(all(v > 0 for v in pair), 'strict endpoint Schur margins')
    margins.append(pair)
check(margins == [[S.Rational(64, 273), S.Rational(47, 84)],
                  [S.Rational(43, 105), S.Rational(23, 420)]], 'listed margins')
check(D * U != U * D, 'coherent guide is not an eigenvector')
check(S.im(simp(z0 / eta)) != 0, 'no real zero of attachment')


def kernel(pp, zz, moving=True):
    block = zz * S.ones(m, 1) * u.conjugate().T
    bottom = D if moving else S.zeros(r)
    return (pp * S.eye(m)).row_join(block).col_join(
        block.conjugate().T.row_join(bottom))


K, A = kernel(p, z), kernel(alpha, eta, moving=False)
check(A.rank() == 4, 'rank four direction')
ell = S.Symbol('ell')
char_expected = ell ** (r - 1) * (ell - alpha) ** (m - 1) * (
    ell ** 2 - alpha * ell - m * eta2 * (u.conjugate().T * u)[0])
check(S.expand(A.charpoly(ell).as_expr() - char_expected) == 0,
      'characteristic polynomial proves inertia (3,1,1)')

reservoir = []
for y in range(1 << r):
    N = D - S.diag(*[int(not (y >> j) & 1) for j in range(r)])
    d = simp((-1) ** (r - y.bit_count()) * N.det())
    a = simp(d * S.trace(N.inv() * U))
    check(d > 0, 'positive reservoir atom')
    v = S.Symbol('v', real=True)
    rank_one = simp((-1) ** (r - y.bit_count()) * (N + v * U).det())
    check(S.expand(rank_one - d - v * a) == 0, 'rank-one atom affine')
    reservoir.append((d, a))
check(sum(d for d, a in reservoir) == 1, 'reservoir normalization')
check(sum(a for d, a in reservoir) == 0, 'rank-one zero total derivative')
check(sum(abs(a) for d, a in reservoir) == 2, 'A_1 equals two')

t = S.Symbol('t', real=True)
pt, st = p + alpha * t, s + sigma * t + eta2 * t ** 2
atoms = []
for mask in range(1 << (m + r)):
    N = K - S.diag(*[int(not (mask >> j) & 1) for j in range(m + r)])
    prob = simp((-1) ** (m + r - mask.bit_count()) * N.det())
    V = N.inv() * A
    vel = simp(prob * S.trace(V))
    acc = simp(prob * (S.trace(V) ** 2 - S.trace(V * V)))
    x, y = mask & ((1 << m) - 1), mask >> m
    k = x.bit_count()
    d, a = reservoir[y]
    R = k / pt - (m - k) / (1 - pt)
    joint = pt ** k * (1 - pt) ** (m - k) * (d - st * a * R)
    jet = [simp(joint.subs(t, 0)),
           simp(S.diff(joint, t).subs(t, 0)),
           simp(S.diff(joint, t, 2).subs(t, 0))]
    check(prob > 0, f'positive full atom {mask}')
    for actual, expected in zip(jet, (prob, vel, acc)):
        check(actual == expected, f'exact moving sampler jet {mask}')
    atoms.append((prob, vel, acc))
for index, expected in ((0, 1), (1, 0), (2, 0)):
    check(sum(row[index] for row in atoms) == expected, 'full atom jet normalization')

pp, ss, lam, aa, vv = S.symbols('p s lam alpha sigma', real=True)
F = pp * S.exp(lam * ss / pp) + (1 - pp) * S.exp(-lam * ss / (1 - pp))
der = lambda f: aa * S.diff(f, pp) + vv * S.diff(f, ss)
square = lam ** 2 * (S.exp(lam * ss / pp) / pp * (vv - aa * ss / pp) ** 2
                    + S.exp(-lam * ss / (1 - pp)) / (1 - pp)
                    * (vv + aa * ss / (1 - pp)) ** 2)
check(S.simplify(der(der(F)) - square) == 0, 'formal perspective square')
check(S.simplify(S.diff(F, ss) - lam * (S.exp(lam * ss / pp)
      - S.exp(-lam * ss / (1 - pp)))) == 0, 'formal strength derivative')

print(f'PASS: {checks} exact assertions (all 32 atom jets and perspective square)', flush=True)

# The following independent integral comparison is numerical, never a sign proof.
mp.mp.dps = 45
to_mp = lambda x: mp.mpf(str(S.N(x, 55)))
pm, sm, am, vm, em = map(to_mp, (p, s, alpha, sigma, eta2))
curvature = sum(to_mp(vel) ** 2 / to_mp(prob) + to_mp(acc) * mp.log(to_mp(prob))
                for prob, vel, acc in atoms)


def integrand(tt, dm, bm):
    if tt == 0:
        return m * bm ** 2 * ((vm - am * sm / pm) ** 2 / pm
              + (vm + am * sm / (1 - pm)) ** 2 / (1 - pm)
              + 2 * em * sm / (pm * (1 - pm)))
    lam = tt * bm
    x1, x0 = lam * sm / pm, -lam * sm / (1 - pm)
    e1, e0 = mp.exp(x1), mp.exp(x0)
    f = pm * e1 + (1 - pm) * e0
    difference = mp.expm1(x1) - mp.expm1(x0)
    fs = lam * difference
    fp = (mp.expm1(x1) - x1 * e1) - (mp.expm1(x0) - x0 * e0)
    dot = am * fp + vm * fs
    w_over_t2 = bm ** 2 * (e1 * (vm - am * sm / pm) ** 2 / pm
                     + e0 * (vm + am * sm / (1 - pm)) ** 2 / (1 - pm))
    w_over_t2 += 2 * em * bm * difference / tt
    return mp.exp(-tt * dm) * (m * f ** (m - 1) * w_over_t2
               + m * (m - 1) * f ** (m - 2) * (dot / tt) ** 2)


parts = []
for d, a in reservoir:
    dm, bm = to_mp(d), to_mp(a)
    parts.append(mp.quad(lambda tt: integrand(tt, dm, bm), [0, 1, 8, 32, mp.inf]))
integral_value = m * am ** 2 / (pm * (1 - pm)) + sum(parts)
error = abs(integral_value - curvature)
assert error < mp.mpf('1e-35'), (integral_value, curvature, error)
print('PASS: separately labeled numerical integral normalization check', flush=True)
print('Direct negative entropy curvature:', mp.nstr(curvature, 30), flush=True)
print('Numerical integral discrepancy:', mp.nstr(error, 5), flush=True)

def entropy(pp, zz):
    ss = simp(zz * S.conjugate(zz))
    total = mp.mpf('0')
    for x in range(1 << m):
        k = x.bit_count()
        w = pp ** k * (1 - pp) ** (m - k)
        R = k / pp - (m - k) / (1 - pp)
        for d, a in reservoir:
            mass = to_mp(simp(w * (d - ss * a * R)))
            total -= mass * mp.log(mass)
    return total

gap = entropy(p, z) - (entropy(p0, z0) + entropy(p1, z1)) / 2
h = lambda q: -q * mp.log(q) - (1 - q) * mp.log(1 - q)
sbar = (simp(z0 * S.conjugate(z0)) + simp(z1 * S.conjugate(z1))) / 2
lower_gap = m * (h(pm) - (h(to_mp(p0)) + h(to_mp(p1))) / 2)
lower_gap += m * 4 / (2 * pm * (1 - pm)) * (to_mp(sbar) ** 2 - sm ** 2)
print('Illustrative midpoint gap and bound:', mp.nstr(gap, 20), mp.nstr(lower_gap, 20))

payload = {
    'exact_assertions': checks,
    'scope': 'analytic sign proof in X047.md; decimals check normalization only',
    'm': m, 'r': r, 'p_mid': str(p), 'z_mid': str(z),
    'alpha': str(alpha), 'eta': str(eta),
    'guide_norms': [str(guide_a), str(guide_b)],
    'endpoint_margins': [[str(v) for v in pair] for pair in margins],
    'inertia': [3, 1, 1],
    'reservoir_atoms': [{'d': str(d), 'a': str(a)} for d, a in reservoir],
    'full_atoms': [{'mask': i, 'p': str(prob), 'v': str(vel), 'a': str(acc)}
                   for i, (prob, vel, acc) in enumerate(atoms)],
    'negative_entropy_curvature_numerical': mp.nstr(curvature, 40),
    'integral_normalization_error_numerical': mp.nstr(error, 10),
    'midpoint_gap_numerical': mp.nstr(gap, 30),
    'midpoint_lower_bound_numerical': mp.nstr(lower_gap, 30),
}
(OUT / 'results.json').write_text(json.dumps(payload, indent=2) + '\n')
