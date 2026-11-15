"""Exact finite checks of the row proof; standard library, no network."""

from fractions import Fraction as F
from itertools import product
from pathlib import Path
import os
import resource
import time

started = time.monotonic()
assert os.environ.get("OMP_NUM_THREADS") == "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
leaves = 8
physical = [1, -1, -1, 1, -1, 1, 1, -1]
# One persistent root-born column Phi=(physical,1), with norm sqrt(2).
# D=2 satisfies the size, private-coordinate and path-count budgets.
rows = [(0, tuple(range(leaves)), [F(1)] * leaves)]
for depth, round_index in [(0, 0), (1, 2), (2, 3)]:
    width = leaves // (2**depth)
    amplitude = F(2 ** (depth // 2))
    for left in range(0, leaves, width):
        support = tuple(range(left, left + width))
        h = [F(0)] * leaves
        for y in support:
            h[y] = amplitude if y < left + width // 2 else -amplitude
        rows.append((round_index, support, h))
assert len(rows) == 8

def integral(values):
    return sum(values, F(0)) / leaves

# Compute the full Gram matrix independently of the stopping construction.
# Haar adjoints h*Phi are orthogonal, with squared norm at most two.
for i, (_, _, a) in enumerate(rows):
    for j, (_, _, b) in enumerate(rows):
        entry = integral([2 * x * y for x, y in zip(a, b)])
        assert entry == 0 if i != j else 0 < entry <= 2
print("Gram matrix: 8 orthogonal rows; joint Bessel norm squared <= 2")

patterns = [tuple(1 if mask & (1 << j) else -1 for j in range(8))
            for mask in range(256)]
patterns += [tuple(0 for _ in rows)]
patterns += [tuple(1 if i == j else 0 for i in range(8)) for j in range(8)]
caps = [1, 2, 4, 32]
thresholds = [F(1, 8), F(1, 2), F(2), F(8)]
checks = 0
saw_branch = saw_omission = saw_overshoot = False
for tests in patterns:
    energy = F(sum(c * c for c in tests))
    g = [[sum((tests[i] * row[2][y] for i, row in enumerate(rows)
               if row[0] == n), F(0)) for y in range(leaves)]
         for n in range(4)]
    for cap, tau in product(caps, thresholds):
        bucket = [1] * leaves
        current = [F(0)] * leaves
        assigned = {}
        history = []
        partial = [F(0)] * leaves
        for n in range(4):
            # Check constancy on every support-partition cell, including
            # the empty round n=1, whose support/observation depth is 1.
            depth = [0, 1, 1, 2][n]
            width = leaves // (2**depth)
            for left in range(0, leaves, width):
                states = {(bucket[y], current[y])
                          for y in range(left, left + width)}
                assert len(states) == 1
            for i, (rn, support, _) in enumerate(rows):
                if rn != n:
                    continue
                b = bucket[support[0]]
                if b <= cap:
                    assigned[i] = b
                elif tests[i]:
                    saw_omission = True
            for y in range(leaves):
                partial[y] += g[n][y]
                if bucket[y] > cap:
                    continue
                current[y] += g[n][y]
                if abs(current[y]) > tau:
                    saw_overshoot |= abs(current[y]) > 2 * tau
                    bucket[y] += 1
                    current[y] = F(0)
            saw_branch |= len(set(bucket)) > 1
            history.append((bucket[:], current[:], partial[:]))
        v = [[sum((tests[i] * rows[i][2][y] for i, b in assigned.items()
                   if b == j), F(0)) for y in range(leaves)]
             for j in range(1, cap + 1)]
        omega = [b == cap + 1 for b in bucket]
        # The original Bessel bound applies to disjoint WHOLE row subsets.
        assert sum(integral([2 * a * a for a in vv]) for vv in v) <= 2 * energy
        omega_measure = F(sum(omega), leaves)
        for y in range(leaves):
            if omega[y]:
                assert all(abs(vv[y]) > tau for vv in v)
            else:
                for buckets, cur, pref in history:
                    completed = sum((v[j][y] for j in range(buckets[y] - 1)), F(0))
                    assert pref[y] == completed + cur[y]
                    assert abs(cur[y]) <= tau
        # This is the manuscript's weaker D^-1=1/2 lower comparison.
        assert omega_measure * cap * tau**2 / 4 <= 2 * energy
        # Check the dyadic-prefix estimate by the direct pointwise maximum.
        maxima_squared = []
        for y in range(leaves):
            value = F(0)
            largest = F(0)
            for vv in v:
                value += vv[y]
                largest = max(largest, 2 * value**2)
            maxima_squared.append(largest)
        binary_levels = 1 + cap.bit_length() - 1
        assert integral(maxima_squared) <= binary_levels**2 * 2 * energy
        checks += 1
assert saw_branch and saw_omission and saw_overshoot
print(f"whole-row assignment, completed buckets, prefix and Bessel checks: {checks}")
print("branch-dependent hits, omitted rows, overshoots and empty rounds exercised")

# Independent Abel checks: direct sum versus summation-by-parts, including
# repeated/skipped reads and absent blocks. All quantities are rational.
reads = [0, 1, 1, 3]
abel_checks = 0
for tests in patterns:
    g = [[sum((tests[i] * row[2][y] for i, row in enumerate(rows)
               if row[0] == n), F(0)) for y in range(leaves)]
         for n in range(4)]
    for schedule, blocks, bound in [
        ([F(0), F(1, 4), F(0), F(1, 4)], [[0, 1, 2, 3]], F(1)),
        ([F(1, 2), F(-1, 2), F(1, 2), F(-1, 2)],
         [[0], [1], [2], [3]], F(1, 2)),
    ]:
        for block in blocks:
            assert max(abs(schedule[s]) for s in block) + sum(
                abs(schedule[b] - schedule[a]) for a, b in zip(block, block[1:])
            ) <= bound
            rounds = [n for n, s in enumerate(reads) if s in block]
            if not rounds:
                continue
            for y in range(leaves):
                # F_s=(schedule[s],0), g_n=g[n][y]*(physical[y],1).
                direct = sum((schedule[reads[n]] * physical[y] * g[n][y]
                              for n in rounds), F(0))
                sums = []
                acc = F(0)
                for n in rounds:
                    acc += g[n][y]
                    sums.append(acc)
                abel = schedule[reads[rounds[-1]]] * physical[y] * sums[-1]
                abel += sum(((schedule[reads[a]] - schedule[reads[b]])
                             * physical[y] * sums[j]
                             for j, (a, b) in enumerate(zip(rounds, rounds[1:]))), F(0))
                assert direct == abel
                assert direct**2 <= bound**2 * max(2 * s**2 for s in sums)
                abel_checks += 1
print(f"Abel identity and block domination checks: {abel_checks}")

# Exact constant identities; the last estimate is checked algebraically
# in PROOF.md by the nonnegative polynomial 30*x+12.
for ld in range(1, 101):
    c_squared = F(64, 9) * (9 + ld**2)
    assert c_squared / 4 == F(16, 9) * (9 + ld**2)
for x in range(1, 101):
    assert 25 * (x + 1)**2 - (9 + (5 * x + 2)**2) == 30 * x + 12
print("maximal-tail coefficient and logarithmic constant identities: passed")

here = Path(__file__).resolve().parent
for name, oldname in [
    ("candidate1-introduction.tex", "candidate1-introduction.tex"),
    ("candidate2-introduction.tex", "candidate2-introduction.tex"),
    ("candidate3-introduction.tex", "candidate3-introduction.tex"),
    ("candidate3-transfer.tex", "candidate3-transfer.tex"),
]:
    prior = Path('~/codex_op_1114r3/briefs/AV_T083/sources')
    assert (here / 'sources' / name).read_text().rstrip() == (prior / oldname).read_text().rstrip()
verification = here / 'VERIFY.md'
if verification.exists():
    text = verification.read_text()
    for n in range(1, 4):
        src = (here / 'sources' / f'candidate{n}-introduction.tex').read_text()
        start = src.index(r'\begin{theorem}\label{thm:main}')
        stop = src.index(r'\end{theorem}', start) + len(r'\end{theorem}')
        assert src[start:stop] in text
    print('three exact main-theorem quotations: passed')
print('four current-source comparisons with round 3: unchanged')
print(f'nice = {os.getpriority(os.PRIO_PROCESS, 0)}')
print(f'peak RSS (macOS bytes) = {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}')
print(f'elapsed seconds = {time.monotonic() - started:.3f}')
