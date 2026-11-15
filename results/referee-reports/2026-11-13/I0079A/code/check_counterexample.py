"""Independent finite checks; the report's nonconvergence proof is analytic.

Run with one process. No simulation and no nonstandard dependencies.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
import json
from pathlib import Path


def reduce_word(word):
    out = []
    for x in word:
        if out and ((x == 1) == (out[-1] == 1)):
            y = out.pop()
            if x != 1:
                z = ((x - 1) + (y - 1)) % 3
                if z:
                    out.append(z + 1)
        else:
            out.append(x)
    return tuple(out)


def ball(radius):
    found = {()}
    frontier = {()}
    for _ in range(radius):
        nxt = {reduce_word(w + (s,)) for w in frontier for s in (1, 2, 3)} - found
        found.update(nxt)
        frontier = nxt
    return found


def distances(w):
    return len(w), len(reduce_word((1,) + w))


def candidate_probability(vertices, q):
    """Integrate a candidate's priority against all closer/tied competitors."""
    total = Fraction(0)
    ds = [distances(w) for w in vertices]
    for i, (r, s) in enumerate(ds):
        closer = ties = 0
        for j, (u, v) in enumerate(ds):
            if i == j:
                continue
            if u < r or v < s:
                closer += 1
            elif u == r or v == s:
                ties += 1
        total += q**closer * (1 - q**(ties + 1)) / (ties + 1)
    return total


def crossing_probability(vertices, q):
    """Alternative calculation: the chosen nearest seed crosses the bridge."""
    ds = [distances(w) for w in vertices]
    total = Fraction(0)
    for endpoint in (0, 1):
        for radius in sorted({d[endpoint] for d in ds}):
            closer = sum(d[endpoint] < radius for d in ds)
            shell = [d for d in ds if d[endpoint] == radius]
            crosses = sum(d[1 - endpoint] == radius - 1 for d in shell)
            total += Fraction(crosses, len(shell)) * (q**closer - q**(closer + len(shell)))
    return total


def main():
    vertices = ball(14)
    spheres = Counter(map(len, vertices))
    half = Counter(len(w) for w in vertices if distances(w)[1] == len(w) + 1)
    for n in range(1, 15):
        expected = 2 * 2**(n // 2) if n % 2 == 0 else 3 * 2**(n // 2)
        assert spheres[n] == expected, (n, spheres[n], expected)
    for n in range(15):
        assert half[n] == 2**((n + 1) // 2)
        expected = (7 if n % 2 == 0 else 10) * 2**(n // 2) - 6
        assert sum(spheres[k] for k in range(n + 1)) == expected
    assert all(abs(u - v) == 1 for u, v in map(distances, vertices))
    assert reduce_word((2, 2, 2)) == ()  # The graph contains a triangle.
    assert reduce_word((1, 1)) == ()

    # Check the telescoping algebra of equation (3) at finite cutoff exactly.
    for q in (Fraction(1, 2), Fraction(2, 3)):
        cutoff = 3
        volumes = [(7 if n % 2 == 0 else 10) * 2**(n // 2) - 6
                   for n in range(2 * cutoff + 1)]
        raw = 2 * sum((Fraction(1, 3) if n % 2 == 0 else Fraction(1, 2))
                      * (q**volumes[n] - q**volumes[n + 1])
                      for n in range(2 * cutoff))
        transformed = (Fraction(2, 3) * (q - q**volumes[-1])
                       + q**(-6) / 3 * sum(q**(5 * 2**k) - q**(7 * 2**k)
                                           for k in range(1, cutoff + 1)))
        assert raw == transformed

    # Independently sum half-shell counts for the family in equation (6).
    for growth in range(2, 21):
        for n in range(11):
            shells = [1] + [growth**((j + 1) // 2) + growth**(j // 2)
                            for j in range(1, n + 1)]
            numerator = ((3 * growth + 1) if n % 2 == 0 else growth * (growth + 3))
            volume = Fraction(numerator * growth**(n // 2) - 2 * (growth + 1), growth - 1)
            assert sum(shells) == volume

    small = ball(4) | {reduce_word((1,) + w) for w in ball(4)}
    finite_results = []
    for q in (Fraction(1, 2), Fraction(2, 3), Fraction(9, 10)):
        by_candidate = candidate_probability(small, q)
        by_crossing = crossing_probability(small, q)
        assert by_candidate == by_crossing
        finite_results.append({"q": str(q), "same_seed_probability": str(by_candidate)})

    evidence = []
    with localcontext() as context:
        context.prec = 60
        for z in (Decimal("0.2"), Decimal("0.1")):
            log_z = z.ln()
            f = sum(((log_z * Decimal(2)**j).exp()
                     - (log_z * Decimal("1.4") * Decimal(2)**j).exp()
                     for j in range(-100, 16)), Decimal(0))
            # These estimates are a reproducibility check, not a proof.
            evidence.append({"phase_q0": str(z), "F_estimate": str(f),
                             "edge_limit_estimate": str((2 + f) / 3)})
    result = {"normal_forms_checked": len(vertices), "shells_checked": 14,
              "finite_universe_vertices": len(small), "exact_rational_checks": finite_results,
              "telescoping_identity_checks": 2, "family_volume_checks": 19 * 11,
              "phase_estimates_evidence_only": evidence,
              "priority_nice": os.getpriority(os.PRIO_PROCESS, 0),
              "proof": "REPORT.md: nonzero first Fourier coefficient; no numerics needed"}
    target = Path(__file__).resolve().parents[1] / "data" / "counterexample_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
