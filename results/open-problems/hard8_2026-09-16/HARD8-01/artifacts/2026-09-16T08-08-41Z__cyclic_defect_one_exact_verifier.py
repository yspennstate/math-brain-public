#!/usr/bin/env python3
"""Exact finite verifier for HARD8-01 checkpoint 3.

Family A_{n,d} on Z/nZ:
    a(i) = i+1 mod n
    b(0) = d
    b(i) = i for i != 0

This program checks, by exact BFS on subset bitmasks, the formulas proved in
2026-09-16T08-08-41Z__report.md:

* A_{n,d} is synchronizing iff gcd(n,d)=1.
* If gcd(n,d)=1, rt(A_{n,d}) = (n-2)(n-d)+n-1.
* For n>=3 and gcd(n,d)=1, the shortest word synchronizing some
  (n-1)-subset has length (n-3)(n-d)+(n-2).

No SAT/SMT solver, randomized search, floating point, or heuristic is used.
"""

from collections import deque
from math import gcd


def apply_subset(mask: int, n: int, d: int, letter: str) -> int:
    """Apply one automaton letter to a subset encoded as a bitmask."""
    if letter == "a":
        full = (1 << n) - 1
        return ((mask << 1) & full) | ((mask >> (n - 1)) & 1)
    if letter != "b":
        raise ValueError(letter)

    # b fixes every state except 0, which is mapped to d.
    out = mask & ~1
    if mask & 1:
        out |= 1 << d
    return out


def exact_reset_threshold(n: int, d: int):
    """Return (distance, shortest_word), or (None, None) if not synchronizing."""
    full = (1 << n) - 1
    q = deque([full])
    dist = {full: 0}
    parent = {}

    while q:
        mask = q.popleft()
        if mask and (mask & (mask - 1)) == 0:
            word = []
            cur = mask
            while cur != full:
                prev, letter = parent[cur]
                word.append(letter)
                cur = prev
            return dist[mask], "".join(reversed(word))

        for letter in ("a", "b"):
            nxt = apply_subset(mask, n, d, letter)
            if nxt not in dist:
                dist[nxt] = dist[mask] + 1
                parent[nxt] = (mask, letter)
                q.append(nxt)

    return None, None


def exact_best_nminus1_threshold(n: int, d: int):
    """Minimum synchronization length over all subsets of cardinality n-1."""
    full = (1 << n) - 1
    starts = [full ^ (1 << missing) for missing in range(n)]

    q = deque(starts)
    dist = {mask: 0 for mask in starts}

    while q:
        mask = q.popleft()
        if mask and (mask & (mask - 1)) == 0:
            return dist[mask]
        for letter in ("a", "b"):
            nxt = apply_subset(mask, n, d, letter)
            if nxt not in dist:
                dist[nxt] = dist[mask] + 1
                q.append(nxt)

    return None


def explicit_reset_word(n: int, d: int) -> str:
    return "b" + ("a" * (n - d) + "b") * (n - 2)


def run(max_n: int = 13) -> None:
    reset_checks = 0
    nonsync_checks = 0
    subset_checks = 0

    for n in range(2, max_n + 1):
        full = (1 << n) - 1
        for d in range(1, n):
            rt, shortest = exact_reset_threshold(n, d)

            if gcd(n, d) == 1:
                expected_rt = (n - 2) * (n - d) + n - 1
                assert rt == expected_rt, (n, d, rt, expected_rt, shortest)

                witness = explicit_reset_word(n, d)
                image = full
                for letter in witness:
                    image = apply_subset(image, n, d, letter)
                assert image and (image & (image - 1)) == 0
                assert len(witness) == expected_rt
                reset_checks += 1

                if n >= 3:
                    expected_subset = (n - 3) * (n - d) + (n - 2)
                    exact_subset = exact_best_nminus1_threshold(n, d)
                    assert exact_subset == expected_subset, (
                        n,
                        d,
                        exact_subset,
                        expected_subset,
                    )
                    subset_checks += 1
            else:
                assert rt is None, (n, d, rt, shortest)
                nonsync_checks += 1

    print(f"verified n=2..{max_n}")
    print(f"coprime exact reset-threshold cases: {reset_checks}")
    print(f"non-coprime nonsynchronizing cases: {nonsync_checks}")
    print(f"coprime exact (n-1)-subset cases: {subset_checks}")
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    run()
