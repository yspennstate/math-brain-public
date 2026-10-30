#!/usr/bin/env python3
"""Exact endpoint diagnostic for B18 robust sink-component peeling.

Enumerates Boolean truth tables modulo global output sign through n=4.
For each coordinate, it detects centered exact-subcube derivative supports
(density at most 1/2), forms reciprocal trigger components, selects one
representative from each sink component of the contracted trigger DAG, and
checks:
  (1) representatives do not lie in the union of selected trigger blocks;
  (2) every nonrepresentative member of a sink component lies in its
      representative's trigger block;
  (3) after exposing the union block, every representative has conditional
      raw influence 0 or 1 on every branch, hence folded influence 0.

The universal theorem in REPORT.md is analytic; this is diagnostic evidence.
"""

from collections import defaultdict


def derivative_support(bits, n, i):
    coords = [k for k in range(n) if k != i]
    support = set()
    for y in range(1 << (n - 1)):
        x0 = 0
        for pos, k in enumerate(coords):
            x0 |= ((y >> pos) & 1) << k
        x1 = x0 | (1 << i)
        if bits[x0] != bits[x1]:
            support.add(y)
    return coords, support


def exact_centered_subcube(coords, support):
    """Return defining-coordinate set, or None.

    We retain only nonempty subcubes of density <= 1/2, the centered
    nontrivial regime used in the analytic argument.
    """
    m = len(coords)
    total = 1 << m
    if not support or len(support) > total // 2:
        return None
    s = len(support)
    if s & (s - 1):
        return None

    fixed = {}
    for pos, k in enumerate(coords):
        vals = {(y >> pos) & 1 for y in support}
        if len(vals) == 1:
            fixed[k] = next(iter(vals))

    if (1 << (m - len(fixed))) != s:
        return None

    reconstructed = set()
    for y in range(total):
        if all(((y >> pos) & 1) == fixed[k]
               for pos, k in enumerate(coords) if k in fixed):
            reconstructed.add(y)
    if reconstructed != support:
        return None
    return frozenset(fixed)


def check_dimension(n):
    stats = defaultdict(int)
    violations = []

    # Normalize global output sign by fixing f(0)=0.
    for mask in range(1 << ((1 << n) - 1)):
        bits = [0] * (1 << n)
        for x in range(1, 1 << n):
            bits[x] = (mask >> (x - 1)) & 1

        rows = {}
        for i in range(n):
            coords, support = derivative_support(bits, n, i)
            trigger = exact_centered_subcube(coords, support)
            if trigger is not None:
                rows[i] = trigger

        stats["functions"] += 1
        if rows:
            stats["functions_with_exact_rows"] += 1
            stats["exact_rows"] += len(rows)

        # Reciprocal trigger graph.
        adjacency = {i: set() for i in rows}
        for i in rows:
            for k in rows:
                if i < k and k in rows[i] and i in rows[k]:
                    adjacency[i].add(k)
                    adjacency[k].add(i)

        seen = set()
        components = []
        for i in rows:
            if i in seen:
                continue
            stack = [i]
            seen.add(i)
            comp = set()
            while stack:
                u = stack.pop()
                comp.add(u)
                for v in adjacency[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
            components.append(comp)

        stats["reciprocal_components"] += len(components)

        # Trigger locking: one signature T_C={i} union F_i per component.
        for comp in components:
            signatures = {frozenset({i} | set(rows[i])) for i in comp}
            if len(signatures) != 1:
                violations.append(("trigger_locking", mask, sorted(comp)))
                return stats, violations

        comp_of = {i: c for c, comp in enumerate(components) for i in comp}
        outgoing = {c: set() for c in range(len(components))}
        for i, trigger in rows.items():
            ci = comp_of[i]
            for k in trigger:
                if k in rows:
                    ck = comp_of[k]
                    if ck != ci:
                        outgoing[ci].add(ck)

        sinks = [c for c in outgoing if not outgoing[c]]
        reps = {c: min(components[c]) for c in sinks}
        rep_set = set(reps.values())
        reveal = set()
        for c, r in reps.items():
            reveal.update(rows[r])

        stats["sink_representatives"] += len(rep_set)

        # Canonical survivor property.
        if rep_set & reveal:
            violations.append(("representative_collision", mask,
                               sorted(rep_set), sorted(reveal)))
            return stats, violations

        for c, r in reps.items():
            # Whole reciprocal component except its representative is exposed.
            for k in components[c]:
                if k != r and k not in rows[r]:
                    violations.append(("component_not_exposed", mask, c, r, k))
                    return stats, violations

            # Endpoint free peeling: after revealing A, r has raw influence
            # 0 or 1 on every A-branch, hence folded influence exactly 0.
            reveal_list = sorted(reveal)
            remaining = [k for k in range(n)
                         if k not in reveal and k != r]
            for a in range(1 << len(reveal_list)):
                sensitive = 0
                denom = 1 << len(remaining)
                for u in range(denom):
                    x0 = 0
                    for pos, k in enumerate(reveal_list):
                        x0 |= ((a >> pos) & 1) << k
                    for pos, k in enumerate(remaining):
                        x0 |= ((u >> pos) & 1) << k
                    x1 = x0 | (1 << r)
                    sensitive += (bits[x0] != bits[x1])
                if sensitive not in (0, denom):
                    violations.append(("nonzero_folded_residual", mask, c, r,
                                       sorted(reveal), a, sensitive, denom))
                    return stats, violations

    return stats, violations


def main():
    total_violations = 0
    for n in range(1, 5):
        stats, violations = check_dimension(n)
        total_violations += len(violations)
        print(
            f"n={n} "
            f"functions={stats['functions']} "
            f"functions_with_exact_rows={stats['functions_with_exact_rows']} "
            f"exact_rows={stats['exact_rows']} "
            f"reciprocal_components={stats['reciprocal_components']} "
            f"sink_representatives={stats['sink_representatives']} "
            f"violations={len(violations)}"
        )
        if violations:
            print("first_violation=", violations[0])
            raise SystemExit(1)
    print(f"TOTAL_VIOLATIONS={total_violations}")
    print("STATUS=PASS_DIAGNOSTIC_ONLY")


if __name__ == "__main__":
    main()
