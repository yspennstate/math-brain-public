from fractions import Fraction
from itertools import product
from collections import Counter, defaultdict


def rank_cols(cols):
    if not cols:
        return 0
    m = len(cols[0]); n = len(cols)
    A = [[Fraction(cols[j][i]) for j in range(n)] for i in range(m)]
    row = col = 0
    while row < m and col < n:
        pivot = next((i for i in range(row, m) if A[i][col]), None)
        if pivot is None:
            col += 1
            continue
        A[row], A[pivot] = A[pivot], A[row]
        p = A[row][col]
        A[row] = [x / p for x in A[row]]
        for i in range(m):
            if i != row and A[i][col]:
                f = A[i][col]
                A[i] = [A[i][j] - f * A[row][j] for j in range(n)]
        row += 1; col += 1
    return row


def rank_vectors(vectors):
    # vectors are rows; transpose by treating them as columns in their own coordinate space.
    if not vectors:
        return 0
    d = len(vectors[0])
    cols = [tuple(v[i] for v in vectors) for i in range(d)]
    return rank_cols(cols)


def bit_indices(mask):
    while mask:
        b = mask & -mask
        yield b.bit_length() - 1
        mask ^= b


def build_dimension(m):
    universe = [tuple((x >> i) & 1 for i in range(m)) for x in range(1, 2 ** m)]
    U = len(universe)
    total = 1 << U

    # Exact real ranks for every universe mask.
    ranks = [0] * total
    for mask in range(1, total):
        ranks[mask] = rank_cols([universe[i] for i in bit_indices(mask)])

    # Exact dissociation by subset-sum injectivity, with subset sums retained.
    zero = (0,) * m
    diss = [False] * total
    sums = [None] * total
    diss[0] = True
    sums[0] = {zero}
    for mask in range(1, total):
        b = mask & -mask
        i = b.bit_length() - 1
        prev = mask ^ b
        if not diss[prev]:
            continue
        old = sums[prev]
        v = universe[i]
        shifted = {tuple(a + z for a, z in zip(s, v)) for s in old}
        if old.isdisjoint(shifted):
            diss[mask] = True
            sums[mask] = old | shifted

    # For each dissociated mask, map universe target index to minimum negative width.
    # Ambient dimension <=4 has dissociated-set size <=5, so direct ternary enumeration is tiny.
    index_of = {v: i for i, v in enumerate(universe)}
    widths = {}
    coeffs = {}
    for mask, ok in enumerate(diss):
        if not ok:
            continue
        inds = list(bit_indices(mask))
        wmap = {}
        cmap = {}
        for cs in product((-1, 0, 1), repeat=len(inds)):
            if not any(cs):
                continue
            vec = tuple(sum(c * universe[i][d] for c, i in zip(cs, inds)) for d in range(m))
            t = index_of.get(vec)
            if t is None:
                continue
            neg = sum(c == -1 for c in cs)
            if t not in wmap or neg < wmap[t]:
                wmap[t] = neg
                cmap[t] = tuple(cs)
        widths[mask] = wmap
        coeffs[mask] = cmap

    return universe, ranks, diss, sums, widths, coeffs


def maximal_sets(Vmask, diss):
    out = []
    sub = Vmask
    while True:
        if diss[sub]:
            rem = Vmask & ~sub
            maximal = True
            rr = rem
            while rr:
                b = rr & -rr
                if diss[sub | b]:
                    maximal = False
                    break
                rr ^= b
            if maximal:
                out.append(sub)
        if sub == 0:
            break
        sub = (sub - 1) & Vmask
    return out


def profile(Vmask, universe, ranks, diss, widths):
    MS = maximal_sets(Vmask, diss)
    data = []
    maxw = 0
    for S in MS:
        ws = {}
        rem = Vmask & ~S
        for i in bit_indices(rem):
            assert i in widths[S]
            w = widths[S][i]
            ws[i] = w
            maxw = max(maxw, w)
        data.append((S, ws))

    rho = {}
    for k in range(maxw + 2):
        best = 10**9
        for S, ws in data:
            H = 0
            for i, w in ws.items():
                if w > k:
                    H |= 1 << i
            best = min(best, ranks[H])
        rho[k] = best
    return rho, data


def signed_relation_rank(Vmask, universe):
    inds = list(bit_indices(Vmask))
    N = len(inds)
    m = len(universe[0])

    # Every signed relation is the difference of two equal subset sums.
    groups = defaultdict(list)
    for smask in range(1 << N):
        s = [0] * m
        for j in range(N):
            if (smask >> j) & 1:
                v = universe[inds[j]]
                for d in range(m):
                    s[d] += v[d]
        groups[tuple(s)].append(smask)

    rels = []
    for masks in groups.values():
        if len(masks) < 2:
            continue
        base = masks[0]
        for other in masks[1:]:
            rel = tuple(((other >> j) & 1) - ((base >> j) & 1) for j in range(N))
            if any(rel):
                rels.append(rel)
    if not rels:
        return 0
    # These relations span all signed relations: within each equal-sum class, differences to one base span all pair differences.
    return rank_vectors(rels)


def unique_basis_coefficients(S, target, universe, widths, coeffs):
    # For a real basis S that is maximal dissociated, its signed representation is unique.
    inds = list(bit_indices(S))
    cs = coeffs[S][target]
    return {i: c for i, c in zip(inds, cs) if c}


