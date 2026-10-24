#!/usr/bin/env python3
"""Independent audit of B05_A023_FULL_RANK_SHIELD_v1.

This code does not import or invoke the author's checker.  It separately
enumerates affine spectral supports, evaluates the upper-set functional from
support counts, reconstructs truth-table Walsh spectra, and checks restriction
and disjoint-tensor identities.  All structural inequalities use exact
Fractions; floating arithmetic is used only for direct redundant U checks.
"""

from fractions import Fraction
from itertools import product
from math import log2
from random import Random


def bitparity(z):
    return z.bit_count() & 1


def gf2_rank(vectors, width):
    pivots = [0] * width
    ans = 0
    for value in vectors:
        v = value
        while v:
            j = v.bit_length() - 1
            if pivots[j]:
                v ^= pivots[j]
            else:
                pivots[j] = v
                ans += 1
                break
    return ans


def matrices(s, m):
    mask = (1 << m) - 1
    for packed in range(1 << (s * m)):
        yield tuple((packed >> (i * m)) & mask for i in range(s))


def image_point(rows, y, shift):
    out = shift
    for i, row in enumerate(rows):
        out ^= bitparity(row & y) << i
    return out


def upper_support_formula(rows, m, shift):
    """Return U(uniform affine image) exactly and cross-check cap counts."""
    s = len(rows)
    support = [image_point(rows, y, shift) for y in range(1 << m)]
    assert len(set(support)) == 1 << m
    rank_sum = 0
    direct_sum = 0
    for alpha in support:
        selected = [rows[i] for i in range(s) if (alpha >> i) & 1]
        r = gf2_rank(selected, m)
        rank_sum += r
        cap = sum(1 for gamma in support if (gamma & alpha) == alpha)
        assert cap > 0 and cap & (cap - 1) == 0
        assert cap == 1 << (m - r)
        direct_sum += cap.bit_length() - 1
    denom = 1 << m
    assert direct_sum == m * denom - rank_sum
    return Fraction(direct_sum, denom), support, rank_sum


def walsh_direct(values):
    n = len(values).bit_length() - 1
    out = []
    for freq in range(1 << n):
        out.append(sum(v * (-1 if bitparity(freq & point) else 1)
                       for point, v in enumerate(values)))
    return out


def truth(rows, m, shift_a, shift_b, core_mask, c=0):
    s = len(rows)
    vals = []
    for point in range(1 << (s + m)):
        x = point & ((1 << s) - 1)
        y = point >> s
        phase = bitparity(shift_a & x) ^ bitparity(shift_b & y) ^ c
        for i, row in enumerate(rows):
            phase ^= ((x >> i) & 1) & bitparity(row & y)
        core_bit = (core_mask >> y) & 1
        vals.append(-1 if phase ^ core_bit else 1)
    return vals


def spectral_u(values):
    W = walsh_direct(values)
    q = len(values) ** 2
    p = [Fraction(w * w, q) for w in W]
    total = 0.0
    for mask, mass in enumerate(p):
        if not mass:
            continue
        cap = sum(p[t] for t in range(len(p)) if (t & mask) == mask)
        total += float(mass) * log2(float(cap / mass))
    return total, p, W


def restrict_values(values, fixed):
    n = len(values).bit_length() - 1
    free = [i for i in range(n) if i not in fixed]
    out = []
    for z in range(1 << len(free)):
        point = 0
        for i, val in fixed.items():
            point |= val << i
        for j, i in enumerate(free):
            point |= ((z >> j) & 1) << i
        out.append(values[point])
    return out


def tensor_values(f, g):
    # f coordinates first, g coordinates second.
    return [f[x] * g[y] for y in range(len(g)) for x in range(len(f))]


