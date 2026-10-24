from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
import json

MAXN = 10

def H(n):
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))

def q(n, i):
    return Fraction(n, 1) / (2 * H(n - 1) * i * (n - i))

for n in range(2, MAXN + 1):
    assert sum((q(n, i) for i in range(1, n)), Fraction(0)) == 1

def root_vector(n):
    v = [0] * (MAXN - 1)
    if n >= 2:
        v[n - 2] = 1
    return tuple(v)

@lru_cache(None)
def law(n):
    if n == 1:
        return {tuple([0] * (MAXN - 1)): Fraction(1)}
    out = defaultdict(Fraction)
    root = root_vector(n)
    for i in range(1, n):
        qi = q(n, i)
        for va, pa in law(i).items():
            for vb, pb in law(n - i).items():
                vv = tuple(root[k] + va[k] + vb[k] for k in range(MAXN - 1))
                out[vv] += qi * pa * pb
    assert sum(out.values(), Fraction(0)) == 1
    return dict(out)

laws = {n: law(n) for n in range(1, MAXN + 1)}

for n in range(2, MAXN + 1):
    for v in laws[n]:
        assert v[n - 2] == 1
        assert sum(v[:n - 1]) == n - 1
        assert all(x == 0 for x in v[n - 1:])

def mean(n, r):
    return sum((p * v[r - 2] for v, p in laws[n].items()), Fraction(0))

def cov(n, r, s):
    mr, ms = mean(n, r), mean(n, s)
    return sum(
        (p * (v[r - 2] - mr) * (v[s - 2] - ms) for v, p in laws[n].items()),
        Fraction(0),
    )

means = {
    (n, r): mean(n, r)
    for n in range(1, MAXN + 1)
    for r in range(2, MAXN + 1)
}
covs = {
    (n, r, s): cov(n, r, s)
    for n in range(1, MAXN + 1)
    for r in range(2, MAXN + 1)
    for s in range(2, MAXN + 1)
}

def eta(n, r, s):
    if n < 2:
        return Fraction(0)
    gr = {i: means[(i, r)] + means[(n - i, r)] for i in range(1, n)}
    gs = {i: means[(i, s)] + means[(n - i, s)] for i in range(1, n)}
    Er = sum((q(n, i) * gr[i] for i in range(1, n)), Fraction(0))
    Es = sum((q(n, i) * gs[i] for i in range(1, n)), Fraction(0))
    return (
        sum(
            (q(n, i) * (gr[i] - Er) * (gs[i] - Es) for i in range(1, n)),
            Fraction(0),
        )
        / n
    )

etas = {
    (n, r, s): eta(n, r, s)
    for n in range(2, MAXN + 1)
    for r in range(2, MAXN + 1)
    for s in range(2, MAXN + 1)
}

@lru_cache(None)
def occ(n, j):
    if n < j:
        return Fraction(0)
    if n == j:
        return Fraction(1)
    return sum(
        (
            Fraction(1, 1) / (H(n - 1) * (n - i)) * occ(i, j)
            for i in range(1, n)
        ),
        Fraction(0),
    )

covariance_recursion_checks = 0
green_representation_checks = 0
support_zero_checks = 0
row_sum_checks = 0
trace_checks = 0

for n in range(2, MAXN + 1):
    hn = H(n - 1)
    for r in range(2, n + 1):
        assert sum((covs[(n, r, s)] for s in range(2, n + 1)), Fraction(0)) == 0
        row_sum_checks += 1
        for s in range(2, n + 1):
            Cn = covs[(n, r, s)] / n
            rhs_rec = sum(
                (
                    (covs[(i, r, s)] / i) / (hn * (n - i))
                    for i in range(1, n)
                ),
                Fraction(0),
            ) + etas[(n, r, s)]
            assert Cn == rhs_rec
            covariance_recursion_checks += 1

            rhs_green = sum(
                (occ(n, j) * etas[(j, r, s)] for j in range(2, n + 1)),
                Fraction(0),
            )
            assert Cn == rhs_green
            green_representation_checks += 1

            for j in range(2, min(max(r, s), n + 1)):
                assert etas[(j, r, s)] == 0
                support_zero_checks += 1

    T = sum((etas[(n, r, r)] for r in range(2, MAXN + 1)), Fraction(0))
    direct = Fraction(0)
    for r in range(2, MAXN + 1):
        vals = {i: means[(i, r)] + means[(n - i, r)] for i in range(1, n)}
        E = sum((q(n, i) * vals[i] for i in range(1, n)), Fraction(0))
        direct += (
            sum((q(n, i) * (vals[i] - E) ** 2 for i in range(1, n)), Fraction(0))
            / n
        )
    assert T == direct
    trace_checks += 1

proj4 = defaultdict(Fraction)
for v, p in laws[4].items():
    proj4[(v[0], v[1], v[2])] += p
assert proj4 == {(1, 1, 1): Fraction(8, 11), (2, 0, 1): Fraction(3, 11)}
assert cov(4, 2, 3) == Fraction(-24, 121)

payload = {
    "result": "PASS",
    "scope": "independent exact P26 finite-core audit of P13/I0051 through n=10",
    "arithmetic": "fractions.Fraction only",
    "split_normalization_checks": MAXN - 1,
    "state_counts": {str(n): len(laws[n]) for n in range(1, MAXN + 1)},
    "n4_joint_law": {
        "(1, 1, 1)": "8/11",
        "(2, 0, 1)": "3/11",
    },
    "n4_cov_N2_N3": str(cov(4, 2, 3)),
    "covariance_recursion_checks": covariance_recursion_checks,
    "green_representation_checks": green_representation_checks,
    "support_zero_checks": support_zero_checks,
    "deterministic_covariance_row_sum_checks": row_sum_checks,
    "trace_forcing_identity_checks": trace_checks,
    "note": "Independent P26 checker; the theorem-sized analytic audit is established separately in the P26 written report.",
}
print("P26-P13-I0051-INDEPENDENT-EXACT-AUDIT: PASS")
print(json.dumps(payload, indent=2, sort_keys=True))
print("END P26-P13-I0051-INDEPENDENT-EXACT-AUDIT")
