#!/usr/bin/env python3
"""Finite audits of PROOF.md. Standard library, small fixed workloads.

env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
    nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt 2>&1
"""

from collections import deque
import csv
from fractions import Fraction as F
import itertools
import json
import math
import os
from pathlib import Path
import resource
import sys
import time

sys.dont_write_bytecode = True
START = time.monotonic()
ROOT = Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
PRIORITY = os.getpriority(os.PRIO_PROCESS, 0)
assert PRIORITY >= 15, PRIORITY
for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    assert os.environ.get(name) == "1", (name, os.environ.get(name))


def h_r(r, t):
    if r == 0:
        return 0.0
    return t if t <= r else r * (1 + math.log(t / r))


def log_exp_sum(t, cap):
    # Recursively form log(t^s/s!), independently of lgamma.
    term = 0.0
    terms = [term]
    for s in range(1, cap + 1):
        term += math.log(t) - math.log(s)
        terms.append(term)
    largest = max(terms)
    return largest + math.log(math.fsum(math.exp(x - largest) for x in terms))


def tilt_checks():
    count = 0
    maximum_excess = 0.0
    for r in (F(0), F(1, 4), F(1), F(2), F(4)):
        for n in (1, 2, 3, 10, 50):
            for ratio in (F(1, 100), F(1, 2), F(1), F(101, 100), F(2), F(100)):
                t = float((r if r else 1) * ratio)
                exact = log_exp_sum(t * n, math.floor(r * n))
                exponent = n * h_r(float(r), t)
                assert exact <= exponent + 2e-10, (r, n, t, exact, exponent)
                # Separate Poisson exponential-Markov calculation.
                if r:
                    theta = max(0.0, math.log(t / float(r)))
                    poisson_expression = t*n + theta*float(r)*n + t*n*math.expm1(-theta)
                    assert abs(poisson_expression - exponent) < 2e-10
                else:
                    assert exact == exponent == 0
                maximum_excess = max(maximum_excess, exact - exponent)
                count += 1
    return count, maximum_excess


def graph_checks():
    # A weighted discrete version of integrated configuration sectors.
    # Sites 0 and 1 are the protected slots. Their mutual edge is absent.
    volumes = (1, 2, 3, 4, 5)
    candidate_edges = [p for p in itertools.combinations(range(5), 2) if p != (0, 1)]
    graph_count = case_count = 0
    for edge_mask in range(1 << len(candidate_edges)):
        edges = [p for bit, p in enumerate(candidate_edges) if edge_mask & (1 << bit)]
        coefficients = [0] * 6
        for subset in range(1 << 5):
            if any((subset & (1 << i)) and (subset & (1 << j)) for i, j in edges):
                continue
            selected = [i for i in range(5) if subset & (1 << i)]
            coefficients[len(selected)] += math.prod(volumes[i] for i in selected)
        graph_count += 1
        for z in (1, 8, 128):
            partition = sum(c * z**s for s, c in enumerate(coefficients))
            insertion_partition = (1 + z) * (1 + 2*z)
            assert partition >= insertion_partition
            for cap in (0, 1):
                numerator = sum(coefficients[s] * z**s for s in range(cap + 1))
                exponential_numerator = sum(
                    (F(z * sum(volumes))**s / math.factorial(s) for s in range(cap + 1)), F(0))
                assert numerator <= exponential_numerator
                assert numerator * insertion_partition <= exponential_numerator * partition
                case_count += 1
    # Negative control: the empty-event bound fails for the event N<=1.
    z = F(8)
    two_slot_partition = (1 + z)**2
    low_count_probability = (1 + 2*z) / two_slot_partition
    empty_probability = 1 / two_slot_partition
    assert low_count_probability > empty_probability
    # The strict r<m_0 condition cannot be removed to force a log-z penalty.
    assert ((1 + z)**2) / two_slot_partition == 1
    return graph_count, case_count


def directions(d):
    return tuple(tuple(sign if k == axis else 0 for k in range(d))
                 for axis in range(d) for sign in (-1, 1))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def grow_animals(d, maximum):
    origin = (0,) * d
    dirs = directions(d)
    families = {1: {frozenset((origin,))}}
    for n in range(2, maximum + 1):
        families[n] = {
            occupied | {add(x, step)}
            for occupied in families[n-1]
            for x in occupied
            for step in dirs
            if add(x, step) not in occupied
        }
    return families


def tree_word(occupied, d):
    origin = (0,) * d
    dirs = directions(d)
    parent = {origin: None}
    children = {x: [] for x in occupied}
    frontier = deque((origin,))
    while frontier:
        x = frontier.popleft()
        for index, step in enumerate(dirs):
            y = add(x, step)
            if y in occupied and y not in parent:
                parent[y] = x
                children[x].append((y, index))
                frontier.append(y)
    assert len(parent) == len(occupied)
    word = []

    def visit(x):
        for y, index in children[x]:
            word.append(index)
            visit(y)
            word.append(index ^ 1)

    visit(origin)
    assert len(word) == 2 * (len(occupied) - 1)
    x = origin
    visited = {origin}
    for index in word:
        x = add(x, dirs[index])
        visited.add(x)
    assert x == origin and frozenset(visited) == occupied
    return tuple(word)


def closed_walk_animals(d, n):
    origin = (0,) * d
    dirs = directions(d)
    found = set()
    for word in itertools.product(range(2*d), repeat=2*(n-1)):
        x = origin
        visited = {origin}
        for index in word:
            x = add(x, dirs[index])
            visited.add(x)
            if len(visited) > n:
                break
        else:
            if x == origin and len(visited) == n:
                found.add(frozenset(visited))
    return found


