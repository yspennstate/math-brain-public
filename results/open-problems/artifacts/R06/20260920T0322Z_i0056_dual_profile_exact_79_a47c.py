from itertools import product
from fractions import Fraction


def canon(seq):
    seq = list(seq)
    n = len(seq)
    vals = []
    for k in range(n):
        vals.append(tuple(seq[k:] + seq[:k]))
    rev = list(reversed(seq))
    for k in range(n):
        vals.append(tuple(rev[k:] + rev[:k]))
    return min(vals)


def cyclic_connected(mask):
    if all(mask) or not any(mask):
        return True
    n = len(mask)
    return sum(mask[i] != mask[(i + 1) % n] for i in range(n)) == 2


def profile_valid(seq):
    if min(seq) != 0:
        return False
    n = len(seq)
    if any(abs(seq[i] - seq[(i + 1) % n]) > 1 for i in range(n)):
        return False
    mx = max(seq)
    if any(sum(x == level for x in seq) > 2 for level in range(mx + 1)):
        return False
    if any(not cyclic_connected([x <= level for x in seq]) for level in range(mx + 1)):
        return False
    return True


expected = {
    4: {(0, 0, 1, 1), (0, 1, 2, 1)},
    5: {(0, 0, 1, 2, 1), (0, 1, 2, 2, 1)},
}

for p in (4, 5):
    got = {canon(s) for s in product(range(p + 1), repeat=p) if profile_valid(s)}
    print(f"p={p} profiles={sorted(got)}")
    assert got == expected[p]

# Exact shell values already certified by the preceding Coxeter/Schreier checker.
S = [
    1, 4, 10, 20, 38, 70, 130, 240, 446, 824,
    1528, 2824, 5234, 9680, 17934, 33178, 61450, 113708, 210566,
]

for n in range(7, len(S)):
    rhs = (
        S[n - 1] + 2 * S[n - 2] - 2 * S[n - 3]
        + 2 * S[n - 4] + S[n - 5] - S[n - 6]
    )
    assert S[n] == rhs, (n, S[n], rhs)

# Verify the claimed numerator/denominator identity through all certified coefficients.
num = [1, 3, 4, 4, 4, 3, 1]
den = [1, -1, -2, 2, -2, -1, 1]
for n in range(len(S)):
    coeff = sum(den[j] * S[n - j] for j in range(min(n, 6) + 1))
    target = num[n] if n < len(num) else 0
    assert coeff == target, (n, coeff, target)

# Method-20 exact sign check: the dominant characteristic root is strictly larger
# than 1 + the current radius-16 ball ratio U=113708/133611.
U = Fraction(113708, 133611)
c = 1 + U


def characteristic(x):
    return x**6 - x**5 - 2*x**4 + 2*x**3 - 2*x**2 - x + 1

pc = characteristic(c)
assert pc < 0
assert characteristic(Fraction(2, 1)) > 0
print("p(1+U) numerator =", pc.numerator)
print("p(1+U) denominator =", pc.denominator)
print("p(2) =", characteristic(Fraction(2, 1)))
print("ALL_EXACT_CHECKS_PASS")
