#!/usr/bin/env python3
"""Exact depth-3 endpoint-state enumeration for D0067 square-lattice SAW.

We fix the first step to (1,0); by fourfold rotational symmetry, unrestricted
counts are four times the totals below.

H0: the first three edges traverse three sides of a unit square, equivalently
    omega_3 is a nearest neighbour of omega_0.
H+: the last three edges traverse three sides of a unit square, equivalently
    omega_{n-3} is a nearest neighbour of omega_n.
O+: the last two edges turn 90 degrees and the fourth corner of that unit
    square has not been visited. Then there is exactly one legal child
    extension that has H+.

The deletion/addition bijection predicts
    #(n-step walks with H0 and O+) = #((n+1)-step walks with H0 and H+).
This script checks it by exact DFS through n=16.
"""
from collections import defaultdict
from fractions import Fraction

NMAX = 16
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def start_hook(path):
    return len(path) >= 4 and manhattan(path[0], path[3]) == 1

def terminal_hook(path):
    return len(path) >= 4 and manhattan(path[-1], path[-4]) == 1

def terminal_open_corner(path, seen):
    if len(path) < 3:
        return False
    a, b, c = path[-3], path[-2], path[-1]
    u, v = sub(b, a), sub(c, b)
    if u[0] * v[0] + u[1] * v[1] != 0:
        return False
    fourth = add(a, v)  # also c-u
    return fourth not in seen

def terminal_category(path, seen):
    if len(path) < 3:
        return "short"
    a, b, c = path[-3], path[-2], path[-1]
    u, v = sub(b, a), sub(c, b)
    if u[0] * v[0] + u[1] * v[1] != 0:
        return "straight"
    fourth = add(a, v)
    if fourth not in seen:
        return "open"
    if len(path) >= 4 and fourth == path[-4]:
        return "hook"
    return "remote_blocked"

total = defaultdict(int)
hh = defaultdict(int)
ho = defaultdict(int)
category = {n: defaultdict(int) for n in range(1, NMAX + 1)}

path = [(0, 0), (1, 0)]
seen = set(path)
total[1] = 1

def dfs():
    n = len(path) - 1
    if n >= 3 and start_hook(path):
        if terminal_hook(path):
            hh[n] += 1
        if terminal_open_corner(path, seen):
            ho[n] += 1
        category[n][terminal_category(path, seen)] += 1

    if n == NMAX:
        return

    x = path[-1]
    for d in DIRS:
        y = add(x, d)
        if y in seen:
            continue
        seen.add(y)
        path.append(y)
        total[n + 1] += 1
        dfs()
        path.pop()
        seen.remove(y)

dfs()

print("D0067 depth-3 endpoint-state exact enumeration")
print("Convention: first step fixed east; multiply TOTAL, HH, HO by 4 for unrestricted oriented starts.")
print("HH = start depth-3 hook AND terminal depth-3 hook.")
print("HO = start depth-3 hook AND terminal open corner (unique legal hook-closing child).")
print()
print("n TOTAL HH HO HH/TOTAL")
for n in range(3, NMAX + 1):
    print(f"{n:2d} {total[n]:7d} {hh[n]:6d} {ho[n]:6d} {Fraction(hh[n], total[n])}")

print()
print("Bijection checks HO[n] == HH[n+1]:")
ok = True
for n in range(3, NMAX):
    passed = ho[n] == hh[n + 1]
    ok &= passed
    print(f"n={n:2d}: {ho[n]} == {hh[n+1]} : {'PASS' if passed else 'FAIL'}")

print()
print("Start-hook terminal-category counts (among first-step-east SAWs):")
print("n straight open hook remote_blocked")
for n in range(3, NMAX):
    c = category[n]
    print(f"{n:2d} {c['straight']:8d} {c['open']:8d} {c['hook']:8d} {c['remote_blocked']:14d}")

if not ok:
    raise SystemExit("BIJECTION CHECK FAILED")
print()
print("ALL_EXACT_CHECKS_PASS")
