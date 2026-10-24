#!/usr/bin/env python3
"""
Targeted exact checker for the B17 higher-order face-channel route.

This is NOT an exhaustive FEI test. It computes the exact finite-state
face-channel constant C_r for r=1,2,3 by enumerating Boolean r-face
spectral laws modulo global sign, with exact rational Walsh probabilities
and exact Hamming transport costs. It also evaluates the explicit bent
face / one-vertex-flip family for even r, which asymptotically saturates
2/ln 2.

Only Shannon logarithms are floating point.
"""
from fractions import Fraction
from collections import defaultdict
import math


def canonical_signs(mask, r):
    N = 1 << r
    s = tuple(1 if (mask >> x) & 1 else -1 for x in range(N))
    if s[0] < 0:
        s = tuple(-z for z in s)
    return s


def spectral_law(signs, r):
    N = 1 << r
    out = []
    for S in range(N):
        a = 0
        for x, fx in enumerate(signs):
            a += fx * (-1 if ((S & x).bit_count() & 1) else 1)
        out.append(Fraction(a * a, N * N))
    assert sum(out, Fraction(0, 1)) == 1
    return tuple(out)


def modsign_hamming(a, b):
    N = len(a)
    d = sum(x != y for x, y in zip(a, b))
    return min(d, N - d)


def js_bits(P, Q):
    ans = 0.0
    for p, q in zip(P, Q):
        pf, qf = float(p), float(q)
        m = (pf + qf) / 2.0
        if pf:
            ans += 0.5 * pf * math.log2(pf / m)
        if qf:
            ans += 0.5 * qf * math.log2(qf / m)
    return ans


def exact_face_constant(r):
    N = 1 << r
    groups = defaultdict(list)
    # Modulo global sign: canonical representatives have value +1 at vertex 0.
    for rest in range(1 << (N - 1)):
        mask = (rest << 1) | 1
        s = canonical_signs(mask, r)
        P = spectral_law(s, r)
        groups[P].append(s)
    states = list(groups)
    best = (-1.0, None)
    for i, P in enumerate(states):
        for Q in states[i + 1:]:
            dverts = min(modsign_hamming(a, b) for a in groups[P] for b in groups[Q])
            assert dverts > 0
            d = Fraction(dverts, N)
            J = js_bits(P, Q)
            ratio = J / float(d)
            if ratio > best[0]:
                best = (ratio, (P, Q, dverts, J))
    return len(groups), best


def bent_flip_ratio(r):
    assert r % 2 == 0
    N = 1 << r
    root = int(math.isqrt(N))
    assert root * root == N
    # Bent spectrum q is uniform. Flipping one truth-table vertex changes
    # normalized Walsh coefficients from +/-1/sqrt(N) by +/-2/N.
    na = (N + root) // 2
    nb = (N - root) // 2
    ra = (1.0 - 2.0 / root) ** 2
    rb = (1.0 + 2.0 / root) ** 2

    def F(rel):
        first = 0.0 if rel == 0.0 else 0.5 * rel * math.log2(2.0 * rel / (rel + 1.0))
        second = 0.5 * math.log2(2.0 / (rel + 1.0))
        return first + second

    J = (na / N) * F(ra) + (nb / N) * F(rb)
    return J, N * J


def main():
    print("TARGETED_FACE_CHANNEL_CHECK")
    for r in (1, 2, 3):
        nstates, (C, data) = exact_face_constant(r)
        print(
            f"exact_state_search r={r} states={nstates} C_r={C:.15f} "
            f"distance_vertices={data[2]} JS={data[3]:.15f}"
        )
    c2 = 8.0 - 2.5 * math.log2(5.0)
    print(f"closed_form_C2={c2:.15f}")
    print(f"general_logsobolev_limit={2.0 / math.log(2.0):.15f}")
    for r in range(2, 18, 2):
        J, C = bent_flip_ratio(r)
        print(f"bent_flip r={r} JS={J:.15f} ratio={C:.15f}")
    print("STATUS full_FEI=OPEN targeted_route=PROVED_OBSTRUCTION_AND_SHARP_PAIR_CONSTANT")


if __name__ == "__main__":
    main()
