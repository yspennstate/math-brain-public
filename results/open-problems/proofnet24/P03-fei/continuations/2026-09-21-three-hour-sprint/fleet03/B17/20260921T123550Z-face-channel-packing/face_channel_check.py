#!/usr/bin/env python3
"""Targeted exact stress test for B17 face-channel information packing.

This is not a FEI proof.  It checks:
  * exact two-face identities on every 4-bit Boolean function and coordinate pair;
  * the proved face-channel log-Sobolev inequality numerically on that finite set;
  * the derived pair corollary;
  * an explicit Boolean counterexample to the false coefficient-2 strengthening.

Walsh coefficients and influence/joint probabilities are exact Fractions.  Logs are
used only for Shannon entropy values in the finite stress test.
"""

from fractions import Fraction
import json
import math

C_LS = 2.0 / math.log(2.0)
CURRENT_FEI_LOWER = 6.5218500836586124436336721990292995262


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def entropy(ps):
    out = 0.0
    for p in ps:
        if p:
            z = float(p)
            out -= z * math.log2(z)
    return out


def fracstr(x):
    return f"{x.numerator}/{x.denominator}"


def face_type_fractions(vals, n, i, j):
    """Return exact fractions t(D faces), w(parity-character faces)."""
    others = [k for k in range(n) if k not in (i, j)]
    dcount = 0
    pcount = 0
    for bits in range(1 << len(others)):
        base = 0
        for a, k in enumerate(others):
            if (bits >> a) & 1:
                base |= 1 << k
        face = []
        # Local index order is 00,01,10,11 up to a coordinate swap.
        for bi in (0, 1):
            for bj in (0, 1):
                face.append(vals[base | (bi << i) | (bj << j)])
        W = fwht(face)
        absW = sorted(abs(z) for z in W)
        if absW == [2, 2, 2, 2]:
            dcount += 1
        elif sum(z != 0 for z in W) == 1:
            nz = next(k for k, z in enumerate(W) if z)
            if nz == 3:
                pcount += 1
        else:
            raise AssertionError(("unexpected 2-face", face, W))
    den = 1 << len(others)
    return Fraction(dcount, den), Fraction(pcount, den)


def pair_stats(vals, n, i, j):
    N = 1 << n
    W = fwht(vals)
    probs = [Fraction(c * c, N * N) for c in W]
    pi = sum((probs[s] for s in range(N) if (s >> i) & 1), Fraction())
    pj = sum((probs[s] for s in range(N) if (s >> j) & 1), Fraction())
    q = sum(
        (probs[s] for s in range(N) if ((s >> i) & 1) and ((s >> j) & 1)),
        Fraction(),
    )
    joint = [1 - pi - pj + q, pi - q, pj - q, q]
    Hpair = entropy(joint)
    Ictrl = sum(
        (
            sum((probs[s] for s in range(N) if (s >> ell) & 1), Fraction())
            for ell in range(n)
            if ell not in (i, j)
        ),
        Fraction(),
    )
    return probs, pi, pj, q, joint, Hpair, Ictrl


def binary_entropy(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def main():
    n = 4
    N = 1 << n
    functions = 1 << N
    tested_pairs = 0
    q_identity_failures = 0
    max_channel_violation = (-1e300, None)
    max_pair_corollary_violation = (-1e300, None)
    max_false_c2_violation = (-1e300, None)

    for mask in range(functions):
        vals = [1 if (mask >> x) & 1 else -1 for x in range(N)]
        for i in range(n):
            for j in range(i + 1, n):
                tested_pairs += 1
                _, pi, pj, q, joint, Hpair, Ictrl = pair_stats(vals, n, i, j)
                t, w = face_type_fractions(vals, n, i, j)

                # Exact Boolean 2-face identity q = w + t/4.
                if q != w + t / 4:
                    q_identity_failures += 1

                # Exact identity H(S_pair)-E H(local face spectrum) = Hpair-2t.
                # The theorem says this is <= (2/ln 2) I_ctrl.
                channel_violation = Hpair - 2.0 * float(t) - C_LS * float(Ictrl)
                if channel_violation > max_channel_violation[0]:
                    max_channel_violation = (
                        channel_violation,
                        (mask, i, j, pi, pj, q, t, w, Hpair, Ictrl, joint),
                    )

                # Corollary using 2t <= 8q.
                corollary_violation = Hpair - C_LS * float(Ictrl) - 8.0 * float(q)
                if corollary_violation > max_pair_corollary_violation[0]:
                    max_pair_corollary_violation = (
                        corollary_violation,
                        (mask, i, j, pi, pj, q, t, w, Hpair, Ictrl, joint),
                    )

                # Deliberately false strengthening C_LS -> 2 in the corollary.
                false_c2_violation = Hpair - 2.0 * float(Ictrl) - 8.0 * float(q)
                if false_c2_violation > max_false_c2_violation[0]:
                    max_false_c2_violation = (
                        false_c2_violation,
                        (mask, i, j, pi, pj, q, t, w, Hpair, Ictrl, joint),
                    )

    def encode_record(rec):
        mask, i, j, pi, pj, q, t, w, Hpair, Ictrl, joint = rec
        return {
            "mask": mask,
            "pair_zero_indexed": [i, j],
            "p_i": fracstr(pi),
            "p_j": fracstr(pj),
            "q_ij": fracstr(q),
            "D_face_fraction_t": fracstr(t),
            "parity_face_fraction_w": fracstr(w),
            "H_pair_bits": Hpair,
            "I_control": fracstr(Ictrl),
            "joint_probabilities_00_10_01_11": [fracstr(x) for x in joint],
        }

    # Updated dangerous-scale independent-pair diagnostic from the peer family.
    p = 1.0 / 64.0
    pair_marginal_excess_at_current_lower = 2.0 * (
        binary_entropy(p) - CURRENT_FEI_LOWER * p
    )
    packed_independence_lower_bound = (math.log(2.0) / 2.0) * (
        2.0 * binary_entropy(p) - 8.0 * p * p
    )

    out = {
        "schema_version": 1,
        "status": "finite_stress_test_not_universal_proof",
        "full_FEI_proved": False,
        "theorem_constant_2_over_ln2": C_LS,
        "enumeration": {
            "n": n,
            "boolean_functions": functions,
            "coordinate_pairs_tested": tested_pairs,
            "q_equals_w_plus_t_over_4_exact_failures": q_identity_failures,
            "max_face_channel_violation": max_channel_violation[0],
            "max_face_channel_witness": encode_record(max_channel_violation[1]),
            "max_pair_corollary_violation": max_pair_corollary_violation[0],
            "max_pair_corollary_witness": encode_record(
                max_pair_corollary_violation[1]
            ),
        },
        "refuted_coefficient_2_strengthening": {
            "max_violation": max_false_c2_violation[0],
            "witness": encode_record(max_false_c2_violation[1]),
            "exact_H_formula": "3-(5/8)log2(5)",
            "exact_false_rhs": "3/2",
        },
        "rare_independent_pair_k6": {
            "p_i_equals_p_j": "1/64",
            "q_ij": "1/4096",
            "current_FEI_lower_bound_used": CURRENT_FEI_LOWER,
            "two_marginal_entropy_excess_at_that_scale": pair_marginal_excess_at_current_lower,
            "old_face_boundary_lower_bound": 7.0 / 128.0,
            "new_packed_channel_lower_bound": packed_independence_lower_bound,
            "explicit_peer_family_actual_I_control": 355.0 / 2048.0,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
