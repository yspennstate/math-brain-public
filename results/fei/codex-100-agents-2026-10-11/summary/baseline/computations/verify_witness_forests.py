#!/usr/bin/env python3
"""Exhaustive exact check of queue witnesses on three coordinates / three gates.

Enumerates every ordered triple of nonempty supports, every nonempty covered
set A, and every assignment of its coordinates to containing gates. For each
assignment it enumerates all source-SCC root choices, directed spanning forests,
attachments, and orders of children sharing an attachment.

Checks source-root support disjointness, existence of every rooted forest,
single visits, exact output, child counts, and the elementary coding bounds.
For the valid specialization theta=1 and pi_l=1/2, it also checks finite-run
probabilities with fractions at lambda=1/3, 1, 7/2, and sums distinct witness
events to at most one. These are finite consistency checks, not a proof for
arbitrary numbers of coordinates or gates. Uses only the standard library.
"""

from collections import Counter, deque
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from math import comb, prod
from pathlib import Path


N = 3
GATES = tuple(range(3))
LAMBDAS = (Fraction(1, 3), Fraction(1), Fraction(7, 2))


def bits(mask):
    return tuple(j for j in range(N) if mask & (1 << j))


def source_components(vertices, outgoing):
    # Reachability gives SCCs without depending on a graph-library traversal.
    reach = {v: {v} | set(outgoing[v]) for v in vertices}
    for _ in vertices:
        for v in vertices:
            reach[v] |= set().union(*(reach[w] for w in tuple(reach[v])))
    remaining = set(vertices)
    components = []
    while remaining:
        v = min(remaining)
        component = tuple(w for w in vertices if w in reach[v] and v in reach[w])
        components.append(component)
        remaining -= set(component)
    sources = []
    for component in components:
        members = set(component)
        if not any(w in members for v in vertices if v not in members
                   for w in outgoing[v]):
            sources.append(component)
    assert sources
    assert set().union(*(reach[r] for comp in sources for r in comp)) == set(vertices)
    return tuple(sources)


def valid_forest(vertices, roots, parents):
    for start in vertices:
        seen = set()
        v = start
        while v not in roots:
            if v in seen or v not in parents:
                return False
            seen.add(v)
            v = parents[v]
    return True


def child_orders(vertices, parents, attachments):
    choices = []
    for v in vertices:
        groups = {}
        for child, parent in parents.items():
            if parent == v:
                groups.setdefault(attachments[child], []).append(child)
        options = [()]
        for coordinate in sorted(groups):
            options = [
                previous + tuple((coordinate, child) for child in ordering)
                for previous in options
                for ordering in permutations(groups[coordinate])
            ]
        choices.append(options)
    for ordered in product(*choices):
        yield dict(zip(vertices, ordered))


def run_queue(supports, assigned, roots, children):
    queue = deque(sorted(roots))
    visited = set()
    output = 0
    trace = []
    probability_after_roots = Fraction(1)
    degrees = [sum(bool(s & (1 << j)) for s in supports) for j in range(N)]
    while queue:
        gate = queue.popleft()
        assert gate not in visited
        visited.add(gate)
        subset = assigned[gate]
        s, c = subset.bit_count(), len(children[gate])
        assert s > 0 and subset & supports[gate] == subset
        assert s * (s + 1) <= 3 ** s
        assert (c + 1) * (c + 2) <= 2 * 3 ** c
        assert comb(s + c - 1, c) <= 2 ** (s + c)
        # theta=1: the subset distribution is uniform among s-subsets.
        probability_after_roots /= s * (s + 1)
        probability_after_roots /= comb(supports[gate].bit_count(), s)
        probability_after_roots /= (c + 1) * (c + 2)
        probability_after_roots /= comb(s + c - 1, c)
        for coordinate, child in children[gate]:
            assert subset & (1 << coordinate)
            assert supports[child] & (1 << coordinate)
            probability_after_roots /= degrees[coordinate]
            queue.append(child)
        output |= subset
        trace.append((gate, subset, children[gate]))
    assert visited == set(assigned)
    assert len(roots) + sum(map(len, children.values())) == len(assigned)
    assert len(assigned) <= output.bit_count()
    return output, tuple(trace), probability_after_roots


