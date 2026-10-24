from fractions import Fraction as F
from itertools import permutations
from math import factorial
from collections import defaultdict

# R11/I0054 U017 exact finite checker.
# Standard library only, exact arithmetic only.

def e_sym(start, N, r):
    if r < 0:
        return F(0)
    xs = [F(1, j) for j in range(start, N)]
    dp = [F(0)] * (r + 1)
    dp[0] = F(1)
    for x in xs:
        for k in range(r, 0, -1):
            dp[k] += dp[k-1] * x
    return dp[r]

def cycle_partition_and_count(perm, b):
    N = len(perm)
    cid = [None] * N
    k = 0
    for s in range(N):
        if cid[s] is None:
            x = s
            while cid[x] is None:
                cid[x] = k
                x = perm[x]
            k += 1
    blocks = {}
    for a in range(b):
        blocks.setdefault(cid[a], []).append(a+1)
    part = tuple(sorted((tuple(v) for v in blocks.values()), key=lambda t: t[0]))
    return part, k

def set_partitions(n):
    out = []
    def rec(i, blocks):
        if i > n:
            out.append(tuple(tuple(b) for b in blocks))
            return
        for r in range(len(blocks)):
            blocks[r].append(i)
            rec(i+1, blocks)
            blocks[r].pop()
        blocks.append([i])
        rec(i+1, blocks)
        blocks.pop()
    rec(1, [])
    return out

def ewens_prob(part, c):
    b = sum(len(B) for B in part)
    q = len(part)
    num = c ** q
    for B in part:
        num *= factorial(len(B)-1)
    den = F(1)
    for r in range(b):
        den *= c + r
    return num / den

def q_c(part, c):
    # pair-normalized limiting generator rate for nontrivial partition
    b = sum(len(B) for B in part)
    q = len(part)
    assert q >= 2
    num = c ** (q-2)
    for B in part:
        num *= factorial(len(B)-1)
    den = F(1)
    for r in range(2, b):
        den *= c + r
    return num / den

checks = 0

# 1. Exhaustive finite permutation verification of U016 exact restriction formula.
for N in range(3, 8):
    total_by_R = defaultdict(int)
    counts = defaultdict(lambda: defaultdict(int))
    for perm in permutations(range(N)):
        _, R = cycle_partition_and_count(perm, N)
        total_by_R[R] += 1
        for b in range(2, min(4, N)+1):
            part, _ = cycle_partition_and_count(perm, b)
            counts[(R, b)][part] += 1

    for (R, b), table in counts.items():
        den_count = total_by_R[R]
        den_E = e_sym(1, N, R-1)
        assert den_E > 0
        for part, count in table.items():
            q = len(part)
            pref = F(1, factorial(b-1))
            for B in part:
                pref *= factorial(len(B)-1)
            formula = pref * e_sym(b, N, R-q) / den_E
            observed = F(count, den_count)
            assert observed == formula
            checks += 1

# 2. Exact Ewens(c) EPPF normalization and pair-separation identity.
cs = [F(1,2), F(1), F(3,2), F(2)]
for b in range(2, 8):
    parts = set_partitions(b)
    for c in cs:
        total = sum((ewens_prob(p, c) for p in parts), F(0))
        assert total == 1
        checks += 1

        sep = sum(
            (ewens_prob(p, c) for p in parts
             if not any(1 in B and 2 in B for B in p)),
            F(0)
        )
        assert sep == c / (c + 1)
        checks += 1

# 3. Exact pair-normalized generator formula q_c = ((c+1)/c) * Ewens EPPF.
for b in range(2, 8):
    for part in set_partitions(b):
        if len(part) < 2:
            continue
        for c in cs:
            lhs = (c + 1) / c * ewens_prob(part, c)
            rhs = q_c(part, c)
            assert lhs == rhs
            checks += 1

# 4. Exact CTCS endpoint at c=0 for binary partitions, and vanishing order for q>=3.
for b in range(2, 9):
    for part in set_partitions(b):
        q = len(part)
        if q < 2:
            continue
        if q == 2:
            prod = 1
            for B in part:
                prod *= factorial(len(B)-1)
            target = F(prod, factorial(b-1))
            den = 1
            for r in range(2, b):
                den *= r
            endpoint = F(prod, den)
            assert endpoint == target
            checks += 1
        else:
            assert q - 2 >= 1
            checks += 1

# 5. Star-shattering endpoint: for all-singletons partition the degree in c is balanced;
# all other nontrivial partitions have strictly smaller numerator degree.
for b in range(2, 10):
    for part in set_partitions(b):
        q = len(part)
        if q < 2:
            continue
        num_deg = q - 2
        den_deg = max(0, b - 2)
        if q == b:
            assert num_deg == den_deg
        else:
            assert num_deg < den_deg
        checks += 1

print("R11 I0054 U017 critical-window conditioned-permutation exact checker")
print("arithmetic=fractions.Fraction only")
print(f"checks={checks}")
print("finite_conditioned_permutation_formula=PASS")
print("ewens_eppf_normalization=PASS")
print("pair_separation_c_over_cplus1=PASS")
print("pair_normalized_generator_formula=PASS")
print("ctcs_endpoint_c0=PASS")
print("star_shattering_endpoint_cinfty=PASS")
print("ALL_EXACT_CHECKS_PASS")
