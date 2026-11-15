#!/usr/bin/env python3
"""Independent bit-mask audit. Only standard library; no asymptotic simulation claim."""
import itertools
import math
import os
import resource
import sys
import time
from collections import Counter
from fractions import Fraction


class Instance:
    def __init__(self, n, graph):
        self.n = n
        self.edges = list(itertools.combinations(range(n), 2))
        self.graph = graph
        self.all_vertices = (1 << n) - 1
        self.all_edges = (1 << len(self.edges)) - 1
        self.internal = [sum(1 << k for k, (u, v) in enumerate(self.edges)
                             if mask >> u & 1 and mask >> v & 1)
                         for mask in range(1 << n)]
        self.cliques = [mask for mask in range(1 << n)
                        if self.internal[mask] & ~graph == 0]

    def edge_count(self, edge_mask, vertices):
        return (edge_mask & self.internal[vertices]).bit_count()


def trajectory(inst, kind=0, query_mode=0, seed=0, schedule=None,
               guess=None, budget=0):
    """Execute B from its permitted transcript, optionally with an A_T output."""
    n = inst.n
    inspected = known = positive = exceptional = current = output = on_time = 0
    order, trace, prefixes = [], [], []
    guards = Counter()
    ever = 0
    coverage = Counter()
    for t in range(n):
        candidates = [v for v in range(n) if not inspected >> v & 1]
        if schedule is not None or seed == 0:
            v = min(candidates)
        else:
            # Adaptive order depends only on currently revealed edge answers.
            def key(v):
                incident = sum(1 << k for k, e in enumerate(inst.edges) if v in e)
                return ((positive & incident).bit_count()
                        - (known & incident & ~positive).bit_count(), v)
            v = max(candidates, key=key)
        bit = 1 << v
        ordinary = inst.internal[inspected | bit] & ~inst.internal[inspected]
        known |= ordinary
        positive |= ordinary & inst.graph
        inspected |= bit
        if query_mode == 0:
            request = 0
        elif query_mode == 1:
            # Deliberately repeat old queries too: E is a union of requested sets.
            request = sum(1 << k for k, e in enumerate(inst.edges)
                          if (t + seed) % n in e)
        else:
            unknown = [k for k in range(len(inst.edges)) if not known >> k & 1]
            request = 1 << unknown[(t + v) % len(unknown)] if unknown else inst.internal[inspected]
        if guess is not None and inst.edge_count(exceptional | request, output) > budget:
            guards['query_stop'] += 1
            assert inst.edge_count(exceptional, output) <= budget
            return output, exceptional, trace, prefixes, guards, coverage
        exceptional |= request
        known |= request
        positive |= request & inst.graph
        old = current
        if schedule is not None:
            proposal = schedule[t]
            # Makes this fixed seed a legitimate B on every graph, not just the
            # particular graph used to enumerate the schedule.
            current = proposal if inst.internal[proposal] & ~positive == 0 else 0
        elif kind == 0:
            available = [m for m in inst.cliques if m & ~inspected == 0]
            # For subsets of inspected vertices the whole induced graph is known.
            # Recheck using positive, to detect accidental access to hidden bits.
            assert available == [m for m in range(1 << n) if m & ~inspected == 0
                                 and inst.internal[m] & ~positive == 0]
            current = max(available, key=lambda m: (m.bit_count(), m ^ (seed * 3)))
        elif kind == 1:
            # Reject early; admit a group of old vertices in the final update.
            available = [m for m in range(1 << n) if m & ~inspected == 0
                         and inst.internal[m] & ~positive == 0]
            current = max(available, key=lambda m: (m.bit_count(), m)) if t == n - 1 else 0
        elif kind == 2:
            # Forced empty rounds create deletion/readmission histories.
            current = 0
            if (t + seed) % 3 != 1:
                for u in reversed(range(n)):
                    proposal = current | (1 << u)
                    if inspected >> u & 1 and inst.internal[proposal] & ~positive == 0:
                        current = proposal
        else:
            # Repeatedly replace a clique by the current vertex and an old one.
            current = bit
            for u in range(n):
                proposal = current | (1 << u)
                if u != v and inspected >> u & 1 and inst.internal[proposal] & ~positive == 0:
                    current = proposal
                    break
        assert current & ~inspected == 0
        assert inst.internal[current] & ~inst.graph == 0
        old_adds = current & ~old & ~bit
        coverage['late_operations'] += old_adds.bit_count()
        coverage['readmissions'] += (old_adds & ever).bit_count()
        coverage['multiple_old_admissions'] += old_adds.bit_count() >= 2
        ever |= current
        if current & bit:
            on_time |= bit
        order.append(v)
        trace.append((v, request, current))
        if guess is not None and current & bit and not guess >> t & 1:
            proposal = output | bit
            if inst.internal[proposal] & ~positive:
                guards['clique_reject'] += 1
            elif inst.edge_count(exceptional, proposal) > budget:
                guards['budget_reject'] += 1
            else:
                output = proposal
        if guess is not None:
            assert inst.internal[output] & ~inst.graph == 0
            assert inst.edge_count(exceptional, output) <= budget
            prefixes.append((inspected, output))
    if guess is None:
        deleted = sum(1 << t for t, v in enumerate(order)
                      if on_time >> v & 1 and not current >> v & 1)
        return current, exceptional, trace, on_time, deleted, coverage
    return output, exceptional, trace, prefixes, guards, coverage


