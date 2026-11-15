"""Exact Gaussian polynomial checks; standard library, no TW simulation.

All coefficients, directions, projections, and moments are rational.
Dimension is at most four; degree is at most five. No random sampling.
"""

import os
import sys

priority = os.getpriority(os.PRIO_PROCESS, 0)
if priority < 15:
    print("NOT RUN: effective nice value is below 15")
    sys.exit(77)
if os.environ.get("OMP_NUM_THREADS") != "1":
    raise RuntimeError("Set OMP_NUM_THREADS=1")

import math
import resource
import time
from fractions import Fraction as R
from functools import lru_cache

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
started = time.monotonic()
print(f"Effective nice value: {priority}")


def check_time():
    if time.monotonic()-started > 55:
        raise RuntimeError("55-second verification budget exceeded")


def add(a, b):
    out = dict(a)
    for exponent, coefficient in b.items():
        out[exponent] = out.get(exponent, R(0))+coefficient
    return {exponent: c for exponent, c in out.items() if c}


def scale(a, c):
    return {exponent: c*coefficient for exponent, coefficient in a.items()
            if c*coefficient}


def mul(a, b):
    out = {}
    for x, c in a.items():
        for y, e in b.items():
            exponent = tuple(i+j for i, j in zip(x, y))
            out[exponent] = out.get(exponent, R(0))+c*e
    return {exponent: c for exponent, c in out.items() if c}


def diff(a, j):
    out = {}
    for exponent, c in a.items():
        if exponent[j]:
            key = list(exponent)
            key[j] -= 1
            out[tuple(key)] = c*exponent[j]
    return out


@lru_cache(None)
def normal_moment(exponent):
    if any(x % 2 for x in exponent):
        return 0
    return math.prod(math.prod(range(1, x, 2)) for x in exponent)


def expectation(a):
    return sum((c*normal_moment(exponent) for exponent, c in a.items()), R(0))


def second(a):
    return expectation(mul(a, a))


def linear_combo(coefficients, polynomials):
    out = {}
    for c, polynomial in zip(coefficients, polynomials):
        out = add(out, scale(polynomial, c))
    return out


def matvec(matrix, polynomials):
    return [linear_combo(row, polynomials) for row in matrix]


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), R(0))


def matmul(a, b):
    return [[dot(row, col) for col in transpose(b)] for row in a]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), R(0))


def frob2(a):
    return sum((x*x for row in a for x in row), R(0))


def hermite_values(linear_form, degree, dim):
    # Probabilists' recurrence, evaluated as multivariate polynomials.
    one = {(0,)*dim: R(1)}
    values = [one, linear_form]
    for j in range(1, degree):
        values.append(add(mul(linear_form, values[-1]),
                          scale(values[-2], -j)))
    return values


