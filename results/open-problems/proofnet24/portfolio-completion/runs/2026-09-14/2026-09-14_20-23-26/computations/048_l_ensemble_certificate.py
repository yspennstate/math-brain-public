"""Exact n=3 affine-K L-ensemble Hessian and marginal-Fisher obstruction.

Only Python's standard library is required. Fractions certify every matrix,
probability, derivative, projection, and stated strict inequality. Rational
logarithm intervals certify the signs of displayed transcendental quantities.
No random samples or finite differences are used.
"""

from fractions import Fraction as F
from itertools import combinations, permutations
import json
from pathlib import Path


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def add(A, B, factor=F(1)):
    return [[a + factor*b for a, b in zip(ar, br)] for ar, br in zip(A, B)]


def mul(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def det(A):
    n = len(A)
    answer = F(0)
    for perm in permutations(range(n)):
        term = F((-1)**sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n)))
        for i, j in enumerate(perm):
            term *= A[i][j]
        answer += term
    return answer


def inv(A):
    n = len(A)
    Z = [row[:] + e for row, e in zip(A, eye(n))]
    for j in range(n):
        k = next(k for k in range(j, n) if Z[k][j])
        Z[k], Z[j] = Z[j], Z[k]
        pivot = Z[j][j]
        Z[j] = [x/pivot for x in Z[j]]
        for i in range(n):
            if i != j:
                multiple = Z[i][j]
                Z[i] = [a-multiple*b for a, b in zip(Z[i], Z[j])]
    return [row[n:] for row in Z]


def sub(A, S):
    return [[A[i][j] for j in S] for i in S]


def det_derivatives(M, D):
    n = len(M)
    out = []
    for order in range(3):
        value = F(0)
        for C in combinations(range(n), order):
            T = [[(D if j in C else M)[i][j] for j in range(n)] for i in range(n)]
            value += det(T)
        out.append(value*(2 if order == 2 else 1))
    return out


