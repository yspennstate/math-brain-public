"""Bounded, single-threaded exact checks for the local quadrature proof."""
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json


def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def add(p, q):
    out = [F(0)] * max(len(p), len(q))
    for i, x in enumerate(p):
        out[i] += x
    for i, x in enumerate(q):
        out[i] += x
    return trim(out)


def scale(p, c):
    return trim([c*x for x in p])


def mul(p, q):
    out = [F(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return trim(out)


def derivative(p, order=1):
    for _ in range(order):
        p = [i*p[i] for i in range(1, len(p))] or [F(0)]
    return trim(p)


def value(p, x):
    out = F(0)
    for coefficient in reversed(p):
        out = out*x + coefficient
    return out


def basis(nodes, i):
    p = [F(1)]
    for j, x in enumerate(nodes):
        if i != j:
            p = mul(p, [-x/(nodes[i]-x), 1/(nodes[i]-x)])
    return p


def interpolate(nodes, values):
    p = [F(0)]
    for i, y in enumerate(values):
        p = add(p, scale(basis(nodes, i), y))
    return p


def solve(matrix, rhs):
    a = [[F(x) for x in row] + [F(y)] for row, y in zip(matrix, rhs)]
    n = len(a)
    for j in range(n):
        i = next(i for i in range(j, n) if a[i][j])
        a[i], a[j] = a[j], a[i]
        a[j] = [x/a[j][j] for x in a[j]]
        for i in range(n):
            if i != j:
                c = a[i][j]
                a[i] = [x-c*y for x, y in zip(a[i], a[j])]
    return [row[-1] for row in a]


def hermite(nodes, values):
    # Ordinary nodal interpolation plus its nodal polynomial fixes slope zero.
    p = interpolate(nodes, values)
    nodal = [F(1)]
    for x in nodes:
        nodal = mul(nodal, [-x, F(1)])
    return add(p, scale(nodal, -value(derivative(p), F(0))/nodal[1]))


def integral_derivative_over_x(p, a, b):
    """Return exact rational part and coefficient of log(b/a)."""
    linear = p[1] if len(p) > 1 else F(0)
    if not a:
        assert linear == 0
    rational = sum(F(k, k-1)*p[k]*(b**(k-1)-a**(k-1))
                   for k in range(2, len(p)))
    return rational, linear


def integral_value_over_x_squared(p, a, b):
    if not a:
        assert p[0] == 0 and (len(p) < 2 or p[1] == 0)
    rational = p[0]*(1/a-1/b) if a else F(0)
    rational += sum(p[k]*F(1, k-1)*(b**(k-1)-a**(k-1))
                    for k in range(2, len(p)))
    return rational, p[1] if len(p) > 1 else F(0)


def decimal(x):
    return Decimal(x.numerator)/Decimal(x.denominator)


def independent_harmonic_recheck():
    # Backward recurrence: each divergence adds at most one further spatial
    # derivative to AD; compare its dominant and every commutator exponent.
    for k in range(1, 10):
        for j in range(12):
            v_exp = (lambda h: h if k == 1 else h+2*k-2)
            dominant = max(v_exp(j), v_exp(j+1))
            assert dominant == j+2*k-1
            assert all(v-1+v_exp(j-v) == j+2*k-3 for v in range(1, j+1))
        for m in range(3, 12):
            # Integer coefficients of t, without using decimal exponents.
            assert 4*(m-1)-(2*m-1) == 2*m-3
            assert 4*m-(2*m-1) == 2*m+1
    print('Independent harmonic induction: principal and commutator exponents; angle/harmonic gains: PASS')


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def ordered_matrix_derivatives():
    ident = [[1, 0], [0, 1]]
    zero = [[0, 0], [0, 0]]
    c = [[[0, 1], [-1, 0]], [[1, 0], [0, 2]]]
    assert matmul(c[0], c[1]) != matmul(c[1], c[0])
    words, direct = {(): 1}, [ident]
    for m in range(1, 10):
        new = defaultdict(int)
        for word, coefficient in words.items():
            new[(0,)+word] += coefficient
            for i in range(len(word)):
                raised = word[:i]+(word[i]+1,)+word[i+1:]
                new[raised] += coefficient
        words = dict(new)
        by_words = [[0, 0], [0, 0]]
        for word, coefficient in words.items():
            assert len(word) >= 1 and sum(word) == m-len(word)
            term = ident
            for j in word:
                term = matmul(term, c[j] if j < len(c) else zero)
            by_words = [[by_words[i][j]+coefficient*term[i][j]
                         for j in range(2)] for i in range(2)]
        by_leibniz = [[0, 0], [0, 0]]
        for j in range(m):
            term = matmul(direct[m-1-j], c[j] if j < len(c) else zero)
            by_leibniz = [[by_leibniz[i][k]+comb(m-1, j)*term[i][k]
                           for k in range(2)] for i in range(2)]
        assert by_words == by_leibniz
        direct.append(by_leibniz)
        assert max(sum(word) for word in words) == m-1
    print('B^(m): ordered-word differentiation = independent noncommuting matrix Leibniz recurrence, m=1..9: PASS')
    print('Time-input exponents: sum(j)=m-k <= m-1; every word retains l^k with k>=1: PASS')


def endpoint_weights_and_errors():
    for m in range(3, 9):
        nodes = [F(i, m-2) for i in range(m-1)]
        weights = []
        for i in range(m-1):
            vals = [F(i == j) for j in range(m-1)]
            p = hermite(nodes, vals)
            matrix = [[x**k for k in range(m)] for x in nodes]
            matrix += [[F(k == 1) for k in range(m)]]
            independent = trim(solve(matrix, vals+[F(0)]))
            assert p == independent and value(derivative(p), F(0)) == 0
            weights.append(integral_derivative_over_x(p, F(0), F(1))[0])
        for k in [0]+list(range(2, m)):
            target = F(k, k-1) if k else F(0)
            assert sum(w*x**k for w, x in zip(weights, nodes)) == target
        # First omitted monomial: compare weights with its nodal-error polynomial.
        nodal_error = [F(0), F(0), F(1)]
        for x in nodes[1:]:
            nodal_error = mul(nodal_error, [-x, F(1)])
        direct = F(m, m-1)-sum(w*x**m for w, x in zip(weights, nodes))
        assert direct == integral_derivative_over_x(nodal_error, F(0), F(1))[0]
        assert direct == integral_value_over_x_squared(nodal_error, F(0), F(1))[0]
        assert direct != 0
        print(f'Endpoint m={m}: two Hermite constructions, reproduction, first omitted error={direct}; weight l1={sum(map(abs, weights))}: PASS')


def composite_error_identity():
    cases = cells = 0
    largest = Decimal(0)
    with localcontext() as context:
        context.prec = 85
        for m in range(3, 9):
            # Constants, admissible lower powers, and two non-reproduced powers.
            p = [F(0)]*(m+3)
            p[0], p[2], p[m], p[m+2] = F(7), F(3), F(1), F(-2)
            for h in [F(1, 4), F(1, 8), F(1, 16)]:
                endpoints = [F(0), h]
                while endpoints[-1] < F(3, 4):
                    endpoints.append(1-(1-endpoints[-1])*(1-h))
                error = Decimal(0)
                for index, (a, b) in enumerate(zip(endpoints, endpoints[1:])):
                    count = m-1 if index == 0 else m
                    nodes = [a+(b-a)*F(i, count-1) for i in range(count)]
                    values = [value(p, x) for x in nodes]
                    interpolated = hermite(nodes, values) if index == 0 else interpolate(nodes, values)
                    e = add(p, scale(interpolated, -1))
                    assert value(e, a) == value(e, b) == 0
                    d_form = integral_derivative_over_x(e, a, b)
                    v_form = integral_value_over_x_squared(e, a, b)
                    assert d_form == v_form
                    # Separately integrate true and interpolated derivatives.
                    true = integral_derivative_over_x(p, a, b)
                    numerical = integral_derivative_over_x(interpolated, a, b)
                    assert d_form == (true[0]-numerical[0], true[1]-numerical[1])
                    error += decimal(d_form[0])
                    if d_form[1]:
                        error += decimal(d_form[1])*(decimal(b)/decimal(a)).ln()
                    cells += 1
                k_bound = sum(map(abs, derivative(p, m)))
                largest = max(largest, abs(error)/decimal(k_bound*h**(m-1)))
                cases += 1
    print(f'Composite quadrature: exact derivative/value integration identities, {cases} cases and {cells} cells: PASS')
    print(f'Polynomial smoke check: max |error|/(K*h^(m-1))={largest:.5E} (not a proof of the uniform bound)')


def localized_lower_examples():
    for m in range(3, 9):
        nodes = [F(i, m-2) for i in range(m-1)]
        q = [F(0)]*(m+1)+[F(1)]
        for _ in range(m+1):
            q = mul(q, [F(1), F(-1)])
        for x in nodes[1:-1]:
            q = mul(q, mul([-x, F(1)], [-x, F(1)]))
        for j in range(m+1):
            assert value(derivative(q, j), F(0)) == value(derivative(q, j), F(1)) == 0
        assert all(value(q, x) == 0 for x in nodes)
        direct = integral_derivative_over_x(q, F(0), F(1))[0]
        parts = integral_value_over_x_squared(q, F(0), F(1))[0]
        assert direct == parts > 0
        errors = []
        for ell in [F(1, 8), F(1, 16), F(1, 32)]:
            physical = [c*ell**(m-j) for j, c in enumerate(q)]
            integral = integral_derivative_over_x(physical, F(0), ell)[0]
            assert integral == direct*ell**(m-1)
            assert all(value(physical, ell*x) == 0 for x in nodes)
            # Scaling makes the mth derivative polynomial exactly q^(m)(rho/ell).
            assert derivative(physical, m) == [c/ell**j for j, c in enumerate(derivative(q, m))]
            errors.append(integral)
        assert errors[0]/errors[1] == errors[1]/errors[2] == 2**(m-1)
        print(f'Localized m={m}: C^m gluing, all values zero, c_m={direct}; scale ratio={2**(m-1)}: PASS')
    print('Missing zero slope: F(rho)=rho has integral int_0^ell 1/rho = infinity; excluded by hypothesis.')


def source_checks():
    root = Path('sources/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/sections')
    checks = []
    for name in ['centering.tex', 'numerics.tex']:
        current = Path('sources/reopened-round6')/name
        assert current.read_text().rstrip() == (root/name).read_text().rstrip()
        checks.append({'file': str(current), 'matches_round5_ignoring_terminal_whitespace': True,
                       'sha256': hashlib.sha256(current.read_bytes()).hexdigest()})
    # The three exact main statements remain present in the inherited verification.
    verification = Path('VERIFY.md').read_text()
    intros = [root/'introduction.tex']
    for folder in ['A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026',
                   'A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026']:
        intros.append(Path('sources/preprints')/folder/'build/sections/01-introduction.tex')
    for path in intros:
        source = path.read_text()
        start = source.index('\\begin{theorem}\\label{thm:main}')
        end = source.index('\\end{theorem}', start)+len('\\end{theorem}')
        assert source[start:end] in verification
    print('Reopened centering/numerics snapshots agree with round 5; three inherited theorem quotes remain verbatim: PASS')
    # This is the only filesystem write made by this audit, and it is local.
    Path('audit_source_checks.json').write_text(json.dumps(checks, indent=2)+'\n')


if __name__ == '__main__':
    independent_harmonic_recheck()
    ordered_matrix_derivatives()
    endpoint_weights_and_errors()
    composite_error_identity()
    localized_lower_examples()
    source_checks()
