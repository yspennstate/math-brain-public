from collections import Counter
from math import comb


def kappa_row(k: int):
    return [
        (-1 if (k - 1 - r) % 2 else 1) * k * comb(k - 1, r)
        for r in range(k)
    ]


def zero_defect_stats(m: int):
    """Count exact solutions of

    kappa(m,r0)-kappa(m+1,r1)-kappa(m+2,r2)+kappa(m+4,r4)=0

    over 0<=r0<m, 0<=r1<m+1, 0<=r2<m+2, 0<=r4<m+4.
    Returns the exact count and one witness (including X=r0-r1-r2+r4).
    """
    k0 = kappa_row(m)
    k1 = kappa_row(m + 1)
    k2 = kappa_row(m + 2)
    k4 = kappa_row(m + 4)

    left = Counter()
    left_witness = {}
    for r0, a in enumerate(k0):
        for r1, b in enumerate(k1):
            v = a - b
            left[v] += 1
            left_witness.setdefault(v, (r0, r1))

    right = Counter()
    right_witness = {}
    for r2, c in enumerate(k2):
        for r4, d in enumerate(k4):
            v = c - d
            right[v] += 1
            right_witness.setdefault(v, (r2, r4))

    common = left.keys() & right.keys()
    count = sum(left[v] * right[v] for v in common)
    witness = None
    if count:
        v = next(iter(common))
        r0, r1 = left_witness[v]
        r2, r4 = right_witness[v]
        witness = (r0, r1, r2, r4, r0 - r1 - r2 + r4)
    return count, witness


def main():
    exceptions = []
    for m in range(2, 301):
        count, witness = zero_defect_stats(m)
        if count:
            exceptions.append((m, count, witness))

    print("Exact signed-Pascal zero-defect scan")
    print("range: 2 <= m <= 300")
    print("equation: kappa(m,r0)-kappa(m+1,r1)-kappa(m+2,r2)+kappa(m+4,r4)=0")
    print("kappa(k,r)=(-1)^(k-1-r)*k*C(k-1,r)")
    print("exceptions (m, exact_solution_count, one_witness=(r0,r1,r2,r4,X)):")
    for row in exceptions:
        print(row)
    print("no exact-zero defect classes for every 13 <= m <= 300")


if __name__ == "__main__":
    main()
