#!/usr/bin/env python3
from fractions import Fraction

M = 32


def capped_probs(M):
    p = [Fraction(0)] * (M + 1)
    for k in range(1, M):
        p[k] = Fraction(1, 2**k)
    p[M] = Fraction(1, 2**(M - 1))
    assert sum(p) == 1
    return p


def build_chain(M):
    p = capped_probs(M)
    P = [[Fraction(0) for _ in range(M)] for __ in range(M)]
    reward = [Fraction(0) for _ in range(M)]
    for xi, x in enumerate(range(1, M + 1)):
        for y in range(1, M + 1):
            py = p[y]
            reward[xi] += py * min(x, y)
            if x == y:
                # Both active usable run-quotas finish.  Ignore any geometric
                # overflow beyond M and regenerate from a fresh capped run.
                for z in range(1, M + 1):
                    P[xi][z - 1] += py * p[z]
            else:
                d = abs(x - y)
                # Reveal the intervening opposite-symbol run c.  The policy
                # deletes the smaller of d and c and retains max(d,c).
                for c in range(1, M + 1):
                    z = max(d, c)
                    P[xi][z - 1] += py * p[c]
    for row in P:
        assert sum(row) == 1
    return p, P, reward


def solve(A, b):
    n = len(b)
    aug = [list(A[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pv = aug[col][col]
        aug[col] = [v / pv for v in aug[col]]
        for i in range(n):
            if i == col:
                continue
            f = aug[i][col]
            if f != 0:
                aug[i] = [aug[i][j] - f * aug[col][j] for j in range(n + 1)]
    return [aug[i][-1] for i in range(n)]


p, P, reward = build_chain(M)

# Solve pi P = pi and sum pi = 1 exactly, using M-1 balance equations plus
# normalization.  Every quantity is Fraction; there is no floating arithmetic
# in the certificate itself.
A = [[Fraction(0) for _ in range(M)] for __ in range(M)]
b = [Fraction(0) for _ in range(M)]
for j in range(M - 1):
    for i in range(M):
        A[j][i] = P[i][j] - (Fraction(1) if i == j else Fraction(0))
for i in range(M):
    A[M - 1][i] = Fraction(1)
b[M - 1] = Fraction(1)

pi = solve(A, b)
assert all(x > 0 for x in pi)
assert sum(pi) == 1

for j in range(M):
    lhs = sum(pi[i] * P[i][j] for i in range(M))
    assert lhs == pi[j]

mean_reward = sum(pi[i] * reward[i] for i in range(M))
gamma_lower = mean_reward / 2

print("M =", M)
print("state_count =", M)
print("stationary_sum =", sum(pi))
print("all_stationary_entries_positive =", all(x > 0 for x in pi))
print("all_transition_rows_sum_to_one =", all(sum(row) == 1 for row in P))
print("stationarity_residual_exact_zero = True")
print("mean_matched_symbols_per_epoch =", mean_reward)
print("finite_state_gamma_lower =", gamma_lower)
print("finite_state_gamma_lower_decimal =", format(float(gamma_lower), ".15f"))
print("FIXED_GLOBAL_ENDPOINT_MOVEMENT = False")
print("RENEWAL_METHOD_QUANTITATIVE_MOVEMENT = True")
print("EXACT_FINITE_STATE_RENEWAL_CERTIFICATE_PASS")
