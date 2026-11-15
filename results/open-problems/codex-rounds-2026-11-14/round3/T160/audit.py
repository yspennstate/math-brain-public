"""Exact checks for PROOF.md; no imports or execution of the earlier audit.

Run: nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py
The infinite conclusions are proved analytically, not inferred from this run.
"""

import csv
from decimal import Decimal, localcontext
import itertools
import math
import os
from pathlib import Path
from fractions import Fraction as F
import resource
import signal
import time

os.environ["OMP_NUM_THREADS"] = "1"
signal.alarm(120)
started = time.monotonic()


def multiply(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def evaluate(a, x):
    out = F(0)
    for c in reversed(a):
        out = out * x + c
    return out


def generation_pgf(pattern, p):
    """Forward PGF composition, using polynomial convolution and Horner's rule."""
    pgf = [F(0), F(1)]
    for b in pattern:
        offspring = [F(1)]
        for _ in range(b):
            offspring = multiply(offspring, [1 - p, p])
        nxt = [F(0)]
        for c in reversed(pgf):
            nxt = multiply(nxt, offspring)
            nxt[0] += c
        while len(nxt) > 1 and nxt[-1] == 0:
            nxt.pop()
        pgf = nxt
    return pgf


def survival(pattern, terminal=F(1)):
    """Backward critical survival, independently of the forward PGF."""
    t = terminal
    for b in reversed(pattern):
        t = t / 2 if b == 1 else t - t * t / 4
    return t


def mean(pattern, p=F(1, 2)):
    return math.prod(b * p for b in pattern)


def rooted_tree(pattern):
    parents = [-1]
    paths = [0]
    level = [0]
    for b in pattern:
        nxt = []
        for parent in level:
            for _ in range(b):
                vertex = len(parents)
                parents.append(parent)
                paths.append(paths[parent] | (1 << (vertex - 1)))
                nxt.append(vertex)
        level = nxt
    return parents, [paths[v] for v in level]


# Recheck the earlier survival and critical-parameter inputs by a forward
# polynomial calculation rather than the earlier distribution-transition code.
moments = prefix_checks = horizon_checks = 0
for n in range(1, 6):
    for pattern in itertools.product((1, 2), repeat=n):
        for p in (F(1, 3), F(1, 2), F(2, 3)):
            pgf = generation_pgf(pattern, p)
            assert sum(pgf) == 1
            ez = sum(i * c for i, c in enumerate(pgf))
            ez2 = sum(i * i * c for i, c in enumerate(pgf))
            m = mean(pattern, p)
            reciprocal_sum = sum(1 / mean(pattern[:i], p) for i in range(1, n + 1))
            assert ez == m
            assert ez2 / m**2 == 1 + (1 - p) * reciprocal_sum
            q = 1 - pgf[0]
            assert q >= m**2 / ez2
            if p == F(1, 2):
                assert q == survival(pattern)
                assert q >= m / (n + 1)
                trailing = 0
                for b in reversed(pattern):
                    if b == 1:
                        break
                    trailing += 1
                if trailing:
                    assert q <= 4 * m / (trailing + 4)
            moments += 1

        # Exact TV distances on F_m reduce to the distribution of Z_m,
        # since both densities are functions of that random variable.
        for m in range(n + 1):
            dist = generation_pgf(pattern[:m], F(1, 2))
            continuation = survival(pattern[m:])
            mass = mean(pattern[:m])
            q = survival(pattern)
            k = sum(F(z * (z - 1), 2) * c for z, c in enumerate(dist))
            conditional_mass = F(0)
            tv = F(0)
            for z, c in enumerate(dist):
                g = 1 - (1 - continuation)**z
                assert 0 <= z * continuation - g <= F(z * (z - 1), 2) * continuation**2
                conditional_mass += c * g
                tv += c * abs(g / q - z / mass) / 2
            assert conditional_mass == q
            assert tv <= k * continuation / mass
            prefix_checks += 1

for n in range(0, 7):
    for pattern in itertools.product((1, 2), repeat=n):
        q = survival(pattern)
        m = mean(pattern)
        for b in (1, 2):
            q_next = survival(pattern + (b,))
            displacement = 1 / q_next - 1 / q
            assert 0 <= displacement <= 1 / m
            assert 1 / (1 + q / m) <= q_next / q <= 1
            horizon_checks += 1

print(f"PASS: {moments} forward-PGF moment identities and survival bounds")
print(f"PASS: {prefix_checks} exact prefix-density and total-variation bounds")
print(f"PASS: {horizon_checks} adjacent-horizon reciprocal and ratio inequalities")


# Enumerate full finite edge configurations, independently of PGF recursion.
# Also sum the forced-path measures explicitly to check the spine construction.
enumerated = spine_configs = spine_patterns = 0
for n in range(1, 4):
    for pattern in itertools.product((1, 2), repeat=n):
        parents, path_masks = rooted_tree(pattern)
        edges = len(parents) - 1
        root_connected_count = 0
        distribution = [0] * (len(path_masks) + 1)
        spine_total = F(0)
        expected_spine_z = F(0)
        for mask in range(1 << edges):
            reached = [True]
            for v in range(1, len(parents)):
                reached.append(reached[parents[v]] and bool(mask & (1 << (v - 1))))
            # Path inclusion counts the same connected endpoints without using
            # the parent-reachability recurrence.
            z = sum((mask & path) == path for path in path_masks)
            assert z == sum(reached[v] for v in range(len(parents) - len(path_masks), len(parents)))
            distribution[z] += 1
            root_connected_count += z > 0
            forced_path_mass = sum(
                (F(1, len(path_masks)) * F(1, 1 << (edges - n)))
                for path in path_masks if (mask & path) == path
            )
            biased_mass = F(1, 1 << edges) * z / mean(pattern)
            assert forced_path_mass == biased_mass
            spine_total += forced_path_mass
            expected_spine_z += z * forced_path_mass
            spine_configs += 1
        assert F(root_connected_count, 1 << edges) == survival(pattern)
        pgf = generation_pgf(pattern, F(1, 2))
        assert [F(c, 1 << edges) for c in distribution] == pgf
        assert spine_total == 1
        ez2 = sum(z * z * c for z, c in enumerate(pgf))
        assert expected_spine_z == ez2 / mean(pattern)
        enumerated += 1
        spine_patterns += 1
print(f"PASS: {enumerated} finite trees, {spine_configs} configurations: survival and explicit spine law")


# Check the union-mixture identity by enumerating the attachment states and
# the two independent branch-success indicators. This also includes open
# attachment edges whose branch does not survive.
union_checks = 0
for a in itertools.product((1, 2), repeat=2):
    for b in itertools.product((1, 2), repeat=2):
        qa, qb = survival(a), survival(b)
        u, v = qa / 2, qb / 2
        d, total = u + v - u * v, u + v
        atoms = []
        edge_numerator = F(0)
        event_mass = F(0)
        for ea, sa, eb, sb in itertools.product((0, 1), repeat=4):
            base = F(1, 4) * (qa if sa else 1 - qa) * (qb if sb else 1 - qb)
            success_a, success_b = ea and sa, eb and sb
            union = success_a or success_b
            mu = base / d if union else F(0)
            mix = base * (int(success_a) + int(success_b)) / total
            intersection = base / (u * v) if success_a and success_b else F(0)
            weight = u * v / total
            assert mix == (1 - weight) * mu + weight * intersection
            atoms.append((mu, mix))
            if union:
                event_mass += base
                edge_numerator += ea * base
        assert event_mass == d
        assert edge_numerator / d == 1 - v / (2 * d)
        tv = sum(abs(x - y) for x, y in atoms) / 2
        assert tv == (u * v / total) * (1 - u * v / d)
        assert tv <= u * v / total
        union_checks += 1
print(f"PASS: {union_checks} exact union-mixture identities and root-edge formulas")


weight_checks = 0
for epsilon in (F(1, 2), F(1, 8), F(1, 32)):
    lo = 1 / (1 + epsilon)
    ratios = (lo, (lo + 1) / 2, F(1))
    for i in range(17):
        w = F(i, 16)
        for ra, rb in itertools.product(ratios, repeat=2):
            nxt = w * ra / (w * ra + (1 - w) * rb)
            assert abs(nxt - w) <= epsilon * w * (1 - w) <= epsilon / 4
            weight_checks += 1
print(f"PASS: {weight_checks} exact mixture-weight increment bounds")


# Construct the suppressed index sets explicitly. Only their O(k^2) indices
# are stored; the exponentially large trees and binary plateaus are not built.
suppressed = {"A": set(), "B": set()}
previous = 0
rows = []
for k in range(1, 41):
    endpoint = 1 << (k * k + 10)
    recipient = "A" if k % 2 else "B"
    suppressed[recipient].update(range(previous + 1, previous + 2 * k))
    da, db = len(suppressed["A"]), len(suppressed["B"])
    assert da + db == k * k
    assert da - db == (-1)**(k + 1) * k
    plateau = endpoint - previous - (2 * k - 1)
    assert plateau >= F(endpoint, 2)
    for s in ("A", "B"):
        assert not any(previous + 2 * k <= i <= endpoint for i in suppressed[s])
    rho = F(16, 1 << k)
    # Reconstruct the old endpoint ratio from the simple independent bounds.
    weaker_d, stronger_d = (da, db) if k % 2 else (db, da)
    ratio_from_bounds = F(4, (1 << weaker_d) * (plateau + 4)) / F(1, (1 << stronger_d) * (endpoint + 1))
    assert ratio_from_bounds <= rho
    row = dict(k=k, D_A=da, D_B=db, endpoint_ratio_upper=str(rho))
    if k >= 2:
        previous_previous = 0 if k == 2 else 1 << ((k - 2)**2 + 10)
        previous_plateau = previous - previous_previous - (2 * k - 3)
        eps = F(8 * (1 << (2 * k - 1)), previous)
        exponent = -k * k + 4 * k - 9
        independent_eps = F(2**exponent) if exponent >= 0 else F(1, 1 << (-exponent))
        assert eps == independent_eps
        assert F(4 * (1 << (2 * k - 1)), previous_plateau) <= eps
        assert F(4 * (1 << (2 * k - 1)), previous_plateau + 4) <= eps
        # A second calculation of suppression relative to the previous endpoint.
        for s in ("A", "B"):
            count_after_previous = sum(i > previous for i in suppressed[s])
            assert count_after_previous in (0, 2 * k - 1)
        row.update(epsilon=str(eps), adjacent_weight_bound=str(eps / 4))
    else:
        row.update(epsilon="not used", adjacent_weight_bound="not used")
    rows.append(row)
    previous = endpoint

with Path("stage_bounds.csv").open("w", newline="") as out:
    writer = csv.DictWriter(out, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

print("PASS: 40 explicit suppression schedules, endpoint ratios and previous-plateau bounds")
print("Certified analytic bounds, not simulated survival probabilities:")
print("k  D_A D_B  weak/strong upper   adjacent-weight increment upper")


def scientific_fraction(value):
    """Render a positive rational without binary-float exponent underflow."""
    value = F(value)
    with localcontext() as context:
        context.prec = 12
        return format(Decimal(value.numerator) / Decimal(value.denominator), ".6e")


for row in rows:
    if row["k"] in (2, 4, 8, 16, 32, 40):
        print(f'{row["k"]:2} {row["D_A"]:4} {row["D_B"]:4}  '
              f'{scientific_fraction(row["endpoint_ratio_upper"])}       '
              f'{scientific_fraction(row["adjacent_weight_bound"])}')

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1_000_000_000
print(f"Priority: {os.getpriority(os.PRIO_PROCESS, 0)}; OMP_NUM_THREADS={os.environ['OMP_NUM_THREADS']}")
print(f"Elapsed seconds: {time.monotonic() - started:.3f}")
print(f"Peak RSS bytes (macOS): {rss}")
print("PASS: all exact checks")
