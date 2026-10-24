"""Bounded exact checks of C0029 boundary claims; no store mutations or third-party packages."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import json
import math
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
GOVERNOR = Path('~/.claude/compute/compute_state.json')


def save(name, payload):
    (ROOT / name).write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')


def fresh_gate():
    st = json.loads(GOVERNOR.read_text(encoding='utf-8-sig'))
    age = time.time() - GOVERNOR.stat().st_mtime
    receipt = {'checked_utc': datetime.now(timezone.utc).isoformat(),
               'source': str(GOVERNOR), 'age_seconds': age,
               'mode': st.get('mode'), 'status': st.get('status'),
               'limits': 'Fresh <=120s; no distress/throttle/stop. Single process, standard library, max n=5 enumeration, no GPU.',
               'policy_source': '~/<private-repo>/12_cognitive_architecture/compute_governor/COMPUTE_DOCTRINE.md:128-130; compute_sense.py:1193-1196'}
    mode = str(st.get('mode', '')).lower()
    status = str(st.get('status', '')).lower()
    permitted = mode in {'normal', 'green', 'ok', 'clear', 'healthy', 'run', 'owner_present_polite'}
    if any(x in mode or x in status for x in ('pause', 'stop', 'distress', 'throttle', 'red', 'retired', 'blocked')):
        permitted = False
    receipt['passed'] = 0 <= age <= 120 and permitted
    save('COMPUTE_GATE.json', receipt)
    if not receipt['passed']:
        raise SystemExit('Compute gate closed or unknown; no experiment run: ' + json.dumps(receipt))
    return receipt


def stirling(n):
    row = [1]
    for k in range(1, n + 1):
        row = [(row[a - 1] if a else 0) - (k - 1) * (row[a] if a < k else 0)
               for a in range(k + 1)]
    return row


def no_collision_formula(n):
    s = stirling(n)
    return sum(s[a] * s[b] * (1 << ((a - 1) * (b - 1)))
               for a in range(1, n + 1) for b in range(1, n + 1))


def partitions(n):
    out = []
    def visit(labels):
        if len(labels) == n:
            out.append(tuple(labels))
            return
        for label in range(max(labels, default=-1) + 2):
            visit(labels + [label])
    visit([])
    return out


def bits_matrix(n, word):
    return [[(word >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]


def projective_labels(rows):
    return [tuple(v ^ row[0] for v in row) for row in rows]


def complies(labels, part):
    return all(labels[i] == labels[j] for i in range(len(part))
               for j in range(i) if part[i] == part[j])


def original_partition_checks():
    results = []
    total_checks = 0
    for n in range(1, 4):
        parts = partitions(n)
        counts = Counter()
        cross = 0
        normalized_counts = Counter()
        for word in range(1 << (n * n)):
            X = bits_matrix(n, word)
            rows = projective_labels(X)
            cols = projective_labels(list(map(list, zip(*X))))
            D = tuple(X[i][j] ^ X[i][0] ^ X[0][j] ^ X[0][0]
                      for i in range(1, n) for j in range(1, n))
            normalized_counts[D] += 1
            good_r = [p for p in parts if complies(rows, p)]
            good_c = [p for p in parts if complies(cols, p)]
            for p in good_r:
                for q in good_c:
                    counts[p, q] += 1
            if n >= 2 and rows[0] == rows[1] and cols[0] == cols[1]:
                cross += 1
        assert len(normalized_counts) == 1 << ((n - 1) ** 2)
        assert set(normalized_counts.values()) == {1 << (2 * n - 1)}
        for p in parts:
            for q in parts:
                a, b = len(set(p)), len(set(q))
                codim = (n - 1) ** 2 - (a - 1) * (b - 1)
                assert counts[p, q] == 1 << (n * n - codim), (n, p, q)
                total_checks += 1
        if n >= 2:
            assert Fraction(cross, 1 << (n * n)) == Fraction(1, 1 << (2 * n - 3))
        results.append({'n': n, 'original_matrices': 1 << (n * n),
                        'partition_pairs': len(parts) ** 2, 'all_passed': True,
                        'specified_cross_collision_count': cross})
    return results, total_checks


def exact_collision_checks():
    results = []
    for n in range(1, 6):
        k = n - 1
        total = 1 << (k * k)
        no_collision = 0
        for word in range(total):
            rows = [0] + [(word >> (i * k)) & ((1 << k) - 1) for i in range(k)]
            if len(set(rows)) != n:
                continue
            cols = [0] + [sum(((rows[i + 1] >> j) & 1) << i for i in range(k)) for j in range(k)]
            no_collision += len(set(cols)) == n
        predicted = no_collision_formula(n)
        assert no_collision == predicted, (n, no_collision, predicted)
        E = Fraction(total - no_collision, total)
        m = 1 << (n - 1)
        same_side_no = math.prod(m - j for j in range(n))
        same_side_E = 1 - Fraction(same_side_no, m ** n)
        independence_prediction = 1 - (1 - same_side_E) ** 2
        if n >= 2:
            A = n * (n - 1) // 2
            lower = Fraction(2 * A, m) - Fraction(3 * A * A - A, m * m)
            upper = Fraction(2 * A, m)
            assert lower <= E <= upper
        results.append({'n': n, 'normalized_matrices': total,
                        'no_collision_count': no_collision, 'collision_probability': str(E),
                        'formula_error': 0,
                        'incorrect_independence_probability': str(independence_prediction),
                        'incorrect_independence_absolute_error': str(abs(E - independence_prediction))})
    return results


def rational_rank(matrix):
    R = [[Fraction(x) for x in row] for row in matrix]
    rank = 0
    for j in range(len(R[0])):
        pivot = next((i for i in range(rank, len(R)) if R[i][j]), None)
        if pivot is None:
            continue
        R[rank], R[pivot] = R[pivot], R[rank]
        v = R[rank][j]
        R[rank] = [x / v for x in R[rank]]
        for i in range(rank + 1, len(R)):
            v = R[i][j]
            if v:
                R[i] = [x - v * y for x, y in zip(R[i], R[rank])]
        rank += 1
    return rank


def counterexample(n):
    T = [[1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
    D = [[0] * (n - 1) for _ in range(n - 1)]
    for i in range(4):
        D[i][:4] = T[i]
    for i in range(4, n - 1):
        D[i][i] = 1
    return [[1] * n] + [[1] + [1 - 2 * v for v in row] for row in D]


def construction_checks():
    results = []
    for n in range(5, 13):
        B = counterexample(n)
        x = [0, 1, -1, -1, 1] + [0] * (n - 5)
        assert all(sum(v * w for v, w in zip(row, x)) == 0 for row in B)
        assert sum(v != 0 for v in x) == 4
        assert rational_rank(B) == n - 1
        minima = []
        for rows in (B, list(zip(*B))):
            minimum = min(2 * min(sum(v != w for v, w in zip(rows[i], rows[j])),
                                  sum(v == w for v, w in zip(rows[i], rows[j])))
                          for i in range(n) for j in range(i))
            assert minimum >= 2
            minima.append(minimum)
        results.append({'n': n, 'exact_rank': n - 1, 'kernel_support': 4,
                        'two_sparse_singular_value_squared': minima, 'all_passed': True})
    save('COUNTEREXAMPLE_N5.json', {'matrix': counterexample(5),
                                 'right_kernel': [0, 1, -1, -1, 1]})
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--inspect-gate', action='store_true')
    args = ap.parse_args()
    gate = fresh_gate()
    if args.inspect_gate:
        print(json.dumps(gate))
        return
    wall, cpu = time.perf_counter(), time.process_time()
    partitions_result, partition_count = original_partition_checks()
    collision_result = exact_collision_checks()
    construction_result = construction_checks()
    t = 0.1
    finite_n1 = math.erf(t / math.sqrt(2))
    limit_law = -math.expm1(-t - t * t / 2)
    receipt = {'command': 'python -X utf8 verify_boundary.py', 'compute_gate': gate,
               'all_checks_passed': True, 'proof_status': 'Exact finite checks only; not a formal proof or independent review.',
               'partition_checks': partitions_result, 'partition_pair_checks': partition_count,
               'collision_checks': collision_result, 'counterexample_checks': construction_result,
               'total_normalized_matrices': sum(r['normalized_matrices'] for r in collision_result),
               'gaussian_finite_law_correction': {'n': 1, 't': t, 'exact_CDF': finite_n1,
                                                 'limiting_CDF': limit_law,
                                                 'absolute_difference': limit_law - finite_n1},
               'elapsed_seconds': time.perf_counter() - wall,
               'cpu_seconds': time.process_time() - cpu}
    save('MEASUREMENTS.json', receipt)
    print(json.dumps({k: receipt[k] for k in ('all_checks_passed', 'partition_pair_checks',
                                            'total_normalized_matrices', 'elapsed_seconds', 'cpu_seconds')}))


if __name__ == '__main__':
    main()
