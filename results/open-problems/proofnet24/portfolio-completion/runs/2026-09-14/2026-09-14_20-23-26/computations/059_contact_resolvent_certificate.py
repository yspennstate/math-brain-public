#!/usr/bin/env python3
"""Exact certificate for fresh chronological two-tag contact transforms.

Finite verification only: kill the relative displacement when it leaves the
l1-ball of radius 2 in Z^3. Every unoriented lattice edge parallel to coordinate
i rings at rate c_i, with c=(1,2,2). The relative generator is independently
built by enumerating the physical edges incident to the two tagged positions.

Run: python computations/059_contact_resolvent_certificate.py
Uses only Python's standard library and exact Fraction arithmetic.
No Monte Carlo, floating point, network, or shell subcalls.
"""

from itertools import product
from fractions import Fraction as F


class Matrix:
    """Minimal exact matrices; elimination is deliberately visible here."""

    def __init__(self, rows):
        self.rows = [[F(x) for x in row] for row in rows]
        self.n = len(self.rows)
        self.m = len(self.rows[0])

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return self.rows[key[0]][key[1]]
        assert self.m == 1
        return self.rows[key][0]

    def __setitem__(self, key, value):
        self.rows[key[0]][key[1]] = F(value)

    def __iter__(self):
        assert self.m == 1
        return iter(row[0] for row in self.rows)

    def __eq__(self, other):
        return self.rows == other.rows

    def __repr__(self):
        return '[' + ', '.join('[' + ', '.join(map(str, row)) + ']'
                               for row in self.rows) + ']'

    def __add__(self, other):
        return Matrix([[self[i, j] + other[i, j] for j in range(self.m)]
                       for i in range(self.n)])

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            assert self.m == other.n
            return Matrix([[sum(self[i, k] * other[k, j] for k in range(self.m))
                            for j in range(other.m)] for i in range(self.n)])
        return Matrix([[x * other for x in row] for row in self.rows])

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * (F(1) / other)

    def __pow__(self, power):
        assert power == 2
        return self * self

    @property
    def T(self):
        return Matrix([[self[j, i] for j in range(self.n)] for i in range(self.m)])

    def extract(self, rows, columns):
        return Matrix([[self[i, j] for j in columns] for i in rows])

    def inv(self):
        assert self.n == self.m
        n = self.n
        augmented = [self.rows[i][:] + [F(i == j) for j in range(n)] for i in range(n)]
        for col in range(n):
            pivot = next(i for i in range(col, n) if augmented[i][col])
            augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
            factor = augmented[col][col]
            augmented[col] = [x / factor for x in augmented[col]]
            for row in range(n):
                if row != col and augmented[row][col]:
                    factor = augmented[row][col]
                    augmented[row] = [x - factor * y
                                      for x, y in zip(augmented[row], augmented[col])]
        assert [row[:n] for row in augmented] == eye(n).rows
        return Matrix([row[n:] for row in augmented])


def zeros(n):
    return Matrix([[0] * n for _ in range(n)])


def eye(n):
    return Matrix([[int(i == j) for j in range(n)] for i in range(n)])


def ones(n, m=1):
    return Matrix([[1] * m for _ in range(n)])


