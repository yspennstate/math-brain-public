#!/usr/bin/env python3
"""Exact finite and arithmetic audits for the no-exceptional-query extension."""
import itertools
import math
import os
import resource
import sys
import time
from collections import Counter
from fractions import Fraction as F


def source_law(n):
    """Forward pure-birth recurrence, with exact rational probabilities."""
    law = [F(1)]
    for _ in range(n):
        new = [F(0)] * (len(law) + 1)
        for j, mass in enumerate(law):
            p = F(1, 1 << j)
            new[j] += mass * (1 - p)
            new[j + 1] += mass * p
        law = new
    return law


def geometric_tail(n, k):
    """Independent convolution of positive geometric waiting times."""
    mass = [F(1)] + [F(0)] * n
    for j in range(k):
        p = F(1, 1 << j)
        waiting = [F(0)] + [p * (1 - p) ** (t - 1) for t in range(1, n + 1)]
        mass = [sum((mass[t - u] * waiting[u] for u in range(1, t + 1)), F(0))
                for t in range(n + 1)]
    return sum(mass, F(0))


def finite_upper(n, k, s):
    ell = k - s
    return min(F(1), F(math.comb(n, ell), 1 << (s * ell + ell * (ell - 1) // 2)))


def recurrence_checks():
    upper_cases = convolution_cases = lower_cases = 0
    for n in range(1, 41):
        law = source_law(n)
        assert sum(law) == 1
        for k in range(1, n + 1):
            tail = sum(law[k:])
            for s in range(k):
                assert tail <= finite_upper(n, k, s)
                upper_cases += 1
            m = n // k
            block_event = math.prod(1 - (1 - F(1, 1 << j)) ** m for j in range(k))
            lower = math.prod(min(F(m, 1 << j), F(1)) / 2 for j in range(k))
            assert lower <= block_event <= tail
            lower_cases += 1
            if n <= 16 and k <= 8:
                assert tail == geometric_tail(n, k)
                convolution_cases += 1
    # Independent backward Bellman recurrence; check its monotonicity explicitly.
    bellman_cases = 0
    for k in range(1, 13):
        values = [F(0)] * k + [F(1)]
        for h in range(1, 25):
            old = values
            values = [(1 - F(1, 1 << j)) * old[j] + F(1, 1 << j) * old[j + 1]
                      for j in range(k)] + [F(1)]
            assert all(values[j + 1] >= values[j] for j in range(k))
            assert values[0] == sum(source_law(h)[k:])
            bellman_cases += 1
    print(f'Exact source checks: upper_bounds={upper_cases}; geometric_convolutions={convolution_cases}; '
          f'block_lower_bounds={lower_cases}; Bellman_steps={bellman_cases}', flush=True)


def run(n, graph, mode, adaptive, revision=False):
    """Policies see only a known-adjacency array. reveal() alone reads graph."""
    known = [0] * n
    seen = current = positive = 0
    checksum = 0
    trace = []
    for t in range(n):
        candidates = [v for v in range(n) if not seen >> v & 1]
        v = candidates[(checksum + t) % len(candidates)] if adaptive else candidates[0]

        def reveal():
            for u in range(n):
                if seen >> u & 1:
                    e = (min(u, v), max(u, v))
                    if e in graph:
                        known[v] |= 1 << u
                        known[u] |= 1 << v
        reveal()
        seen |= 1 << v
        checksum = (checksum * 5 + known[v] + t) % 65521

        def clique(mask):
            return all((mask & ~(1 << u)) & ~known[u] == 0
                       for u in range(n) if mask >> u & 1)

        compatible = known[v] & current == current
        if not revision:
            admit = compatible and (mode == 0 or
                    (mode == 1 and t % 2 == 0) or
                    (mode == 2 and (not current or (known[v] & ~current).bit_count() % 2 == 0)) or
                    (mode == 3 and (checksum + v) % 3 != 0))
            if admit:
                current |= 1 << v
        elif mode == 0:
            if compatible:
                current |= 1 << v
        elif mode == 1:
            current = max((mask for mask in range(1 << n) if mask & ~seen == 0 and clique(mask)),
                          key=lambda mask: (mask.bit_count(), mask))
        elif mode == 2:
            current = 1 << v
        else:
            current = 0
            if t % 3 != 1:
                for u in reversed(range(n)):
                    if seen >> u & 1 and clique(current | (1 << u)):
                        current |= 1 << u
        assert current & ~seen == 0 and clique(current)
        if current >> v & 1:
            positive |= 1 << v
        trace.append((v, current))
    return current, positive, trace


def exhaustive_policies():
    source_runs = revision_runs = joint_cases = greedy_matches = cover_cases = 0
    mixed = 0
    illegal_numerator = 0
    for n in range(1, 6):
        edges = list(itertools.combinations(range(n), 2))
        graph_count = 1 << len(edges)
        source_hist = {(mode, order): Counter() for mode in range(4) for order in range(2)}
        revision_hist = {(mode, order): Counter() for mode in range(4) for order in range(2)}
        for encoded in range(graph_count):
            graph = frozenset(e for i, e in enumerate(edges) if encoded >> i & 1)
            for mode, order in itertools.product(range(4), range(2)):
                final, _, _ = run(n, graph, mode, order)
                source_hist[mode, order][final.bit_count()] += 1
                source_runs += 1
                final, positive, trace = run(n, graph, mode, order, revision=True)
                core = final & positive
                deleted = positive & ~final
                late = final & ~positive
                revision_hist[mode, order][core.bit_count(), deleted.bit_count()] += 1
                revision_runs += 1
                mixed += bool(core and deleted and late)
                # Correct-word prefix checked independently of the old simulator.
                for k in range(1, core.bit_count() + 1):
                    word = []
                    kept = 0
                    for v, state in trace:
                        if state >> v & 1:
                            word.append(int(bool(final >> v & 1)))
                            if word[-1]:
                                kept |= 1 << v
                            assert all((min(u, v), max(u, v)) in graph
                                       for u in range(n) if u != v and kept >> u & 1) if word[-1] else True
                            if kept.bit_count() == k:
                                break
                    assert word[-1] == 1 and sum(word) == k
                    assert word.count(0) <= deleted.bit_count()
                    assert kept & ~core == 0
                    cover_cases += 1
            if n == 5:
                # Full-information clique selection is an illegal irrevocable policy.
                illegal_numerator += any(all(e in graph for e in itertools.combinations(vertices, 2))
                                         for vertices in itertools.combinations(range(n), 3))
        law = source_law(n)
        for key, hist in source_hist.items():
            for k in range(1, n + 1):
                probability = F(sum(count for size, count in hist.items() if size >= k), graph_count)
                greedy_tail = sum(law[k:])
                assert probability <= greedy_tail
                if key[0] == 0:
                    assert probability == greedy_tail
                    greedy_matches += 1
        for hist in revision_hist.values():
            for k in range(1, n + 1):
                for r in range(n + 1):
                    probability = F(sum(count for (core, deleted), count in hist.items()
                                        if core >= k and deleted <= r), graph_count)
                    words = math.comb(k + r, k)
                    assert probability <= min(F(1), words * sum(law[k:]))
                    assert probability <= min(F(1), words * min(finite_upper(n, k, s) for s in range(k)))
                    joint_cases += 1
    illegal = F(illegal_numerator, 1024)
    greedy = sum(source_law(5)[3:])
    assert illegal > greedy
    assert mixed > 0
    print(f'All graph inputs n=1..5: source_runs={source_runs}; revision_runs={revision_runs}; '
          f'joint_bounds={joint_cases}; greedy_exact_matches={greedy_matches}; '
          f'correct_word_prefixes={cover_cases}; mixed_core_D_R={mixed}', flush=True)
    print(f'Failure fixture with full future information: n=5, k=3; maximum-clique success={illegal}; '
          f'legal greedy success={greedy}', flush=True)
    # No queries or final deletion disagreements, but final late admissions can be large.
    final, positive = (1 << 7) - 1, 1 << 6
    assert (final & positive).bit_count() == 1 and (positive & ~final).bit_count() == 0
    print('Late-admission fixture: complete graph n=7; final=7; core=1; D=0; R=6', flush=True)


def log1p_pow2(t):
    return max(t, 0) + math.log1p(2 ** (-abs(t))) / math.log(2)


def large_arithmetic():
    eta = F(1, 2)
    gamma = 1 + eta
    critical = eta * eta / (2 * gamma)
    old = eta * eta / (64 * gamma)
    interior = critical / 2
    assert critical == F(1, 12) and old == F(1, 384) and critical / old == 32
    assert interior == F(1, 24) and eta * eta / 2 - interior * gamma == F(1, 16)
    assert gamma + eta == 2
    print(f'Exact constants: eta={eta}; critical_a={critical}; previous_strict_ceiling={old}; '
          f'power_ratio={critical/old}; interior_a={interior}; interior_coefficient=1/16; '
          f'endpoint_second_coefficient={gamma+eta}', flush=True)
    for x in (120, 240, 480, 960):
        n = 1 << x
        k = int(gamma * x)
        s = x
        ell = k - s
        r = 1 << int(critical * x)
        assert r ** critical.denominator == n
        word_count = math.comb(k + r, k)
        time_count = math.comb(n, ell)
        source_power = s * ell + ell * (ell - 1) // 2
        log_words = math.log2(word_count)
        log_tail = math.log2(time_count) - source_power
        total = log_words + log_tail
        # Independent products of factors, without constructing binomial integers.
        log_words_alt = math.fsum(math.log2(r + j) - math.log2(j) for j in range(1, k + 1))
        log_tail_alt = math.fsum(math.log2(n - j) - math.log2(j + 1)
                                 for j in range(ell)) - source_power
        assert math.isclose(log_words, log_words_alt, abs_tol=1e-7)
        assert math.isclose(log_tail, log_tail_alt, abs_tol=1e-7)
        assert total < 0
        # Explicit factorial-integral expression, independently expanded.
        constant = float(gamma + eta) * math.log2(math.e) - float(gamma) * math.log2(float(gamma)) \
                   - float(eta) * math.log2(float(eta)) + float(eta) / 2
        expanded = -float(gamma + eta) * x * math.log2(x) + constant * x \
                   + k * math.log1p(k / r) / math.log(2)
        direct = k * math.log2(k + r) - k * math.log2(k) + k * math.log2(math.e) \
                 + ell * (x - s) - ell * (ell - 1) / 2 \
                 - ell * math.log2(ell) + ell * math.log2(math.e)
        assert math.isclose(expanded, direct, abs_tol=1e-7)
        assert total <= expanded + 1e-7
        # A separate geometric Chernoff upper bound. Choose lambda=ell/n and
        # use exp(lambda)-1 >= lambda, evaluating all factors in log space.
        chernoff = ell / math.log(2) - math.fsum(log1p_pow2(math.log2(ell) - x + j)
                                               for j in range(k))
        m = n // k
        block_lower = -k - math.fsum(max(0, j - math.log2(m)) for j in range(k))
        assert block_lower <= log_tail + 1e-7
        assert block_lower <= chernoff + 1e-7
        assert chernoff < 0
        # Natural logarithms independently check the combined sign and units.
        natural = math.log(word_count) + math.log(time_count) - source_power * math.log(2)
        assert math.isclose(natural, total * math.log(2), abs_tol=1e-7)
        print(f'x={x}; k={k}; r=2^{int(critical*x)}; log2_words={log_words:.9f}; '
              f'log2_source={log_tail:.9f}; log2_joint_bound={total:.9f}; '
              f'endpoint_ratio={-total/(x*math.log2(x)):.9f}; '
              f'factorial_upper={expanded:.9f}; geometric_upper={chernoff:.9f}; '
              f'block_lower={block_lower:.9f}', flush=True)


def main():
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    started = time.monotonic()
    print(f'nice={priority}; OMP_NUM_THREADS=1; CPU limit=120s', flush=True)
    recurrence_checks()
    assert time.monotonic() - started < 180
    exhaustive_policies()
    assert time.monotonic() - started < 180
    large_arithmetic()
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == 'darwin' else rss * 1024
    assert rss_bytes < 1_000_000_000
    assert time.monotonic() - started < 180
    print(f'PASS; elapsed={time.monotonic()-started:.3f}s; peak_RSS={rss_bytes} bytes', flush=True)


if __name__ == '__main__':
    main()
