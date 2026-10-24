from fractions import Fraction as F
from itertools import product, permutations
from collections import Counter

# Exact rational 2x2 rank-one PSD certificate from the report.
u = [
    (F(1), F(0)),
    (F(7, 25), F(24, 25)),
    (F(0), F(1)),
    (F(1), F(0)),
]
s = [F(1), F(1, 10), F(2), F(1)]


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


G = [[abs(dot(u[i], u[j])) for j in range(4)] for i in range(4)]
assert all(dot(x, x) == 1 for x in u)


def word_norm(w):
    # For A_i = s_i u_i u_i^T with unit u_i:
    # ||A_i A_j A_k A_l|| = product scales * product adjacent |Gram|.
    z = F(1)
    for i in w:
        z *= s[i]
    for i, j in zip(w[:-1], w[1:]):
        z *= G[i][j]
    return z


perms = list(permutations(range(4)))
S = sum((word_norm(w) for w in perms), F(0))

words_211 = []
for w in product(range(4), repeat=4):
    mult = sorted(Counter(w).values(), reverse=True)
    if mult == [2, 1, 1]:
        words_211.append(w)
assert len(words_211) == 144
Q211 = sum((word_norm(w) for w in words_211), F(0))

assert S == F(672, 3125), S
assert Q211 == F(444759, 390625), Q211
assert Q211 / S == F(21179, 4000), Q211 / S
assert Q211 < 6*S

# Check the positional class decomposition too.
classes = {(i, j): F(0) for i in range(4) for j in range(i+1, 4)}
for w in words_211:
    c = Counter(w)
    r = next(k for k, v in c.items() if v == 2)
    pos = tuple(i for i, x in enumerate(w) if x == r)
    classes[pos] += word_norm(w)
assert sum(classes.values(), F(0)) == Q211

print('S =', S)
print('Q211 =', Q211)
print('Q211/S =', Q211 / S, '=', float(Q211 / S))
print('6S-Q211 =', 6*S-Q211, '>', 0)
print('positional ratios C_rs/S:')
for pos in sorted(classes):
    print(tuple(i+1 for i in pos), classes[pos] / S, float(classes[pos] / S))

# General-family formula check at the exact rational point.
a = F(7, 25)
b = F(24, 25)
t = F(2)
eps = F(1, 10)
formula = (
    F(1) + t + F(3)*(a+1)/(b*t)
    + eps*(a+b+1)
    + eps*(a*a+a+1)/(b*t)
)
assert formula == Q211 / S
print('closed-form formula verified exactly')

# The limiting family bound is 1+2*sqrt(3): this script does not use
# floating-point arithmetic to certify that irrational limit.  The report
# derives it analytically by minimizing 1+t+3(a+1)/(b t) and taking a->0+.
