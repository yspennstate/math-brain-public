"""Exact finite checks of the tagged-flow identity. Standard library only.

Run: OMP_NUM_THREADS=1 nice -n 15 python3 -B check_conditional.py
Each averaged-flow matrix has denominator 2**t, so all checks use integers.
No random sampling or Lean execution is involved.
"""

import json
import os
from collections import defaultdict, deque
from fractions import Fraction
from itertools import product
from pathlib import Path
import re
import resource
import time

ROOT = Path(__file__).resolve().parent
PREVIOUS = ROOT.parent.parent.parent / "codex_op_1114r5" / "briefs" / "AV_T176"
# Keep even accidental expansions below the author's per-run limits.
resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
# Darwin rejects the requested RLIMIT_AS here. Inputs are bounded below;
# also stop at 256 MiB observed RSS, well below the 1 GB task ceiling.
assert os.environ.get("OMP_NUM_THREADS") == "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15


def earlier_recheck():
    """Use a queue and Kahn elimination, unlike the previous recursive DFS."""
    folder = PREVIOUS / "sources" / "lean"
    bodies = {p.stem: p.read_text() for p in folder.glob("*.lean")}
    dependencies = {}
    external = set()
    for name, text in bodies.items():
        dependencies[name] = set()
        for dep in re.findall(r"^import\s+(\S+)", text, re.MULTILINE):
            if dep.startswith("OAI.Probability.ThorpShuffle."):
                dependencies[name].add(dep.rsplit(".", 1)[1])
            else:
                external.add(dep)
    queue = deque(["Main"])
    closure = set()
    while queue:
        name = queue.popleft()
        if name in closure:
            continue
        assert name in bodies
        closure.add(name)
        queue.extend(dependencies[name])
    remaining = {name: dependencies[name] & closure for name in closure}
    while remaining:
        leaves = {name for name, deps in remaining.items() if not deps}
        assert leaves, "cycle"
        remaining = {name: deps - leaves for name, deps in remaining.items()
                     if name not in leaves}
    assert len(closure) == 51 and len(bodies) == 55
    assert external == {"Mathlib"}
    assert "FirstMain" not in closure
    assert Fraction(5, 8) * (1 + Fraction(4, 5)**4) == Fraction(881, 1000)
    assert Fraction(5, 4)**2 * Fraction(4, 5)**4 == Fraction(16, 25)
    assert Fraction(881, 1000) <= Fraction(9, 10)
    assert Fraction(16, 25) <= Fraction(9, 10)**2
    assert 7**2 * 8 // 4 == 98 and 98 * 32 == 3136
    assert 8 * 4 * 3 == 96 and 8 * 200 == 1600
    assert 2 - 16 * Fraction(1, 4) == -2
    # Freshly reopened bodies have exactly the same text as round 5.
    for name in ("ConditionalLaw", "MaskedResampling"):
        assert (ROOT / "sources" / (name + ".lean")).read_text().strip() == bodies[name].strip()
    return {"main_modules": len(closure), "saved_modules": len(bodies),
            "acyclic": True, "outside_imports": sorted(external),
            "fresh_identity_sources_match": True,
            "rational_constants": ["881/1000", "16/25", 98, 3136, 96, 1600]}


