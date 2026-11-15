#!/usr/bin/env python3
"""Independent exact tests of the weighted exposure-charge bound."""
import itertools
import math
import os
import resource
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction as F


def upper(n, k, s, q):
    ell = k - s
    exponent = q - s * ell - ell * (ell - 1) // 2
    raw = F(math.comb(n, ell)) * (F(2) ** exponent)
    return min(F(1), raw)


def execute(n, graph, policy, query_mode, adaptive, revising=False):
    edges = list(itertools.combinations(range(n), 2))
    pair_masks = [[0] * n for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        pair_masks[u][v] = pair_masks[v][u] = 1 << i
    all_edges = (1 << len(edges)) - 1
    known = answers = queries = seen = kept = positive = 0
    checksum = 0
    trace = []
    charges = []
    accepted_at = []
    charged_pairs = 0

    def reveal(request):
        nonlocal known, answers
        known |= request
        answers |= request & graph

    def internal(vertices):
        return sum(1 << i for i, (u, v) in enumerate(edges)
                   if vertices >> u & 1 and vertices >> v & 1)

    def clique(vertices):
        return internal(vertices) & ~answers == 0

    for t in range(n):
        candidates = [v for v in range(n) if not seen >> v & 1]
        def score(v):
            incident = sum(pair_masks[u][v] for u in range(n) if kept >> u & 1)
            return ((known & incident & ~answers).bit_count() * -10 +
                    (answers & incident).bit_count(), (v + checksum) % n)
        v = max(candidates, key=score) if adaptive else min(candidates)
        to_kept = sum(pair_masks[u][v] for u in range(n) if kept >> u & 1)
        preknown = known & to_kept
        b = preknown.bit_count()
        ordinary = sum(pair_masks[u][v] for u in range(n) if seen >> u & 1)
        reveal(ordinary)
        seen |= 1 << v
        if query_mode == 0:
            request = 0
        elif query_mode == 1:
            request = all_edges if t == 0 else 0
        elif query_mode == 2:
            remaining = [u for u in range(n) if not seen >> u & 1]
            u = remaining[(checksum + t) % len(remaining)] if remaining else v
            request = sum(pair_masks[u][w] for w in range(n) if w != u)
        elif query_mode == 3:
            unknown = [i for i in range(len(edges)) if not known >> i & 1]
            request = 1 << unknown[(checksum + t) % len(unknown)] if unknown else ordinary
        else:
            remaining = [u for u in range(n) if not seen >> u & 1]
            request = sum(pair_masks[u][w] for u in remaining for w in range(n)
                          if kept >> w & 1)
        queries |= request
        reveal(request)
        checksum = (checksum * 7 + answers + t) % 65521
        old = kept
        if not revising:
            compatible = clique(kept | (1 << v))
            admit = compatible and (policy == 0 or
                    (policy == 1 and (checksum + v) % 3 != 0) or
                    (policy == 2 and t % 2 == 0))
            if policy == 3:
                target = max((mask for mask in range(1 << n) if clique(mask)),
                             key=lambda mask: (mask.bit_count(), mask))
                admit = compatible and bool(target >> v & 1)
            if admit:
                kept |= 1 << v
                accepted_at.append(t)
                charges.append(b)
                assert not charged_pairs & preknown
                charged_pairs |= preknown
        elif policy == 0:
            if clique(kept | (1 << v)):
                kept |= 1 << v
        elif policy == 1:
            kept = max((mask for mask in range(1 << n) if mask & ~seen == 0 and clique(mask)),
                       key=lambda mask: (mask.bit_count(), mask))
        elif policy == 2:
            kept = 1 << v
        else:
            kept = 0
            if t % 3 != 1:
                for u in reversed(range(n)):
                    if seen >> u & 1 and clique(kept | (1 << u)):
                        kept |= 1 << u
        assert kept & ~seen == 0 and clique(kept)
        if kept >> v & 1:
            positive |= 1 << v
        # All choices and all revealed answers are included in the history.
        trace.append((v, request, kept, known, answers, queries, checksum))
    q = (queries & internal(kept)).bit_count()
    if not revising:
        assert sum(charges) == charged_pairs.bit_count() <= q
        assert charged_pairs & ~queries == 0
        assert charged_pairs & ~internal(kept) == 0
    return kept, positive, q, tuple(trace), tuple(accepted_at), tuple(charges)


def finite_checks():
    source_runs = revision_runs = source_bounds = revision_bounds = weighted_cases = 0
    nonzero_charge_runs = full_query_successes = 0
    for n in range(1, 6):
        graph_count = 1 << (n * (n - 1) // 2)
        max_q = n * (n - 1) // 2
        for policy, query_mode, adaptive in itertools.product(range(4), range(5), range(2)):
            source_hist, revision_hist = Counter(), Counter()
            denominators = Counter()
            numerators = defaultdict(F)
            for graph in range(graph_count):
                final, positive, q, trace, times, charges = execute(n, graph, policy, query_mode, adaptive)
                source_runs += 1
                source_hist[final.bit_count(), q] += 1
                nonzero_charge_runs += bool(sum(charges))
                full_query_successes += query_mode == 1 and final.bit_count() >= 3
                if n <= 4:
                    # Verify the conditional weighted tuple inequality itself,
                    # grouping all graph inputs by the complete hitting history.
                    for s in range(min(final.bit_count(), n - 1) + 1):
                        prefix = () if s == 0 else trace[:times[s - 1] + 1]
                        history_key = (s, prefix)
                        denominators[history_key] += 1
                        for k in range(s + 1, final.bit_count() + 1):
                            selected_times = times[s:k]
                            z = sum(charges[s:k])
                            numerators[history_key, k, selected_times] += F(1, 1 << z)
                final, positive, q, _, _, _ = execute(n, graph, policy, query_mode, adaptive, revising=True)
                revision_runs += 1
                revision_hist[(final & positive).bit_count(), (positive & ~final).bit_count(), q] += 1
            for (history_key, k, times), weighted_sum in numerators.items():
                s = history_key[0]
                ell = k - s
                assert weighted_sum <= F(denominators[history_key],
                                          1 << (s * ell + ell * (ell - 1) // 2))
                weighted_cases += 1
            for k in range(1, n + 1):
                for q in range(max_q + 1):
                    probability = F(sum(count for (size, used), count in source_hist.items()
                                        if size >= k and used <= q), graph_count)
                    for s in range(k):
                        assert probability <= upper(n, k, s, q)
                        source_bounds += 1
                    for r in range(n + 1):
                        probability = F(sum(count for (core, deleted, used), count in revision_hist.items()
                                            if core >= k and deleted <= r and used <= q), graph_count)
                        bound = min(upper(n, k, s, q) for s in range(k)) * math.comb(k + r, k)
                        assert probability <= min(F(1), bound)
                        revision_bounds += 1
    assert nonzero_charge_runs > 0 and full_query_successes > 0
    print(f'Exact queried-policy audit: source_runs={source_runs}; revision_runs={revision_runs}; '
          f'source_joint_bounds={source_bounds}; revision_joint_bounds={revision_bounds}; '
          f'conditional_weighted_tuples={weighted_cases}; '
          f'nonzero_charge_runs={nonzero_charge_runs}; full_query_successes={full_query_successes}', flush=True)


def arithmetic_checks():
    eta = F(1, 2)
    gamma = 1 + eta
    c = eta * eta / 8
    a = (eta * eta / 2 - c) / gamma
    old = eta * eta / (64 * gamma)
    assert (c, a, old, a / old) == (F(1, 32), F(1, 16), F(1, 384), F(24))
    assert eta * eta / 2 - c - (a / 2) * gamma == F(3, 64)
    print(f'Query-budget constants: eta={eta}; c={c}; critical_a={a}; old_strict_ceiling={old}; '
          f'ratio={a/old}; half_critical_a={a/2}; remaining_coefficient=3/64', flush=True)
    for x in (128, 256, 512, 1024):
        n, k, s = 1 << x, int(gamma * x), x
        ell = k - s
        r = 1 << int(a * x)
        # Use the slightly larger c*x^2 cap for an exact endpoint cancellation;
        # the preceding report's c*(x-1)^2 cap is therefore also covered.
        q = int(c * x * x)
        assert F(q) == c * x * x and r ** a.denominator == n
        words, times = math.comb(k + r, k), math.comb(n, ell)
        exponent = q - s * ell - ell * (ell - 1) // 2
        log_bound = math.log2(words) + math.log2(times) + exponent
        alternate = math.fsum(math.log2(r + j) - math.log2(j) for j in range(1, k + 1)) \
                    + math.fsum(math.log2(n - j) - math.log2(j + 1) for j in range(ell)) + exponent
        assert math.isclose(log_bound, alternate, abs_tol=1e-7)
        assert log_bound < 0
        constant = float(gamma + eta) * math.log2(math.e) - float(gamma) * math.log2(float(gamma)) \
                   - float(eta) * math.log2(float(eta)) + float(eta) / 2
        factorial = -float(gamma + eta) * x * math.log2(x) + constant * x \
                    + k * math.log1p(k / r) / math.log(2)
        assert log_bound <= factorial + 1e-7
        natural = math.log(words) + math.log(times) + exponent * math.log(2)
        assert math.isclose(natural, log_bound * math.log(2), abs_tol=1e-7)
        print(f'Queried endpoint: x={x}; k={k}; r=2^{int(a*x)}; q={q}; '
              f'log2_bound={log_bound:.9f}; factorial_upper={factorial:.9f}; '
              f'endpoint_ratio={-log_bound/(x*math.log2(x)):.9f}', flush=True)


def main():
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    started = time.monotonic()
    print(f'nice={priority}; OMP_NUM_THREADS=1; CPU limit=120s', flush=True)
    finite_checks()
    arithmetic_checks()
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == 'darwin' else rss * 1024
    assert rss_bytes < 1_000_000_000 and time.monotonic() - started < 180
    print(f'PASS; elapsed={time.monotonic()-started:.3f}s; peak_RSS={rss_bytes} bytes', flush=True)


if __name__ == '__main__':
    main()
