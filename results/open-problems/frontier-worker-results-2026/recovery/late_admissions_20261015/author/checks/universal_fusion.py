"""Exact small-grid prototype: one physical edge, then unit-strength fusion.

No old certificate or generator is modified. Zero probability observations
are discarded before posterior normalization. Balanced groups use independent
copies of experiment LAWS, never shared random observations.
"""
import ast
import array
import hashlib
import json
import pathlib
import sys
import time
from fractions import Fraction as F
from itertools import product
from quantized_bp import orbits, simplex_split
from ternary_bp_int import NAMES, apply_table

ROOT = pathlib.Path(__file__).resolve().parent


def unit_table(N):
    # Preserve the audited integer cancellation, changing only cache namespace
    # and the necessary zero-likelihood boundary handling at strength one.
    path = ROOT / 'ternary_bp_int.py'
    tree = ast.parse(path.read_text(encoding='utf-8'))
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
              and n.name == 'asymmetric_table')
    source = ast.get_source_segment(path.read_text(encoding='utf-8'), fn)
    assert source.count("ROOT/f'ternary_asymmetric_") == 1
    source = source.replace("ROOT/f'ternary_asymmetric_", "ROOT/f'universal_unit_")
    assert source.count('                assert total > 0') == 1
    source = source.replace('                assert total > 0',
                            '                if total == 0:\n                    continue\n                assert total > 0')
    scope = dict(globals())
    exec(compile(source, str(path) + ':unit-boundary-adaptation', 'exec'), scope)
    return scope['asymmetric_table'](N, F(1))


def reference_pair(N, keys, i, j):
    """Independent all-orientation rational definition; no packed coefficients."""
    _, vertices = orbits(N)
    lookup = {k: n for n, k in enumerate(keys)}
    out = {}
    zeros = 0
    for p, r in product(vertices[i], vertices[j]):
        z = [F(p[a] * r[a], N * N) for a in range(3)]
        den = sum(z)
        if den == 0:
            zeros += 1
            continue
        weight = 3 * den / (len(vertices[i]) * len(vertices[j]))
        for v, w in simplex_split([v / den for v in z], N):
            k = lookup[tuple(sorted(v))]
            out[k] = out.get(k, F(0)) + weight * w
    assert sum(out.values()) == 1
    return out, zeros


def edge_table(N, eta, keys):
    assert 0 <= eta <= 1
    lookup = {k: i for i, k in enumerate(keys)}
    den = 3 * eta.denominator
    rows = []
    for key in keys:
        p = [F(1, 3) + eta * (F(v, N) - F(1, 3)) for v in key]
        row = {}
        for v, w in simplex_split(p, N):
            dest = lookup[tuple(sorted(v))]
            num = w * den
            assert num.denominator == 1 and num >= 0
            row[dest] = row.get(dest, 0) + int(num)
        assert sum(row.values()) == den
        rows.append(row)
    return den, rows


