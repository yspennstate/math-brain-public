#!/usr/bin/env python3
from itertools import product, combinations
from fractions import Fraction

def chi(mask, x):
    return -1 if ((mask & x).bit_count() & 1) else 1

def walsh(vals):
    N = len(vals)
    return [Fraction(sum(vals[x] * chi(s, x) for x in range(N)), N)
            for s in range(N)]

def verify(fvals, r, s, Z, m):
    d = r + s
    n = d + m
    N = 1 << n
    vals = [fvals[x & ((1 << r) - 1)] for x in range(N)]
    for z in Z:
        vals[z] *= -1
    assert sum(vals) == 0

    gh = walsh(vals)
    fh = walsh(fvals)
    eps = Fraction(2, 1 << n)

    A = []
    for R in range(1 << d):
        a = 0
        for z in Z:
            x = z & ((1 << r) - 1)
            a += fvals[x] * chi(R, z)
        A.append(a)

    for R in range(1 << d):
        base = fh[R & ((1 << r) - 1)] if (R >> r) == 0 else Fraction(0)
        for V in range(1 << m):
            got = gh[R | (V << d)]
            want = (base if V == 0 else 0) - eps * A[R]
            assert got == want

    q = sum(gh[R | (V << d)] ** 2
            for R in range(1 << d) for V in range(1, 1 << m))
    a2 = sum(a * a for a in A)
    assert a2 == (1 << d) * len(Z)
    q_want = ((1 << m) - 1) * eps * eps * a2
    assert q == q_want

    ideg = sum((R.bit_count() + V.bit_count()) * gh[R | (V << d)] ** 2
               for R in range(1 << d) for V in range(1, 1 << m))
    dA = sum(R.bit_count() * a * a for R, a in enumerate(A))
    i_want = eps * eps * (((1 << m) - 1) * dA
                          + m * (1 << (m - 1)) * a2)
    assert ideg == i_want

def main():
    cases = 0
    patterns = 0
    for r in range(1, 4):
        for fvals in product((-1, 1), repeat=1 << r):
            if sum(fvals) != 0:
                continue
            s = 1
            d = r + s
            pos = [z for z in range(1 << d)
                   if fvals[z & ((1 << r) - 1)] == 1]
            neg = [z for z in range(1 << d)
                   if fvals[z & ((1 << r) - 1)] == -1]

            Zs = [(p, q) for p in pos for q in neg]
            if r <= 2:
                Zs += [pp + qq for pp in combinations(pos, 2)
                                for qq in combinations(neg, 2)]
            else:
                for j, (pp, qq) in enumerate(
                        product(combinations(pos, 2), combinations(neg, 2))):
                    if j >= 40:
                        break
                    Zs.append(pp + qq)

            patterns += len(Zs)
            for Z in Zs:
                for m in (1, 2, 3):
                    verify(fvals, r, s, Z, m)
                    cases += 1

    print("PASS")
    print("exact_small_source_cases", cases)
    print("balanced_flip_patterns", patterns)
    print("checked_r", "1..3")
    print("checked_extra_scaffold_bits", 1)
    print("checked_free_dummy_bits", "1,2,3")

if __name__ == "__main__":
    main()
