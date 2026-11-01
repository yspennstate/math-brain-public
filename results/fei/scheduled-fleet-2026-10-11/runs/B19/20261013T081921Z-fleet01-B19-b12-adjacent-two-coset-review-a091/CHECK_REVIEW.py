#!/usr/bin/env python3
"""Independent audit of B12's adjacent two-coset local theorem and hierarchy claim."""

from fractions import Fraction
from decimal import Decimal, getcontext
import json
import math

getcontext().prec = 90


def fwht(vals):
    a = [Fraction(v) for v in vals]
    h = 1
    while h < len(a):
        for start in range(0, len(a), 2 * h):
            for j in range(start, start + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / len(a) for x in a]


def phi_decimal(u):
    if not u:
        return Decimal(0)
    z = Decimal(u.numerator) / Decimal(u.denominator)
    return z * (Decimal(1) / z).ln()


def eraw_decimal(vals):
    return sum(phi_decimal(c * c) for c in fwht(vals))


def eraw(vals):
    ans = 0.0
    for c in fwht(vals):
        if c:
            u = float(c * c)
            ans += u * math.log(1.0 / u)
    return ans


def influence(vals):
    n = len(vals).bit_length() - 1
    ans = Fraction(0)
    for bit in range(n):
        ans += sum((Fraction(vals[x]) - Fraction(vals[x ^ (1 << bit)])) ** 2
                   for x in range(len(vals))) / (4 * len(vals))
    return ans


def span(gens):
    out = {0}
    for g in gens:
        out |= {x ^ g for x in list(out)}
    return frozenset(out)


def subspaces(n):
    spaces = {frozenset({0})}
    for x in range(1, 1 << n):
        for V in list(spaces):
            if x not in V:
                spaces.add(span(list(V) + [x]))
    return spaces


def affine_cosets(n):
    result = []
    for V in subspaces(n):
        unseen = set(range(1 << n))
        while unseen:
            a = min(unseen)
            A = frozenset(a ^ v for v in V)
            unseen -= A
            result.append((A, V, a))
    return result


def local_objects(n, A, B):
    N = 1 << n
    s = [int(z in A or z in B) for z in range(N)]
    one_a = [int(z in A) for z in range(N)]
    one_b = [int(z in B) for z in range(N)]
    d, a0, F = [], [], []
    for selector in (0, 1):
        x = 1 if selector == 0 else -1
        for z in range(N):
            dv = selector * s[z]
            d.append(dv)
            a0.append(x + dv)
            F.append(x + 2 * dv)
    omega = eraw(F) - eraw(a0) - eraw(d)
    return s, one_a, one_b, d, omega


def extend_with_free_bits(vals, extra):
    return vals * (1 << extra)


def restrict(vals, bit, value):
    n = len(vals).bit_length() - 1
    out = []
    for y in range(1 << (n - 1)):
        low = y & ((1 << bit) - 1)
        high = y >> bit
        x = low | (value << bit) | (high << (bit + 1))
        out.append(vals[x])
    return out


def main():
    total = local_pass = refund_pass = 0
    largest_ratio = -1.0
    for n in range(1, 5):
        cosets = affine_cosets(n)
        for i, (A, VA, aa) in enumerate(cosets):
            for B, VB, bb in cosets[i + 1:]:
                if not A.isdisjoint(B):
                    continue
                total += 1
                s, one_a, one_b, d, omega = local_objects(n, A, B)
                infd = influence(d)
                if omega > 8 * math.log(2) * float(infd) + 1e-11:
                    raise AssertionError((n, A, B, "local theorem"))
                local_pass += 1
                if eraw(s) > eraw(one_a) + eraw(one_b) + 1e-11:
                    raise AssertionError((n, A, B, "Hadamard refund"))
                refund_pass += 1
                if infd:
                    largest_ratio = max(largest_ratio, omega / float(infd))

    scalar = 0
    for alpha in range(80):
        for beta in range(alpha, 80):
            for q in range(1, 161):
                lhs = 2 * q
                rhs = (2 ** beta) * (1 + max(0, q - 1 - alpha))
                rhs += (2 ** alpha) * (1 + max(0, q - 1 - beta))
                if lhs > rhs:
                    raise AssertionError((alpha, beta, q, "rank scalar"))
                scalar += 1

    # Literal hierarchy counterexample.  The author's own maximising finite
    # pair is A={0}, B={1,2} in F_2^4.  Add two completely free coordinates.
    # Revealing the free coordinates level by level is pathwise nonreusing;
    # every reached restriction has exactly the same positive local charge.
    A = frozenset({0})
    B = frozenset({1, 2})
    s0, a_ind0, b_ind0, d0, _ = local_objects(4, A, B)
    # Re-evaluate the displayed certificate at 90 decimal digits.
    N = 16
    a0, F0 = [], []
    for selector in (0, 1):
        x = 1 if selector == 0 else -1
        for z in range(N):
            dv = selector * s0[z]
            a0.append(x + dv)
            F0.append(x + 2 * dv)
    omega0 = eraw_decimal(F0) - eraw_decimal(a0) - eraw_decimal(d0)
    inf0 = influence(d0)
    d_ext = extend_with_free_bits(d0, 2)
    if influence(d_ext) != inf0:
        raise AssertionError("free coordinates changed influence")
    # The appended free variables are bits 5 and 6 (d0 has 5 variables).
    for value in (0, 1):
        child = restrict(d_ext, 6, value)
        if child != extend_with_free_bits(d0, 1):
            raise AssertionError("first free restriction changed source")
        for value2 in (0, 1):
            if restrict(child, 5, value2) != d0:
                raise AssertionError("second free restriction changed source")
    weighted_two_level_charge = 2 * omega0
    claimed_budget = 8 * Decimal(2).ln() * (Decimal(inf0.numerator) / Decimal(inf0.denominator))
    if not weighted_two_level_charge > claimed_budget:
        raise AssertionError("expected hierarchy falsifier did not violate")

    result = {
        "status": "PASS",
        "local_disjoint_affine_pairs_checked": total,
        "local_8ln2_checks": local_pass,
        "Hadamard_refund_checks": refund_pass,
        "rank_scalar_tuples_checked": scalar,
        "largest_local_ratio_nats_per_influence": format(largest_ratio, ".15f"),
        "hierarchy_falsifier": {
            "ambient_active_dimension": 4,
            "A": [0],
            "B": [1, 2],
            "free_restriction_coordinates": 2,
            "one_node_Omega": str(+omega0),
            "source_influence": str(inf0),
            "two_level_weighted_charge": str(+weighted_two_level_charge),
            "claimed_8ln2_source_budget": str(+claimed_budget),
            "strict_violation_margin": str(+(weighted_two_level_charge - claimed_budget)),
            "interpretation": "Pathwise coordinate nonreuse alone does not make full reached-source influence single-use."
        },
        "scope": "Finite independent reproduction plus an exact cylinder-extension falsifier; the all-parameter local theorem is established analytically in PROOF_RECONSTRUCTION.md."
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