def log_unit_interval(r, terms=60):
    assert 1 <= r <= 2
    x = (r-1)/(r+1)
    lo = 2*sum((x**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    err = 2*x**(2*terms+1)/(F(2*terms+1)*(1-x*x))
    return lo, lo+err


def interval_scale(c, interval):
    lo, hi = interval
    return (c*lo, c*hi) if c >= 0 else (c*hi, c*lo)


def interval_sum(items):
    return tuple(sum((a[i] for a in items), F(0)) for i in range(2))


def log_interval(q):
    assert q > 0
    r, k = q, 0
    while r < 1:
        r *= 2
        k -= 1
    while r >= 2:
        r /= 2
        k += 1
    return interval_sum([log_unit_interval(r), interval_scale(k, log_unit_interval(F(2)))])


def output_interval(interval):
    scale = 10**12
    lo = F((interval[0].numerator*scale)//interval[0].denominator, scale)
    hi = F(-((-interval[1].numerator*scale)//interval[1].denominator), scale)
    assert lo <= interval[0] <= interval[1] <= hi
    return {'lower_exact': str(lo), 'upper_exact': str(hi),
            'lower_decimal': float(lo), 'upper_decimal': float(hi)}


eps = F(1, 1_000_000)
K = [[(eps if i == j else F(0)) + (F(1, 2)-eps)/3 for j in range(3)] for i in range(3)]
A = [[F(1, 5), F(2, 5), F(0)], [F(2, 5), F(4, 5), F(0)], [F(0), F(0), F(1)]]
I = eye(3)
IK = add(I, K, -1)
R = inv(IK)
L = add(R, I, -1)
B = mul(mul(R, A), R)
C = mul(mul(B, IK), B)
alpha = tr(mul(IK, B))
gamma = tr(mul(mul(IK, B), mul(IK, B)))
assert mul(A, A) == A and tr(A) == 2 and det(A) == 0
assert mul(K, A) != mul(A, K)
for j in range(1, 4):
    assert det(sub(K, list(range(j)))) > 0
    assert det(sub(IK, list(range(j)))) > 0
assert mul(R, IK) == I
assert C == mul(mul(mul(mul(R, A), R), A), R)

atoms = []
for mask in range(8):
    S = [i for i in range(3) if mask & (1 << i)]
    M = [[K[i][j] if j in S else IK[i][j] for j in range(3)] for i in range(3)]
    D = [[A[i][j] if j in S else -A[i][j] for j in range(3)] for i in range(3)]
    p, dp, ddp = det_derivatives(M, D)
    assert p > 0 and p == det(sub(L, S))/det(R)
    if S:
        LS_inv = inv(sub(L, S))
        T = mul(LS_inv, sub(B, S))
        g, d, c = tr(T), tr(mul(T, T)), tr(mul(LS_inv, sub(C, S)))
    else:
        g = d = c = F(0)
    score = g-alpha
    r = score*score+2*c-d-gamma
    Z = [[F(0) for j in range(3)] for i in range(3)]
    if S:
        for i, row in enumerate(S):
            for j, col in enumerate(S):
                Z[row][col] = LS_inv[i][j]
    Delta = add(Z, IK, -1)
    DeltaB = mul(Delta, B)
    kappa = tr(mul(DeltaB, DeltaB))
    assert tr(DeltaB) == score
    assert kappa == d-2*c+gamma
    assert r == score*score-kappa
    assert kappa >= 0 and score*score <= 2*kappa
    assert dp == p*score
    assert ddp == p*r
    atoms.append({'S': S, 'p': p, 'dp': dp, 'ddp': ddp,
                  'g': g, 'd': d, 'c': c, 'score': score, 'r': r, 'kappa': kappa})

assert sum(a['p'] for a in atoms) == 1
assert sum(a['dp'] for a in atoms) == 0
assert sum(a['ddp'] for a in atoms) == 0
fisher = sum(a['dp']**2/a['p'] for a in atoms)
assert sum(a['p']*a['g'] for a in atoms) == alpha
assert sum(a['p']*(2*a['c']-a['d']) for a in atoms) == gamma-fisher
assert sum(a['p']*a['c'] for a in atoms) == gamma
assert sum(a['p']*a['kappa'] for a in atoms) == fisher
tau_mass = sum(a['p']*max(a['r'], 0) for a in atoms)
assert tau_mass == sum(a['p']*max(-a['r'], 0) for a in atoms)
assert tau_mass <= fisher/2

Sigma = [[K[i][i]*(1-K[i][i]) if i == j else -K[i][j]*K[j][i]
          for j in range(3)] for i in range(3)]
ad = [[A[i][i]] for i in range(3)]
theta = mul(inv(Sigma), ad)
fisher_one = sum(A[i][i]*theta[i][0] for i in range(3))
assert fisher_one == 16/(1+8*eps-8*eps**2) + F(52, 25)/(1+2*eps-2*eps**2)
assert fisher_one < F(452, 25)
residual_fisher = F(0)
for a in atoms:
    projection = sum(theta[i][0]*(F(i in a['S'])-K[i][i]) for i in range(3))
    a['marginal_projection'] = projection
    a['residual_score'] = a['score']-projection
    residual_fisher += a['p']*a['residual_score']**2
assert fisher == fisher_one+residual_fisher
for i in range(3):
    assert sum(a['p']*a['residual_score']*(F(i in a['S'])-K[i][i]) for a in atoms) == 0

q = F(1, 30)+F(14, 15)*eps
h = [F(4, 5), F(1, 5), F(0)]
for a in atoms:
    assert a['ddp'] == 2*(-1)**(3-len(a['S']))*(q-sum(h[i] for i in range(3) if i not in a['S']))

R1 = (1+eps)**2/(3*eps*(2-eps))
R2 = (2-eps)**2/(3*(1-eps**2))
assert R1 > 2**17 and R2 > 1 and 1-q > F(24, 25)
assert log_interval(F(2))[0] > F(2, 3)
assert R1 < 1/eps and R2 < 1/eps and 1/eps < 2**20
assert log_interval(F(2))[1] < 1
curvature = interval_sum([interval_scale(-a['ddp'], log_interval(a['p'])) for a in atoms])
curvature_beta = interval_sum([interval_scale(2*(1-q), log_interval(R1)), interval_scale(2*q, log_interval(R2))])
assert curvature[0] <= curvature_beta[1] and curvature_beta[0] <= curvature[1]
assert curvature[0] > F(544, 25) > F(452, 25) > fisher_one
assert curvature[1] < 40
pair23 = next(a for a in atoms if a['S'] == [1, 2])
assert pair23['dp'] > F(3, 10)
assert pair23['p'] < eps/3
assert fisher > pair23['dp']**2/pair23['p'] > F(27, 100)/eps == 270_000
entropy_hessian = interval_sum([(-fisher, -fisher), curvature])
assert entropy_hessian[1] < -269_960

# Separate L-affine Hessian and the compulsory nonlinear-coordinate correction.
mean_c = sum(a['p']*a['c'] for a in atoms)
acceleration = interval_sum([interval_scale(-2*a['p']*(a['c']-mean_c), log_interval(a['p'])) for a in atoms])
linear_l_hessian = interval_sum([entropy_hessian, interval_scale(-1, acceleration)])
assert acceleration[0] > 0

# A global segment covered by the spectral-band theorem, with unequal atoms.
band_K0 = [[F(x, 100) for x in row] for row in [[49, 1, 1], [1, 50, 1], [1, 1, 51]]]
band_K1 = add(band_K0, A, F(1, 20))
assert band_K1 == [[F(x, 100) for x in row] for row in [[50, 3, 1], [3, 54, 1], [1, 1, 56]]]
assert mul(band_K0, A) != mul(A, band_K0)
for Q in [band_K0, band_K1]:
    error = add(Q, I, -F(1, 2))
    assert max(sum(abs(x) for x in row) for row in error) < F(3, 20)
    ps = []
    for site in range(3):
        MM = [[Q[i][j] if j == site else I[i][j]-Q[i][j] for j in range(3)] for i in range(3)]
        ps.append(det(MM))
    assert len(set(ps)) > 1
assert 3*log_interval(F(13, 7))[1] < F(180, 91) < 2

def encode(value):
    if isinstance(value, F):
        return str(value)
    raise TypeError(type(value).__name__)

output = {
    'epsilon': str(eps), 'K': K, 'A': A, 'R': R, 'L': L, 'B': B, 'C': C,
    'alpha': alpha, 'gamma': gamma, 'atoms': atoms, 'q': q,
    'Sigma': Sigma, 'theta': theta, 'R1': R1, 'R2': R2,
    'fisher_exact': fisher, 'fisher_decimal': float(fisher),
    'marginal_fisher_exact': fisher_one, 'marginal_fisher_decimal': float(fisher_one),
    'residual_fisher_exact': residual_fisher, 'residual_fisher_decimal': float(residual_fisher),
    'entropy_log_curvature': output_interval(curvature),
    'entropy_hessian': output_interval(entropy_hessian),
    'nonlinear_l_acceleration': output_interval(acceleration),
    'linear_l_hessian': output_interval(linear_l_hessian),
    'band_example_K0': band_K0, 'band_example_K1': band_K1,
    'checks': 'All exact algebraic checks and rational logarithm-interval inequalities passed.'
}
path = Path(__file__).with_name('048_l_ensemble_certificate_output.json')
path.write_text(json.dumps(output, default=encode, indent=2)+'\n')
print(json.dumps({k: (v if not isinstance(v, dict) else {a: b for a, b in v.items() if a.endswith('_decimal')})
                  for k, v in output.items() if k.endswith('_decimal') or k in
                  ['checks', 'entropy_log_curvature', 'entropy_hessian', 'nonlinear_l_acceleration', 'linear_l_hessian']}, indent=2))
