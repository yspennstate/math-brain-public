#!/usr/bin/env python3
"""Exact checks for the literature proof and its change of alphabet.

This is a small proof audit, not the distribution/spectrum experiment in steps 2–3.
Run from the task directory: python3 code/audit_literature.py
"""
import os
for variable in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                 "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[variable] = "1"
try:
    if os.getpriority(os.PRIO_PROCESS, 0) < 10:
        os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
except PermissionError:
    raise SystemExit("Cannot ensure nice >= 10; no calculation started")

import itertools
import json
import random
import resource
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from sympy import Matrix

ROOT = Path(__file__).resolve().parents[1]
rng = random.Random(6006)

def bareiss(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign, previous = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = p * a[i][j] - a[i][k] * a[k][j]
                quotient, remainder = divmod(numerator, previous)
                assert remainder == 0
                a[i][j] = quotient
            a[i][k] = 0
        previous = p
    return sign * a[-1][-1]

counts = {}
def checked_det(a):
    answer = bareiss(a)
    # SymPy uses its independent permutation formula on orders <= 3 and its
    # domain elimination method on larger orders.
    assert answer == int(Matrix(a).det(method="domain-ge"))
    return answer

def sign_border(b):
    m = len(b)
    return [[1] * (m + 1)] + [[1] + [1 - 2*x for x in row] for row in b]

count = 0
for m in range(1, 4):
    for bits in itertools.product((0, 1), repeat=m*m):
        b = [list(bits[i*m:(i+1)*m]) for i in range(m)]
        assert checked_det(sign_border(b)) == (-2)**m * checked_det(b)
        count += 1
for m in range(4, 9):
    for _ in range(5):
        b = [[rng.randrange(2) for _ in range(m)] for _ in range(m)]
        assert checked_det(sign_border(b)) == (-2)**m * checked_det(b)
        count += 1
counts["binary_to_sign_border"] = count

# Lemma 6: replace a row w-u-v with three binary rows and two columns.
count = 0
for n in range(1, 7):
    for _ in range(10):
        u, v, w = [[rng.randrange(2) for _ in range(n)] for _ in range(3)]
        c = [[rng.randrange(2) for _ in range(n)] for _ in range(n-1)]
        enlarged = [[1, 0] + u, [0, 1] + v, [1, 1] + w]
        enlarged += [[0, 0] + row for row in c]
        original = [[w[j] - u[j] - v[j] for j in range(n)]] + c
        assert checked_det(enlarged) == checked_det(original)
        count += 1
counts["row_gadget"] = count

# Lemma 7: binary positional representation of a large row.
count = 0
for n in range(1, 5):
    for b in range(1, 6):
        e = [[rng.randrange(-1, 2) for _ in range(n)] for _ in range(b)]
        c = [[rng.randrange(2) for _ in range(n)] for _ in range(n-1)]
        top = []
        for i in range(b):
            row = [int(i == j) - 2*int(i == j+1) for j in range(b-1)]
            top.append(row + e[i])
        enlarged = top + [[0]*(b-1) + row for row in c]
        large_row = [sum(2**(b-1-i) * e[i][j] for i in range(b)) for j in range(n)]
        assert checked_det(enlarged) == checked_det([large_row] + c)
        count += 1
counts["binary_positional_row"] = count

# Lemma 9: the scalar can occupy ANY row/column, via a Schur complement.
# This checks the off-diagonal use in the proof of Theorem 13.
count = 0
for n in range(2, 6):
    for q in range(2, 6):
        m = q-1
        core = [[int(i == j) if i >= j else rng.randrange(2)
                 for j in range(m)] for i in range(m)]
        u, v = [[rng.randrange(2) for _ in range(m)] for _ in range(2)]
        alpha = checked_det([[0] + u] + [[v[i]] + core[i] for i in range(m)])
        for r, s in [(0, n-1), (n-1, 0), (n-1, n-1)]:
            a = [[rng.randrange(-2, 3) for _ in range(n)] for _ in range(n)]
            a[r][s] = alpha
            extended = [row[:] + [0]*m for row in a]
            extended[r][s] = 0
            extended[r][n:] = u
            for i in range(m):
                row = [0]*n + core[i]
                row[s] = v[i]
                extended.append(row)
            assert checked_det(extended) == checked_det(a)
            count += 1
counts["scalar_substitution_including_off_diagonal"] = count

# The signed-base determinant is a^t-1 in the coverage bound, not a^(t-1).
count = 0
for alpha in (-5, -3, 2, 4):
    for t in range(2, 6):
        for _ in range(5):
            eps = [rng.randrange(1-abs(alpha), abs(alpha)) for _ in range(t)]
            d = [eps] + [[alpha*int(j == i-1) + int(j == i)
                          for j in range(t)] for i in range(1, t)]
            assert checked_det(d) == sum(e*(-alpha)**i for i, e in enumerate(eps))
            count += 1
counts["signed_base_determinant"] = count

result = {
    "timestamp": datetime.now(ZoneInfo("Asia/Tbilisi")).isoformat(),
    "seed": 6006,
    "nice": os.getpriority(os.PRIO_PROCESS, 0),
    "threads": 1,
    "counts": counts,
    "all_checks_passed": True,
    "rounding_correction": {
        "example_max_digit_a": 4,
        "printed_floor_log2_a_plus_1": 2,
        "required_bits": 3,
        "explanation": "Use a.bit_length() = ceil(log2(a+1)) for a positive maximum digit."
    },
    "peak_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
}
(ROOT / "data" / "literature_audit_checks.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
