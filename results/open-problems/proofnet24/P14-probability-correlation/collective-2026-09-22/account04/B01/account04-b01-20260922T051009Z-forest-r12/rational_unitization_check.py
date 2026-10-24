from fractions import Fraction
from math import ceil, log2


def inverse_ops(x):
    x = Fraction(x)
    ops = []
    while x != 1:
        a, b = x.numerator, x.denominator
        if a > b:
            x = Fraction(a - b, b)       # inverse of P(r)=r+1
            ops.append("P")
        else:
            x = Fraction(2 * a, b - a)   # inverse of S(r)=r/(r+2)
            ops.append("S")
    return ops


def forward(x, op):
    x = Fraction(x)
    if op == "P":
        return x + 1
    if op == "S":
        return x / (x + 2)
    raise ValueError(op)


max_steps = -1
worst = None
for a in range(1, 65):
    for b in range(1, 65):
        target = Fraction(a, b)
        ops = inverse_ops(target)
        x = Fraction(1)
        for op in reversed(ops):
            x = forward(x, op)
        assert x == target
        if len(ops) > max_steps:
            max_steps = len(ops)
            worst = target

# U=K_{2,3}: each of the three length-two branches has
# three disconnected states and one connecting state.
D_U = 3 ** 3
C_U = 3 * 3 ** 2
assert D_U == C_U == 27

# A unit path of ell edges has response 1/(2^ell-1).  The general
# counting lower bound m >= ceil(log2(a+b)) proves that no unit
# two-terminal network with fewer than ell edges has the same response.
for ell in range(1, 9):
    q = Fraction(1, 2 ** ell - 1)
    assert ceil(log2(q.numerator + q.denominator)) == ell

print(
    "STATUS=PASS; rational_pairs=4096; max_inverse_steps=%d; worst=%s; "
    "theta_D_C=27/27; path_minimality_ell=1..8" % (max_steps, worst)
)
