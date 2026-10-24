"""Independent audit of workers 048 and 056; standard-library exact arithmetic.

The source certificates are read as inert JSON and are never executed/imported.
Atom derivatives are obtained by inclusion-exclusion of principal determinant
polynomials computed with recursive Laplace expansion.  Matrix inverses use
cofactors, not the source scripts' elimination.  Log bounds use an alternating
log(1+y) series with base 3/2, not their base-2 atanh series.

Only 066-prefixed output is written.  Numerical examples certify those examples;
the accompanying report supplies the general mathematical audit.
"""

from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib
import json


HERE = Path(__file__).resolve().parent
SESSION = HERE.parent


def mat(values):
    return [[Q(x) for x in row] for row in values]


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def add(a, b, multiplier=Q(1)):
    return [[a[i][j] + multiplier*b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def scale(a, multiplier):
    return [[multiplier*x for x in row] for row in a]


def mul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Q(0))


def sub(a, selected):
    return [[a[i][j] for j in selected] for i in selected]


def minor(a, row, col):
    return [[x for j, x in enumerate(ar) if j != col]
            for i, ar in enumerate(a) if i != row]


def det(a):
    if not a:
        return Q(1)
    return sum(((-1)**j*a[0][j]*det(minor(a, 0, j))
                for j in range(len(a))), Q(0))


def inverse(a):
    determinant = det(a)
    assert determinant
    answer = [[(-1)**(i+j)*det(minor(a, j, i))/determinant
               for j in range(len(a))] for i in range(len(a))]
    assert mul(a, answer) == eye(len(a))
    return answer


def polynomial_add(a, b, multiplier=Q(1)):
    c = [Q(0)]*max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += multiplier*x
    return c


def polynomial_mul(a, b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def determinant_polynomial(a, b):
    """All coefficients of det(a+t b), by recursive polynomial expansion."""
    if not a:
        return [Q(1)]
    answer = [Q(0)]*(len(a)+1)
    for j in range(len(a)):
        term = polynomial_mul([a[0][j], b[0][j]],
                              determinant_polynomial(minor(a, 0, j),
                                                     minor(b, 0, j)))
        answer = polynomial_add(answer, term, (-1)**j)
    return answer


def subsets(n):
    return [tuple(i for i in range(n) if mask & (1 << i))
            for mask in range(1 << n)]


def kernel_atoms(kernel, direction):
    n = len(kernel)
    all_sets = subsets(n)
    minors = {s: determinant_polynomial(sub(kernel, s), sub(direction, s))
              for s in all_sets}
    answer = []
    for s in all_sets:
        polynomial = [Q(0)]*(n+1)
        for u in all_sets:
            if set(s) <= set(u):
                polynomial = polynomial_add(polynomial, minors[u],
                                            (-1)**(len(u)-len(s)))
        answer.append({'S': list(s), 'p': polynomial[0], 'dp': polynomial[1],
                       'ddp': 2*polynomial[2], 'polynomial': polynomial})
    assert all(a['p'] > 0 for a in answer)
    assert [sum(a['polynomial'][i] for a in answer) for i in range(n+1)] == [Q(1)]+[Q(0)]*n
    for i in range(n):
        included = [a for a in answer if i in a['S']]
        assert sum(a['p'] for a in included) == kernel[i][i]
        assert sum(a['dp'] for a in included) == direction[i][i]
        assert sum(a['ddp'] for a in included) == 0
    return answer


def l_affine_atoms(lmat, direction):
    n = len(lmat)
    denominator = determinant_polynomial(add(eye(n), lmat), direction)
    answer = []
    for s in subsets(n):
        numerator = determinant_polynomial(sub(lmat, s), sub(direction, s))
        numerator += [Q(0)]*(3-len(numerator))
        quotient = []
        for i in range(3):
            quotient.append((numerator[i]-sum((denominator[j]*quotient[i-j]
                                              for j in range(1, i+1)), Q(0)))
                            /denominator[0])
        answer.append({'S': list(s), 'p': quotient[0], 'dp': quotient[1],
                       'ddp': 2*quotient[2]})
    return answer


def interval_add(pairs):
    pairs = list(pairs)
    return tuple(sum((p[i] for p in pairs), Q(0)) for i in range(2))


def interval_scale(c, pair):
    return (c*pair[0], c*pair[1]) if c >= 0 else (c*pair[1], c*pair[0])


def log_reduced(r):
    """120 terms of alternating log(1+y); 0 <= y <= 1/2."""
    assert 1 <= r <= Q(3, 2)
    y = r-1
    partial = sum(((-1)**(j+1)*y**j/j for j in range(1, 121)), Q(0))
    return partial, partial+y**121/121


@lru_cache(maxsize=None)
def logarithm(q):
    assert q > 0
    r, exponent = q, 0
    while r < 1:
        r *= Q(3, 2)
        exponent -= 1
    while r >= Q(3, 2):
        r *= Q(2, 3)
        exponent += 1
    return interval_add([log_reduced(r),
                         interval_scale(exponent, log_reduced(Q(3, 2)))])


def round_interval(pair, places=15):
    grid = 10**places
    lo_integer = pair[0].numerator*grid//pair[0].denominator
    hi_integer = -((-pair[1].numerator*grid)//pair[1].denominator)
    lo, hi = Q(lo_integer, grid), Q(hi_integer, grid)
    assert lo <= pair[0] <= pair[1] <= hi

    def decimal(integer):
        whole, fractional = divmod(abs(integer), grid)
        return f'{"-" if integer < 0 else ""}{whole}.{fractional:0{places}d}'

    return {'lower_exact': str(lo), 'upper_exact': str(hi),
            'lower_decimal': decimal(lo_integer),
            'upper_decimal': decimal(hi_integer)}


def check_source_enclosure(source, new):
    assert Q(source['lower_exact']) <= new[0] <= new[1] <= Q(source['upper_exact'])


def entropy_interval(atoms):
    return interval_add(interval_scale(-a['p'], logarithm(a['p'])) for a in atoms)


def evaluate(kernel, direction, source_atoms=None, rank=None):
    n = len(kernel)
    ident = eye(n)
    complement = add(ident, kernel, -1)
    for j in range(1, n+1):
        assert det(sub(kernel, range(j))) > 0
        assert det(sub(complement, range(j))) > 0
    rmat = inverse(complement)
    lmat = add(rmat, ident, -1)
    bmat = mul(mul(rmat, direction), rmat)
    cmat = mul(mul(bmat, complement), bmat)
    atoms = kernel_atoms(kernel, direction)
    linear_atoms = l_affine_atoms(lmat, bmat)
    acceleration_atoms = l_affine_atoms(lmat, cmat)
    mean_z = scale(ident, 0)
    gamma = trace(mul(mul(complement, bmat), mul(complement, bmat)))
    alpha = trace(mul(complement, bmat))
    for idx, atom in enumerate(atoms):
        s = atom['S']
        z = scale(ident, 0)
        if s:
            local_inverse = inverse(sub(lmat, s))
            for i, row in enumerate(s):
                for j, col in enumerate(s):
                    z[row][col] = local_inverse[i][j]
        mean_z = add(mean_z, z, atom['p'])
        g = trace(mul(z, bmat))
        d = trace(mul(mul(z, bmat), mul(z, bmat)))
        c = trace(mul(z, cmat))
        delta_b = mul(add(z, complement, -1), bmat)
        score = trace(delta_b)
        kappa = trace(mul(delta_b, delta_b))
        tau = score**2-kappa
        assert score == g-alpha and kappa == d-2*c+gamma
        assert atom['p'] == det(sub(lmat, s))/det(rmat)
        assert atom['dp'] == atom['p']*score
        assert atom['ddp'] == atom['p']*tau
        assert atom['ddp'] == linear_atoms[idx]['ddp']+2*acceleration_atoms[idx]['dp']
        atom.update({'g': g, 'd': d, 'c': c, 'score': score, 'kappa': kappa, 'tau': tau})
        if rank:
            assert kappa >= 0 and score**2 <= rank*kappa
        if source_atoms:
            source = source_atoms[idx]
            assert source['S'] == s
            for key in ['p', 'dp', 'ddp', 'score', 'kappa']:
                assert atom[key] == Q(source[key])
            for key in ['g', 'd', 'c', 'tau']:
                if key in source:
                    assert atom[key] == Q(source[key])
            if 'r' in source:
                assert tau == Q(source['r'])
            if 'acceleration_atom' in source:
                assert c == Q(source['acceleration_atom'])
    assert mean_z == complement
    fisher = sum(a['dp']**2/a['p'] for a in atoms)
    assert sum(a['p']*a['kappa'] for a in atoms) == fisher
    assert sum(a['p']*a['c'] for a in atoms) == gamma
    assert sum(a['p']*a['d'] for a in atoms) == fisher+gamma
    positive_mass = sum(max(a['ddp'], 0) for a in atoms)
    assert positive_mass == sum(max(-a['ddp'], 0) for a in atoms)
    if rank:
        assert positive_mass <= Q(rank-1, rank)*fisher
    curvature = interval_add(interval_scale(-a['ddp'], logarithm(a['p'])) for a in atoms)
    hessian = interval_add([(-fisher, -fisher), curvature])
    acceleration = interval_add(interval_scale(-2*a['dp'], logarithm(a['p']))
                                for a in acceleration_atoms)
    linear_curvature = interval_add(interval_scale(-a['ddp'], logarithm(a['p']))
                                    for a in linear_atoms)
    linear_hessian = interval_add([(-fisher, -fisher), linear_curvature])
    return {'atoms': atoms, 'L': lmat, 'R': rmat, 'B': bmat, 'C': cmat,
            'alpha': alpha, 'gamma': gamma, 'fisher': fisher,
            'curvature': curvature, 'hessian': hessian,
            'acceleration': acceleration, 'linear_hessian': linear_hessian,
            'positive_mass': positive_mass}


def principal_trace(lmat, s, u):
    return trace(inverse(add(sub(lmat, s), eye(len(s)), u))) if s else Q(0)


def resolvent(data, u):
    raw = centered = Q(0)
    for atom in data['atoms']:
        s = atom['S']
        val = principal_trace(data['L'], s, u)
        residual = val-sum((1/(data['L'][i][i]+u) for i in s), Q(0))
        assert residual >= 0
        raw += atom['ddp']*val
        centered += atom['ddp']*residual
    assert raw == centered
    return raw


def main():
    old48 = json.loads((HERE/'048_l_ensemble_certificate_output.json').read_text())
    old56 = json.loads((HERE/'056_resolvent_certificate.json').read_text())
    pmat = mat([['1/5', '2/5', 0], ['2/5', '4/5', 0], [0, 0, 1]])
    assert mul(pmat, pmat) == pmat and trace(pmat) == 2 and det(pmat) == 0

    eps = Q(1, 10**6)
    k48 = [[(eps if i == j else Q(0))+(Q(1, 2)-eps)/3 for j in range(3)]
           for i in range(3)]
    assert k48 == mat(old48['K']) and pmat == mat(old48['A'])
    data48 = evaluate(k48, pmat, old48['atoms'], 2)
    for key in ['R', 'L', 'B', 'C']:
        assert data48[key] == mat(old48[key])
    for key in ['alpha', 'gamma']:
        assert data48[key] == Q(old48[key])
    assert data48['fisher'] == Q(old48['fisher_exact'])
    for source, new in [('entropy_log_curvature', 'curvature'),
                        ('entropy_hessian', 'hessian'),
                        ('nonlinear_l_acceleration', 'acceleration'),
                        ('linear_l_hessian', 'linear_hessian')]:
        check_source_enclosure(old48[source], data48[new])
    sigma = [[k48[i][i]*(1-k48[i][i]) if i == j else -k48[i][j]*k48[j][i]
              for j in range(3)] for i in range(3)]
    adiag = [[pmat[i][i]] for i in range(3)]
    theta = mul(inverse(sigma), adiag)
    fisher1 = sum(pmat[i][i]*theta[i][0] for i in range(3))
    assert sigma == mat(old48['Sigma']) and theta == mat(old48['theta'])
    assert fisher1 == Q(old48['marginal_fisher_exact'])
    assert fisher1 == 16/(1+8*eps-8*eps**2)+Q(52, 25)/(1+2*eps-2*eps**2)
    residual = Q(0)
    for a, old in zip(data48['atoms'], old48['atoms']):
        projection = sum(theta[i][0]*(Q(i in a['S'])-k48[i][i]) for i in range(3))
        assert projection == Q(old['marginal_projection'])
        assert a['score']-projection == Q(old['residual_score'])
        residual += a['p']*(a['score']-projection)**2
    assert residual == data48['fisher']-fisher1 == Q(old48['residual_fisher_exact'])
    q = Q(1, 30)+Q(14, 15)*eps
    hdiag = [Q(4, 5), Q(1, 5), Q(0)]
    cardinality_values = [(1-eps)**2/2, (1-eps**2)/6, eps*(2-eps)/6, eps**2/2]
    for a in data48['atoms']:
        assert a['p'] == cardinality_values[len(a['S'])]
        assert a['ddp'] == 2*(-1)**(3-len(a['S']))*(q-sum(hdiag[i] for i in range(3) if i not in a['S']))
    assert [sum(a['ddp']/2 for a in data48['atoms'] if len(a['S']) == j)
            for j in range(4)] == [1-q, 3*q-2, 1-3*q, q]
    r1 = cardinality_values[1]**2/(cardinality_values[0]*cardinality_values[2])
    r2 = cardinality_values[2]**2/(cardinality_values[1]*cardinality_values[3])
    assert r1 == Q(old48['R1']) and r2 == Q(old48['R2'])
    assert r1 > 2**17 and r2 > 1 and 1-q > Q(24, 25)
    assert logarithm(Q(2))[0] > Q(2, 3)
    assert data48['curvature'][0] > Q(544, 25) > Q(452, 25) > fisher1
    pair23 = data48['atoms'][6]
    assert pair23['dp'] == Q(3, 10)+Q(2, 3)*eps-Q(14, 15)*eps**2
    assert pair23['dp'] > Q(3, 10) and pair23['p'] < eps/3
    assert data48['fisher'] > pair23['dp']**2/pair23['p'] > 270000
    assert r1 < 1/eps < 2**20 and r2 < 1/eps and logarithm(Q(2))[1] < 1
    assert data48['curvature'][1] < 40 and data48['hessian'][1] < -269960
    assert data48['acceleration'][0] > 0

    band0 = mat([[Q(49, 100), Q(1, 100), Q(1, 100)],
                 [Q(1, 100), Q(1, 2), Q(1, 100)],
                 [Q(1, 100), Q(1, 100), Q(51, 100)]])
    band1 = add(band0, pmat, Q(1, 20))
    assert band0 == mat(old48['band_example_K0']) and band1 == mat(old48['band_example_K1'])
    band_rows = []
    for kernel in [band0, band1]:
        bound = max(sum(abs(x) for x in row) for row in add(kernel, eye(3), -Q(1, 2)))
        assert bound <= Q(8, 100) < Q(3, 20)
        band_rows.append(bound)
        atoms = kernel_atoms(kernel, pmat)
        assert len({a['p'] for a in atoms if len(a['S']) == 1}) > 1
    assert mul(band0, pmat) != mul(pmat, band0)
    assert 3*logarithm(Q(13, 7))[1] < Q(180, 91) < 2

    corr = mat([[1, '1/2', '1/2'], ['1/2', 1, '1/3'], ['1/2', '1/3', 1]])
    l56 = scale(corr, 20)
    k56 = add(eye(3), inverse(add(eye(3), l56)), -1)
    assert k56 == mat(old56['K0'])
    assert k56 == scale(mat([[45580, 1290, 1290], [1290, 46080, 360], [1290, 360, 46080]]), Q(1, 49149))
    edge = mat([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    edge_data = evaluate(k56, edge, old56['edge']['atoms'])
    plane_data = evaluate(k56, pmat, old56['positive_plane']['atoms'], 2)
    for key, data in [('edge', edge_data), ('positive_plane', plane_data)]:
        assert data['fisher'] == Q(old56[key]['fisher_exact'])
        for old_key, new_key in [('curvature', 'curvature'), ('entropy_hessian', 'hessian'),
                                 ('nonlinear_L_correction', 'acceleration')]:
            check_source_enclosure(old56[key][old_key], data[new_key])
    assert edge_data['fisher'] == Q(24241, 294894)
    assert plane_data['fisher'] == Q(38627782337, 1327023000)
    differences = []
    for shift in [Q(0), Q(1)]:
        d0 = principal_trace(corr, [1, 2], shift)-principal_trace(corr, [1], shift)-principal_trace(corr, [2], shift)
        d1 = principal_trace(corr, [0, 1, 2], shift)-principal_trace(corr, [0, 1], shift)-principal_trace(corr, [0, 2], shift)+principal_trace(corr, [0], shift)
        differences.append([d0, d1])
    assert differences == [[Q(1, 4), Q(-1, 30)], [Q(1, 35), Q(1, 150)]]
    j0, j20 = resolvent(edge_data, Q(0)), resolvent(edge_data, Q(20))
    assert j0 == Q(35, 27432) > 0 and j20 == Q(-991, 1200150) < 0
    a11 = k56[0][0]
    expected_ddp = [-2*(1-a11), -2*a11, 2*(1-a11), 2*a11,
                    2*(1-a11), 2*a11, -2*(1-a11), -2*a11]
    assert [a['ddp'] for a in edge_data['atoms']] == expected_ddp
    # Coefficients of u^-1 and u^-2 vanish; u^-3 independently by principal powers.
    moment_coefficients = []
    for degree in range(3):
        total = Q(0)
        for a in edge_data['atoms']:
            local = sub(l56, a['S'])
            power = eye(len(local))
            for _ in range(degree):
                power = mul(power, local)
            total += a['ddp']*((-1)**degree)*trace(power)
        moment_coefficients.append(total)
    assert moment_coefficients == [0, 0, Q(-1600, 9)]
    # Post-audit extension: exact polynomial proof of a unique sign crossing.
    # x = 1+u/20; D(x) = det(C0+(x-1)I).
    dpoly = [Q(1, 6), -Q(11, 18), Q(0), Q(1)]
    qpoly = [-Q(1, 4), Q(0), Q(1)]
    dprime = [-Q(11, 18), Q(0), Q(3)]
    d1numerator = polynomial_add(
        polynomial_mul(polynomial_mul([Q(0), Q(1)], qpoly), dprime),
        polynomial_mul(polynomial_add(qpoly, [Q(0), Q(0), Q(4)], -1), dpoly))
    cubic = [Q(-3), Q(22), Q(-36), Q(16)]
    assert d1numerator == [x/72 for x in cubic]+[Q(0), Q(0)]
    quadratic = [-Q(1, 2), Q(1, 3), Q(1)]
    numerator_x = polynomial_add(
        [1328*x for x in polynomial_mul(qpoly, quadratic)],
        [1060*x for x in polynomial_mul([Q(1, 3), Q(1)], cubic)])
    numerator_x = [Q(3, 2)*x for x in numerator_x]
    assert numerator_x == [Q(-1341), Q(6724), Q(14406), Q(-48096), Q(27432)]
    numerator_y = [sum((numerator_x[k]*comb(k, j)
                       for k in range(j, len(numerator_x))), Q(0))
                   for j in range(len(numerator_x))]
    assert numerator_y == [Q(-875), Q(976), Q(34710), Q(61632), Q(27432)]
    assert all(x > 0 for x in numerator_y[1:])
    evaluate_poly = lambda p, z: sum((c*z**j for j, c in enumerate(p)), Q(0))
    assert evaluate_poly(numerator_y, Q(1, 8)) < 0
    assert evaluate_poly(numerator_y, Q(2, 15)) > 0
    for u in [Q(0), Q(5, 2), Q(8, 3), Q(20)]:
        x = 1+u/20
        denominator = 1234440*x*(x*x-Q(1, 4))*(x*x-Q(1, 9))*(x*x+x/3-Q(1, 2))
        assert -evaluate_poly(numerator_y, u/20)/denominator == resolvent(edge_data, u)
    det_ratio0 = det(sub(l56, [1, 2]))/(l56[1][1]*l56[2][2])
    det_ratio1 = det(l56)*l56[0][0]/(det(sub(l56, [0, 1]))*det(sub(l56, [0, 2])))
    assert det_ratio0 == Q(8, 9) and det_ratio1 == Q(80, 81)
    integrated = interval_add([interval_scale(2*(1-a11), logarithm(det_ratio0)),
                               interval_scale(2*a11, logarithm(det_ratio1))])
    check_source_enclosure(old56['resolvent']['integrated_curvature_closed_formula'], integrated)
    assert integrated[1] < 0 and edge_data['hessian'][1] < 0
    assert any(a['kappa'] < 0 for a in edge_data['atoms'])

    assert det(corr) == Q(5, 9)
    tbound = logarithm(Q(9, 5))
    check_source_enclosure(old56['dependence_bound']['minus_log_det_correlation'], tbound)
    theorem_bound = interval_add([(-plane_data['fisher'], -plane_data['fisher']),
                                 interval_scale(plane_data['fisher']/2, tbound)])
    check_source_enclosure(old56['dependence_bound']['positive_plane_hessian_upper_bound'], theorem_bound)
    assert plane_data['hessian'][1] < theorem_bound[0] < 0

    eta = Q(1, 1000)
    k1 = add(k56, pmat, eta)
    assert k1 == mat(old56['complete_segment']['K1'])
    assert mul(k56, pmat) != mul(pmat, k56)
    norm_bound = eta*41**2/(1-41*eta)
    correlation_lower = det(l56)/22**3
    assert norm_bound == Q(1681, 959) < 2
    assert correlation_lower == Q(5000, 11979)
    assert Q(1, 41)-eta > 0
    assert Q(11979, 5000) < Q(12, 5) < Q(8, 3)
    assert logarithm(1/correlation_lower)[1] < 1
    assert det(l56) == Q(40000, 9) and logarithm(det(l56))[0] > 2
    for point in [k56, add(k56, pmat, eta/2), k1]:
        data = evaluate(point, pmat, rank=2)
        assert all(data['L'][i][i] < 22 for i in range(3))
        assert det(data['L']) >= det(l56)
    gap = interval_add([entropy_interval(kernel_atoms(add(k56, pmat, eta/2), pmat)),
                        interval_scale(-Q(1, 2), entropy_interval(edge_data['atoms'])),
                        interval_scale(-Q(1, 2), entropy_interval(kernel_atoms(k1, pmat)))])
    check_source_enclosure(old56['complete_segment']['midpoint_chord_gap'], gap)
    assert gap[0] > Q(1, 3000000)
    assert Q(4, 3)*eta**2 == Q(1, 750000)

    inputs = ['agents/048.md', 'agents/056.md',
              'computations/048_l_ensemble_certificate.py',
              'computations/048_l_ensemble_certificate_output.json',
              'computations/056_resolvent_certificate.py',
              'computations/056_resolvent_certificate.json']
    result = {
        'worker': '066', 'audit_status': 'All independent exact comparisons passed',
        'input_sha256': {p: hashlib.sha256((SESSION/p).read_bytes()).hexdigest() for p in inputs},
        'method': 'Inclusion-exclusion of recursive principal-determinant polynomials; cofactor inverses; base-3/2 alternating logarithm intervals',
        '048': {'atoms': data48['atoms'], 'fisher': data48['fisher'],
                'one_point_fisher': fisher1, 'residual_fisher': residual,
                'curvature': round_interval(data48['curvature']),
                'hessian': round_interval(data48['hessian']),
                'nonlinear_L_acceleration': round_interval(data48['acceleration']),
                'direct_L_affine_hessian': round_interval(data48['linear_hessian']),
                'spectral_band_row_norm_bounds': band_rows},
        '056': {'edge_atoms': edge_data['atoms'], 'plane_atoms': plane_data['atoms'],
                'edge_fisher': edge_data['fisher'], 'plane_fisher': plane_data['fisher'],
                'edge_curvature': round_interval(edge_data['curvature']),
                'edge_hessian': round_interval(edge_data['hessian']),
                'plane_hessian': round_interval(plane_data['hessian']),
                'resolvent_differences': differences,
                'J_at_0': j0, 'J_at_20': j20,
                'resolvent_large_u_coefficients': moment_coefficients,
                'post_audit_exact_sign_change': {
                    'variable': 'y=u/20, x=1+y',
                    'numerator_ascending_coefficients': numerator_y,
                    'formula': 'J(u)=-N(u/20)/(1234440*x*(x^2-1/4)*(x^2-1/9)*(x^2+x/3-1/2))',
                    'unique_positive_zero_bracket_u': [Q(5, 2), Q(8, 3)]},
                'integrated_J': round_interval(integrated),
                'norm_increment_bound': norm_bound, 'correlation_determinant_lower_bound': correlation_lower,
                'midpoint_gap': round_interval(gap), 'chord_coefficient': Q(1, 750000)},
        'limits': 'This certificate checks exact examples and stored artifacts. General proofs and domain/convergence audits are in agents/066.md. Full Lyons remains open.'}

    def encode(obj):
        if isinstance(obj, Q):
            return str(obj)
        raise TypeError(type(obj).__name__)

    path = HERE/'066_independent_audit.json'
    path.write_text(json.dumps(result, default=encode, indent=2)+'\n')
    print(json.dumps({'status': result['audit_status'],
                      'J_at_0': str(j0), 'J_at_20': str(j20),
                      'edge_fisher': str(edge_data['fisher']),
                      'all_source_exact_enclosures_verified': True,
                      'artifact': str(path)}, indent=2))


if __name__ == '__main__':
    main()
