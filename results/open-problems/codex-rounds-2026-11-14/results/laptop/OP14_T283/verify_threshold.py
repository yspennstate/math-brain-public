"""Exhaustive audits for PROOF.md; stdlib only, single process, bounded sizes."""
import ctypes
import itertools as it
import json
import math
import os
from pathlib import Path
import time

os.environ['OMP_NUM_THREADS'] = '1'
if os.name == 'nt':
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel.GetCurrentProcess.restype = ctypes.c_void_p
    if not kernel.SetPriorityClass(ctypes.c_void_p(kernel.GetCurrentProcess()), 0x4000):
        raise ctypes.WinError(ctypes.get_last_error())


def subset_girth(columns):
    """Direct subset enumeration; None means independent."""
    sums = [0] * (1 << len(columns))
    best = None
    for mask in range(1, len(sums)):
        bit = mask & -mask
        sums[mask] = sums[mask ^ bit] ^ columns[bit.bit_length() - 1]
        if sums[mask] == 0:
            size = mask.bit_count()
            best = size if best is None else min(best, size)
    return best


def dynamic_girth(columns):
    """Independent shortest-syndrome dynamic program, no subset masks."""
    dist = {0: 0}
    best = None
    for value in columns:
        if value in dist:
            candidate = dist[value] + 1
            best = candidate if best is None else min(best, candidate)
        updated = dict(dist)
        for syndrome, weight in dist.items():
            target = syndrome ^ value
            updated[target] = min(updated.get(target, len(columns) + 1), weight + 1)
        dist = updated
    return best


def wedge(u, v, k):
    result = 0
    for pos, (a, b) in enumerate(it.combinations(range(k), 2)):
        value = ((u >> a) & (v >> b) & 1) ^ ((u >> b) & (v >> a) & 1)
        result |= value << pos
    return result


def form_matrices(k):
    """Enumerate actual alternating matrices, not wedge coordinates."""
    pairs = list(it.combinations(range(k), 2))
    for bits in range(1 << len(pairs)):
        rows = [0] * k
        for pos, (a, b) in enumerate(pairs):
            if (bits >> pos) & 1:
                rows[a] |= 1 << b
                rows[b] |= 1 << a
        yield rows


def evaluate_form(u, v, rows):
    # Direct matrix multiplication u^T B v.
    value = 0
    for a, row in enumerate(rows):
        if (u >> a) & 1:
            value ^= (row & v).bit_count() & 1
    return value


def truth_signatures(k):
    forms = list(form_matrices(k))
    return {(u, v): sum(evaluate_form(u, v, matrix) << b
                        for b, matrix in enumerate(forms))
            for u in range(1 << k) for v in range(u, 1 << k)}


def check_config(vectors, k, signatures):
    g = subset_girth(vectors)
    assert g == dynamic_girth(vectors), ('vector algorithms', vectors)
    pairs = list(it.combinations(vectors, 2))
    features = [wedge(u, v, k) for u, v in pairs]
    observed = subset_girth(features)
    truth = [signatures[tuple(sorted((u, v)))] for u, v in pairs]
    second = dynamic_girth(truth)
    expected = None if g is None else g - 1
    assert observed == second == expected, (k, vectors, g, observed, second)
    return g, observed


def gf2_rank(rows):
    pivots = {}
    for row in rows:
        while row:
            pos = row.bit_length() - 1
            if pos in pivots:
                row ^= pivots[pos]
            else:
                pivots[pos] = row
                break
    return len(pivots)


def graph_rank_audit():
    out = []
    for n in range(2, 7):
        edges = list(it.combinations(range(n), 2))
        count = 0
        for bits in range(1, 1 << len(edges)):
            adjacency = [0] * n
            t = 0
            for pos, (i, j) in enumerate(edges):
                if (bits >> pos) & 1:
                    adjacency[i] |= 1 << j
                    adjacency[j] |= 1 << i
                    t += 1
            incident = {i for i, row in enumerate(adjacency) if row}
            h = len(incident)
            remaining = set(incident)
            c = 0
            while remaining:
                c += 1
                stack = [remaining.pop()]
                while stack:
                    vertex = stack.pop()
                    found = {j for j in remaining if (adjacency[vertex] >> j) & 1}
                    remaining -= found
                    stack.extend(found)
            rank = gf2_rank(adjacency)
            assert rank % 2 == 0
            assert rank >= 2 * c and t >= h - c and h - rank // 2 <= t
            count += 1
        assert count == (1 << len(edges)) - 1
        out.append({'n': n, 'graphs': count})
    return out


