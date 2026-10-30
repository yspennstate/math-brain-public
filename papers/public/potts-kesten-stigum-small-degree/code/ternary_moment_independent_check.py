"""Validate the new moment certificates without importing their builders.

Exact Bayesian evaluations restore every cleared denominator and radial rescaling.
Each stored Bernstein transform is also checked by independent slice summation.
The proof interpreting these inequalities still requires mathematical review.
"""
import gc, hashlib, itertools, json, math, pathlib, time
from fractions import Fraction as F

ROOT = pathlib.Path(__file__).resolve().parent


def load(stem, phase):
    data = json.loads((ROOT / f'{stem}_{phase}.json').read_text(encoding='utf-8'))
    return {tuple(k): v for k, v in data.pop('poly')}, data


def evaluate(poly, point, degrees, bernstein=False):
    tables = []
    den = 1
    for x, n in zip(point, degrees):
        a, b = x.numerator, x.denominator
        den *= b ** n
        if bernstein:
            tables.append([math.comb(n, k) * a ** k * (b-a) ** (n-k)
                           for k in range(n+1)])
        else:
            tables.append([a ** k * b ** (n-k) for k in range(n+1)])
    return F(sum(v * math.prod(tables[i][k] for i, k in enumerate(key))
                 for key, v in poly.items()), den)


def sorted_posterior(radius, shape):
    return [(1-radius)/3, (1-radius)/3 + radius*shape/2,
            (1-radius)/3 + radius*(1-shape/2)]


def bayesian(point, meta, family):
    t, s, y, z = point
    lam = F(meta['lambda_common'])
    left = sorted_posterior(lam*t, y)
    right = sorted_posterior(lam*s, z)
    assert min(left+right) >= 0 and sum(left) == sum(right) == 1
    a = [3*v-1 for v in left]
    b = [3*v-1 for v in right]
    ma, mb = sum(v*v for v in a), sum(v*v for v in b)
    ta, tb = sum(v**3 for v in a), sum(v**3 for v in b)
    out4 = out3 = F(0)
    D = F(1)
    B = lam.denominator
    for rr in itertools.permutations(right):
        products = [9*left[i]*rr[i] for i in range(3)]
        S = sum(products)
        assert S > 0
        posterior = [v/S for v in products]
        deviations = [3*v-1 for v in posterior]
        # Six orientations, tuple density S/3 relative to product marginal laws.
        out4 += S/18 * sum(v*v for v in deviations)**2
        out3 += S/18 * sum(v**3 for v in deviations)
        D *= (4*B*B*S)**(3 if family == 'fourth' else 2)
    if family == 'fourth':
        C = F(meta['C_edge_scaled'])
        gap = lam**4*(ma*ma+mb*mb) + C*ma*mb - lam**4*out4
        denominator = 32*C.denominator*B**8*D
    else:
        C = F(meta['C_cubic'])
        sign = 1 if meta['mode'] == 'upper' else -1
        gap = sign*(ta+tb-out3) + C*ma*mb
        denominator = 144*C.denominator*B**4*D
    return gap, denominator


