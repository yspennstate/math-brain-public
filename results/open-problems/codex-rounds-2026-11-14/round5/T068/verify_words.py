#!/usr/bin/env python3
"""Finite audits of the word reduction, using sets and a graph-query oracle."""
import itertools
import math
import os
import resource
import sys
import time
from collections import Counter
from fractions import Fraction
from functools import lru_cache


@lru_cache(None)
def pairs(vertices):
    return frozenset(itertools.combinations(sorted(vertices), 2))


def words(k, r):
    for d in range(r + 1):
        for zeros in itertools.combinations(range(k + d - 1), d):
            z = set(zeros)
            yield tuple(int(i not in z) for i in range(k + d))


def execute(n, graph, schedule=None, mode=0, query_mode=0, adaptive=False,
            word=None, budget=0):
    """Only reveal() accesses graph. Decisions use the known-answer dictionary."""
    known, exceptional = {}, set()
    inspected, current, positive_vertices, kept = set(), frozenset(), set(), set()
    order, trace = [], []
    guards = Counter()
    pointer = 0
    for t in range(n):
        remaining = set(range(n)) - inspected
        if adaptive:
            v = max(remaining, key=lambda u: (
                sum(2 * bit - 1 for e, bit in known.items() if u in e), u))
        else:
            v = min(remaining)

        def reveal(request):
            for e in request:
                known[e] = e in graph

        reveal(pairs(frozenset(inspected | {v})) - pairs(frozenset(inspected)))
        inspected.add(v)
        if query_mode == 0:
            request = frozenset()
        elif query_mode == 1:
            request = frozenset(e for e in pairs(frozenset(range(n))) if t % n in e)
        else:
            unknown = sorted(pairs(frozenset(range(n))) - known.keys())
            request = frozenset([unknown[(t + v) % len(unknown)]]) if unknown else pairs(frozenset(inspected))
        if word is not None and len((exceptional | request) & pairs(frozenset(kept))) > budget:
            guards['query_stop'] += 1
            break
        reveal(request)
        exceptional.update(request)

        def is_known_clique(vertices):
            return all(known.get(e, False) for e in pairs(frozenset(vertices)))

        if schedule is not None:
            proposal = schedule[t]
            current = proposal if is_known_clique(proposal) else frozenset()
        elif mode == 0:
            candidates = (frozenset(c) for j in range(len(inspected) + 1)
                          for c in itertools.combinations(sorted(inspected), j))
            current = max((c for c in candidates if is_known_clique(c)),
                          key=lambda c: (len(c), tuple(sorted(c))))
        elif mode == 1:
            proposal = set()
            if t % 3 != 1:
                for u in sorted(inspected, reverse=True):
                    if is_known_clique(proposal | {u}):
                        proposal.add(u)
            current = frozenset(proposal)
        else:
            # Reject everything until a final old-vertex admission.
            proposal = set()
            if t == n - 1:
                for u in sorted(inspected):
                    if is_known_clique(proposal | {u}):
                        proposal.add(u)
            current = frozenset(proposal)
        assert current <= inspected and is_known_clique(current)
        order.append(v)
        trace.append((v, request, current))
        if v in current:
            positive_vertices.add(v)
            if word is not None:
                symbol = word[pointer]
                pointer += 1
                if symbol:
                    proposal = frozenset(kept | {v})
                    if not is_known_clique(proposal):
                        guards['clique_reject'] += 1
                    elif len(exceptional & pairs(proposal)) > budget:
                        guards['budget_reject'] += 1
                    else:
                        kept.add(v)
                if pointer == len(word):
                    guards['word_stop'] += 1
                    break
    if word is None:
        return current, frozenset(exceptional), trace, frozenset(positive_vertices)
    assert len(exceptional & pairs(frozenset(kept))) <= budget
    assert pairs(frozenset(kept)) <= graph
    return frozenset(kept), frozenset(exceptional), trace, guards


