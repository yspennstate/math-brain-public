"""Exact, bounded standard-library checks for PROOF.md; no simulations."""
from fractions import Fraction as F
from math import comb, factorial


def p_add(a, b):
    out = a.copy()
    for powers, coefficient in b.items():
        out[powers] = out.get(powers, F(0)) + coefficient
    return {powers: coefficient for powers, coefficient in out.items() if coefficient}


def p_scale(a, scale):
    return {powers: scale * coefficient for powers, coefficient in a.items() if scale * coefficient}


def p_mul(a, b):
    out = {}
    for (i, j), v in a.items():
        for (k, ell), w in b.items():
            powers = (i+k, j+ell)
            out[powers] = out.get(powers, F(0)) + v*w
    return {powers: coefficient for powers, coefficient in out.items() if coefficient}


def p_diff(a, slot):
    out = {}
    for powers, coefficient in a.items():
        if powers[slot]:
            lower = list(powers)
            lower[slot] -= 1
            out[tuple(lower)] = coefficient*powers[slot]
    return out


ONE, W, P = {(0, 0): F(1)}, {(1, 0): F(1)}, {(0, 1): F(1)}


def univariate_product(a, b):
    out = [F(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def ordinary_basis(nodes, index):
    out = [F(1)]
    for j, node in enumerate(nodes):
        if j != index:
            out = univariate_product(out, [-node/(nodes[index]-node), 1/(nodes[index]-node)])
    return out


def inherited_independent_recheck():
    expected = [F(4), F(10), F(16), F(694, 27), F(983, 27), F(6698, 125)]
    for order, target in zip(range(3, 9), expected):
        nodes = [F(i, order-2) for i in range(order-1)]
        nodal = [F(1)]
        for node in nodes:
            nodal = univariate_product(nodal, [-node, F(1)])
        weights = []
        for index in range(len(nodes)):
            basis = ordinary_basis(nodes, index) + [F(0)]
            correction = -basis[1]/nodal[1]
            hermite = [x+correction*y for x, y in zip(basis, nodal)]
            assert hermite[1] == 0
            weights.append(sum(F(j, j-1)*hermite[j] for j in range(2, order)))
        assert sum(map(abs, weights)) == target
        for degree in [0] + list(range(2, order)):
            moment = sum(weight*node**degree for weight, node in zip(weights, nodes))
            assert moment == (F(degree, degree-1) if degree else 0)
    r_values = [F(1, 3), F(1, 10**12), F(1, 10**50)]
    for r in r_values:
        s = F(2, 7)
        for q in [F(-3), F(1, 5)]:
            for d in [F(7, 3), F(-2)]:
                for w in [F(-4, 9), F(5)]:
                    assert -q*d*(-r*w)/(r*s) == q*d*w/s
    assert F(1, 2)-F(5, 640) == F(63, 128) > F(1, 3)
    assert F(1, 3)-F(1, 4) == F(1, 12)
    print('Inherited recheck: Hermite bases by nodal correction (orders 3..8), coefficient cancellation, 63/128 and 1/12: PASS')


def stationary_operators():
    # Raw Gaussian moments, without quadrature or random sampling.
    cases = 0
    for q in [F(3, 4), F(7, 6)]:
        for mean in [F(0), F(3, 2), F(10**12)]:
            b = -q*mean
            scores = [p_add(p_scale(W, q), p_scale(ONE, b)), P]

            def expectation(poly):
                def moments(mu, variance, degree):
                    out = [F(1), mu]
                    for j in range(2, degree+1):
                        out.append(mu*out[-1]+(j-1)*variance*out[-2])
                    return out
                mw, mp = moments(mean, 1/q, 16), moments(F(0), F(1), 16)
                return sum(value*mw[i]*mp[j] for (i, j), value in poly.items())

            def divergence(v):
                out = {}
                for slot in range(2):
                    out = p_add(out, p_add(p_scale(p_diff(v[slot], slot), -1), p_mul(scores[slot], v[slot])))
                return out

            def generator(phi):
                # Hamiltonian vector field, independent of weighted-divergence code.
                return p_add(p_mul(P, p_diff(phi, 0)), p_scale(p_mul(scores[0], p_diff(phi, 1)), -1))

            v = [p_add(p_add(p_mul(W, W), p_mul(W, P)), p_scale(P, 2)),
                 p_add(p_add(p_mul(W, p_mul(P, P)), p_scale(W, -3)), ONE)]
            div = divergence(v)
            direct = expectation(p_mul(div, div))
            cross = sum(expectation(p_mul(p_diff(v[i], j), p_diff(v[j], i)))
                        for i in range(2) for j in range(2))
            hessian = q*expectation(p_mul(v[0], v[0])) + expectation(p_mul(v[1], v[1]))
            assert direct == cross+hessian
            upper = sum(expectation(p_mul(p_diff(v[i], j), p_diff(v[i], j)))
                        for i in range(2) for j in range(2))
            upper += max(q, 1)*sum(expectation(p_mul(x, x)) for x in v)
            assert 0 <= direct <= upper

            x = p_add(W, p_scale(ONE, -mean))
            alpha, beta = F(2, 9), F(0)
            phi = p_add(p_scale(x, alpha), p_scale(ONE, 10**15))
            for k in range(1, 9):
                raw = generator(phi)
                via_adjoint = divergence([p_scale(p_diff(phi, 1), -1), p_diff(phi, 0)])
                assert raw == via_adjoint
                alpha, beta = -q*beta, alpha
                closed = p_add(p_scale(x, alpha), p_scale(P, beta))
                assert raw == closed
                assert expectation(p_mul(raw, raw)) == alpha**2/q + beta**2
                assert expectation(raw) == 0
                phi = raw
            cases += 1
    print(f'Weighted-divergence identity/inequality and harmonic generator: {cases} translated quadratics, derivatives 1..8: PASS')


def stencil_and_exponents():
    for order in range(2, 10):
        nodes = list(map(F, range(order)))
        direct = [ordinary_basis(nodes, j)[1] for j in range(order)]
        closed = [-sum(F(1, j) for j in range(1, order))]
        closed += [F((-1)**(j+1)*comb(order-1, j), j) for j in range(1, order)]
        assert direct == closed
        for power in range(order):
            assert sum(weight*node**power for weight, node in zip(direct, nodes)) == F(power == 1)
        omitted = sum(weight*node**order for weight, node in zip(direct, nodes))
        assert omitted == (-1)**order*factorial(order-1)
        # Second derivation: the interpolant of z^m is z^m minus its nodal product.
        nodal = [F(1)]
        for node in nodes:
            nodal = univariate_product(nodal, [-node, F(1)])
        assert omitted == -nodal[1]
        for t in [F(1, 1000), F(1, 2000)]:
            angle = 4*t*(order-1)-t*(2*order-1)
            harmonic = 4*t*order-t*(2*order-1)
            assert angle == 2*t*order-3*t
            assert harmonic == 2*t*order+t
            assert angle - (2*t*order-4*t) == t
            assert harmonic - 2*t*order == t

    # Propagate inverse-R exponents from each base hypothesis, without substituting the claimed answer.
    for base_shift in [-1, 0]:
        previous = {j: j+base_shift for j in range(1, 25)}
        for k in range(1, 7):
            current = {}
            for j in range(0, 24-2*k):
                candidates = [previous[j+1], previous[j+2]]
                candidates += [v-1+previous[j-v+1] for v in range(1, j+1)]
                current[j] = max(candidates)
                assert current[j] == j+2*k+base_shift
            previous = current
    print('Angle weights/orders 2..9: basis derivative = closed formula; first omitted moment by two methods: PASS')
    print('Derivative-exponent recursion: R^(-(j+2k-1)); weaker base loses the R gain: PASS')
    print('Delta exponents by two forms: angle 2tm-3t; harmonic 2tm+t; both gain t: PASS')
    correlated_variance = F(1, 2)+F(1, 2)+2*F(1, 2)
    assert correlated_variance == 2
    print('Correlated-anchor failure: Var(W_pi/4)=2 versus stationary variance 1 (exact identity).')


if __name__ == '__main__':
    inherited_independent_recheck()
    stationary_operators()
    stencil_and_exponents()