def main():
    affine_cases = 0
    exact_cap_checks = 0
    strengthened_checks = 0
    max_ratio = Fraction(0)
    max_case = None

    # Exhaust all full-column-rank matrices and affine x-shifts in the listed
    # ranges.  This checks both the author's constant 4 and the new constant 2.
    for s, m in [(1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (3, 3),
                 (4, 1), (4, 2), (4, 3)]:
        for rows in matrices(s, m):
            if gf2_rank(rows, m) != m:
                continue
            nonzero = sum(bool(row) for row in rows)
            for a in range(1 << s):
                ua, support, rank_sum = upper_support_formula(rows, m, a)
                # The beta block is a uniform m-cube and contributes m/2.
                up = ua + Fraction(m, 2)
                zero_affine = sum(1 for i, row in enumerate(rows)
                                  if row == 0 and ((a >> i) & 1))
                ix = Fraction(nonzero, 2) + zero_affine
                assert up <= 2 * ix              # reviewer sharpening
                assert up <= 4 * ix              # author's stated theorem

                # Independent basis-row proof: greedily extract m independent
                # physical rows, then average their selected indicators.
                basis = []
                old = 0
                for i, row in enumerate(rows):
                    new = gf2_rank([rows[j] for j in basis] + [row], m)
                    if new > old:
                        basis.append(i)
                        old = new
                assert len(basis) == m
                selected_basis_sum = sum(
                    sum((alpha >> i) & 1 for i in basis) for alpha in support
                )
                assert selected_basis_sum == m * (1 << (m - 1))
                assert rank_sum >= selected_basis_sum

                ratio = up / ix
                if ratio > max_ratio:
                    max_ratio, max_case = ratio, (s, m, rows, a, up, ix)
                affine_cases += 1
                exact_cap_checks += len(support)
                strengthened_checks += 4

    assert max_ratio == 2

    # Direct Walsh reconstruction, independent of the affine-support proof.
    walsh_instances = 0
    walsh_atoms = 0
    for s, m in [(1, 1), (2, 1), (2, 2), (3, 1), (3, 2)]:
        for rows in matrices(s, m):
            if gf2_rank(rows, m) != m:
                continue
            core_choices = range(1 << (1 << m))
            # Full affine enumeration for m=1; deterministic representative
            # phases for m=2 keeps this independent check bounded.
            phase_choices = product(range(1 << s), range(1 << m), range(2))
            phases = list(phase_choices)
            if m == 2 and s == 3:
                phases = phases[::5]
            for a, b, c in phases:
                for dmask in core_choices:
                    vals = truth(rows, m, a, b, dmask, c)
                    W = walsh_direct(vals)
                    nz = [w for w in W if w]
                    assert len(nz) == 1 << (2 * m)
                    assert all(abs(w) == 1 << s for w in nz)
                    walsh_instances += 1
                    walsh_atoms += len(W)

    # Seeded larger Walsh reconstructions with arbitrary cores.
    rng = Random(190941)
    for s, m in [(4, 3), (5, 3), (5, 4)]:
        for _ in range(35):
            while True:
                rows = tuple(rng.randrange(1 << m) for _ in range(s))
                if gf2_rank(rows, m) == m:
                    break
            vals = truth(rows, m, rng.randrange(1 << s), rng.randrange(1 << m),
                         rng.randrange(1 << (1 << m)), rng.randrange(2))
            W = walsh_direct(vals)
            nz = [w for w in W if w]
            assert len(nz) == 1 << (2 * m)
            assert all(abs(w) == 1 << s for w in nz)
            walsh_instances += 1
            walsh_atoms += len(W)

    # Direct restriction and tensor checks on fresh samples.  These are
    # redundant to the analytic nonnegativity/tensorization proof.
    tree_checks = 0
    tensor_checks = 0
    telescoping_checks = 0
    rng = Random(23094)
    for _ in range(500):
        m = rng.choice([1, 2, 3])
        s = rng.choice([m, m + 1])
        while True:
            rows = tuple(rng.randrange(1 << m) for _ in range(s))
            if gf2_rank(rows, m) == m:
                break
        a = rng.randrange(1 << s)
        vals = truth(rows, m, a, rng.randrange(1 << m),
                     rng.randrange(1 << (1 << m)), rng.randrange(2))
        root_u, _, _ = spectral_u(vals)
        nonzero = sum(bool(row) for row in rows)
        zero_affine = sum(1 for i, row in enumerate(rows)
                          if row == 0 and ((a >> i) & 1))
        ix = nonzero / 2 + zero_affine
        assert root_u <= 2 * ix + 1e-11

        n = s + m
        i = rng.randrange(n)
        branch = [spectral_u(restrict_values(vals, {i: bit}))[0] for bit in [0, 1]]
        loss = root_u - sum(branch) / 2
        assert loss <= root_u + 1e-12 <= 2 * ix + 1e-10
        tree_checks += 1

        # Branch-dependent second query: exact telescoping of signed charges.
        choices = []
        leaf_u = []
        local_second = []
        for bit in [0, 1]:
            candidates = [j for j in range(n) if j != i]
            j = rng.choice(candidates)
            choices.append(j)
            child_u = branch[bit]
            gs = [spectral_u(restrict_values(vals, {i: bit, j: z}))[0]
                  for z in [0, 1]]
            leaf_u.extend(gs)
            local_second.append(0.5 * (child_u - sum(gs) / 2))
        root_charge = root_u - sum(branch) / 2
        node_sum = root_charge + sum(local_second)
        endpoint = root_u - sum(leaf_u) / 4
        assert abs(node_sum - endpoint) < 2e-11
        assert endpoint <= root_u + 1e-12
        telescoping_checks += 1

        h = [rng.choice([-1, 1]) for _ in range(4)]
        hu, _, _ = spectral_u(h)
        product_u, _, _ = spectral_u(tensor_values(vals, h))
        assert abs(product_u - root_u - hu) < 3e-10
        for bit in [0, 1]:
            child = restrict_values(vals, {i: bit})
            cu, _, _ = spectral_u(child)
            chu, _, _ = spectral_u(tensor_values(child, h))
            assert abs(chu - cu - hu) < 3e-10
        tensor_checks += 3

    # Sharpness: square invertible support and a complete reveal have leaf U=0.
    sharpness_checks = 0
    for m in range(1, 9):
        rows = tuple(1 << i for i in range(m))
        ua, _, _ = upper_support_formula(rows, m, 0)
        up = ua + Fraction(m, 2)
        ix = Fraction(m, 2)
        assert up == m and up == 2 * ix
        sharpness_checks += 1

    print("INDEPENDENT FULL-RANK SHIELD REVIEW: PASS")
    print("affine support cases:", affine_cases)
    print("exact cap/rank identities:", exact_cap_checks)
    print("exact theorem/sharpening assertions:", strengthened_checks)
    print("direct Walsh instances:", walsh_instances)
    print("direct Walsh atoms:", walsh_atoms)
    print("one-step restriction checks:", tree_checks)
    print("adaptive two-level telescoping checks:", telescoping_checks)
    print("disjoint tensor-additivity checks:", tensor_checks)
    print("sharpness checks:", sharpness_checks)
    print("maximum exact U/I_x ratio:", max_ratio)
    print("maximizer witness:", max_case)
    print("verdict v1: ACCEPTED at declared constants 4/2")
    print("new reviewer-derived strengthening: constant 2 for every full-column-rank M")
    print("full FEI: OPEN")


if __name__ == "__main__":
    main()