def audit_case(n, graph, counts, guards, budgets=(0,), **kwargs):
    final, exceptional, trace, positive = execute(n, graph, **kwargs)
    core, deleted = final & positive, positive - final
    counts['original_runs'] += 1
    r = min(n, 2)
    for k in range(1, n + 1):
        correct = None
        wanted = set()
        if len(core) >= k:
            bits = []
            for v, _, state in trace:
                if v in state:
                    bits.append(int(v in final))
                    if v in final:
                        wanted.add(v)
                    if len(wanted) == k:
                        break
            assert len(wanted) == k and bits[-1] == 1
            if bits.count(0) <= r:
                correct = tuple(bits)
        for budget in budgets:
            good = len(exceptional & pairs(final)) <= budget
            seen_correct = False
            for word in words(k, r):
                kept, queried, simulated, gc = execute(
                    n, graph, word=word, budget=budget, **kwargs)
                counts['guarded_runs'] += 1
                guards.update(gc)
                assert len(kept) <= k
                if word == correct and good:
                    seen_correct = True
                    assert kept == frozenset(wanted)
                    assert simulated == trace[:len(simulated)]
                    assert len(simulated) > 0
                    # The word ends exactly at the kth core inspection round.
                    assert simulated[-1][0] in wanted
                    assert sum(v in core for v, _, _ in simulated) == k
                    assert queried == frozenset().union(*(s for _, s, _ in simulated))
                    counts['correct_events'] += 1
                    counts['early_stops'] += len(simulated) < n
                    counts['deletions_after_stop'] += any(
                        v in deleted for v, _, _ in trace[len(simulated):])
                    counts['late_and_deleted'] += bool(final - positive) and bool(deleted)
                    counts['prefix_only_events'] += len(deleted) > r
            assert seen_correct == (correct is not None and good)


def finite_checks(started):
    counts, guards = Counter(), Counter()
    for n in range(1, 5):
        edges = sorted(pairs(frozenset(range(n))))
        subsets = [frozenset(c) for j in range(n + 1)
                   for c in itertools.combinations(range(n), j)]
        for mask in range(1 << len(edges)):
            graph = frozenset(e for i, e in enumerate(edges) if mask >> i & 1)
            counts['exhaustive_graphs'] += 1
            choices = [[c for c in subsets if c <= set(range(t + 1)) and pairs(c) <= graph]
                       for t in range(n)]
            for schedule in itertools.product(*choices):
                counts['exhaustive_trajectories'] += 1
                audit_case(n, graph, counts, guards, schedule=schedule)
            assert time.monotonic() - started < 180
    print('All-trajectory audit:', dict(sorted(counts.items())), flush=True)
    for n in range(2, 5):
        edges = sorted(pairs(frozenset(range(n))))
        for mask in range(1 << len(edges)):
            graph = frozenset(e for i, e in enumerate(edges) if mask >> i & 1)
            for mode, query_mode, adaptive in itertools.product(range(3), (1, 2), (False, True)):
                audit_case(n, graph, counts, guards, (0, 1, 3), mode=mode,
                           query_mode=query_mode, adaptive=adaptive)
            assert time.monotonic() - started < 180
    assert all(guards[label] > 0 for label in ('query_stop', 'clique_reject', 'budget_reject', 'word_stop'))
    assert all(counts[label] > 0 for label in ('early_stops', 'deletions_after_stop', 'late_and_deleted'))
    print('Combined audit:', dict(sorted(counts.items())), flush=True)
    print('Guard coverage:', dict(sorted(guards.items())), flush=True)
    return counts