def diag(values):
    return Matrix([[value if i == j else 0 for j in range(len(values))]
                   for i, value in enumerate(values)])


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

    free = zeros(len(domain))
    for x in domain:
        ix = domain_index[x]
        for e, rate in steps:
            free[ix, ix] -= 2 * rate
            y = add(x, e)
            if y in domain_index:
                free[ix, domain_index[y]] += 2 * rate

    # Direct interchange construction: one clock per UNORIENTED physical edge.
    direct = zeros(ni)
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
    formula = zeros(ni)
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

    contact_correction = zeros(len(contact))
    for ia, a in enumerate(contact):
        contact_correction[ia, ia] = step_rates[a]
        contact_correction[ia, contact.index(neg(a))] = step_rates[a]

    # Free-resolvent kill-at-zero identity, then finite contact correction.
    zero_index = domain_index[origin]
    free_contact_indices = [domain_index[a] for a in contact]
    for discount in (F(0), F(1), F(7, 3)):
        free_resolvent = (discount * eye(len(domain)) - free).inv()
        killed_contact = free_resolvent.extract(free_contact_indices, free_contact_indices)
        to_zero = free_resolvent.extract(free_contact_indices, [zero_index])
        from_zero = free_resolvent.extract([zero_index], free_contact_indices)
        killed_contact -= to_zero * from_zero / free_resolvent[zero_index, zero_index]
        predicted = (killed_contact.inv() - contact_correction).inv()
        observed = (discount * eye(ni) - direct).inv().extract(
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
    quotient = zeros(2)
    for i, orbit in enumerate(orbits):
        representative = orbit[0]
        for j, target in enumerate(orbits):
            quotient[i, j] = sum(trace[representative, b] for b in target)
            for a in orbit:
                assert sum(trace[a, b] for b in target) == quotient[i, j]
    assert quotient == Matrix([[-73, 8], [4, -58]]) / 5
    killing = -quotient * ones(2)
    assert killing == Matrix([[13], [F(54, 5)]])

    # Cramer's rule gives exact POLYNOMIAL coefficients, beyond point checks.
    a, b = quotient[0, 0], quotient[0, 1]
    c, d = quotient[1, 0], quotient[1, 1]
    denominator = [F(1), -a-d, a*d-b*c]
    numerators = [[killing[0], -d*killing[0]+b*killing[1]],
                  [killing[1], -a*killing[1]+c*killing[0]]]
    assert [25*x for x in denominator] == [25, 655, 4202]
    assert [[25*x for x in row] for row in numerators] == [[325, 4202], [270, 4202]]

    def transform(i, s):
        return (numerators[i][0]*s + numerators[i][1]) / (
            denominator[0]*s*s + denominator[1]*s + denominator[2])

    # Full finite-state Feynman--Kac equation: death has terminal value one.
    reward = diag([int(x in contact) for x in states])
    physical_killing = -direct * ones(ni)
    for laplace in (F(0), F(1), F(7, 3)):
        exact_values = (-direct + laplace * reward).inv() * physical_killing
        assert exact_values[state_index[units[0]]] == transform(0, laplace)
        assert exact_values[state_index[units[1]]] == transform(1, laplace)

    first_derivative = quotient * ones(2)
    second_derivative = quotient**2 * ones(2)
    defects = [second_derivative[i] - first_derivative[i]**2
               for i in range(2)]
    assert defects == [F(88, 25), -F(44, 25)]

    # Exact short-return lower bound used in the infinite Z^4 proof.
    signed_units = [e for v in units for e in (v, neg(v))]
    four_step_returns = sum(
        all(sum(path[t][i] for t in range(4)) == 0 for i in range(dim))
        for path in product(signed_units, repeat=4))
    assert four_step_returns == 90
    green_lower_bound = 1 + F(1, 6) + F(four_step_returns, 6**4)
    assert green_lower_bound == F(89, 72)
    assert green_lower_bound > F(6, 5)

    print('Finite killed l1-ball: dimension=3, radius=2, edge rates=(1,2,2)')
    print(f'States: {len(domain)} free, {ni} nonzero relative, {len(contact)} contact')
    print('Physical-edge enumeration equals relative-generator formula: PASS')
    print('Free rate=20; adjacent total rates=19 (c=1), 18 (c=2)')
    print('Contact resolvent identity at lambda=0,1,7/3: PASS')
    print('Trace Schur complement equals negative inverse contact Green: PASS')
    print(f'Two-type trace Q = {quotient}')
    print(f'Contact-clock killing hazards = {list(killing)}')
    print('Laplace transform from c=1 contact = (325*s+4202)/(25*s*s+655*s+4202)')
    print('Laplace transform from c=2 contact = (270*s+4202)/(25*s*s+655*s+4202)')
    print('Full-state Feynman--Kac checks at s=0,1,7/3: PASS')
    print(f'Survival second-derivative defects = {defects}')
    print(f'Z^3 four-step return paths = {four_step_returns}; G_3(0) >= {green_lower_bound} > 6/5')
    print('All exact assertions passed. This computation alone is not an infinite-volume proof.')


if __name__ == '__main__':
    main()