def permutation_examples():
    results = []
    for length in range(3, 6):
        k = length - 1
        vectors = [1 << a for a in range(k)] + [(1 << k) - 1]
        forms = list(form_matrices(k))
        star = [(0, j) for j in range(1, length)]
        total = negative = zero_functions = 0
        for perm in it.permutations(range(length)):
            function = []
            for matrix in forms:
                parity = 0
                for i, j in star:
                    parity ^= evaluate_form(vectors[perm[i]], vectors[perm[j]], matrix)
                function.append(parity)
                negative += parity
                total += 1
            zero_functions += not any(function)
        # Since this example consists of the circuit itself, every spanning star is zero.
        assert negative == 0
        results.append({'circuit_size': length, 'permutation_form_pairs': total,
                        'parity_expectation_numerator': total - 2 * negative,
                        'parity_expectation_denominator': total,
                        'zero_functions': zero_functions})
    # Circuit plus a separate independent vector: averaging must weaken, not erase, bias.
    vectors = [1, 2, 3, 4]
    k = 3
    forms = list(form_matrices(k))
    numer = denom = zero_functions = 0
    for perm in it.permutations(range(4)):
        evaluations = [evaluate_form(vectors[perm[0]], vectors[perm[1]], matrix)
                       ^ evaluate_form(vectors[perm[0]], vectors[perm[2]], matrix)
                       for matrix in forms]
        zero_functions += not any(evaluations)
        numer += sum(1 - 2 * value for value in evaluations)
        denom += len(evaluations)
    assert (numer, denom, zero_functions) == (48, 192, 6)
    results.append({'vectors': vectors, 'edges': [[0, 1], [0, 2]],
                    'numerator': numer, 'denominator': denom,
                    'zero_functions': zero_functions, 'permutations': 24})
    # Independent resampling at rate 1/2 multiplies this degree-two coefficient by 1/4.
    # Enumerate all replacement masks and fresh bits, without using the multiplier formula.
    noisynum = noisydenom = 0
    for perm in it.permutations(range(4)):
        for matrix in forms:
            old = [evaluate_form(vectors[perm[0]], vectors[perm[j]], matrix) for j in (1, 2)]
            for replacements in it.product((0, 1), repeat=2):
                for fresh in it.product((0, 1), repeat=2):
                    values = [fresh[j] if replacements[j] else old[j] for j in range(2)]
                    noisynum += 1 - 2 * (values[0] ^ values[1])
                    noisydenom += 1
    assert (noisynum, noisydenom) == (192, 3072)
    results.append({'resampling_rate': '1/2', 'numerator': noisynum,
                    'denominator': noisydenom})
    return results


def main():
    start = time.monotonic()
    records = []
    total_configs = 0
    for k in range(1, 5):
        signatures = truth_signatures(k)
        count = 0
        histogram = {}
        for n in range(2, min(5, (1 << k) - 1) + 1):
            for vectors in it.combinations(range(1, 1 << k), n):
                g, edge = check_config(vectors, k, signatures)
                key = 'infinity' if g is None else str(g)
                histogram[key] = histogram.get(key, 0) + 1
                count += 1
        assert count == sum(math.comb((1 << k) - 1, n)
                            for n in range(2, min(5, (1 << k) - 1) + 1))
        independent_count = sum(math.prod((1 << k) - (1 << j) for j in range(n))
                                // math.factorial(n) for n in range(2, min(5, k) + 1))
        assert histogram.get('infinity', 0) == independent_count
        if k == 4:
            # Every 5-circuit in F_2^4 has exactly five bases, and each basis
            # extends to one 5-circuit by adjoining the sum of its four vectors.
            basis_count = math.prod(16 - (1 << j) for j in range(4)) // math.factorial(4)
            assert histogram['5'] == basis_count // 5 == 168
        records.append({'k': k, 'kind': 'distinct_nonzero', 'configurations': count,
                        'vector_girth_histogram': histogram})
        total_configs += count
    for k in range(1, 4):
        signatures = truth_signatures(k)
        count = 0
        for n in range(2, 6):
            for vectors in it.combinations_with_replacement(range(1, 1 << k), n):
                check_config(vectors, k, signatures)
                count += 1
        assert count == sum(math.comb((1 << k) + n - 2, n) for n in range(2, 6))
        records.append({'k': k, 'kind': 'nonzero_multisets', 'configurations': count})
        total_configs += count
    # Zero-vector exception is intentional; the g-1 formula excludes zero vectors.
    assert subset_girth([0, 1]) == 1
    assert subset_girth([wedge(0, 1, 1)]) == 1
    assert total_configs == 5884
    resource = {'OMP_NUM_THREADS': os.environ['OMP_NUM_THREADS']}
    if os.name == 'nt':
        class Counters(ctypes.Structure):
            _fields_ = [('cb', ctypes.c_ulong), ('PageFaultCount', ctypes.c_ulong)] + [
                (name, ctypes.c_size_t) for name in (
                    'PeakWorkingSetSize', 'WorkingSetSize', 'QuotaPeakPagedPoolUsage',
                    'QuotaPagedPoolUsage', 'QuotaPeakNonPagedPoolUsage',
                    'QuotaNonPagedPoolUsage', 'PagefileUsage', 'PeakPagefileUsage')]
        counters = Counters()
        counters.cb = ctypes.sizeof(counters)
        handle = ctypes.c_void_p(kernel.GetCurrentProcess())
        psapi = ctypes.WinDLL('psapi', use_last_error=True)
        if not psapi.GetProcessMemoryInfo(handle, ctypes.byref(counters), counters.cb):
            raise ctypes.WinError(ctypes.get_last_error())
        resource.update(peak_working_set_bytes=counters.PeakWorkingSetSize,
                        peak_private_commit_bytes=counters.PeakPagefileUsage,
                        priority_class=kernel.GetPriorityClass(handle))
        assert counters.PeakWorkingSetSize < 1_000_000_000
        assert counters.PeakPagefileUsage < 1_000_000_000
        assert resource['priority_class'] == 0x4000
    data = {'status': 'PASS', 'total_vector_configurations': total_configs,
            'configurations': records, 'graph_rank_audit': graph_rank_audit(),
            'permutation_and_noise_audit': permutation_examples(),
            'zero_vector_exception': {'vector_girth': 1, 'edge_girth': 1},
            'resource_audit': resource,
            'elapsed_seconds': round(time.monotonic() - start, 3)}
    Path('verification.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
