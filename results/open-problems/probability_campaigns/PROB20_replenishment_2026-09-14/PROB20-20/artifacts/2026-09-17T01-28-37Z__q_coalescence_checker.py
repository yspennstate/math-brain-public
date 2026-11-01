from fractions import Fraction
from math import factorial

# Exact finite self-check for the q-box coalescence identity used in the
# 2026-09-17 PROB20-20 report.  This is a checker, not a proof of the
# asymptotic theorem.


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for x in range(total + 1):
        for rest in compositions(total - x, parts - 1):
            yield (x,) + rest


def falling(r, q):
    ans = 1
    for j in range(q):
        ans *= max(r - j, 0)
    return ans


# Deliberately irregular positive rational weights.
w = [
    Fraction(1, 1),
    Fraction(3, 2),
    Fraction(2, 3),
    Fraction(5, 4),
    Fraction(1, 2),
    Fraction(7, 5),
    Fraction(3, 7),
    Fraction(11, 9),
    Fraction(2, 5),
    Fraction(13, 10),
]

n = 5
m = 9
K = 1
q = 3

configs = list(compositions(m, n))
raw = {}
Z = Fraction(0, 1)
for y in configs:
    wt = Fraction(1, 1)
    for x in y:
        wt *= w[x]
    raw[y] = wt
    Z += wt

# Check the exact orbit/coalescence identity
# P(Y1=a,Y2=b,Y3=d) = [w_a w_b w_d/(w_{a+b+d} w_0^2)]
#                         P(Y1=a+b+d,Y2=0,Y3=0)
# after summing over the remaining coordinates.
identity_checks = 0
for a in range(K + 1, m + 1):
    for b in range(K + 1, m + 1 - a):
        for d in range(K + 1, m + 1 - a - b):
            c = a + b + d
            lhs = sum(
                wt for y, wt in raw.items()
                if y[0] == a and y[1] == b and y[2] == d
            ) / Z
            rhs_event = sum(
                wt for y, wt in raw.items()
                if y[0] == c and y[1] == 0 and y[2] == 0
            ) / Z
            factor = w[a] * w[b] * w[d] / (w[c] * w[0] ** 2)
            assert lhs == factor * rhs_event
            identity_checks += 1


def A_q(c):
    # q=3 interior convolution, with every summand > K.
    total = Fraction(0, 1)
    for a in range(K + 1, c + 1):
        for b in range(K + 1, c - a + 1):
            d = c - a - b
            if d > K:
                total += w[a] * w[b] * w[d]
    return total


Q = Fraction(0, 1)
argmax_c = None
for c in range(q * (K + 1), m + 1):
    value = A_q(c) / (w[c] * w[0] ** (q - 1))
    if value > Q:
        Q = value
        argmax_c = c

R_falling_expectation = sum(
    wt * falling(sum(x > K for x in y), q)
    for y, wt in raw.items()
) / Z

n_falling_q = Fraction(factorial(n), factorial(n - q))
bound = n_falling_q * Q
assert R_falling_expectation <= bound

p_first_q_large = sum(
    wt for y, wt in raw.items()
    if all(y[j] > K for j in range(q))
) / Z
assert R_falling_expectation == n_falling_q * p_first_q_large

print(f"identity_checks={identity_checks}")
print(f"Z={Z}")
print(f"Q={Q} ~= {float(Q):.15g}; argmax_c={argmax_c}")
print(
    "E[(R)_q]="
    f"{R_falling_expectation} ~= {float(R_falling_expectation):.15g}"
)
print(f"(n)_q Q={bound} ~= {float(bound):.15g}")
print(f"exact_slack={bound - R_falling_expectation}")
print("PASS")
