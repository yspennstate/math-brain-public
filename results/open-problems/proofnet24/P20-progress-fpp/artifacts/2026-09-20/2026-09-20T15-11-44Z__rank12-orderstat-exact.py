from fractions import Fraction
from math import comb
from itertools import combinations
from decimal import Decimal, getcontext


def J(n: int) -> Fraction:
    """Integral of [exp(-t)(1+t)]^n from 0 to infinity."""
    s = Fraction(0, 1)
    fact = 1
    for m in range(n + 1):
        if m:
            fact *= m
        s += Fraction(comb(n, m) * fact, n ** (m + 1))
    return s


def expected_sum_first_k_gamma2(N: int, K: int) -> Fraction:
    """Exact E[sum_{r=1}^K X_(r)] for N iid Gamma(2,1)."""
    ans = Fraction(0, 1)
    for q in range(K):
        inner = Fraction(0, 1)
        for a in range(q + 1):
            inner += Fraction((-1) ** a * comb(q, a), 1) * J(N - q + a)
        ans += (K - q) * comb(N, q) * inner
    return ans


def construct_paths(W, S):
    """K+1 edge-disjoint 2-edge routes from K active inputs to distinct outputs."""
    S = set(S)
    K = len(S)
    assert 3 <= K <= W
    chosen = None
    direction = None
    for i in sorted(S):
        if 1 <= i <= W - 1:
            if i + 1 not in S:
                chosen, direction = i, "right"
                break
            if i - 1 not in S:
                chosen, direction = i, "left"
                break
    assert chosen is not None, (W, sorted(S))
    i = chosen
    paths = []
    for r in sorted(S):
        if r == i and direction == "right":
            paths.append((("I", r), ("M", r - 1), ("O", r)))
        elif r == i and direction == "left":
            paths.append((("I", r), ("M", r), ("O", r)))
        elif r < W:
            paths.append((("I", r), ("M", r), ("O", r)))
        else:
            paths.append((("I", r), ("M", r - 1), ("O", r)))
    if direction == "right":
        paths.append((("I", i), ("M", i), ("O", i + 1)))
    else:
        paths.append((("I", i), ("M", i - 1), ("O", i - 1)))
    return paths


def edge_set(path):
    return {
        tuple(sorted((path[0], path[1]))),
        tuple(sorted((path[1], path[2]))),
    }


K = 12
N = K + 1
eta = Fraction(1, 10)
Emin = J(N)
Esum = expected_sum_first_k_gamma2(N, K)
q = (1 - eta) * Emin + eta * Esum / K

lambda_reserve = Fraction(3, 5)
q_upper = Fraction(537, 1000)
candidate_allowance = Fraction(63, 1000)
outer_threshold = Fraction(25, 1)
source_diag_cap = Fraction(3002823, 5000000)
defect_reserve = source_diag_cap - lambda_reserve

assert q < q_upper
assert q_upper + candidate_allowance == lambda_reserve
assert defect_reserve == Fraction(2823, 5000000)

coercive_at_outer = Fraction(2, 1) + eta * (K - 1) - eta * outer_threshold
assert coercive_at_outer == lambda_reserve
assert Fraction(3, 50) < candidate_allowance

finite_error_const = Fraction(2, 1) + eta * (K - 1) + Fraction(48, 1) - lambda_reserve
assert finite_error_const == Fraction(101, 2)

for W in range(3, 10):
    universe = range(W + 1)
    for K0 in range(3, W + 1):
        for S in combinations(universe, K0):
            ps = construct_paths(W, S)
            assert len(ps) == K0 + 1
            outs = [p[-1] for p in ps]
            assert len(set(outs)) == K0 + 1
            seen = set()
            for p in ps:
                ee = edge_set(p)
                assert seen.isdisjoint(ee), (W, S, p, seen, ee)
                seen |= ee

getcontext().prec = 60
q_dec = Decimal(q.numerator) / Decimal(q.denominator)
print("K =", K, "N =", N, "eta =", eta)
print("Emin exact =", Emin)
print("Esum_first_K exact =", Esum)
print("q exact =", q)
print("q decimal =", q_dec)
print("q < 537/1000 =", q < q_upper)
print("candidate allowance =", candidate_allowance, float(candidate_allowance))
print("outer average threshold =", outer_threshold)
print("parent reserve defect =", defect_reserve, float(defect_reserve))
print("finite-to-infinite additive/N constant =", finite_error_const, float(finite_error_const))
print("SMALL_MATCHING_SANITY_PASS = True")
print("P20-T10-RANK12-ORDERSTAT-CERT: ALL_EXACT_CHECKS_PASS = True")
