#!/usr/bin/env python3
"""Exact-rational consistency check for the PROB20-14 one-sided entropy lemma.

This is a finite-support algebraic certificate only.  It does NOT verify the
infinite-variance universal theorem.  It checks on an exactly enumerated
critical lattice law that:

1. the one-coordinate law under S_n=n-1 is normalized and has exact mean
   (n-1)/n;
2. marginal relative entropy is <= lambda_n/n, where lambda_n=-log P(S_n=n-1);
3. for several truncations K,
      E_Q[X;X>K] <= E_pi[X;X>K] + sqrt(2 D(Q||pi) E_pi[X^2;X<=K]).

Only Python's standard library is used.
"""

from fractions import Fraction
import math


PI = {
    0: Fraction(1, 2),
    1: Fraction(1, 4),
    3: Fraction(1, 4),
}
N = 14

assert sum(PI.values()) == 1
assert sum(Fraction(x) * p for x, p in PI.items()) == 1

max_sum = N * max(PI)
dp = [[Fraction(0) for _ in range(max_sum + 1)] for __ in range(N + 1)]
dp[0][0] = Fraction(1)

for i in range(N):
    for s, ps in enumerate(dp[i]):
        if ps == 0:
            continue
        for x, px in PI.items():
            dp[i + 1][s + x] += ps * px

a_n = dp[N][N - 1]
assert a_n > 0
lambda_n = -math.log(float(a_n))

Q = {}
for d, pd in PI.items():
    target = N - 1 - d
    rem = dp[N - 1][target] if 0 <= target <= max_sum else Fraction(0)
    Q[d] = pd * rem / a_n

assert sum(Q.values()) == 1
assert sum(Fraction(d) * qd for d, qd in Q.items()) == Fraction(N - 1, N)

D = 0.0
for d, qd in Q.items():
    if qd:
        D += float(qd) * math.log(float(qd / PI[d]))

assert D <= lambda_n / N + 1e-12

rows = []
for K in (0, 1, 2):
    tail_Q = sum(float(qd) * d for d, qd in Q.items() if d > K)
    tail_P = sum(float(pd) * d for d, pd in PI.items() if d > K)
    V_K = sum(float(pd) * d * d for d, pd in PI.items() if d <= K)
    rhs = tail_P + math.sqrt(2.0 * D * V_K)
    assert tail_Q <= rhs + 1e-12
    rows.append((K, tail_Q, tail_P, V_K, rhs))

print("a_n =", a_n)
print("lambda_n =", lambda_n)
print("Q =", Q)
print("D(Q||pi) =", D)
print("lambda_n/n =", lambda_n / N)
for K, tail_Q, tail_P, V_K, rhs in rows:
    print(
        f"K={K}: tail_Q={tail_Q:.16g}, tail_pi={tail_P:.16g}, "
        f"V_K={V_K:.16g}, rhs={rhs:.16g}"
    )
print("all assertions passed")
