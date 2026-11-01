#!/usr/bin/env python3
"""B13: exact disjoint-gate B_can recurrences + block-restriction Booleanity checks.

Finite checks are self-checks only.  The analytic statements are proved in REPORT.md.
No truth table larger than four variables is generated for the recursive calibration.
"""
import collections
import hashlib
import itertools
import math
import random
from fractions import Fraction


def phi(x):
    return 0.0 if x <= 0.0 else x * math.log2(1.0 / x)


def V(p):
    return 4.0 * p * (1.0 - p)


def C_and(p, q):
    return (
        phi((1.0 - 2.0 * p * q) ** 2)
        - q * phi((1.0 - 2.0 * p) ** 2)
        - p * phi((1.0 - 2.0 * q) ** 2)
        + q * q * V(p) * math.log2(1.0 / q)
        + p * p * V(q) * math.log2(1.0 / p)
    )


def rec_and(s, t):
    p, I, B, d = s
    q, J, D, e = t
    return (
        p * q,
        q * I + p * J,
        q * B + p * D + C_and(p, q),
        hashlib.sha256(b"A" + d + e).digest(),
    )


def rec_or(s, t):
    p, I, B, d = s
    q, J, D, e = t
    return (
        1.0 - (1.0 - p) * (1.0 - q),
        (1.0 - q) * I + (1.0 - p) * J,
        (1.0 - q) * B + (1.0 - p) * D + C_and(1.0 - p, 1.0 - q),
        hashlib.sha256(b"O" + d + e).digest(),
    )


LEAF = (0.5, 1.0, 0.0, hashlib.sha256(b"x").digest())


def walsh(values):
    N = len(values)
    return [
        Fraction(
            sum(
                values[x] * (-1 if ((S & x).bit_count() & 1) else 1)
                for x in range(N)
            ),
            N,
        )
        for S in range(N)
    ]


def metrics(values):
    coeff = walsh(values)
    N = len(values)
    masses = [a * a for a in coeff]
    p = Fraction(sum(v == -1 for v in values), N)
    I = sum(Fraction(S.bit_count()) * masses[S] for S in range(N))
    B = 0.0
    for A, pa in enumerate(masses):
        if not pa:
            continue
        u = sum(masses[S] for S in range(N) if (S & A) == A)
        B += float(pa) * math.log2(float(u / pa))
    return float(p), float(I), B, coeff, masses


def recurrence_truth_table_test():
    funcs = []
    for mask in range(16):
        vals = [-1 if (mask >> x) & 1 else 1 for x in range(4)]
        if len(set(vals)) > 1:
            funcs.append(vals)
    err = 0.0
    checks = 0
    for va in funcs:
        sa = metrics(va)[:3] + (b"a",)
        for vb in funcs:
            sb = metrics(vb)[:3] + (b"b",)
            for gate in "AO":
                out = []
                for y in range(4):
                    for x in range(4):
                        aa, bb = va[x], vb[y]
                        is_true = (
                            aa == -1 and bb == -1
                            if gate == "A"
                            else aa == -1 or bb == -1
                        )
                        out.append(-1 if is_true else 1)
                direct = metrics(out)[:3]
                rec = (rec_and(sa, sb) if gate == "A" else rec_or(sa, sb))[:3]
                err = max(err, max(abs(direct[i] - rec[i]) for i in range(3)))
                checks += 1
    print("RECURRENCE_CHECKS", checks, "MAXERR", f"{err:.3e}")


