# Exact finite check for R7-06 / G0001, run 2026-09-18.
# Enumerates rooted nearest-neighbour site animals of sizes 1,2,3 in Z^d
# and records external vertex-boundary sizes. No random/numerical approximation.

from itertools import combinations, product


def neighbors(x):
    d = len(x)
    for i in range(d):
        for s in (-1, 1):
            y = list(x)
            y[i] += s
            yield tuple(y)


def connected(A):
    A = set(A)
    seen = {next(iter(A))}
    stack = list(seen)
    while stack:
        x = stack.pop()
        for y in neighbors(x):
            if y in A and y not in seen:
                seen.add(y)
                stack.append(y)
    return len(seen) == len(A)


def boundary(A):
    A = set(A)
    return {y for x in A for y in neighbors(x) if y not in A}


def animals(d, k):
    zero = (0,) * d
    candidates = []
    for x in product(range(-(k - 1), k), repeat=d):
        if x != zero and sum(abs(a) for a in x) <= k - 1:
            candidates.append(x)
    ans = set()
    for comb in combinations(candidates, k - 1):
        A = frozenset((zero,) + comb)
        if connected(A):
            ans.add(A)
    return ans


for d in range(3, 11):
    print(f"d={d}")
    for k in (1, 2, 3):
        hist = {}
        A = animals(d, k)
        for a in A:
            m = len(boundary(a))
            hist[m] = hist.get(m, 0) + 1
        print(f"  k={k}: total={len(A)}, boundary_hist={dict(sorted(hist.items()))}")

# Expected closed forms:
# k=1: total 1, boundary 2d.
# k=2: total 2d, boundary 4d-2.
# k=3: 3d straight animals with boundary 6d-4 and
#      6d(d-1) bent animals with boundary 6d-5.
