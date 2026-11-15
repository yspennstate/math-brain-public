#!/usr/bin/env python3
"""Exact constants and algebra audits for the GOE repulsion bound. Stdlib only."""
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import json
import os
import resource
import time

START = time.monotonic()
P = F(22, 7)


def guard():
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    assert time.monotonic() - START < 120
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 256 * 1024**2


def fourth_bound(r, k):
    degree = k*(k-1)//2
    superfactorial = 1
    for n in range(k):
        superfactorial *= factorial(n)
    a = F(k-1, 4) + sum((F(1, j*j) for j in range(1, k+1)), F(0))
    product = a**k
    for i in range(1, k+1):
        product *= F(k, i*i) + P*P*sum(
            (F(1, (i+j)**2) for j in range(1, k+1) if j != i), F(0))
    return (2**(4*(k-1)) * k**(2*k) * r**(4*(k+degree)) *
            (P/4)**(4*degree) * product / (factorial(k)*superfactorial)**4)


def envelope_bound(r, k):
    # Construct entrywise majorants, rather than reusing a_k or c_ki.
    majorant = [[F(0) for _ in range(2*k)] for _ in range(2*k)]
    for i in range(k):
        for j in range(k):
            if i != j:
                majorant[2*i][2*j] = F(1, 2)
                majorant[2*i+1][2*j+1] = P/(i+j+2)
            majorant[2*i][2*j+1] = F(1, j+1)
            majorant[2*j+1][2*i] = F(1, j+1)
    row_product = F(1)
    for row in majorant:
        row_product *= sum((entry*entry for entry in row), F(0))
    result = row_product
    # Fourth powers of the integration and Chebyshev factors. No factorial
    # function, degree exponent K, or closed-form row bounds are used here.
    coefficient = F(1)
    for n in range(k):
        if n:
            coefficient *= r*P/(4*n)
            result *= 16
        result *= coefficient**4 * k*k * r**4 / (n+1)**4
    return result


def fourth_root_enclosure(value, digits):
    scale = 10**digits
    integer = value.numerator * scale**4 // value.denominator
    lower = isqrt(isqrt(integer))
    lo, hi = F(lower, scale), F(lower+1, scale)
    assert lo**4 <= value < hi**4
    return lo, hi


def audit_constants():
    rows = []
    checks = 0
    for r in (F(1, 2), F(1), F(2)):
        first = None
        for k in range(1, 25):
            guard()
            value = fourth_bound(r, k)
            assert value == envelope_bound(r, k)
            if k % 2 == 0 and first is None and value < F(1, 10**24):
                first = k
            checks += 1
        value = fourth_bound(r, first)
        lo, hi = fourth_root_enclosure(value, 12)
        rows.append(dict(R=str(r), first_even_order=first,
                         lower=str(lo), upper=str(hi)))
    assert [row['first_even_order'] for row in rows] == [6, 8, 10]
    q10 = fourth_bound(F(2), 10)
    assert F(517385, 10**12)**4 < q10 < F(517386, 10**12)**4 < F(1, 10**24)
    assert all(fourth_bound(F(2), k) > F(1, 10**24) for k in range(2, 10, 2))
    q12 = fourth_bound(F(2), 12)
    q20 = fourth_bound(F(2), 20)
    e20 = max(e for e in range(1, 201) if q20 < F(1, 10**(4*e)))
    # Independent integer cross multiplication of the saved b20 certificate.
    assert q20.numerator * 10**(4*e20) < q20.denominator
    lo20, hi20 = fourth_root_enclosure(q20, e20+7)
    lo12, hi12 = fourth_root_enclosure(q12, 22)
    # Check pi<22/7's polynomial division and integration independently.
    quotient = [4, 0, -4, 0, 5, -4, 1]
    product = [0]*9
    for n, coefficient in enumerate(quotient):
        product[n] += coefficient
        product[n+2] += coefficient
    product[0] -= 4
    assert product == [0, 0, 0, 0, 1, -4, 6, -4, 1]
    assert sum((F(c, i+1) for i, c in enumerate(quotient)), F(0)) == P
    return dict(direct_vs_entrywise_envelope_checks=checks,
                rows=rows, R2_order10_fourth_power=str(q10),
                R2_order12_enclosure=[str(lo12), str(hi12)],
                R2_order20_fourth_power=str(q20),
                R2_order20_enclosure=[str(lo20), str(hi20)],
                R2_order20_less_than_power_of_ten=-e20,
                pi_upper_bound_polynomial_identity=True)


