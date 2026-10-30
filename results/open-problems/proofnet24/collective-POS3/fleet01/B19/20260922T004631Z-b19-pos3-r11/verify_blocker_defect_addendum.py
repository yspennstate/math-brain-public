#!/usr/bin/env python3
"""Exhaustive check of the chain-blocker union formula for ordered profiles."""


def local_counts(A, B):
    a0, a1 = A
    b0, b1 = B
    uv = sum(1 for a in range(a0, a1 + 1)
             for b in range(b0, b1 + 1) if a <= b)
    vu = sum(1 for b in range(b0, b1 + 1)
             for a in range(a0, a1 + 1) if b <= a)
    return uv, vu


def blocker_defect(Iu, Iv, L, U):
    lu, ru = Iu
    lv, rv = Iv
    A = range(max(lu, L), min(ru, U) + 1)
    B = range(max(lv, L), min(rv, U) + 1)
    blockers = set(range(lu + 1, lv + 1)) | set(range(ru + 1, rv + 1))
    return sum(1 for a in A for b in B
               if a <= b and any(a < j <= b for j in blockers))


def main():
    checked = 0
    for m in range(1, 9):
        intervals = [(lo, hi) for lo in range(m + 1)
                     for hi in range(lo, m + 1)]
        for Iu in intervals:
            for Iv in intervals:
                if not (Iu[0] <= Iv[0] and Iu[1] <= Iv[1]):
                    continue
                # Overlap is the source-valid case for incomparable u,v.
                if max(Iu[0], Iv[0]) > min(Iu[1], Iv[1]):
                    continue
                for L in range(m + 1):
                    for U in range(L, m + 1):
                        A = (max(Iu[0], L), min(Iu[1], U))
                        B = (max(Iv[0], L), min(Iv[1], U))
                        if A[0] > A[1] or B[0] > B[1]:
                            continue
                        uv, vu = local_counts(A, B)
                        assert uv - vu == blocker_defect(Iu, Iv, L, U)
                        checked += 1
    print(f"ordered_overlapping_contexts={checked}")
    print("POS3_CHAIN_BLOCKER_DEFECT_CHECK_PASS")


if __name__ == "__main__":
    main()
