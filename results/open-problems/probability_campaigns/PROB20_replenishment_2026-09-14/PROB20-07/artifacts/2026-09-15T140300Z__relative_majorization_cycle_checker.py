"""PROB20-07 exact rational relative-majorization checker.

This file supports the report:
  runs/2026-09-15/2026-09-15T135950Z__report.md

It performs exact Fraction arithmetic for the finite Blackwell/stop-loss
criterion associated with a prescribed two-cycle at coefficient floor a.

For x,y in the 3-simplex and floor a, define:
  U(z) = unordered iid-parent-pair distribution on
         (11,12,13,22,23,33),
  C=(y-a*1)/(1-3a), D=(x-a*1)/(1-3a).
A necessary-and-sufficient binary relative-majorization criterion is
  sum_k (D_k-lambda C_k)_+ <= sum_r (U_r(y)-lambda U_r(x))_+
for all lambda >= 0; it is enough to check the finite union of source and
target likelihood-ratio breakpoints.

The script exactly verifies the rational lower-family member s=1/30,
a=11/133 and reproduces the stop-loss table archived in the report.
"""

from fractions import Fraction as F


def positive_part(x):
    return x if x > 0 else F(0)


def unordered_pair_distribution(x):
    x1, x2, x3 = x
    return [
        x1*x1,
        2*x1*x2,
        2*x1*x3,
        x2*x2,
        2*x2*x3,
        x3*x3,
    ]


def cycle_stop_loss_table(x, y, a):
    """Return exact stop-loss slacks at all finite breakpoints.

    Inputs x,y are length-3 lists of Fraction summing to 1.
    The floor must satisfy a<1/3 and x_i,y_i>a for ratio evaluation.
    """
    b = 1 - 3*a
    assert b > 0
    assert sum(x, F(0)) == 1
    assert sum(y, F(0)) == 1
    assert min(x) > a and min(y) > a

    A = unordered_pair_distribution(x)
    B = unordered_pair_distribution(y)
    C = [(yi-a)/b for yi in y]
    D = [(xi-a)/b for xi in x]

    lambdas = {F(0)}
    for br, ar in zip(B, A):
        assert ar > 0
        lambdas.add(br/ar)
    for dk, ck in zip(D, C):
        assert ck > 0
        lambdas.add(dk/ck)

    rows = []
    for lam in sorted(lambdas):
        source = sum((positive_part(br-lam*ar) for br, ar in zip(B, A)), F(0))
        target = sum((positive_part(dk-lam*ck) for dk, ck in zip(D, C)), F(0))
        rows.append((lam, source-target, source, target))
    return rows, (A, B, C, D)


# Exact established lower-family member s=1/30.
s = F(1, 30)
a = (1 - 9*s*s) / (12 - 27*s*s)
assert a == F(11, 133)

x = [F(1,3)+s, F(1,3)-s, F(1,3)]
y = [x[1], x[0], x[2]]

rows, (A, B, C, D) = cycle_stop_loss_table(x, y, a)

assert C == [F(289,1000), F(1133,3000), F(1,3)]
assert D == [F(1133,3000), F(289,1000), F(1,3)]
assert A == [F(121,900), F(11,50), F(11,45), F(9,100), F(1,5), F(1,9)]
assert B == [F(9,100), F(11,50), F(1,5), F(121,900), F(11,45), F(1,9)]

expected = [
    (F(0), F(0)),
    (F(81,121), F(0)),
    (F(867,1133), F(199,15450)),
    (F(9,11), F(0)),
    (F(1), F(1,4500)),
    (F(11,9), F(0)),
    (F(1133,867), F(2189,130050)),
    (F(121,81), F(0)),
]

assert [(lam, slack) for lam, slack, _, _ in rows] == expected
assert all(slack >= 0 for _, slack, _, _ in rows)
assert dict((lam, slack) for lam, slack, _, _ in rows)[F(1)] == F(1,4500)

print("ALL EXACT RELATIVE-MAJORIZATION CHECKS PASSED")
print("floor a =", a)
print("x =", x)
print("y =", y)
for lam, slack, source, target in rows:
    print("lambda=", lam, "slack=", slack, "source=", source, "target=", target)