def audit_case(inst, counts, guards, budgets, **kwargs):
    final, queries, trace, on_time, deleted, coverage = trajectory(inst, **kwargs)
    counts['original_runs'] += 1
    counts.update(coverage)
    core = final & on_time
    late = final & ~on_time
    assert core.bit_count() == final.bit_count() - late.bit_count()
    for budget in budgets:
        good = inst.edge_count(queries, final) <= budget
        for guess in range(1 << inst.n):
            kept, exceptional, simulated, prefixes, gc, _ = trajectory(
                inst, guess=guess, budget=budget, **kwargs)
            counts['guarded_runs'] += 1
            guards.update(gc)
            if guess == deleted and good:
                assert kept == core
                assert exceptional == queries
                assert simulated == trace
                assert all(k == core & inspected for inspected, k in prefixes)
                counts['correct_guess_events'] += 1
                if late and deleted and core:
                    counts['mixed_correct_events'] += 1


def finite_checks(started):
    counts, guards = Counter(), Counter()
    for n in range(1, 5):
        for graph in range(1 << (n * (n - 1) // 2)):
            inst = Instance(n, graph)
            counts['exhaustive_graphs'] += 1
            choices = [[m for m in inst.cliques if m < (1 << (t + 1))]
                       for t in range(n)]
            # All legal clique sequences, including every old-vertex revision,
            # for every graph with fixed inspection order and no extra queries.
            for schedule in itertools.product(*choices):
                counts['exhaustive_trajectories'] += 1
                audit_case(inst, counts, guards, (0,), schedule=schedule)
            assert time.monotonic() - started < 180
    print('All-trajectory audit:', dict(sorted(counts.items())), flush=True)
    for n in range(2, 6):
        graph_limit = 1 << (n * (n - 1) // 2)
        graphs = range(graph_limit) if n < 5 else sorted(set(range(0, graph_limit, 33)) | {graph_limit - 1})
        for graph in graphs:
            inst = Instance(n, graph)
            counts['adaptive_test_graphs'] += 1
            for kind, query_mode, seed in itertools.product(range(4), (1, 2), (0, 1)):
                audit_case(inst, counts, guards, (0, 1, 3), kind=kind,
                           query_mode=query_mode, seed=seed)
            assert time.monotonic() - started < 180
    for label in ('query_stop', 'clique_reject', 'budget_reject'):
        assert guards[label] > 0
    for label in ('readmissions', 'multiple_old_admissions', 'mixed_correct_events'):
        assert counts[label] > 0
    print('Combined audit:', dict(sorted(counts.items())), flush=True)
    print('Guards:', dict(sorted(guards.items())), flush=True)


def arithmetic_checks():
    cases = 0
    for n in range(1, 13):
        histogram = Counter(mask.bit_count() for mask in range(1 << n))
        for r in range(n + 1):
            m = sum(math.comb(n, j) for j in range(r + 1))
            assert m == sum(histogram[j] for j in range(r + 1))
            assert m <= (r + 1) * n ** r
            cases += 1
    eps = Fraction(1, 2)
    beta = eps / 2
    eta = eps - beta
    h = min(eta * eta, 1)
    c, xi, a = h / 8, h / 64, h / 128
    assert (c, xi, a) == (Fraction(1, 128), Fraction(1, 1024), Fraction(1, 2048))
    print(f'Exact counting cases={cases}; epsilon={eps}, beta={beta}, eta={eta}, c={c}, xi={xi}, a={a}')
    for x in (4096, 8192):
        n, r, s = 1 << x, int(a * x), int(beta * x)
        target = (1 + eps) * x
        assert target - s == (1 + eta) * x
        # Integer binomial computation versus the independent leading product.
        m = sum(math.comb(n, j) for j in range(r + 1))
        log_m = math.log2(m)
        alternate = r * x - sum(math.log2(j) for j in range(1, r + 1))
        assert abs(log_m - alternate) < 1e-9
        exponent = log_m - float(xi * (x - 1) ** 2)
        crude = math.log2(r + 1) + r * x - float(xi * (x - 1) ** 2)
        expanded = -float((xi - a) * x * x) + float(2 * xi * x - xi) + math.log2(r + 1)
        assert abs(crude - expanded) < 1e-9
        assert exponent <= crude < 0
        natural = math.log(m) - float(xi) * ((x - 1) * math.log(2)) ** 2 / math.log(2)
        assert math.isclose(natural, exponent * math.log(2), rel_tol=1e-12)
        print(f'x={x}, r={r}, s={s}, core_target={target-s}: log2M={log_m:.9f}, exponent={exponent:.9f}, crude={crude:.9f}')


def main():
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    started = time.monotonic()
    print(f'nice={priority}; OMP_NUM_THREADS=1; CPU limit=120s', flush=True)
    arithmetic_checks()
    finite_checks(started)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == 'darwin' else rss * 1024
    assert rss_bytes < 1_000_000_000
    print(f'PASS; elapsed={time.monotonic()-started:.3f}s; peak_RSS={rss_bytes} bytes')


if __name__ == '__main__':
    main()
