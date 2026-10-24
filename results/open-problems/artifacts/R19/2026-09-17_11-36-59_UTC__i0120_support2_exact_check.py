from itertools import combinations
from math import gcd, comb

K = 14
THRESHOLD_DENOM = K + 1


def folded(x, p):
    x %= p
    return min(x, p-x)


def bad_mask(v, p):
    n = (p-1)//2
    ans = 0
    for a in range(1, n+1):
        # At t=a/p, v is bad iff ||av/p|| < 1/15.
        if THRESHOLD_DENOM * folded(a*v, p) < p:
            ans |= 1 << (a-1)
    return ans


def support_hist(p, fixed):
    n = (p-1)//2
    masks = [0] + [bad_mask(v, p) for v in range(1, n+1)]
    full = (1 << n) - 1
    fixed = tuple(sorted(set(fixed)))
    fixed_mask = 0
    for v in fixed:
        fixed_mask |= masks[v]
    remaining = [v for v in range(1, n+1) if v not in fixed]
    hist = {}
    for j in range(0, K-len(fixed)+1):
        for choice in combinations(remaining, j):
            mask = fixed_mask
            for v in choice:
                mask |= masks[v]
            if mask == full:
                s = len(fixed) + j
                hist[s] = hist.get(s, 0) + 1
    return hist


def marked_candidate_count(hist):
    # One normalized marked speed (unrestricted) or one normalized marked
    # relation pair (relation-sliced). A covering total support of size s
    # contributes C(13,s-1) marked multiplicity patterns.
    return sum(count * comb(13, s-1) for s, count in hist.items())


def support_two_shapes():
    out = []
    for a in range(2, 32):
        for b in range(1, a):
            if a+b <= 31 and (a+b) % 2 == 1 and gcd(a, b) == 1:
                out.append((a, b))
    return out


SHAPES = support_two_shapes()
assert len(SHAPES) == 106


def ratio_class(shape, p):
    a, b = shape
    return folded(a * pow(b, -1, p), p)


print("R19 I0120 exact support-two relation-slice check")
print("support_two_shapes =", len(SHAPES))
assert (2, 1) in SHAPES and (4, 1) in SHAPES

for p in (37, 41, 43):
    n = (p-1)//2

    # For the first three primes above 31, floor((p-1)/15)=2,
    # so every folded bad-time set has exactly two vertices.
    assert (p-1)//15 == 2
    for v in range(1, n+1):
        assert bad_mask(v, p).bit_count() == 2

    base_hist = support_hist(p, (1,))
    base_count = marked_candidate_count(base_hist)

    ratios = sorted({ratio_class(shape, p) for shape in SHAPES})
    rows = []
    for r in ratios:
        hist = support_hist(p, (1, r))
        count = marked_candidate_count(hist)
        rows.append((r, count, sum(hist.values()), min(hist), dict(sorted(hist.items()))))

    minimum = min(row[1] for row in rows)
    maximum = max(row[1] for row in rows)
    min_ratios = [row[0] for row in rows if row[1] == minimum]
    max_ratios = [row[0] for row in rows if row[1] == maximum]
    r2 = next(row for row in rows if row[0] == 2)
    r4 = next(row for row in rows if row[0] == 4)

    inv2 = folded(pow(2, -1, p), p)
    inv4 = folded(pow(4, -1, p), p)
    assert set(min_ratios) == {2, inv2}
    assert set(max_ratios) == {4, inv4}
    assert r2[1] == minimum and r4[1] == maximum

    # Exact pre-cover marked-orbit candidate-space ratio.
    unrestricted_precover = comb(n+12, 13)
    relation_precover = comb(n+11, 12)
    assert unrestricted_precover * 13 == relation_precover * (n+12)

    print(f"p={p} n={n} relation_ratio_classes={len(ratios)}")
    print("  normalized_unrestricted_cover_hist =", dict(sorted(base_hist.items())))
    print("  normalized_unrestricted_marked_candidates =", base_count)
    print(f"  r=2 hist={r2[4]} supports={r2[2]} marked_candidates={r2[1]}")
    print(f"  r=4 hist={r4[4]} supports={r4[2]} marked_candidates={r4[1]}")
    print("  minimum_candidate_ratios =", min_ratios, "value =", minimum)
    print("  maximum_candidate_ratios =", max_ratios, "value =", maximum)
    print(
        "  pre_cover_candidate_ratio =",
        f"{unrestricted_precover}/{relation_precover} = (n+12)/13 = {n+12}/13",
    )

print("ALL_EXACT_CHECKS_PASS")