def physical_from_bits(n, c):
    h = n // 2
    return tuple(2 * (x % h) + ((x // h) ^ ((c >> (x % h)) & 1))
                 for x in range(n))


def physical_from_deck(n, c):
    """Direct cut-and-drop operation, then invert output deck to positions."""
    deck = []
    for j in range(n // 2):
        pair = [j, j + n // 2]
        if (c >> j) & 1:
            pair.reverse()
        deck.extend(pair)
    inverse = [0] * n
    for position, label in enumerate(deck):
        inverse[label] = position
    return tuple(inverse)


def iterate(n, initial_B, coins, permutations):
    """Flow in physical positions; return its scaled matrix and exact run."""
    B = initial_B
    mat = [[int(y == x) for x in range(n)] for y in range(n)]
    run = tuple(range(n))
    for c in coins:
        p = permutations[c]
        nxt = [None] * n
        for j in range(n // 2):
            k = j + n // 2
            if (B >> j) & (B >> k) & 1:
                row = [a + b for a, b in zip(mat[j], mat[k])]
                nxt[2*j] = row
                nxt[2*j+1] = row.copy()
            else:
                nxt[p[j]] = [2*a for a in mat[j]]
                nxt[p[k]] = [2*a for a in mat[k]]
        B = sum(1 << p[x] for x in range(n) if (B >> x) & 1)
        mat = nxt
        run = tuple(p[x] for x in run)
    return mat, run, B


def endpoint_check(n, t, masks):
    """All initial basis weights and all endpoint-indicator tests at once.

    Use the full ordered complement of B as e. Equality for a sublist,
    repeated exposed labels, or a reordering follows by mapping these keys.
    """
    permutations = [physical_from_deck(n, c) for c in range(1 << (n//2))]
    assert all(p == physical_from_bits(n, c) for c, p in enumerate(permutations))
    histories_per_mask = len(permutations)**t
    cells = 0
    for initial_B in masks:
        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 256 * 1024**2
        exposed = tuple(x for x in range(n) if not ((initial_B >> x) & 1))
        actual = defaultdict(lambda: [0]*n)
        averaged = defaultdict(lambda: [0]*n)
        for coins in product(range(len(permutations)), repeat=t):
            mat, run, B = iterate(n, initial_B, coins, permutations)
            endpoint = tuple(run[x] for x in exposed)
            assert B == sum(1 << run[x] for x in range(n) if (initial_B >> x) & 1)
            for x in range(n):
                actual[(endpoint, run[x])][x] += 1
            for y in range(n):
                acc = averaged[(endpoint, y)]
                for x in range(n):
                    acc[x] += mat[y][x]
        for key in actual.keys() | averaged.keys():
            lhs, rhs = actual[key], averaged[key]
            assert [a * (1 << t) for a in lhs] == rhs, (n, t, initial_B, key)
            cells += n
    return {"n": n, "t": t, "masks": len(masks),
            "histories_per_mask": histories_per_mask,
            "history_mask_cases": len(masks)*histories_per_mask,
            "basis_indicator_equalities": cells, "max_error": 0}


def cylinder_check(n, t, B, tag):
    """A second method: group direct histories by the entire exposed paths.

    On each group compare empirical conditional tag masses with delta_tag
    passed through the flow, without centering. Then check centered masses.
    """
    exposed = tuple(x for x in range(n) if not ((B >> x) & 1))
    permutations = [physical_from_deck(n, c) for c in range(1 << (n//2))]
    grouped = {}
    m = B.bit_count()
    assert (B >> tag) & 1
    scale = 1 << t
    for coins in product(range(len(permutations)), repeat=t):
        run = tuple(range(n))
        path = []
        for c in coins:
            run = tuple(permutations[c][x] for x in run)
            path.append(tuple(run[x] for x in exposed))
        mat, independently_run, end_B = iterate(n, B, coins, permutations)
        assert run == independently_run
        p_scaled = tuple(mat[y][tag] for y in range(n))
        key = tuple(path)
        if key not in grouped:
            grouped[key] = [0, [0]*n, p_scaled, end_B]
        entry = grouped[key]
        assert p_scaled == entry[2] and end_B == entry[3]
        entry[0] += 1
        entry[1][run[tag]] += 1
        # Uniform initial free mass is transported exactly, history by history.
        for y in range(n):
            assert sum(mat[y][x] for x in range(n) if (B >> x) & 1) == (
                scale if (end_B >> y) & 1 else 0)
    for count, empirical, p_scaled, end_B in grouped.values():
        for y in range(n):
            assert empirical[y] * scale == count * p_scaled[y]
            # Multiply centered conditional equality by m*scale*count.
            lhs = m * empirical[y] * scale - count * scale * ((end_B >> y) & 1)
            rhs = count * (m * p_scaled[y] - scale * ((end_B >> y) & 1))
            assert lhs == rhs
    return {"n": n, "t": t, "B": B, "tag": tag,
            "path_cylinders": len(grouped), "max_error": 0}


def invalid_variants():
    # If an exposed point is itself free, the joint identity can fail.
    direct = Fraction(1)
    falsely_averaged = Fraction(1, 2)
    got_direct = got_flow = Fraction(0)
    for c in range(2):
        mat, run, _ = iterate(2, 3, (c,), [physical_from_deck(2, z) for z in range(2)])
        got_direct += Fraction(int(run[0] == run[0]), 2)
        got_flow += Fraction(mat[run[0]][0], 4)
    assert got_direct == direct and got_flow == falsely_averaged
    # If the resampling mask equals its current coin, the masked coin is biased.
    ones = sum((r if c else c) for c in (0, 1) for r in (0, 1))
    assert Fraction(ones, 4) == Fraction(1, 4)
    return {"free_exposed_point": {"direct": str(got_direct), "flow": str(got_flow)},
            "coin_dependent_mask_P_one": "1/4"}


def main():
    start = time.monotonic()
    out = {"priority": os.getpriority(os.PRIO_PROCESS, 0),
           "earlier_result": earlier_recheck()}
    checks = []
    for n, max_t in [(2, 4), (4, 4)]:
        for t in range(max_t + 1):
            checks.append(endpoint_check(n, t, list(range(1 << n))))
    # All free sets on 8 cards for two steps; selected boundary/mixed sets for three.
    checks.append(endpoint_check(8, 2, list(range(256))))
    checks.append(endpoint_check(8, 3, [0, 1, 15, 85, 129, 170, 254, 255]))
    out["endpoint_checks"] = checks
    out["path_checks"] = [cylinder_check(4, 4, 3, 0),
                          cylinder_check(8, 3, 15, 0),
                          cylinder_check(8, 3, 85, 2),
                          cylinder_check(8, 3, 255, 7),
                          cylinder_check(8, 3, 1, 0)]
    out["invalid_variants"] = invalid_variants()
    out["total_history_mask_cases"] = sum(c["history_mask_cases"] for c in checks)
    out["total_basis_indicator_equalities"] = sum(c["basis_indicator_equalities"] for c in checks)
    out["elapsed_seconds"] = round(time.monotonic() - start, 3)
    out["max_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert out["max_rss_bytes"] < 256 * 1024**2
    out["status"] = "all exact checks passed; no Lean build"
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