def check_block(values):
    _, _, _, coeff, masses = metrics(values)
    N = len(values)
    n = N.bit_length() - 1
    full = N - 1
    count = 0
    for A in range(1, N):
        k = A.bit_count()
        delta = Fraction(1, 2 ** (k - 1))
        u = sum(masses[S] for S in range(N) if (S & A) == A)
        remain = full ^ A
        sub = remain
        while True:
            jj = [r for r in range(n) if (sub >> r) & 1]
            total = Fraction(0)
            for z in range(1 << len(jj)):
                val = Fraction(0)
                D = sub
                while True:
                    parity = sum(
                        1
                        for t, r in enumerate(jj)
                        if ((D >> r) & 1) and ((z >> t) & 1)
                    ) & 1
                    val += coeff[A | D] * (-1 if parity else 1)
                    if D == 0:
                        break
                    D = (D - 1) & sub
                total += abs(val)
            avg = total / Fraction(1 << len(jj))
            assert u >= delta * avg
            count += 1
            if sub == 0:
                break
            sub = (sub - 1) & remain
        for j in range(n):
            bit = 1 << j
            if A & bit:
                continue
            R = sum(
                coeff[C] * coeff[C | bit]
                for C in range(N)
                if (C & A) == A and not (C & bit)
            )
            a, b = coeff[A], coeff[A | bit]
            assert u + 2 * R >= delta * abs(a + b)
            assert u - 2 * R >= delta * abs(a - b)
            count += 2
    return count


def block_test():
    checks = 0
    for mask in range(256):
        vals = [-1 if (mask >> x) & 1 else 1 for x in range(8)]
        checks += check_block(vals)
    rng = random.Random(202609211223)
    for _ in range(200):
        vals = [-1 if rng.getrandbits(1) else 1 for _ in range(16)]
        checks += check_block(vals)
    print("FUNCTIONS", 456, "INEQUALITY_CHECKS", checks, "STATUS PASS")


def recursive_calibration():
    s = LEAF
    rows = []
    best = (-1.0, None)
    for n in range(1, 65):
        if n > 1:
            s = rec_and(s, LEAF)
        r = s[2] / s[1] if s[1] else 0.0
        rows.append((n, r, s[0], s[1]))
        best = max(best, (r, n))
    print("AND_BEST", best)
    print(
        "AND_SELECTED",
        [(n, round(rows[n - 1][1], 12)) for n in [2, 3, 4, 5, 8, 16, 32, 64]],
    )

    states = [LEAF]
    for n in range(2, 19):
        states = [z for s0 in states for z in (rec_and(s0, LEAF), rec_or(s0, LEAF))]
        if n in [4, 8, 12, 16, 18]:
            b = max(states, key=lambda z: z[2] / z[1])
            print(
                "CHAIN",
                n,
                f"{b[2] / b[1]:.12f}",
                f"{b[0]:.12f}",
                f"{b[1]:.12f}",
                b[3].hex()[:16],
            )

    rng = random.Random(20260921)
    pool = [LEAF]
    for level in range(1, 11):
        base = []
        for s0 in pool:
            base.append(s0)
            p, I, B, d = s0
            base.append((1.0 - p, I, B, hashlib.sha256(b"N" + d).digest()))
        pairs = (
            list(itertools.product(base, repeat=2))
            if len(base) <= 60
            else [(rng.choice(base), rng.choice(base)) for _ in range(15000)]
        )
        bins = collections.defaultdict(list)
        for aa, bb in pairs:
            for z in (rec_and(aa, bb), rec_or(aa, bb)):
                if z[1] > 1e-15:
                    bins[min(79, max(0, int(z[0] * 80)))].append(z)
        keep = []
        for vals in bins.values():
            vals.sort(key=lambda z: z[2] / z[1], reverse=True)
            keep += vals[:3]
        keep.sort(key=lambda z: z[2] / z[1], reverse=True)
        pool = keep[:240]
        b = pool[0]
        print(
            "BEAM",
            2**level,
            f"{b[2] / b[1]:.12f}",
            f"{b[0]:.12f}",
            f"{b[1]:.12f}",
            b[3].hex()[:16],
        )
    b = pool[0]
    print("BEAM_1024_FULL_DIGEST", b[3].hex())
    print("BEAM_1024_B", repr(b[2]))

    for m in [3, 5, 9, 31, 101, 501, 1001]:
        r = (m - 1) // 2
        alpha = Fraction(math.comb(2 * r, r), 2 ** (2 * r))
        print("MAJ_CHILD", m, f"{float(m * alpha):.12f}")


if __name__ == "__main__":
    recurrence_truth_table_test()
    recursive_calibration()
    block_test()