def verify_common_negative_pivots(Vmask, r, k, data, universe, ranks, diss, widths, coeffs):
    checks = 0
    for S, ws in data:
        if S.bit_count() != r:
            continue
        omitted = list(bit_indices(Vmask & ~S))
        if len(omitted) != 3:
            continue
        heavy = [t for t in omitted if ws[t] > k]
        if len(heavy) < 2 or 2 * (k + 1) <= r:
            continue
        for u, v in __import__("itertools").permutations(heavy, 2):
            a = unique_basis_coefficients(S, u, universe, widths, coeffs)
            b = unique_basis_coefficients(S, v, universe, widths, coeffs)
            common_neg = [i for i in a if a[i] == -1 and b.get(i) == -1]
            assert common_neg
            for s in common_neg:
                Sprime = (S ^ (1 << s)) | (1 << u)
                assert diss[Sprime]
                assert ranks[Sprime] == r
                if v in widths[Sprime]:
                    # At a common negative pivot, signed compatibility forces the other
                    # heavy target to become light at any scale with 2(k+1)>r.
                    assert widths[Sprime][v] <= k
                else:
                    # If the transformed real coordinates leave {-1,0,1}, then no
                    # signed representation exists, exactly meaning v can be adjoined.
                    assert diss[Sprime | (1 << v)]
                checks += 1
    return checks


def synthetic_common_negative_checks(max_r=5):
    checks = 0
    for r in range(1, max_r + 1):
        vecs = [v for v in product((-1, 0, 1), repeat=r) if any(v)]
        for k in range(r + 1):
            if 2 * (k + 1) <= r:
                continue
            heavy = [v for v in vecs if sum(x == -1 for x in v) > k]
            for a in heavy:
                Na = {i for i, x in enumerate(a) if x == -1}
                for b in heavy:
                    common = [i for i in Na if b[i] == -1]
                    assert common
                    for s in common:
                        # Pivot on a_s=b_s=-1. New coefficient on entering basis element is +1;
                        # old coordinates transform as b_i-a_i.
                        transformed = [b[i] - a[i] for i in range(r) if i != s]
                        if all(x in (-1, 0, 1) for x in transformed):
                            neg = sum(x == -1 for x in transformed)  # entering coefficient is +1
                            assert neg <= k
                        else:
                            assert any(abs(x) == 2 for x in transformed)
                        checks += 1
    return checks


def main():
    total_configs = 0
    total_profile_checks = 0
    sigma_counts = Counter()
    profile_value_counts = Counter()
    max_ratio_num = 0
    max_ratio_den = 1
    max_ratio_witness = None
    common_pivot_checks = 0
    synthetic_pivot_checks = synthetic_common_negative_checks()
    rho3_checks = 0
    sigma_le2_checks = 0
    high_threshold_checks = 0
    local_by_dim = Counter()

    for m in range(1, 5):
        universe, ranks, diss, sums, widths, coeffs = build_dimension(m)
        U = len(universe)
        for Vmask in range(1, 1 << U):
            N = Vmask.bit_count()
            r = ranks[Vmask]
            if N - r != 3:
                continue
            total_configs += 1
            local_by_dim[m] += 1

            rho, data = profile(Vmask, universe, ranks, diss, widths)
            sigma = signed_relation_rank(Vmask, universe)
            assert 0 <= sigma <= 3
            sigma_counts[sigma] += 1

            # Prior signed-rank omission theorem.
            for S, ws in data:
                assert N - S.bit_count() <= sigma

            # Full profile inequality on the census.
            for k, z in rho.items():
                assert (k + 1) * z <= r
                total_profile_checks += 1
                profile_value_counts[z] += 1
                num = (k + 1) * z
                den = r
                if den and num * max_ratio_den > max_ratio_num * den:
                    max_ratio_num, max_ratio_den = num, den
                    max_ratio_witness = (m, Vmask, r, sigma, k, z, dict(rho))

                # New rank-three-heavy theorem.
                if z == 3:
                    assert 3 * (k + 1) <= r - 1
                    rho3_checks += 1

            # New sigma<=2 theorem (the census verifies its conclusion instance-by-instance).
            if sigma <= 2:
                for k, z in rho.items():
                    assert (k + 1) * z <= r
                    sigma_le2_checks += 1

            # New high-threshold vanishing rho(r)=0.
            # rho dictionary is computed through max width + 1; if r is beyond it, rho is automatically zero.
            if r in rho:
                assert rho[r] == 0
            else:
                maxw = max((w for _, ws in data for w in ws.values()), default=0)
                assert r > maxw
            high_threshold_checks += 1

            # Exact common-negative pivot lemma on every qualifying basis state and threshold.
            for k in range(0, r + 1):
                common_pivot_checks += verify_common_negative_pivots(
                    Vmask, r, k, data, universe, ranks, diss, widths, coeffs
                )

    print("DIMENSION_COUNTS", dict(sorted(local_by_dim.items())))
    print("TOTAL_NULLITY3_CONFIGURATIONS", total_configs)
    print("SIGNED_RELATION_RANK_COUNTS", dict(sorted(sigma_counts.items())))
    print("PROFILE_VALUE_COUNTS", dict(sorted(profile_value_counts.items())))
    print("PROFILE_INEQUALITY_CHECKS", total_profile_checks)
    print("SIGMA_LE2_PROFILE_CHECKS", sigma_le2_checks)
    print("RHO3_THEOREM_CHECKS", rho3_checks)
    print("HIGH_THRESHOLD_CHECKS", high_threshold_checks)
    print("COMMON_NEGATIVE_PIVOT_CHECKS", common_pivot_checks)
    print("SYNTHETIC_COMMON_NEGATIVE_ALGEBRA_CHECKS", synthetic_pivot_checks)
    print("MAX_OBSERVED_RATIO", f"{max_ratio_num}/{max_ratio_den}")
    print("MAX_RATIO_WITNESS", max_ratio_witness)
    print("ALL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
