"""Exact finite checks and arithmetic certificates for PROOF.md.

No finite computation is used to infer the infinite conclusion. The stage
certificates evaluate proven bounds without constructing exponential trees.
"""
import csv
import itertools
import math
import os
from pathlib import Path
from fractions import Fraction as F
import resource
import signal
import time

os.environ["OMP_NUM_THREADS"] = "1"
signal.alarm(120)
started = time.monotonic()


def backward(bs, p):
    ts = [F(0)] * (len(bs) + 1)
    ts[-1] = F(1)
    for i in range(len(bs) - 1, -1, -1):
        ts[i] = 1 - (1 - p * ts[i + 1]) ** bs[i]
    return ts


def forward_distribution(bs, p):
    dist = {1: F(1)}
    for b in bs:
        nxt = {}
        for z, mass in dist.items():
            trials = b * z
            for h in range(trials + 1):
                prob = F(math.comb(trials, h)) * p**h * (1-p)**(trials-h)
                nxt[h] = nxt.get(h, F(0)) + mass * prob
        dist = nxt
    return dist


pattern_checks = 0
half_checks = 0
for length in range(1, 7):
    for bs in itertools.product((1, 2), repeat=length):
        for p in (F(1, 3), F(1, 2), F(2, 3)):
            ts = backward(bs, p)
            dist = forward_distribution(bs, p)
            assert sum(dist.values()) == 1
            assert ts[0] == 1 - dist.get(0, F(0))
            means = [F(1)]
            for b in bs:
                means.append(means[-1] * b * p)
            ez = sum(z * w for z, w in dist.items())
            ez2 = sum(z*z*w for z, w in dist.items())
            assert ez == means[-1]
            assert ez2 / ez**2 == 1 + (1-p) * sum(1/m for m in means[1:])
            assert ts[0] >= ez**2 / ez2
            pattern_checks += 1
            if p == F(1, 2):
                reciprocal = 1 / means[-1]
                for i, b in enumerate(bs):
                    if b == 2:
                        c = 1 / (4 * (1 - ts[i+1]/4))
                        assert F(1, 4) <= c <= F(1, 3)
                        reciprocal += c / means[i]
                assert reciprocal == 1 / ts[0]
                assert ts[0] >= means[-1] / (length + 1)
                trailing = 0
                for b in reversed(bs):
                    if b != 2:
                        break
                    trailing += 1
                if trailing:
                    assert ts[0] <= 4 * means[-1] / (trailing + 4)
                half_checks += 1
print(f"PASS: {pattern_checks} exact forward-distribution/backward-recursion comparisons")
print(f"PASS: {pattern_checks} exact second-moment identities and survival lower bounds")
print(f"PASS: {half_checks} reciprocal identities, critical bounds, and available plateau bounds")


def finite_two_branch_tree(a_bs, b_bs):
    parents = [-1, 0, 0]
    depths = [0, 1, 1]
    for root, bs in ((1, a_bs), (2, b_bs)):
        level = [root]
        for b in bs:
            nxt = []
            for v in level:
                for _ in range(b):
                    nxt.append(len(parents))
                    parents.append(v)
                    depths.append(depths[v] + 1)
            level = nxt
    return parents, depths


root_checks = 0
configurations = 0
for a_bs in itertools.product((1, 2), repeat=2):
    for b_bs in itertools.product((1, 2), repeat=2):
        parents, depths = finite_two_branch_tree(a_bs, b_bs)
        edges = len(parents) - 1
        boundary = [i for i, d in enumerate(depths) if d == 3]
        event_count = edge_event_count = 0
        for mask in range(1 << edges):
            reached = [True] + [False] * edges
            for v in range(1, len(parents)):
                reached[v] = reached[parents[v]] and bool(mask & (1 << (v-1)))
            if any(reached[v] for v in boundary):
                event_count += 1
                edge_event_count += bool(mask & 1)
        u = backward(a_bs, F(1, 2))[0] / 2
        v = backward(b_bs, F(1, 2))[0] / 2
        expected = 1 - (v/2)/(u+v-u*v)
        assert F(edge_event_count, event_count) == expected
        assert F(event_count, 1 << edges) == u+v-u*v
        configurations += 1 << edges
        root_checks += 1
print(f"PASS: {root_checks} fixed-edge formulas by exhaustive enumeration of {configurations} configurations")

rows = []
da = db = 0
sum_a = sum_b = 0
previous_n = 0
for k in range(1, 33):
    n = 1 << (k*k + 10)
    for _ in range(2*k - 1):
        if k % 2:
            da += 1
        else:
            db += 1
        sum_a += 1 << da
        sum_b += 1 << db
    plateau = n - previous_n - (2*k - 1)
    sum_a += plateau * (1 << da)
    sum_b += plateau * (1 << db)
    assert plateau >= F(n, 2)
    assert da + db == k*k
    assert da-db == (-1)**(k+1) * k
    assert da == (k*k + (-1)**(k+1)*k)//2
    assert db == (k*k - (-1)**(k+1)*k)//2
    lower_a = 1 / (1 + F(sum_a, 2))
    lower_b = 1 / (1 + F(sum_b, 2))
    upper_a = F(4, (1 << da) * (plateau+4))
    upper_b = F(4, (1 << db) * (plateau+4))
    rho = upper_a/lower_b if k % 2 else upper_b/lower_a
    assert rho <= F(16, 1 << k)
    if k % 2:
        h_lower = F(1, 2)
        h_upper = min(F(1), F(1, 2) + rho/2)
    else:
        h_lower = max(F(1, 2), 1-rho/2)
        h_upper = F(1)
    rows.append(dict(k=k, N_k=n, D_A=da, D_B=db, binary_plateau=plateau,
                     weaker_branch="A" if k % 2 else "B",
                     survival_ratio_upper=str(rho), H_lower=str(h_lower), H_upper=str(h_upper)))
    previous_n = n
with Path("stage_certificates.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
print("PASS: 32 stage counts, final-plateau inequalities, and exact ratio certificates")
print("Certificates are bounds from the proof, not simulated survival probabilities.")
print("k  D_A  D_B  weaker  certified interval for P(e_A open | reach N_k+1)")
for row in rows:
    if row["k"] in (1, 2, 8, 9, 16, 17, 32):
        print(f'{row["k"]:2d} {row["D_A"]:4d} {row["D_B"]:4d} '
              f'{row["weaker_branch"]:>6}  '
              f'[{float(F(row["H_lower"])):.12f}, {float(F(row["H_upper"])):.12f}]')
print(f"Priority: {os.getpriority(os.PRIO_PROCESS, 0)}; OMP_NUM_THREADS={os.environ['OMP_NUM_THREADS']}")
print(f"Elapsed seconds: {time.monotonic()-started:.3f}")
print(f"Peak RSS bytes (macOS): {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}")
print("PASS: all exact checks")
