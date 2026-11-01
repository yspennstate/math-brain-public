from fractions import Fraction

# Exact finite self-check for the refined q-box coalescence identity.
# This is NOT a proof of the asymptotic theorem.

weights = [
    Fraction(1,1), Fraction(3,2), Fraction(2,3), Fraction(5,4), Fraction(1,2),
    Fraction(7,5), Fraction(3,7), Fraction(11,9), Fraction(2,5), Fraction(13,10)
]
n = 5
m = 9
K = 1
q = 3

def comps(total, parts):
    if parts == 1:
        yield (total,)
        return
    for a in range(total + 1):
        for rest in comps(total - a, parts - 1):
            yield (a,) + rest

def weight(y):
    z = Fraction(1, 1)
    for a in y:
        z *= weights[a]
    return z

def falling(x, r):
    z = 1
    for j in range(r):
        z *= x - j
    return z

states = list(comps(m, n))
Z = sum(weight(y) for y in states)

A = {}
for c in range(q * (K + 1), m + 1):
    total = Fraction(0, 1)
    for split in comps(c, q):
        if all(a > K for a in split):
            z = Fraction(1, 1)
            for a in split:
                z *= weights[a]
            total += z
    A[c] = total

Q = max(
    A[c] / (weights[c] * weights[0] ** (q - 1))
    for c in A
)

lhs_num = Fraction(0, 1)
rhs_num = Fraction(0, 1)

for y in states:
    wy = weight(y)
    R = sum(a > K for a in y)
    lhs_num += wy * falling(R, q)

    N0 = sum(a == 0 for a in y)
    fiber_term = Fraction(0, 1)
    for a in y:
        if a >= q * (K + 1):
            fiber_term += (
                falling(N0, q - 1)
                * A[a]
                / (weights[a] * weights[0] ** (q - 1))
            )
    rhs_num += wy * fiber_term

lhs = lhs_num / Z
rhs = rhs_num / Z

# Deterministic target-count improvement:
# N_{>=q(K+1)} <= m/[q(K+1)] and (N0)_{q-1} <= n^{q-1}.
refined_bound = Q * Fraction(m, q * (K + 1)) * n ** (q - 1)

assert lhs == rhs
assert lhs <= refined_bound

print(f"states={len(states)}")
print(f"Z={Z}")
print(f"Q={Q}")
print(f"E[(R_K)_q]={lhs}")
print(f"fiber_identity_rhs={rhs}")
print(f"refined_bound={refined_bound}")
print(f"refined_slack={refined_bound-lhs}")
print("PASS")