def arithmetic_checks():
    cases = 0
    for k in range(1, 7):
        for r in range(7):
            family = list(words(k, r))
            # Independent enumeration of all binary words through length k+r.
            brute = [bits for m in range(k, k + r + 1)
                     for bits in itertools.product((0, 1), repeat=m)
                     if bits[-1] == 1 and sum(bits) == k]
            assert set(family) == set(brute)
            assert len(family) == math.comb(k + r, r)
            # An independent Pascal recurrence on the rectangular grid.
            grid = [[1] * (r + 1) for _ in range(k + 1)]
            for i in range(1, k + 1):
                for j in range(1, r + 1):
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
            assert len(family) == grid[k][r]
            cases += 1
    print(f'Exact word-family cases={cases}', flush=True)
    eps, beta = Fraction(1), Fraction(1, 2)
    eta = eps - beta
    h = min(eta * eta, 1)
    c, xi = h / 8, h / 64
    a = h / (128 * (1 + eta))
    assert (c, xi, a, xi - a * (1 + eta)) == (
        Fraction(1, 32), Fraction(1, 256), Fraction(1, 768), Fraction(1, 512))
    print(f'epsilon={eps}; beta={beta}; eta={eta}; c={c}; xi={xi}; a={a}; coefficient={xi-a*(1+eta)}')
    for x in (7680, 15360, 23040):
        raw = (1 + eta) * (x - 1)
        k = math.ceil(raw)
        r = 1 << int(a * x)
        n = 1 << x
        assert r ** a.denominator == n
        exact = math.comb(k + r, k)
        log_count = math.log2(exact)
        alternate = math.fsum(math.log2(r + j) - math.log2(j) for j in range(1, k + 1))
        assert math.isclose(log_count, alternate, rel_tol=1e-12, abs_tol=1e-8)
        thinning = k * math.log2(1 + r / k) + r * math.log1p(k / r) / math.log(2)
        elementary = k * math.log2(math.e * (k + r) / k)
        assert log_count <= thinning <= elementary + 1e-8
        quadratic = xi * (x - 1) ** 2
        exponent = log_count - float(quadratic)
        natural = math.log(exact) - float(quadratic) * math.log(2)
        assert math.isclose(natural, exponent * math.log(2), rel_tol=1e-12)
        leading = -float((xi - a * (1 + eta)) * x * x)
        assert exponent < leading < 0
        print(f'x={x}; k={k}; r={r}; old_explicit_r={int(h*x/128)}; '
              f'log2N={log_count:.9f}; thinning_cost={thinning:.9f}; '
              f'log2_bound={exponent:.9f}; leading={leading:.9f}', flush=True)


def independent_count_check(counts):
    # Sum schedules before graphs. Each schedule forces its clique-edge union.
    schedules = guarded = 0
    for n in range(1, 5):
        local = 0
        choices = [[frozenset(v for v in range(t + 1) if mask >> v & 1)
                    for mask in range(1 << (t + 1))] for t in range(n)]
        for schedule in itertools.product(*choices):
            required = frozenset().union(*(pairs(c) for c in schedule))
            local += 1 << (n * (n - 1) // 2 - len(required))
        schedules += local
        family_total = sum(math.comb(k + min(n, 2), k) for k in range(1, n + 1))
        guarded += local * family_total
    assert schedules == counts['exhaustive_trajectories'] == 23112
    adaptive_runs = (2 + 8 + 64) * 3 * 2 * 2
    adaptive_guarded = sum((1 << (n * (n - 1) // 2)) * 12 * 3 *
                          sum(math.comb(k + 2, k) for k in range(1, n + 1))
                          for n in range(2, 5))
    assert counts['original_runs'] == schedules + adaptive_runs
    assert counts['guarded_runs'] == guarded + adaptive_guarded
    print(f'Independent totals: trajectories={schedules}; original={schedules+adaptive_runs}; guarded={guarded+adaptive_guarded}')


def adversarial_fixtures():
    # Four final deletion disagreements occur strictly after the two core
    # vertices have already been inspected. No zeros need to be guessed.
    n = 7
    graph = pairs(frozenset(range(n)))
    schedule = (frozenset({0}), frozenset({0, 1}), frozenset({2}),
                frozenset({3}), frozenset({4}), frozenset({5}), frozenset({0, 1}))
    final, exceptional, trace, positive = execute(n, graph, schedule=schedule)
    kept, queries, prefix, _ = execute(n, graph, schedule=schedule, word=(1, 1), budget=0)
    assert final & positive == kept == frozenset({0, 1})
    assert len(positive - final) == 4
    assert len(prefix) == 2 and prefix == trace[:2]
    assert exceptional == queries == frozenset()
    print('Prefix fixture: core=2; total_D=4; guessed_zeros=0; stopping_round=2')

    # The final maximum clique can consist almost entirely of late admissions.
    final, exceptional, trace, positive = execute(n, graph, mode=2)
    assert len(final) == n and len(final & positive) == 1
    assert len(positive - final) == 0 and not exceptional
    print('Late-admission fixture: final=7; core=1; D=0; R=6; E=0')


def main():
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15
    resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
    started = time.monotonic()
    print(f'nice={priority}; OMP_NUM_THREADS=1; CPU limit=180s', flush=True)
    arithmetic_checks()
    adversarial_fixtures()
    counts = finite_checks(started)
    independent_count_check(counts)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == 'darwin' else rss * 1024
    assert rss_bytes < 1_000_000_000
    print(f'PASS; elapsed={time.monotonic()-started:.3f}s; peak_RSS={rss_bytes} bytes')


if __name__ == '__main__':
    main()
