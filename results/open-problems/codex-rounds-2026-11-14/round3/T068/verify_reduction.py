#!/usr/bin/env python3
"""Small exhaustive checks of the deletion-to-irrevocable reduction.

Run: OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_reduction.py
This checks a finite family of policies, not the asymptotic hardness theorem.
"""

import itertools
import math
import os
import resource
import time
from collections import Counter
from fractions import Fraction


def pairs(vertices):
    return set(itertools.combinations(sorted(vertices), 2))


def edge(u, v):
    return (min(u, v), max(u, v))


def choose_vertex(n, inspected, known, seed):
    remaining = set(range(n)) - set(inspected)
    if seed == 0:
        return min(remaining)
    # Information-dependent order using only previously revealed pairs.
    def key(v):
        score = sum(2 * bit - 1 for e, bit in known.items() if v in e)
        return score, v
    return max(remaining, key=key)


def choose_queries(n, t, v, inspected, known, mode):
    if mode == 0:
        return set()
    remaining = set(range(n)) - set(inspected)
    if mode == 1:
        # Early look-ahead followed by queries among already inspected pairs.
        if remaining and t % 2 == 0:
            w = min(remaining)
            return {edge(w, u) for u in range(n) if u != w}
        return pairs(inspected)
    # Query one unrevealed future pair if possible, otherwise a known pair.
    candidates = sorted(pairs(range(n)) - set(known))
    if candidates:
        return {candidates[(t + v) % len(candidates)]}
    return set(sorted(pairs(inspected))[:1])


def decide(t, v, current, known, mode, seed):
    current = set(current)
    if mode == 0 and (t + seed) % 3 == 2 and current:
        current.remove(min(current))
    # Delete conflicts, then accept the current vertex. No old vertex is added.
    current = {u for u in current if known[edge(u, v)] == 1}
    current.add(v)
    if mode == 2 and (t + seed) % 4 == 3:
        # An immediate rejection/deletion of the current vertex.
        current.remove(v)
    return current


def run(n, graph, mode, seed, guess=None, budget=None):
    known, exceptional = {}, set()
    inspected, current, admitted = [], set(), {}
    kept, transcript, prefixes = set(), [], []
    counters = Counter()
    for t in range(n):
        v = choose_vertex(n, inspected, known, seed)
        for u in inspected:
            e = edge(u, v)
            known[e] = int(e in graph)
        inspected.append(v)
        requested = choose_queries(n, t, v, inspected, known, mode)
        if guess is not None and len((exceptional | requested) & pairs(kept)) > budget:
            counters['query_guard_stops'] += 1
            # Remaining ordinary inspections cannot change kept or exceptional.
            assert len(exceptional & pairs(kept)) <= budget
            return kept, exceptional, transcript, prefixes, counters
        exceptional |= requested
        for e in requested:
            known[e] = int(e in graph)
        previous = current
        current = decide(t, v, current, known, mode, seed)
        assert current <= previous | {v}
        assert pairs(current) <= graph
        if v in current:
            admitted[v] = t
        transcript.append((v, frozenset(requested), frozenset(current)))
        if guess is not None and v in current and t not in guess:
            proposal = kept | {v}
            if not pairs(proposal) <= graph:
                counters['clique_guard_rejections'] += 1
            elif len(exceptional & pairs(proposal)) > budget:
                counters['addition_budget_rejections'] += 1
            else:
                kept = proposal
        if guess is not None:
            assert pairs(kept) <= graph
            assert len(exceptional & pairs(kept)) <= budget
            prefixes.append((frozenset(inspected), frozenset(kept)))
    if guess is None:
        deleted = {t for v, t in admitted.items() if v not in current}
        return current, exceptional, transcript, deleted
    return kept, exceptional, transcript, prefixes, counters