def product_hermite_coefficients(poly):
    # Independent basis conversion: invert monomials one coordinate at a time.
    # x^n = sum_j n!/(2^j j! (n-2j)!) He_(n-2j)(x).
    out = {}
    for exponent, coefficient in poly.items():
        expansion = {(): coefficient}
        for n in exponent:
            updated = {}
            for old, c in expansion.items():
                for j in range(n//2+1):
                    factor = R(math.factorial(n),
                               2**j*math.factorial(j)*math.factorial(n-2*j))
                    updated[old+(n-2*j,)] = c*factor
            expansion = updated
        out = add(out, expansion)
    return out


def chaos_variance_and_energy(poly):
    coefficients = product_hermite_coefficients(poly)
    variance = energy = R(0)
    for exponent, c in coefficients.items():
        if sum(exponent):
            term = c*c*math.prod(math.factorial(x) for x in exponent)
            variance += term
            energy += sum(exponent)*term
    return variance, energy


# Rational orthonormal basis of the complement of e=(1,1,1,1)/2.
Q = [[R(1, 2), R(1, 2), R(1, 2)],
     [R(1, 2), R(-1, 2), R(-1, 2)],
     [R(-1, 2), R(1, 2), R(-1, 2)],
     [R(-1, 2), R(-1, 2), R(1, 2)]]
assert matmul(transpose(Q), Q) == [[R(i == j) for j in range(3)]
                                  for i in range(3)]
assert all(sum(col) == 0 for col in transpose(Q))

designs = {
    "orthogonal": [[R(i == j) for i in range(4)] for j in range(4)],
    "correlated": [[R(1), R(0)], [R(0), R(1)],
                   [R(3, 5), R(4, 5)], [R(3, 5), R(-4, 5)]],
    "repeated_antipodal": [[R(1), R(0)], [R(1), R(0)],
                           [R(-1), R(0)], [R(0), R(1)]],
}
activations = {
    "He2": {2: R(1)},
    "He3": {3: R(1)},
    "He4+He2/3": {2: R(1, 3), 4: R(1)},
    "He5+He3/2+He2/5": {2: R(1, 5), 3: R(1, 2), 5: R(1)},
}
matrices = [
    [[R(i == j) for j in range(3)] for i in range(3)],
    [[R(1), R(1, 3), R(-1, 2)],
     [R(1, 3), R(-2), R(2, 5)],
     [R(-1, 2), R(2, 5), R(1, 7)]],
    [[x*y for y in (R(1), R(-2), R(3))]
     for x in (R(1), R(-2), R(3))],
]

count = 0
largest_degree = 0
for design_name, columns in designs.items():
    dim, n = len(columns[0]), len(columns)
    assert all(dot(col, col) == 1 for col in columns)
    U = transpose(columns)
    forms = [{tuple(int(i == j) for i in range(dim)): col[j]
              for j in range(dim) if col[j]} for col in columns]
    for activation_name, coefficients in activations.items():
        k = max(coefficients)
        largest_degree = max(largest_degree, k)
        v = sum(c*c*math.factorial(j) for j, c in coefficients.items())
        q = 2*coefficients.get(2, R(0))**2
        rows = []
        derivative_rows = []
        for form in forms:
            hermites = hermite_values(form, k, dim)
            rows.append(linear_combo([coefficients.get(j, R(0))
                                      for j in range(k+1)], hermites))
            derivative_rows.append(linear_combo(
                [coefficients.get(j+1, R(0))*(j+1) for j in range(k)],
                hermites[:k]))
        assert all(expectation(row) == 0 for row in rows)
        covariance = [[expectation(mul(x, y)) for y in rows] for x in rows]
        independent_covariance = [[sum(
            c*c*math.factorial(j)*dot(x, y)**j
            for j, c in coefficients.items()) for y in columns] for x in columns]
        assert covariance == independent_covariance
        assert all(covariance[i][i] == v for i in range(n))
        z = matvec(transpose(Q), rows)
        T = matmul(matmul(transpose(Q), covariance), Q)
        assert T == [[expectation(mul(x, y)) for y in z] for x in z]
        # Independently verify the exact projected trace defect.
        D = [[covariance[i][j]-v*R(i == j) for j in range(n)] for i in range(n)]
        assert trace(T)-3*v == -sum(map(sum, D))/n
        D4four = expectation(mul(mul(derivative_rows[0], derivative_rows[0]),
                                mul(derivative_rows[0], derivative_rows[0])))
        for A in matrices:
            Az = matvec(A, z)
            F = linear_combo([R(1)]*len(z), [mul(x, y) for x, y in zip(z, Az)])
            mean = expectation(F)
            assert mean == trace(matmul(A, T))
            variance = second(F)-mean*mean
            energy = sum(second(diff(F, j)) for j in range(dim))
            independent_variance, independent_energy = chaos_variance_and_energy(F)
            assert (variance, energy) == (independent_variance, independent_energy)
            assert variance <= energy
            L = matvec(Q, Az)
            gradient = matvec(U, [mul(x, y) for x, y in zip(derivative_rows, L)])
            assert all(diff(F, j) == scale(gradient[j], 2) for j in range(dim))
            mixed = sum(expectation(mul(mul(dp, dp), mul(ell, ell)))
                        for dp, ell in zip(derivative_rows, L))
            assert energy <= 4*n*mixed  # ||U||_op^2 <= ||U||_F^2 = n.
            linear_second = sum(second(ell) for ell in L)
            assert linear_second == trace(matmul(matmul(A, A), T))
            for ell in L:
                assert second(mul(ell, ell)) <= 9**k*second(ell)**2
            assert mixed*mixed <= D4four*9**k*linear_second**2
            assert linear_second <= trace(T)*frob2(A)
            assert variance**2 <= 16*n*n*D4four*9**k*(trace(T)*frob2(A))**2
            count += 1
            check_time()
        print(f"  {design_name}: {activation_name}, v={v}, q={q}: passed")

print(f"Exact polynomial covariance / gradient / concentration chains: {count} cases")
print("Monomial Gaussian moments and independent Hermite Parseval: exact agreement")

# A failure case: derivative and feature cannot be treated as independent.
# sigma=He2, L=He2 in one Gaussian coordinate.
one_dim = hermite_values({(1,): R(1)}, 2, 1)[2]
derivative = diff(one_dim, 0)
mixed = expectation(mul(mul(derivative, derivative), mul(one_dim, one_dim)))
false_factorization = second(derivative)*second(one_dim)
var_square = second(mul(one_dim, one_dim))-second(one_dim)**2
assert (mixed, false_factorization, var_square) == (40, 8, 56)
assert var_square > 4*false_factorization
print(f"Dependence failure: E[sigma'^2 L^2]={mixed}; product of means={false_factorization}")
print(f"  Var(He2(Z)^2)={var_square} exceeds naive derivative bound {4*false_factorization}")

# Exact scalar fourth moments for standard Hermite examples, two routes.
for degree, fourth in ((2, 60), (3, 3348), (4, 368064)):
    polynomial = hermite_values({(1,): R(1)}, degree, 1)[degree]
    square = mul(polynomial, polynomial)
    direct = second(square)
    via_chaos = sum(c*c*math.factorial(exponent[0])
                    for exponent, c in product_hermite_coefficients(square).items())
    assert direct == via_chaos == fourth
print("Hermite fourth moments: He2=60, He3=3348, He4=368064, two exact routes")

elapsed = time.monotonic()-started
rss_mib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024)
assert rss_mib < 1024
print(f"PASS: exact algebra only; max degree {largest_degree}; "
      f"elapsed {elapsed:.3f}s; peak RSS {rss_mib:.1f} MiB")