def apply_edge(edge, masses, scale, vertex):
    den, rows = edge
    raw = [0] * len(masses)
    for mass, row in zip(masses, rows):
        for dest, num in row.items():
            raw[dest] += mass * num
    assert sum(raw) == scale * den
    out = [v // den for v in raw]
    lost = scale - sum(out)
    out[vertex] += lost
    return out, lost


def balanced_step(table, edge, masses, scale, degree):
    keys = table[0]
    vertex = keys.index((0, 0, sum(keys[0])))
    child, lost = apply_edge(edge, masses, scale, vertex)
    losses = [lost]
    result = None
    power = child
    remaining = degree
    while remaining:
        if remaining & 1:
            if result is None:
                result = power
            else:
                result, lost = apply_table(table, result, power, scale, False)
                losses.append(lost)
        remaining >>= 1
        if remaining:
            power, lost = apply_table(table, power, power, scale, False)
            losses.append(lost)
    assert sum(result) == scale
    return result, losses


def exact_depth_one(degree, eta):
    """Enumerate labelled leaf counts, not quantized transitions."""
    import math
    result = F(0)
    diag, off = (1 + 2 * eta) / 3, (1 - eta) / 3
    for a in range(degree + 1):
        for b in range(degree - a + 1):
            counts = (a, b, degree - a - b)
            likelihoods = [diag**v * off**(degree-v) for v in counts]
            total = sum(likelihoods)
            if total == 0:
                continue
            multinomial = math.comb(degree, a) * math.comb(degree-a, b)
            result += multinomial * (sum(v*v for v in likelihoods) / total - total/3) / 3
    return result


def signal(keys, masses, N, scale):
    return sum(F(m, scale) * (sum(F(v, N)**2 for v in k)-F(1, 3))
               for k, m in zip(keys, masses))


def validate():
    started = time.monotonic()
    N, scale = 6, 1 << 32
    table = unit_table(N)
    keys, common, ii, jj, offsets, dests, nums = table
    zero_pairs = 0
    references = {}
    for row in range(len(ii)):
        expected, zeros = reference_pair(N, keys, ii[row], jj[row])
        actual = {dests[k]: F(nums[k], common)
                  for k in range(offsets[row], offsets[row+1])}
        assert actual == expected
        references[ii[row], jj[row]] = expected
        zero_pairs += zeros
    assert zero_pairs > 0
    vertex = keys.index((0, 0, N))
    uniform = keys.index((N//3,)*3)
    pure = [0] * len(keys)
    pure[vertex] = scale
    controls = []
    for eta in (F(0), F(1), F(161, 360), F(53, 237)):
        edge = edge_table(N, eta, keys)
        for i, row in enumerate(edge[1]):
            if eta == 1:
                assert row == {i: edge[0]}
            if eta == 0:
                assert row == {uniform: edge[0]}
        for degree in (3, 5, 21):
            masses = pure[:]
            for depth in range(1, 5):
                old = masses[:]
                masses, losses = balanced_step(table, edge, old, scale, degree)
                # Independent rational matrices and explicit group-size recursion.
                child = [F(0)] * len(keys)
                for i, m in enumerate(old):
                    for k, num in edge[1][i].items():
                        child[k] += F(m * num, edge[0] * scale)
                def rounded(law):
                    out = [int(v * scale) for v in law]
                    out[vertex] += scale - sum(out)
                    return [F(v, scale) for v in out]
                child = rounded(child)
                def fusion(left, right):
                    out = [F(0)] * len(keys)
                    for i, x in enumerate(left):
                        for j, y in enumerate(right):
                            if x and y:
                                for k, w in references[i, j].items():
                                    out[k] += x*y*w
                    return rounded(out)
                # Mirror grouping via explicit sizes rather than bitwise loop.
                groups = {1: child}
                for bit in range(1, degree.bit_length()):
                    size = 1 << bit
                    groups[size] = fusion(groups[size//2], groups[size//2])
                selected = [groups[1<<bit] for bit in range(degree.bit_length())
                            if degree & (1<<bit)]
                law = selected[0]
                for group in selected[1:]:
                    law = fusion(law, group)
                assert law == [F(v, scale) for v in masses]
                x = signal(keys, masses, N, scale)
                if depth == 1:
                    exact = exact_depth_one(degree, eta)
                    assert x >= exact
                if eta == 0:
                    assert x == 0
                if eta == 1:
                    assert x == F(2, 3)
            controls.append({'degree': degree, 'eta': str(eta),
                             'depths': 4, 'last_signal': str(x)})
    out = {'status': 'PASS: prototype validation only, no new nonreconstruction theorem',
           'grid': N, 'all_ordered_rows': len(ii),
           'zero_probability_orientations_skipped': zero_pairs,
           'independent_fraction_trajectories': controls,
           'depth_one_multinomial_comparisons': len(controls),
           'source_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
           'seconds': time.monotonic()-started}
    path = ROOT/'universal_fusion_small_validation.json'
    path.write_text(json.dumps(out, indent=2), encoding='utf-8')
    print(json.dumps(out), flush=True)


if __name__ == '__main__':
    if sys.argv[1:] == ['build96']:
        import shutil
        from fourth_polynomial_certificate import memory_check
        memory_check()
        assert shutil.disk_usage(ROOT).free > 2 * 1024**3
        table = unit_table(96)
        keys, common, ii, jj, offsets, dests, nums = table
        selected = sorted(set([0, len(ii)-1, len(ii)//2] +
                              [(k*7919+17) % len(ii) for k in range(28)]))
        for row in selected:
            expected, zeros = reference_pair(96, keys, ii[row], jj[row])
            actual = {dests[k]: F(nums[k], common)
                      for k in range(offsets[row], offsets[row+1])}
            assert actual == expected
        out = {'status': 'PASS: selected rows and all generated row sums',
               'grid': 96, 'ordered_rows': len(ii), 'reference_rows': len(selected),
               'common': common,
               'packed_bytes': sum(v.itemsize*len(v) for v in table[2:])}
        (ROOT/'universal_fusion_N96_validation.json').write_text(
            json.dumps(out, indent=2), encoding='utf-8')
        print(json.dumps(out), flush=True)
    else:
        assert not sys.argv[1:]
        validate()
