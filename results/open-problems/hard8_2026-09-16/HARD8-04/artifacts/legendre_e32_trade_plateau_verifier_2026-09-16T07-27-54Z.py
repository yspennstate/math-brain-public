"""Exact verifier for HARD8-04 checkpoint 2026-09-16T07:27:54Z.

Pure Python; no external packages and no floating point.

It verifies:
  * the support-set formula for normalized binary Legendre candidates;
  * exact E=32 classification as one surplus and one deficit difference class;
  * exhaustive balanced-exchange repair data through odd length 19;
  * exact quotient consistency used to make the v=15,17,19 enumeration small;
  * the explicit v=19 energy path 32 -> 32 -> 32 -> 0.

A "round" lets each support independently stay fixed or exchange one occupied
position for one unoccupied position.  All arithmetic is integer arithmetic.
"""

from collections import defaultdict, Counter, deque
from itertools import combinations


def balanced_masks(v):
    k = (v + 1) // 2
    ans = []
    for comb in combinations(range(v), k):
        m = 0
        for i in comb:
            m |= 1 << i
        ans.append(m)
    return ans


def rotl(m, t, v):
    full = (1 << v) - 1
    if t == 0:
        return m
    return ((m << t) & full) | (m >> (v - t))


def half_difference_vector(m, v):
    """nu_A(t)=|A intersect (A-t)| for 1 <= t <= (v-1)/2."""
    return tuple((m & rotl(m, t, v)).bit_count()
                 for t in range(1, (v + 1) // 2))


def sequence_from_mask(m, v):
    return [1 if (m >> i) & 1 else -1 for i in range(v)]


def paf(a, t):
    v = len(a)
    return sum(a[i] * a[(i + t) % v] for i in range(v))


def half_defect_from_masks(ma, mb, v):
    a = sequence_from_mask(ma, v)
    b = sequence_from_mask(mb, v)
    return tuple(paf(a, t) + paf(b, t) + 2
                 for t in range(1, (v + 1) // 2))


def energy_from_vectors(x, y, v):
    k = (v + 1) // 2
    # d_t = 4*(nu_A(t)+nu_B(t)-k)
    return 16 * sum((a + b - k) ** 2 for a, b in zip(x, y))


def one_exchange_masks(m, v, include_self=True):
    ones = [i for i in range(v) if (m >> i) & 1]
    zeros = [i for i in range(v) if not ((m >> i) & 1)]
    if include_self:
        yield m
    for p in ones:
        for q in zeros:
            yield m ^ (1 << p) ^ (1 << q)


def support_tuple(m, v):
    return tuple(i for i in range(v) if (m >> i) & 1)


def verify_support_formula(v, ma, mb):
    k = (v + 1) // 2
    x = half_difference_vector(ma, v)
    y = half_difference_vector(mb, v)
    d1 = half_defect_from_masks(ma, mb, v)
    d2 = tuple(4 * (a + b - k) for a, b in zip(x, y))
    assert d1 == d2, (v, support_tuple(ma, v), support_tuple(mb, v), d1, d2)
    return d1


def build_quotient(v):
    """Build the exact finite quotient by one-round reachable N-vectors.

    The code *checks*, rather than assumes, that at the requested length:
      (1) a reach signature determines the current N-vector; and
      (2) masks with the same signature have the same neighboring signature set.
    These checked facts make type-level plateau paths valid for every concrete mask
    represented by a type.
    """
    masks = balanced_masks(v)
    vectors = [half_difference_vector(m, v) for m in masks]
    vector_values = sorted(set(vectors))
    vector_id = {x: i for i, x in enumerate(vector_values)}
    mask_index = {m: i for i, m in enumerate(masks)}

    reach_bits = []
    for m, x in zip(masks, vectors):
        bits = 1 << vector_id[x]
        for nm in one_exchange_masks(m, v, include_self=False):
            nx = vectors[mask_index[nm]]
            bits |= 1 << vector_id[nx]
        reach_bits.append(bits)

    signatures = sorted(set(reach_bits))
    signature_id = {b: i for i, b in enumerate(signatures)}
    types = [signature_id[b] for b in reach_bits]

    type_members = defaultdict(list)
    for i, t in enumerate(types):
        type_members[t].append(i)

    # Fact (1): signature -> unique current N-vector.
    type_vector = {}
    for t, inds in type_members.items():
        vals = {vectors[i] for i in inds}
        assert len(vals) == 1, (v, t, len(vals))
        type_vector[t] = next(iter(vals))

    # Fact (2): signature -> unique set of neighboring signatures.
    type_neighbors = {}
    for t, inds in type_members.items():
        baseline = None
        for i in inds:
            m = masks[i]
            ntypes = {types[mask_index[nm]]
                      for nm in one_exchange_masks(m, v, include_self=True)}
            if baseline is None:
                baseline = ntypes
            else:
                assert ntypes == baseline, (v, t, inds[0], i)
        type_neighbors[t] = baseline

    type_reach_bits = {t: signatures[t] for t in type_members}

    return {
        "v": v,
        "masks": masks,
        "vectors": vectors,
        "vector_values": vector_values,
        "vector_id": vector_id,
        "mask_index": mask_index,
        "reach_bits": reach_bits,
        "types": types,
        "type_members": type_members,
        "type_vector": type_vector,
        "type_neighbors": type_neighbors,
        "type_reach_bits": type_reach_bits,
    }


def enumerate_e32_type_states(Q):
    v = Q["v"]
    k = (v + 1) // 2
    h = (v - 1) // 2
    type_vector = Q["type_vector"]
    vector_to_types = defaultdict(list)
    for t, x in type_vector.items():
        vector_to_types[x].append(t)

    states = set()
    for ta, x in type_vector.items():
        base = [k - z for z in x]
        for p in range(h):
            for q in range(h):
                if p == q:
                    continue
                y = base.copy()
                y[p] += 1
                y[q] -= 1
                y = tuple(y)
                for tb in vector_to_types.get(y, ()):  # empty if impossible
                    assert energy_from_vectors(x, type_vector[tb], v) == 32
                    states.add((ta, tb))
    return states


def complement_reach_bits(Q):
    v = Q["v"]
    k = (v + 1) // 2
    values = Q["vector_values"]
    vid = Q["vector_id"]
    comp = {}
    for i, x in enumerate(values):
        y = tuple(k - z for z in x)
        if y in vid:
            comp[i] = vid[y]

    out = {}
    for t, bits in Q["type_reach_bits"].items():
        cbits = 0
        b = bits
        while b:
            low = b & -b
            i = low.bit_length() - 1
            b -= low
            if i in comp:
                cbits |= 1 << comp[i]
        out[t] = cbits
    return out


def classify_plateau(v):
    Q = build_quotient(v)
    states = enumerate_e32_type_states(Q)
    comp_bits = complement_reach_bits(Q)

    direct = {
        st for st in states
        if Q["type_reach_bits"][st[0]] & comp_bits[st[1]]
    }
    hard = states - direct

    # One E=32 plateau step into a direct state.
    one_step = set()
    for a, b in hard:
        found = False
        for aa in Q["type_neighbors"][a]:
            for bb in Q["type_neighbors"][b]:
                if (aa, bb) in direct:
                    one_step.add((a, b))
                    found = True
                    break
            if found:
                break

    remaining = hard - one_step

    # For any remainder, permit one plateau step into a state that itself is in
    # one_step (so total plateau distance is two before the final repair).
    two_step = set()
    for a, b in remaining:
        found = False
        for aa in Q["type_neighbors"][a]:
            for bb in Q["type_neighbors"][b]:
                if (aa, bb) in one_step:
                    two_step.add((a, b))
                    found = True
                    break
            if found:
                break

    unresolved = remaining - two_step

    # Weighted counts recover concrete ordered support-pair counts exactly.
    def weight(st):
        return (len(Q["type_members"][st[0]]) *
                len(Q["type_members"][st[1]]))

    weighted = {
        0: sum(weight(st) for st in direct),
        1: sum(weight(st) for st in one_step),
        2: sum(weight(st) for st in two_step),
    }
    type_counts = {0: len(direct), 1: len(one_step), 2: len(two_step)}

    return Q, states, direct, one_step, two_step, unresolved, type_counts, weighted


def assert_expected_counts():
    expected = {
        5:  (50,       {0: 50}),
        7:  (882,      {0: 882}),
        9:  (6804,     {0: 6804}),
        11: (49610,    {0: 49610}),
        13: (223080,   {0: 223080}),
        15: (981000,   {0: 934200, 1: 46800}),
        17: (3745440,  {0: 2728160, 1: 1017280}),
        19: (13099968, {0: 4535604, 1: 8551368, 2: 12996}),
    }

    summaries = {}
    for v in (5, 7, 9, 11, 13, 15, 17, 19):
        Q, states, direct, one, two, unresolved, tc, wc = classify_plateau(v)
        assert not unresolved, (v, len(unresolved))
        total = sum(wc.values())
        want_total, want_by_distance = expected[v]
        assert total == want_total, (v, total, want_total)
        got = {d: c for d, c in wc.items() if c}
        assert got == want_by_distance, (v, got, want_by_distance)

        # Every type state really has E=32 by exact vector arithmetic.
        for a, b in states:
            assert energy_from_vectors(Q["type_vector"][a],
                                       Q["type_vector"][b], v) == 32

        summaries[v] = (len(Q["masks"]), len(Q["type_members"]),
                        len(states), tc, got)
        print("v=%d masks=%d types=%d E32_types=%d type_dist=%s weighted_dist=%s" %
              (v, len(Q["masks"]), len(Q["type_members"]),
               len(states), tc, got))

    return summaries


def mask_from_support(S):
    m = 0
    for i in S:
        m |= 1 << i
    return m


def verify_explicit_v19_path():
    v = 19
    supports = [
        ((0,1,2,3,4,5,8,10,14,16),
         (0,1,2,3,5,9,10,12,15,16)),
        ((0,2,3,4,5,7,8,10,14,16),
         (0,1,3,5,9,10,11,12,15,16)),
        ((0,2,3,4,5,7,10,14,16,18),
         (1,2,3,5,9,10,11,12,15,16)),
        ((0,1,2,4,5,7,10,14,16,18),
         (1,2,3,4,5,9,11,12,15,16)),
    ]
    expected_defects = [
        (0,0,0,0,0,4,0,-4,0),
        (-4,0,0,0,4,0,0,0,0),
        (0,0,-4,0,4,0,0,0,0),
        (0,0,0,0,0,0,0,0,0),
    ]
    expected_energy = [32, 32, 32, 0]

    masks = [(mask_from_support(A), mask_from_support(B)) for A, B in supports]
    for i, ((ma, mb), want_d, want_e) in enumerate(zip(masks, expected_defects, expected_energy)):
        d = verify_support_formula(v, ma, mb)
        e = sum(z*z for z in d)
        assert d == want_d, (i, d, want_d)
        assert e == want_e, (i, e, want_e)

    # Each transition is at most one balanced exchange in each support.
    for (a0, b0), (a1, b1) in zip(masks, masks[1:]):
        assert (a0 ^ a1).bit_count() in (0, 2)
        assert (b0 ^ b1).bit_count() in (0, 2)
        assert a0.bit_count() == a1.bit_count() == 10
        assert b0.bit_count() == b1.bit_count() == 10

    print("explicit v=19 path energies:", expected_energy)


def main():
    summaries = assert_expected_counts()
    verify_explicit_v19_path()
    print("ALL EXACT CHECKS PASSED")
    return summaries


if __name__ == "__main__":
    main()
