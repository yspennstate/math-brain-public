#!/usr/bin/env python3
"""Exact/numerical audit of the Boolean root signed-KL payment."""

from math import log2, log


def walsh(v):
    return [sum(y * (-1 if (s & x).bit_count() & 1 else 1)
                for x, y in enumerate(v)) / len(v) for s in range(len(v))]


def h2(x):
    return sum(-z * log2(z) for z in (x, 1-x) if z > 0)


def dhalf(alpha):
    return 1-h2((1+alpha)/2)


def audit_table(v):
    c = walsh(v)
    n = (len(v)-1).bit_length()
    root = singleton = 0.0
    assertions = 0
    for i in range(n):
        bit = 1 << i
        conv = sum(c[s]*c[s ^ bit] for s in range(1 << n))
        assert abs(conv) < 2e-12
        a, b = c[0], c[bit]
        m = a*a+b*b
        k0 = 0.0 if m == 0 else m*dhalf(2*a*b/m)
        assert k0 <= 4*b*b + 2e-12
        root += k0
        singleton += b*b
        assertions += 2
        for j in range(i+1, n):
            bj = 1 << j
            conv2 = sum(c[s]*c[s ^ bit ^ bj] for s in range(1 << n))
            assert abs(conv2) < 2e-12
            assertions += 1
    assert root <= 4*singleton + 2e-12
    return assertions + 1, root, singleton


def point_defect(n):
    return [-1] + [1]*((1 << n)-1)


def main():
    cases = assertions = 0
    max_ratio = 0.0
    for n in range(1, 5):
        N = 1 << n
        for table in range(1 << N):
            v = [1 if table >> x & 1 else -1 for x in range(N)]
            a, r, s = audit_table(v)
            assertions += a
            if s > 0:
                max_ratio = max(max_ratio, r/s)
            cases += 1

    defect = []
    for n in range(2, 25):
        t = 2**(1-n)
        a, b = 1-t, t
        m = a*a+b*b
        ratio = m*dhalf(2*a*b/m)/(b*b)
        defect.append((n, ratio))
        assert ratio < 4

    print('B07/A031 ROOT_KL_PAYMENT_PASS')
    print('boolean_truth_tables', cases)
    print('assertions', assertions)
    print('maximum_finite_boolean_ratio', format(max_ratio, '.15g'))
    print('point_defect_n24_ratio', format(defect[-1][1], '.15g'))
    print('limiting_lower_obstruction_2_over_ln2', format(2/log(2), '.15g'))
    print('proved_coefficient', 4)
    print('universal_GU', 'OPEN')


if __name__ == '__main__':
    main()