def determinant(matrix):
    # Gaussian elimination; independent of recursive Pfaffian expansion.
    a = [row[:] for row in matrix]
    result = F(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            result = -result
        p = a[j][j]
        result *= p
        for i in range(j+1, len(a)):
            multiplier = a[i][j]/p
            for h in range(j+1, len(a)):
                a[i][h] -= multiplier*a[j][h]
    return result


def pfaffian(a):
    if not a:
        return F(1)
    answer = F(0)
    for j in range(1, len(a)):
        keep = [i for i in range(1, len(a)) if i != j]
        minor = [[a[i][h] for h in keep] for i in keep]
        answer += (-1)**(j+1)*a[0][j]*pfaffian(minor)
    return answer


def multiply(a, b):
    return [[sum((a[i][h]*b[h][j] for h in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def divided_difference(nodes, values):
    # Newton's recursion, independent of the barycentric formula used in T.
    work = list(values)
    for order in range(1, len(nodes)):
        work = [(work[i+1]-work[i])/(nodes[i+order]-nodes[i])
                for i in range(len(nodes)-order)]
    return work[0]


def polynomial_kernel(z):
    # An exact polynomial model tests congruence algebra and jump handling.
    # It is not a GOE correlation kernel and is not used to bound a GOE moment.
    s = d = integral = F(0)
    for n in range(6):
        coefficient = F((-1)**n * 3**(2*n), factorial(2*n+1))
        s += coefficient*z**(2*n)
        integral += coefficient*z**(2*n+1)/(2*n+1)
        if n:
            d += 2*n*coefficient*z**(2*n-1)
    jump = F((z > 0)-(z < 0), 2)
    return s, d, integral-jump


def audit_congruence():
    cases = mixed_checks = double_checks = 0
    for k in range(1, 6):
        base = [F(i, k+1) for i in range(k)]
        node_sets = [base, list(reversed(base)),
                     [x/F(10000) for x in base],
                     [2*x-1 for x in base]]
        for nodes in node_sets:
            guard()
            a = [[F(0) for _ in range(2*k)] for _ in range(2*k)]
            t = [[F(0) for _ in range(2*k)] for _ in range(2*k)]
            vandermonde = F(1)
            for i in range(k):
                t[2*i][2*i] = F(1)
                for j in range(i):
                    vandermonde *= nodes[i]-nodes[j]
                scale = F(factorial(i), 3**i)
                for j in range(i+1):
                    denominator = F(1)
                    for h in range(i+1):
                        if h != j:
                            denominator *= nodes[j]-nodes[h]
                    t[2*i+1][2*j+1] = scale/denominator
                for j in range(k):
                    s, d, integral = polynomial_kernel(nodes[i]-nodes[j])
                    a[2*i][2*j] = -integral
                    a[2*i][2*j+1] = s
                    a[2*i+1][2*j] = -s
                    a[2*i+1][2*j+1] = d
            b = multiply(multiply(t, a), list(map(list, zip(*t))))
            assert all(b[i][j] == -b[j][i] for i in range(2*k) for j in range(2*k))
            assert all(b[i][i] == 0 for i in range(2*k))
            for i in range(k):
                for j in range(k):
                    assert b[2*i][2*j] == a[2*i][2*j]
                    mixed = divided_difference(nodes[:j+1],
                        [polynomial_kernel(nodes[i]-x)[0] for x in nodes[:j+1]])
                    assert b[2*i][2*j+1] == F(factorial(j), 3**j)*mixed
                    mixed_checks += 1
                    values = [divided_difference(nodes[:i+1],
                        [polynomial_kernel(x-y)[1] for x in nodes[:i+1]])
                        for y in nodes[:j+1]]
                    double = divided_difference(nodes[:j+1], values)
                    assert b[2*i+1][2*j+1] == F(factorial(i)*factorial(j), 3**(i+j))*double
                    double_checks += 1
            expected_det_t = F(1, vandermonde)
            for n in range(k):
                expected_det_t *= F(factorial(n), 3**n)
            assert determinant(t) == expected_det_t
            pa, pb = pfaffian(a), pfaffian(b)
            assert pb == expected_det_t*pa
            assert determinant(a) == pa*pa
            assert determinant(b) == pb*pb
            cases += 1
    return dict(polynomial_model_cases=cases,
                recursive_vs_barycentric_mixed_entries=mixed_checks,
                recursive_vs_barycentric_double_entries=double_checks,
                reordered_and_clustered_nodes=True,
                actual_GOE_samples=False,
                determinant_vs_pfaffian_checks=2*cases)


def chebyshev_values(z, k):
    result = [F(1)]
    if k > 1:
        result.append(z)
    for n in range(2, k):
        result.append(2*z*result[-1]-result[-2])
    return result


def audit_vandermonde():
    cases = entries = 0
    for r in (F(1, 2), F(1), F(2)):
        for k in range(1, 13):
            guard()
            # Include endpoints, negative Chebyshev arguments and tight nodes.
            base = [F(i, max(k-1, 1))*r for i in range(k)]
            for nodes in (base, [r/3+x/100 for x in base]):
                monomials = [[x**n for n in range(k)] for x in nodes]
                cheb = [chebyshev_values(2*x/r-1, k) for x in nodes]
                assert all(abs(x) <= 1 for row in cheb for x in row)
                monic = [[row[n]*(2*(r/4)**n if n else 1)
                          for n in range(k)] for row in cheb]
                value = F(1)
                for i in range(k):
                    for j in range(i):
                        value *= nodes[i]-nodes[j]
                assert determinant(monomials) == determinant(monic) == value
                column_product = F(1)
                for j in range(k):
                    column_product *= sum((monic[i][j]**2 for i in range(k)), F(0))
                bound_squared = k**k * 2**(2*(k-1)) * (r/4)**(k*(k-1))
                assert value*value <= column_product <= bound_squared
                entries += k*k
                cases += 1
    return dict(exact_matrix_cases=cases, exact_Chebyshev_entries=entries,
                product_vs_two_determinants=True,
                entrywise_and_Hadamard_bounds=True)


def main():
    guard()
    result = dict(constants=audit_constants(), congruence=audit_congruence(),
                  vandermonde=audit_vandermonde())
    guard()
    result['resources'] = dict(nice=os.getpriority(os.PRIO_PROCESS, 0),
        OMP_NUM_THREADS=os.environ['OMP_NUM_THREADS'],
        peak_rss_bytes_macos=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        elapsed_seconds=round(time.monotonic()-START, 3),
        measured_rss_guard_bytes=256*1024**2, elapsed_guard_seconds=120,
        os_hard_memory_cap=False, processes=1, standard_library_only=True)
    Path(__file__).with_name('repulsion_data.json').write_text(json.dumps(result, indent=2)+'\n')
    print('All exact repulsion-bound checks passed.')
    for key, value in result.items():
        if key == 'constants':
            brief = {k: v for k, v in value.items() if 'fourth_power' not in k}
            print(key+': '+json.dumps(brief, sort_keys=True))
        else:
            print(key+': '+json.dumps(value, sort_keys=True))


if __name__ == '__main__':
    main()
