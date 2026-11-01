#!/usr/bin/env python3
import csv
import sys
import numpy as np
from scipy.optimize import linear_sum_assignment

N = 11
A = np.array([2*i + 1 - N for i in range(N)], dtype=np.int64)
SRC = np.array([(int(A[r]), int(A[s])) for r in range(N) for s in range(N)], dtype=np.int64)
CELL_RHS = 7 * N * N * (N * N - 1)  # 101640
ID = tuple(range(N))
REV = tuple(range(N-1, -1, -1))

def inv(p):
    q = [0] * N
    for i, x in enumerate(p):
        q[x] = i
    return tuple(q)

def revconj(p):
    return tuple(N - 1 - p[N - 1 - i] for i in range(N))

def canon(p):
    p = tuple(p)
    a = inv(p)
    b = revconj(p)
    c = inv(b)
    return min(p, a, b, c)

def build_canonical(residual_csv):
    reps = set()
    rows = 0
    with open(residual_csv, newline='') as f:
        for row in csv.reader(f):
            if not row:
                continue
            if len(row) != 12:
                raise AssertionError(f'expected 11 permutation entries plus margin, got {len(row)}')
            p = tuple(map(int, row[:11]))
            reps.add(canon(p))
            rows += 1
    if rows != 427007:
        raise AssertionError(rows)
    reps = sorted(reps)
    if len(reps) != 109285:
        raise AssertionError(len(reps))
    return reps

def exact_cell_margin(p):
    # Eleven copies of each target branch enforce exact branch capacity 11.
    targ = np.repeat(
        np.array([(int(A[l]), int(A[p[l]])) for l in range(N)], dtype=np.int64),
        N,
        axis=0,
    )
    weights = SRC @ targ.T
    rr, cc = linear_sum_assignment(weights, maximize=True)

    # Numerical assignment is only a locator. Recompute the returned certificate exactly.
    caps = [0] * N
    W = 0
    for si, cj in zip(rr, cc):
        si = int(si)
        cj = int(cj)
        r, s = divmod(si, N)
        l = cj // N
        caps[l] += 1
        W += int(A[r]) * int(A[l]) + int(A[s]) * int(A[p[l]])
    if caps != [N] * N:
        raise AssertionError(caps)
    return 15 * W - CELL_RHS

def reversal_equal_slab_check():
    d = [2*j - 10 for j in range(11)]
    SD = sum(abs(d[i] - d[j]) for i in range(11) for j in range(i+1, 11))
    if SD != 440:
        raise AssertionError(SD)
    # D=SD/11=40, G=7/15, H=2/3. Multiply Delta/h^2 by 3:
    # 3*(55*7/15 - 40*2/3) = 77-80 = -3.
    delta_times_3 = 77 - 80
    if delta_times_3 != -3:
        raise AssertionError(delta_times_3)
    return SD, delta_times_3

def main():
    if len(sys.argv) not in (2, 4):
        print('usage: phase2.py residual.csv [start end]', file=sys.stderr)
        return 2
    reps = build_canonical(sys.argv[1])
    start, end = (0, len(reps)) if len(sys.argv) == 2 else (int(sys.argv[2]), int(sys.argv[3]))
    if not (0 <= start <= end <= len(reps)):
        raise AssertionError((start, end, len(reps)))

    successes = 0
    failures = []
    min_success = None
    min_success_p = None
    for p in reps[start:end]:
        margin = exact_cell_margin(p)
        if margin >= 0:
            successes += 1
            if min_success is None or margin < min_success:
                min_success = margin
                min_success_p = p
        else:
            failures.append((p, margin))

    SD, delta_times_3 = reversal_equal_slab_check()
    print('canonical_total=', len(reps))
    print('checked_range=', start, end)
    print('successes=', successes)
    print('failures=', failures)
    print('min_success_margin=', min_success)
    print('min_success_perm=', min_success_p)
    print('reversal_SD=', SD)
    print('reversal_Delta_over_h2=', delta_times_3, '/3')

    if start == 0 and end == len(reps):
        expected = {(ID, -720), (REV, -720)}
        if set(failures) != expected:
            raise AssertionError(failures)
        if successes != 109283:
            raise AssertionError(successes)
        if min_success != 0:
            raise AssertionError(min_success)
        print('EXACT S11 N11 PHASE2 PASSED')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
