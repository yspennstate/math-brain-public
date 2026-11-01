from fractions import Fraction
from collections import defaultdict
from math import log

support = [0, 1, 3, 5]
pi = {0: Fraction(1, 2), 1: Fraction(1, 4), 3: Fraction(1, 8), 5: Fraction(1, 8)}
nu = sum(Fraction(k) * p for k, p in pi.items())
qbar = {k: Fraction(k) * p / nu for k, p in pi.items() if k > 0}

def conv_pmf(N):
    d = {0: Fraction(1)}
    for _ in range(N):
        nd = defaultdict(Fraction)
        for s, ps in d.items():
            for k, pk in pi.items():
                nd[s + k] += ps * pk
        d = dict(nd)
    return d

PMF = {N: conv_pmf(N) for N in range(0, 7)}

def palm_kernel(N, M):
    pNM = PMF[N].get(M, Fraction(0))
    if pNM == 0:
        return None
    out = {}
    for k, pk in pi.items():
        if k <= 0:
            continue
        prev = PMF[N - 1].get(M - k, Fraction(0))
        if prev:
            out[k] = Fraction(N * k, M) * pk * prev / pNM
    return out

def KL(P, Q):
    return sum(float(p) * (log(float(p)) - log(float(Q[k]))) for k, p in P.items())

def b(N, M):
    return -log(float(PMF[N][M]))

def binary_kl(a, q):
    if a == 0:
        return -log(1-q)
    if a == 1:
        return -log(q)
    return a*log(a/q) + (1-a)*log((1-a)/(1-q))

max_identity_err = 0.0
min_binary_slack = float("inf")
tested_states = 0

for N in range(2, 7):
    for M, pNM in PMF[N].items():
        if M == 0 or pNM == 0:
            continue
        K = palm_kernel(N, M)
        if not K:
            continue
        if sum(K.values()) != 1:
            raise AssertionError(("kernel normalization", N, M, sum(K.values())))

        lhs = b(N, M) - sum(float(pk) * b(N - 1, M - k) for k, pk in K.items())
        rhs = KL(K, qbar) + log((M / N) / float(nu))
        max_identity_err = max(max_identity_err, abs(lhs-rhs))

        for L in (1, 2, 3, 4):
            alpha = sum(float(pk) for k, pk in K.items() if k > L)
            q = sum(float(pk) for k, pk in qbar.items() if L < k <= M)
            if alpha == 0 or q == 0:
                continue
            d = binary_kl(alpha, q)
            lower = alpha * log(1/q) - log(2)
            min_binary_slack = min(min_binary_slack, d-lower)
        tested_states += 1

# Deterministic pathwise cloud-hit check.
# At any history, size-biased next-box cloud probability equals remaining cloud mass / remaining total.
allocations = [
    [9, 8, 4, 2, 1],
    [12, 7, 6, 3, 1, 1],
    [15, 10, 5, 4, 2, 1],
]
min_pathwise_slack = float("inf")
for y in allocations:
    L = 5
    cloud0 = sum(v for v in y if v > L)
    total0 = sum(y)
    removed_cap = max(1, cloud0 // 4)
    n = len(y)
    for mask in range(1 << n):
        removed = [y[i] for i in range(n) if mask & (1 << i)]
        rem = [y[i] for i in range(n) if not (mask & (1 << i))]
        if not rem or sum(removed) >= removed_cap:
            continue
        rem_total = sum(rem)
        rem_cloud = sum(v for v in rem if v > L)
        hit = rem_cloud / rem_total
        deterministic_lower = max(0.0, (cloud0 - removed_cap) / total0)
        min_pathwise_slack = min(min_pathwise_slack, hit - deterministic_lower)

print(f"nu={float(nu):.12g}")
print(f"qbar_normalization={float(sum(qbar.values())):.12g}")
print(f"tested_exact_sum_states={tested_states}")
print(f"max_one_step_identity_error={max_identity_err:.3e}")
print(f"min_binary_KL_slack={min_binary_slack:.12g}")
print(f"min_pathwise_cloud_hit_slack={min_pathwise_slack:.12g}")

if max_identity_err > 1e-12:
    raise SystemExit("FAIL: Palm identity")
if min_binary_slack < -1e-12:
    raise SystemExit("FAIL: binary KL lower bound")
if min_pathwise_slack < -1e-12:
    raise SystemExit("FAIL: pathwise cloud hit lower bound")
print("PASS")