def verify_axis(before, after, axis, degree):
    """Group a full coefficient slice and compute each output by a dot product."""
    slices = {}
    for key, value in before.items():
        rest = key[:axis] + key[axis+1:]
        slices.setdefault(rest, {})[key[axis]] = value
    L = math.lcm(*(math.comb(degree, i) for i in range(degree+1)))
    matrix = [[math.comb(k, i)*(L//math.comb(degree, i))
               if i <= k else 0 for i in range(degree+1)]
              for k in range(degree+1)]
    expected = {}
    content = 0
    for rest, values in slices.items():
        for k in range(degree+1):
            value = sum(matrix[k][i]*v for i, v in values.items())
            if value:
                key = rest[:axis] + (k,) + rest[axis:]
                expected[key] = value
                content = math.gcd(content, value)
    assert content > 0 and len(expected) == len(after)
    assert all(after.get(key) == value//content for key, value in expected.items())


def check(stem, family):
    raw, meta = load(stem, 'raw')
    degrees = meta['degrees']
    previous = raw
    hashes = {f'{stem}_raw.json': hashlib.sha256((ROOT/f'{stem}_raw.json').read_bytes()).hexdigest()}
    for number, axis in enumerate((2, 3, 0, 1), 1):
        current, final_meta = load(stem, f'bern{number}')
        verify_axis(previous, current, axis, degrees[axis])
        if number > 1:
            del previous
        previous = current
        gc.collect()
    bern = current
    assert final_meta['status'].startswith('PASS') and min(bern.values()) > 0
    assert len(bern) == math.prod(d+1 for d in degrees)
    origin = (F(0),)*4
    factor = evaluate(bern, origin, degrees, True)/evaluate(raw, origin, degrees)
    assert factor > 0
    samples = [(F(1,2),)*4, (F(1),F(1),F(0),F(0)),
               (F(1),F(1),F(1),F(1)),
               (F(1,4),F(3,4),F(1,2),F(1,4)),
               (F(3,4),F(1,4),F(1),F(0))]
    L, R = F(meta['raw_domain_t_upper']), F(meta['raw_domain_s_upper'])
    domain_den = L.denominator**degrees[0]*R.denominator**degrees[1]
    rows = []
    for point in samples:
        value = evaluate(raw, point, degrees)
        assert evaluate(bern, point, degrees, True) == factor*value
        actual = (L*point[0], R*point[1], point[2], point[3])
        gap, denominator = bayesian(actual, meta, family)
        restored = value*int(meta['raw_gcd_divided_out'])/domain_den
        restored *= actual[0]**2*actual[1]**2
        assert gap >= 0 and restored == gap*denominator
        rows.append({'normalized_point': list(map(str, point)), 'gap': str(gap)})
    for corner in itertools.product((F(0), F(1)), repeat=4):
        assert evaluate(bern, corner, degrees, True) == factor*evaluate(raw, corner, degrees)
    hashes[f'{stem}_bern4.json'] = hashlib.sha256((ROOT/f'{stem}_bern4.json').read_bytes()).hexdigest()
    print('PASS', stem, len(bern), 'strictly positive coefficients; every transform and five exact Bayesian gaps', flush=True)
    return {'stem': stem, 'degrees': degrees, 'coefficients': len(bern),
            'minimum_positive_integer': str(min(bern.values())), 'samples': rows,
            'raw_bernstein_scale': str(factor), 'sha256': hashes}


def main():
    started = time.monotonic()
    results = [check('ternary_fourth_'+mode, 'fourth') for mode in ('prefix', 'merge')]
    results += [check('ternary_cubic_'+mode, 'cubic') for mode in ('upper', 'lower')]
    # Negative controls test the probability evaluator at weak nonuniform messages.
    point = (F(1,1000), F(1,1000), F(1,3), F(2,3))
    controls = []
    for mode, bad in (('prefix', F(2,5)), ('merge', F(39,10)*F(99,140)**4)):
        _, meta = load('ternary_fourth_'+mode, 'raw')
        meta['C_edge_scaled'] = str(bad)
        gap, _ = bayesian(point, meta, 'fourth')
        assert gap < 0
        controls.append({'fourth_mode': mode, 'bad_constant': str(bad), 'gap': str(gap)})
    # At small symmetric vectors the cubic increment is +ma*mb to leading order.
    _, meta = load('ternary_cubic_upper', 'raw')
    meta['C_cubic'] = '9/10'
    gap, _ = bayesian(point, meta, 'cubic')
    assert gap < 0
    controls.append({'cubic_bad_constant': '9/10', 'gap': str(gap)})
    out = {'status': 'PASS independent exact algebra checks',
           'scope': 'all stored axis transforms, integer signs, five exact Bayesian restorations per tensor, all 16 corners, three negative controls',
           'certificates': results, 'negative_controls': controls,
           'wall_seconds': time.monotonic()-started}
    ROOT.joinpath('ternary_moment_independent_check.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
    print(out['status'], 'seconds', round(out['wall_seconds'], 2), flush=True)


if __name__ == '__main__':
    main()