def animal_checks():
    rows = []
    for d, maximum in ((2, 5), (3, 4)):
        families = grow_animals(d, maximum)
        for n, family in families.items():
            words = {tree_word(occupied, d) for occupied in family}
            assert len(words) == len(family)
            assert len(family) <= (2*d)**(2*(n-1))
            rows.append(dict(d=d, n=n, exact_count=len(family), word_upper_bound=(2*d)**(2*(n-1))))
        independent_family = closed_walk_animals(d, maximum)
        assert independent_family == families[maximum]
        print(f"animals d={d}: counts={[len(families[n]) for n in families]}; independent_closed_walk_match=PASS")
    return rows


def geometry_checks():
    a, ell, margin = F(1, 4), F(4), F(5, 4)
    h = 1 + 2*a
    k = 1 + (ell - 2*margin) // h
    assert k == 2
    for d in (2, 3):
        base = tuple(itertools.product((F(5, 4), F(11, 4)), repeat=d))
        assert len(base) == 2**d
        for p in base:
            assert all(margin <= x <= ell - margin for x in p)
        assert min(sum((x-y)**2 for x, y in zip(p, q))
                   for p, q in itertools.combinations(base, 2)) == h*h
        adjacent = tuple(tuple(x + (ell if axis == 0 else 0) for axis, x in enumerate(p)) for p in base)
        assert min(sum((x-y)**2 for x, y in zip(p, q)) for p in base for q in adjacent) == F(25, 4)
        # Large-box version of the periodic insertion corollary, P=Z^d.
        length = F(100)
        mean = ((length - 2*margin) / h)**d
        m_0 = math.floor(mean)
        r = length**d / 4
        assert m_0 > r
        print(f"periodic_slots d={d}: ell=100, rho=1/4, m_0={m_0}, r={r}, limiting_slot_density={1/h**d}")


def constant_checks():
    rows = []
    rationals = {}
    for d, threshold, expected in ((2, 4096, F(4, 9)), (3, 65536, F(729, 16384))):
        m_0, v, r = 2**d, 4**d, 2**(d-1)
        b_lower = F(3, 16) if d == 2 else F(1, 16)
        e_upper = F(3)
        # Exact calculation from r log[z b^2 r/(e v)], without pi or floating point.
        vacancy_factor = (e_upper * v / (r * b_lower*b_lower * threshold))**r
        q_upper = (2*d)**2 * vacancy_factor
        assert q_upper == expected < 1
        rationals[str(d)] = dict(activity_threshold=threshold, q_upper=str(q_upper),
                                 exp_minus_tau_upper=str(vacancy_factor))
        b = math.pi/16 if d == 2 else math.pi/48
        for z in ((4096, 10000, 1000000) if d == 2 else (10000, 65536, 1000000)):
            tau = m_0 * math.log1p(z*b) - h_r(r, z*v)
            denominator_constant = 2048 if d == 2 else 36864
            tau_second = r * math.log(z * math.pi**2 / (denominator_constant * math.e))
            assert tau >= tau_second - 2e-13
            # Exact identity for the difference between the two expressions.
            correction = m_0 * math.log1p(1/(z*b))
            assert abs((tau - tau_second) - correction) < 2e-13
            q = (2*d)**2 * math.exp(-tau)
            if z >= threshold:
                assert q <= float(q_upper)
            rows.append(dict(d=d, z=z, m_0=m_0, r=r, b=b, tau=tau,
                             tau_logarithmic_lower=tau_second, q=q,
                             root_cluster_tail_n10=min(1.0, q**10/(2*d)**2)))
            print(f"d={d}, z={z}: tau={tau:.12g}, tau_lower={tau_second:.12g}, q={q:.12g}")
        print(f"exact sufficient threshold d={d}: z>={threshold}, exp(-tau)<={vacancy_factor}, q<={q_upper}")
    return rows, rationals


def main():
    print("Finite audits of integrated low-occupation and connected-set bounds.")
    print(f"nice_priority={PRIORITY}; thread_environment=1; CPU_limit_seconds=60")
    geometry_checks()
    tilt_count, maximum_excess = tilt_checks()
    print(f"tilt_cases={tilt_count}; all_finite_sums_below_exponent=PASS; independent_Poisson_derivation=PASS")
    graphs, graph_cases = graph_checks()
    print(f"weighted_graphs={graphs}; exact_low_count_ratio_cases={graph_cases}; negative_controls=PASS")
    animals = animal_checks()
    constants, rationals = constant_checks()
    for filename, rows in (("animal_counts.csv", animals), ("contour_bounds.csv", constants)):
        with (ROOT / filename).open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_mib = rss / (1024**2 if sys.platform == "darwin" else 1024)
    assert peak_mib < 128
    result = dict(status="PASS", nice_priority=PRIORITY, tilt_cases=tilt_count,
                  maximum_log_sum_excess=maximum_excess, weighted_graphs=graphs,
                  exact_graph_cases=graph_cases, animal_counts=animals,
                  sufficient_thresholds=rationals, contour_examples=constants,
                  elapsed_seconds=time.monotonic()-START, peak_rss_mib=peak_mib)
    (ROOT / "verification.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS; elapsed_seconds={result['elapsed_seconds']:.3f}; peak_rss_mib={peak_mib:.3f}")
    print("Wrote animal_counts.csv, contour_bounds.csv, verification.json")


if __name__ == "__main__":
    main()
