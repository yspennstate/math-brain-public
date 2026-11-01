from fractions import Fraction
import itertools
import sympy as sp


def main():
    out = []
    out.append("D0069 run17 exact symbolic self-check")
    out.append("")

    # Local cut obstruction enumeration for the degree-6 type [3,1,1,1].
    # At the only difficult S-S path position, a finite component receives
    # one triple class T (3 copies) and one singleton class S (1 copy) from w.
    # If the skeleton boundary has k classes, among the k-2 other boundary
    # classes let t be T and s be S. Then q=3t+s edge copies return to the
    # earlier prefix. For a finite set C, the T-perfect-matching cut count a
    # and the singleton-3-factor cut count b have the same parity as |C|.
    failures = []
    for k in range(4, 13):
        for t in range(k - 1):
            s = k - 2 - t
            if s < 0:
                continue
            a = 1 + t
            b = 1 + s
            q = 3 * t + s
            parity_ok = ((a - b) % 2 == 0)
            if parity_ok and q < 4:
                failures.append((k, t, s, a, b, q))
    assert failures == [(4, 0, 2, 1, 3, 2)]
    out.append("CUT_PROFILE_ENUMERATION_PASS")
    out.append(f"only_failure_profile={failures[0]}  # (k,t,s,a,b,q)")
    out.append("")

    # K4 transfer calculation at z=1/sqrt(5).
    z = 1 / sp.sqrt(5)
    V = range(4)

    def simple_paths(a, b):
        others = [v for v in V if v not in (a, b)]
        paths = [(a, b)]
        paths += [(a, c, b) for c in others]
        paths += [(a,) + perm + (b,) for perm in itertools.permutations(others)]
        assert len(paths) == 5
        return paths

    def internal_path_mass(path, internal_T):
        mass = sp.Integer(1)
        for u, v in zip(path, path[1:]):
            e = tuple(sorted((u, v)))
            m = 3 if e in internal_T else 1
            mass *= m * z
        return sp.simplify(mass)

    # Case A: all heavy T edges are external; internal K4 edges are singletons.
    # The outgoing external edge has multiplicity 3.
    extT_values = set()
    for a in V:
        for b in V:
            if a == b:
                continue
            mass = sum(internal_path_mass(p, set()) for p in simple_paths(a, b))
            mass = sp.simplify(3 * z * mass)
            extT_values.add(mass)
    assert extT_values == {sp.Rational(21, 25) + 6 * sp.sqrt(5) / 25}
    extT = next(iter(extT_values))
    assert sp.simplify(extT - 1) > 0
    out.append(f"K4_EXTERNAL_T_MASS={extT}")
    out.append("K4_EXTERNAL_T_GT_ONE_PASS")

    # Case B: all heavy T edges are internal, hence form a perfect matching;
    # external edges are singletons.
    internal_T = {(0, 1), (2, 3)}
    matched_values = set()
    unmatched_values = set()
    for a in V:
        for b in V:
            if a == b:
                continue
            mass = sum(internal_path_mass(p, internal_T) for p in simple_paths(a, b))
            mass = sp.simplify(z * mass)  # outgoing external singleton
            if tuple(sorted((a, b))) in internal_T:
                matched_values.add(mass)
            else:
                unmatched_values.add(mass)
    assert matched_values == {sp.Rational(21, 25) + 2 * sp.sqrt(5) / 25}
    assert unmatched_values == {sp.Rational(3, 5) + 6 * sp.sqrt(5) / 25}
    matched = next(iter(matched_values))
    unmatched = next(iter(unmatched_values))
    assert sp.simplify(matched - 1) > 0
    assert sp.simplify(unmatched - 1) > 0
    assert sp.simplify(matched <= unmatched) == True
    out.append(f"K4_INTERNAL_T_MATCHED_PORT_MASS={matched}")
    out.append(f"K4_INTERNAL_T_UNMATCHED_PORT_MASS={unmatched}")
    out.append("K4_INTERNAL_T_MIN_GT_ONE_PASS")
    out.append("")

    # Exact comparison for the minimum block mass:
    # 21/25 + 2*sqrt(5)/25 > 1 iff 2*sqrt(5)>4, whose square is 20>16.
    assert 20 > 16
    out.append("MIN_BLOCK_MASS_GT_ONE_EXACT_SQUARE_CHECK: 20>16 PASS")
    out.append("")
    out.append("ALL_EXACT_SELF_CHECKS_PASS")
    print("\n".join(out))


if __name__ == "__main__":
    main()
