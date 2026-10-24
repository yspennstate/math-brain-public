"""Exact exclusion of a low-degree Paley orientation-code ansatz for HARD8-04.

Pinned input: the 58 F_617 Gauss periods from the previously verified
split-617 checker. This script does not recompute that unchanged field
checkpoint; it uses it exactly as directed by the campaign's reuse rule.

Ansatz (broader d=9 GS profile |X|=(253,253,253,244)):
  * every X_i contains 0;
  * among each negation-pair of K-orbits {C_j,C_{j+29}}, choose at most one;
  * for i=0,1,2, omit one pair a and orient all other pairs by
        s(j)=sigma*Legendre(j-a mod 29);
  * for i=3, omit two pairs a<b and orient all other pairs by
        s(j)=sigma*Legendre((j-a)(j-b) mod 29).

For each block we compute the exact 29 F_617 split-prime contributions
F(c)F(c+29). The GS target is that the four contributions sum to 523 in
every coordinate c=0,...,28. A meet-in-the-middle exhaustive search proves
that no quartet in this ansatz even satisfies c=0,1,2 simultaneously, hence
none satisfies all 29 equations.
"""

from collections import Counter

Q = 617
TARGET = 523
ETA = [
    522, 572, 267, 172, 212, 89, 589, 353, 199, 88, 561, 370,
    96, 573, 266, 565, 427, 588, 88, 596, 142, 29, 595, 286,
    498, 22, 552, 282, 237, 195, 443, 578, 28, 264, 109, 480,
    218, 588, 387, 388, 330, 400, 10, 59, 556, 569, 86, 56,
    218, 531, 368, 38, 177, 342, 548, 351, 82, 274,
]

assert len(ETA) == 58
assert sum(ETA) % Q == Q - 1


def legendre29(a: int) -> int:
    a %= 29
    if a == 0:
        return 0
    return 1 if pow(a, 14, 29) == 1 else -1


def one_hole_block(a: int, sigma: int):
    sel = []
    for j in range(29):
        if j == a:
            continue
        s = sigma * legendre29(j - a)
        assert s in (-1, 1)
        sel.append(j if s == 1 else j + 29)
    assert len(sel) == 28
    return tuple(sel)


def two_hole_block(a: int, b: int, sigma: int):
    assert 0 <= a < b < 29
    sel = []
    for j in range(29):
        if j in (a, b):
            continue
        s = sigma * legendre29((j - a) * (j - b))
        assert s in (-1, 1)
        sel.append(j if s == 1 else j + 29)
    assert len(sel) == 27
    return tuple(sel)


def fourier_values(sel):
    # 0 belongs to every negative set in the (17,17,17,35) profile.
    return tuple((1 + sum(ETA[(c + j) % 58] for j in sel)) % Q for c in range(58))


def contribution(sel):
    f = fourier_values(sel)
    return tuple((f[c] * f[c + 29]) % Q for c in range(29))


ONE = []
for a in range(29):
    for sigma in (-1, 1):
        sel = one_hole_block(a, sigma)
        ONE.append((contribution(sel), (a, sigma), sel))

TWO = []
for a in range(29):
    for b in range(a + 1, 29):
        for sigma in (-1, 1):
            sel = two_hole_block(a, b, sigma)
            TWO.append((contribution(sel), (a, b, sigma), sel))

assert len(ONE) == 58
assert len(TWO) == 2 * (29 * 28 // 2) == 812

# First three GS blocks are interchangeable. It is enough for existence to
# enumerate an unordered pair for the first two, and an arbitrary third block.
pair_prefix = {r: Counter() for r in (1, 2, 3)}
pair_full = {}
pair_count = 0
for i, (u, _, _) in enumerate(ONE):
    for j in range(i, len(ONE)):
        v = ONE[j][0]
        w = tuple((u[c] + v[c]) % Q for c in range(29))
        pair_count += 1
        pair_full.setdefault(w, (i, j))
        for r in (1, 2, 3):
            pair_prefix[r][w[:r]] += 1

assert pair_count == 58 * 59 // 2 == 1711

# Exhaustively count symmetry-reduced quartets satisfying the first r target
# equations. If r=3 has zero candidates, the full 29-equation system is
# certainly empty in this ansatz.
prefix_hits = {1: 0, 2: 0, 3: 0}
first_example = {}
for k, (u3, _, _) in enumerate(ONE):
    for ell, (u4, _, _) in enumerate(TWO):
        need = tuple((TARGET - u3[c] - u4[c]) % Q for c in range(29))
        for r in (1, 2, 3):
            hits = pair_prefix[r][need[:r]]
            prefix_hits[r] += hits
            if hits and r not in first_example:
                first_example[r] = (k, ell, need[:r], hits)

assert prefix_hits[1] == 130692
assert prefix_hits[2] == 192
assert prefix_hits[3] == 0

# Full-vector MITM check, logically redundant after the prefix-3 exclusion.
full_solution = None
for k, (u3, _, _) in enumerate(ONE):
    for ell, (u4, _, _) in enumerate(TWO):
        need = tuple((TARGET - u3[c] - u4[c]) % Q for c in range(29))
        if need in pair_full:
            full_solution = (pair_full[need], k, ell)
            break
    if full_solution is not None:
        break
assert full_solution is None

print("field", "F_617")
print("profile_negative_set_sizes", (253, 253, 253, 244))
print("one_hole_codewords", len(ONE))
print("two_hole_codewords", len(TWO))
print("unordered_first_pair_count", pair_count)
print("distinct_full_first_pair_sums", len(pair_full))
print("labelled_ansatz_quartets", len(ONE) ** 3 * len(TWO))
print("prefix1_symmetry_reduced_hits", prefix_hits[1])
print("prefix2_symmetry_reduced_hits", prefix_hits[2])
print("prefix3_symmetry_reduced_hits", prefix_hits[3])
print("full_solution", full_solution)
print("THEOREM_CHECK: no low-degree Paley orientation-code quartet satisfies the d=9 split-617 GS equations")
print("ALL_EXACT_PALEY_CODE_EXCLUSION_CHECKS_PASSED")
