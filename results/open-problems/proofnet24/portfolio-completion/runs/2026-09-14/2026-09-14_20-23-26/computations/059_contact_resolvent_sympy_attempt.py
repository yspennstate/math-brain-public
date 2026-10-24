#!/usr/bin/env python3
"""Exact certificate for fresh chronological two-tag contact transforms.

Finite verification only: kill the relative displacement when it leaves the
l1-ball of radius 2 in Z^3. Every unoriented lattice edge parallel to coordinate
i rings at rate c_i, with c=(1,2,2). The relative generator is independently
built by enumerating the physical edges incident to the two tagged positions.

Run: python computations/059_contact_resolvent_certificate.py
Dependency: sympy. No Monte Carlo, floating point, network, or shell subcalls.
"""

from itertools import product
import sympy as sp


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def neg(x):
    return tuple(-a for a in x)


def main():
    dim = 3
    rates = (1, 2, 2)
    origin = (0,) * dim
    units = [tuple(int(i == j) for i in range(dim)) for j in range(dim)]
    steps = [(e, rates[i]) for i, v in enumerate(units) for e in (v, neg(v))]
    domain = sorted(x for x in product(range(-2, 3), repeat=dim)
                    if sum(abs(v) for v in x) <= 2)
    states = [x for x in domain if x != origin]
    contact = [e for v in units for e in (v, neg(v))]
    outside_contact = [x for x in states if x not in contact]
    domain_index = {x: i for i, x in enumerate(domain)}
    state_index = {x: i for i, x in enumerate(states)}
    contact_indices = [state_index[x] for x in contact]
    outside_indices = [state_index[x] for x in outside_contact]
    ni = len(states)

    free = sp.zeros(len(domain))
    for x in domain:
        ix = domain_index[x]
        for e, rate in steps:
            free[ix, ix] -= 2 * rate
            y = add(x, e)
            if y in domain_index:
                free[ix, domain_index[y]] += 2 * rate

    # Direct interchange construction: one clock per UNORIENTED physical edge.
    direct = sp.zeros(ni)
    for z in states:
        iz = state_index[z]
        incident_edges = {}
        for tag in (origin, z):
            for e, rate in steps:
                edge = tuple(sorted((tag, add(tag, e))))
                if edge in incident_edges:
                    assert incident_edges[edge] == rate
                incident_edges[edge] = rate
        for (u, v), rate in incident_edges.items():
            x_after = v if origin == u else u if origin == v else origin
            y_after = v if z == u else u if z == v else z
            displacement = sub(y_after, x_after)
            assert displacement != origin
            assert displacement != z
            direct[iz, iz] -= rate
            if displacement in state_index:
                direct[iz, state_index[displacement]] += rate

    # Separately stated relative formula: independent jumps, omit collision,
    # add the one common-edge swap at rate c_i.
    formula = sp.zeros(ni)
    step_rates = dict(steps)
    for z in states:
        iz = state_index[z]
        for e, rate in steps:
            y = add(z, e)
            if y == origin:
                continue
            formula[iz, iz] -= 2 * rate
            if y in state_index:
                formula[iz, state_index[y]] += 2 * rate
        if z in step_rates:
            rate = step_rates[z]
            formula[iz, iz] -= rate
            formula[iz, state_index[neg(z)]] += rate
    assert direct == formula
    assert direct == direct.T
    assert -direct[state_index[units[0]], state_index[units[0]]] == 19
    assert -direct[state_index[units[1]], state_index[units[1]]] == 18
    assert -direct[state_index[(1, 1, 0)], state_index[(1, 1, 0)]] == 20

    contact_correction = sp.zeros(len(contact))
    for ia, a in enumerate(contact):
        contact_correction[ia, ia] = step_rates[a]
        contact_correction[ia, contact.index(neg(a))] = step_rates[a]

    # Free-resolvent kill-at-zero identity, then finite contact correction.
    zero_index = domain_index[origin]
    free_contact_indices = [domain_index[a] for a in contact]
    for discount in (sp.Integer(0), sp.Integer(1), sp.Rational(7, 3)):
        free_resolvent = (discount * sp.eye(len(domain)) - free).inv()
        killed_contact = free_resolvent.extract(free_contact_indices, free_contact_indices)
        to_zero = free_resolvent.extract(free_contact_indices, [zero_index])
        from_zero = free_resolvent.extract([zero_index], free_contact_indices)
        killed_contact -= to_zero * from_zero / free_resolvent[zero_index, zero_index]
        predicted = (killed_contact.inv() - contact_correction).inv()
        observed = (discount * sp.eye(ni) - direct).inv().extract(
            contact_indices, contact_indices)
        assert predicted == observed

    # Trace generator from excursion elimination, independently of resolvents.
    laa = direct.extract(contact_indices, contact_indices)
    lab = direct.extract(contact_indices, outside_indices)
    lba = direct.extract(outside_indices, contact_indices)
    lbb = direct.extract(outside_indices, outside_indices)
    trace = laa + lab * (-lbb).inv() * lba
    green_contact = (-direct).inv().extract(contact_indices, contact_indices)
    assert trace == -green_contact.inv()
    assert trace == trace.T
    assert all(trace[i, j] >= 0 for i in range(6) for j in range(6) if i != j)

    # Lump the two c=1 directions and the four c=2 directions.
    orbits = [[0, 1], [2, 3, 4, 5]]
    quotient = sp.zeros(2)
    for i, orbit in enumerate(orbits):
        representative = orbit[0]
        for j, target in enumerate(orbits):
            quotient[i, j] = sum(trace[representative, b] for b in target)
            for a in orbit:
                assert sum(trace[a, b] for b in target) == quotient[i, j]
    assert quotient == sp.Matrix([[-73, 8], [4, -58]]) / 5
    killing = -quotient * sp.ones(2, 1)
    assert killing == sp.Matrix([13, sp.Rational(54, 5)])

    s = sp.symbols('s', nonnegative=True)
    transforms = (s * sp.eye(2) - quotient).inv() * killing
    transforms = transforms.applyfunc(sp.factor)
    denominator = 25 * s**2 + 655 * s + 4202
    assert sp.cancel(transforms[0] - (325 * s + 4202) / denominator) == 0
    assert sp.cancel(transforms[1] - (270 * s + 4202) / denominator) == 0

    # Full finite-state Feynman--Kac equation: death has terminal value one.
    reward = sp.diag(*(int(x in contact) for x in states))
    physical_killing = -direct * sp.ones(ni, 1)
    for laplace in (sp.Integer(0), sp.Integer(1), sp.Rational(7, 3)):
        exact_values = (-direct + laplace * reward).inv() * physical_killing
        assert exact_values[state_index[units[0]]] == transforms[0].subs(s, laplace)
        assert exact_values[state_index[units[1]]] == transforms[1].subs(s, laplace)

    first_derivative = quotient * sp.ones(2, 1)
    second_derivative = quotient**2 * sp.ones(2, 1)
    defects = [sp.factor(second_derivative[i] - first_derivative[i]**2)
               for i in range(2)]
    assert defects == [sp.Rational(88, 25), -sp.Rational(44, 25)]

    # Exact short-return lower bound used in the infinite Z^4 proof.
    signed_units = [e for v in units for e in (v, neg(v))]
    four_step_returns = sum(
        all(sum(path[t][i] for t in range(4)) == 0 for i in range(dim))
        for path in product(signed_units, repeat=4))
    assert four_step_returns == 90
    green_lower_bound = 1 + sp.Rational(1, 6) + sp.Rational(four_step_returns, 6**4)
    assert green_lower_bound == sp.Rational(89, 72)
    assert green_lower_bound > sp.Rational(6, 5)

    print('Finite killed l1-ball: dimension=3, radius=2, edge rates=(1,2,2)')
    print(f'States: {len(domain)} free, {ni} nonzero relative, {len(contact)} contact')
    print('Physical-edge enumeration equals relative-generator formula: PASS')
    print('Free rate=20; adjacent total rates=19 (c=1), 18 (c=2)')
    print('Contact resolvent identity at lambda=0,1,7/3: PASS')
    print('Trace Schur complement equals negative inverse contact Green: PASS')
    print(f'Two-type trace Q = {quotient}')
    print(f'Contact-clock killing hazards = {list(killing)}')
    print(f'Laplace transform from c=1 contact = {transforms[0]}')
    print(f'Laplace transform from c=2 contact = {transforms[1]}')
    print('Full-state Feynman--Kac checks at s=0,1,7/3: PASS')
    print(f'Survival second-derivative defects = {defects}')
    print(f'Z^3 four-step return paths = {four_step_returns}; G_3(0) >= {green_lower_bound} > 6/5')
    print('All exact assertions passed. This computation alone is not an infinite-volume proof.')


if __name__ == '__main__':
    main()