def check_reduction():
    counts = Counter()
    guard_counts = Counter()
    deadline = time.monotonic() + 180
    for n in range(2, 6):
        all_pairs = sorted(pairs(range(n)))
        guesses = [frozenset(s) for k in range(min(2, n) + 1)
                   for s in itertools.combinations(range(n), k)]
        for mask in range(1 << len(all_pairs)):
            graph = {e for i, e in enumerate(all_pairs) if mask & (1 << i)}
            counts['graphs'] += 1
            for mode in range(3):
                for seed in range(2):
                    final, query_union, trace, deleted = run(n, graph, mode, seed)
                    counts['original_runs'] += 1
                    for budget in (0, 1, 3):
                        for guess in guesses:
                            result = run(n, graph, mode, seed, guess, budget)
                            kept, exceptional, sim_trace, prefixes, counters = result
                            guard_counts.update(counters)
                            counts['guarded_runs'] += 1
                            if guess == deleted and len(query_union & pairs(final)) <= budget:
                                assert kept == final
                                assert exceptional == query_union
                                assert sim_trace == trace
                                for inspected, prefix_kept in prefixes:
                                    assert prefix_kept == final & inspected
                                counts['correct_guess_events'] += 1
                                if len(final) >= 2 and deleted:
                                    counts['nontrivial_correct_guess_events'] += 1
            if mask % 64 == 0:
                assert time.monotonic() < deadline, '180-second verification limit'
    assert all(guard_counts[name] > 0 for name in (
        'query_guard_stops', 'clique_guard_rejections', 'addition_budget_rejections'))
    assert counts['nontrivial_correct_guess_events'] > 0
    print('Exhaustive reduction checks:', dict(sorted(counts.items())))
    print('Adversarial guard coverage:', dict(sorted(guard_counts.items())))


def check_constants():
    cases = 0
    for n in range(1, 21):
        row = [1]
        for _ in range(n):
            row = [1] + [row[i - 1] + row[i] for i in range(1, len(row))] + [1]
        for r in range(n + 1):
            m1 = sum(math.comb(n, j) for j in range(r + 1))
            m2 = sum(row[:r + 1])
            assert m1 == m2
            assert m1 <= (r + 1) * n ** r
            cases += 1
    eps = Fraction(1, 2)
    xi = min(eps * eps, 1) / 64
    c = min(eps * eps, 1) / 8
    assert c == Fraction(1, 32) and xi == Fraction(1, 256)
    print(f'Exact combinatorial-count checks: {cases}; epsilon=1/2, c={c}, xi={xi}')
    for x in (1024, 4096, 16384):
        n = 1 << x
        r = int(xi * x / 2)
        m = sum(math.comb(n, j) for j in range(r + 1))
        exact_log_count = math.log2(m)
        # Independently, sum_j binom(n,j) ~ n^r/r! in these large-n cases.
        factorial_approx = r * x - sum(math.log2(j) for j in range(1, r + 1))
        assert abs(exact_log_count - factorial_approx) < 1e-8
        exponent = exact_log_count - float(xi * (x - 1) ** 2)
        crude_exponent = math.log2(r + 1) + r * x - float(xi * (x - 1) ** 2)
        assert exponent <= crude_exponent
        assert exponent <= -float(xi * x * x / 4)
        ln_bound = math.log(2) * exact_log_count - float(xi) * (x - 1) ** 2 * math.log(2)
        assert math.isclose(exponent * math.log(2), ln_bound, rel_tol=1e-12)
        print(f'x={x}, r={r}: log2 M={exact_log_count:.6f}, '
              f'log2 probability upper bound={exponent:.6f}, '
              f'crude exponent={crude_exponent:.6f}')


def main():
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    # Fail before computation if the scheduler priority is not sufficiently low.
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15, f'Expected nice >= 15, observed {priority}'
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    # The algorithms enumerate at most 1,024 graphs, one at a time; no graph list
    # or exponential-size family of runs is retained. The largest integer below
    # has under 600,000 bits. Peak RSS is measured before returning.
    started = time.monotonic()
    print(f'nice={priority}; OMP_NUM_THREADS=1; no numerical-library imports')
    check_constants()
    check_reduction()
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # macOS reports bytes; Linux reports KiB.
    import sys
    rss_bytes = rss if sys.platform == 'darwin' else rss * 1024
    assert rss_bytes < 1_000_000_000
    print(f'PASS; elapsed={time.monotonic() - started:.3f}s; peak_RSS={rss_bytes} bytes')


if __name__ == '__main__':
    main()