def main():
    counts = Counter()
    active_histogram = Counter()
    root_histogram = Counter()
    maxima = {lam: (Fraction(0), None) for lam in LAMBDAS}

    for supports in product(range(1, 1 << N), repeat=len(GATES)):
        counts["support_triples"] += 1
        covered = supports[0] | supports[1] | supports[2]
        witness_keys = set()
        mass = {lam: Fraction(0) for lam in LAMBDAS}
        for a_mask in range(1, 1 << N):
            if a_mask & covered != a_mask:
                continue
            counts["covered_nonempty_sets"] += 1
            coordinates = bits(a_mask)
            eligible = [tuple(g for g in GATES if supports[g] & (1 << j))
                        for j in coordinates]
            for assignment in product(*eligible):
                counts["admissible_assignments"] += 1
                assigned = {}
                for coordinate, gate in zip(coordinates, assignment):
                    assigned[gate] = assigned.get(gate, 0) | (1 << coordinate)
                vertices = tuple(sorted(assigned))
                active_histogram[len(vertices)] += 1
                outgoing = {
                    v: tuple(w for w in vertices if v != w
                             and assigned[v] & supports[w])
                    for v in vertices
                }
                sources = source_components(vertices, outgoing)
                for root_tuple in product(*sources):
                    roots = frozenset(root_tuple)
                    counts["source_root_choices"] += 1
                    root_histogram[len(roots)] += 1
                    # This is the crucial support-disjointness assertion.
                    for left, right in combinations(roots, 2):
                        assert a_mask & supports[left] & supports[right] == 0
                    assert sum((a_mask & supports[r]).bit_count() for r in roots) <= len(coordinates)
                    nonroots = tuple(v for v in vertices if v not in roots)
                    parent_options = [
                        tuple(v for v in vertices if child in outgoing[v])
                        for child in nonroots
                    ]
                    forests_for_roots = 0
                    for parent_tuple in product(*parent_options):
                        parents = dict(zip(nonroots, parent_tuple))
                        if not valid_forest(vertices, roots, parents):
                            counts["cyclic_parent_choices_rejected"] += 1
                            continue
                        forests_for_roots += 1
                        counts["directed_spanning_forests"] += 1
                        attachment_options = [
                            bits(assigned[parents[child]] & supports[child])
                            for child in nonroots
                        ]
                        for attachment_tuple in product(*attachment_options):
                            attachments = dict(zip(nonroots, attachment_tuple))
                            counts["attached_forests"] += 1
                            for children in child_orders(vertices, parents, attachments):
                                output, trace, nonroot_probability = run_queue(
                                    supports, assigned, roots, children)
                                assert output == a_mask
                                key = (tuple(sorted(roots)), trace)
                                assert key not in witness_keys
                                witness_keys.add(key)
                                counts["ordered_finite_witnesses"] += 1

                                # Independent product over the prescribed forest,
                                # compared with the queue's sequential probabilities.
                                denominator = 1
                                for gate in vertices:
                                    s, c = assigned[gate].bit_count(), len(children[gate])
                                    denominator *= s * (s + 1) * comb(supports[gate].bit_count(), s)
                                    denominator *= (c + 1) * (c + 2) * comb(s + c - 1, c)
                                for coordinate in attachments.values():
                                    denominator *= sum(bool(r & (1 << coordinate)) for r in supports)
                                assert nonroot_probability == Fraction(1, denominator)
                                for lam in LAMBDAS:
                                    odds = lam / 2
                                    root_probability = prod(
                                        odds / (1 + odds) if gate in roots else 1 / (1 + odds)
                                        for gate in GATES)
                                    analytic_probability = odds ** len(roots) / (
                                        (1 + odds) ** len(GATES) * denominator)
                                    actual_probability = root_probability * nonroot_probability
                                    assert actual_probability == analytic_probability
                                    assert 0 < actual_probability <= 1
                                    mass[lam] += actual_probability
                                    counts["exact_probability_checks"] += 1
                    assert forests_for_roots > 0
        for lam in LAMBDAS:
            assert 0 <= mass[lam] <= 1
            counts["disjoint_witness_mass_checks"] += 1
            if mass[lam] > maxima[lam][0]:
                maxima[lam] = (mass[lam], supports)

    assert counts["support_triples"] == 7 ** 3
    report = {
        "status": "PASS",
        "domain": {
            "coordinates": N,
            "gates": len(GATES),
            "supports": "All ordered triples of nonempty subsets; repeated supports included.",
            "sets_and_assignments": "All nonempty covered sets and all admissible assignments.",
            "forests": "All source-SCC root representatives, spanning forests, attachments, and permitted child orders.",
        },
        "arithmetic": "Exact integers and fractions.Fraction; no floating-point comparisons.",
        "case_counts": dict(sorted(counts.items())),
        "assignments_by_active_gate_count": dict(sorted(active_histogram.items())),
        "root_choices_by_root_count": dict(sorted(root_histogram.items())),
        "probability_specialization": {
            "theta": "All subset weights equal 1.",
            "pi": "All gate rarity weights equal 1/2.",
            "lambda": [str(lam) for lam in LAMBDAS],
            "maximum_sum_of_distinct_witness_probabilities": {
                str(lam): {"mass": str(value), "support_masks": supports}
                for lam, (value, supports) in maxima.items()
            },
        },
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Finite consistency checks only; the general forest and variational inequalities require the manuscript proofs.",
    }
    rendered = json.dumps(report, indent=2)
    Path(__file__).with_suffix(".json").write_text(rendered + "\n")
    print(rendered)


if __name__ == "__main__":
    main()

