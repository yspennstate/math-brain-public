"""Exact verifier for HARD8-04 low-order quotient theorems.

Standard-library only.  No floating point, randomness, external solver, or
nonexistence inference from timeouts.

It verifies the quotient-autocorrelation certificates constructed in the
2026-09-16T11-18-30Z report for d=2,3,4.  The verified objects are quotient
occupancy vectors, not the original binary cyclic difference families.
"""

from math import isqrt


MAX_V = 4000


SMALL_D4 = {
    1: [(1, 0, 0, 0), (1, 1, 0, 0), (1, 1, 0, 0), (1, 0, 1, 0)],
    2: [(3, 0, 0, 0), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1)],
    3: [(3, 2, 0, 0), (2, 1, 2, 1), (2, 1, 2, 1), (2, 1, 2, 1)],
    4: [(4, 2, 1, 0), (3, 2, 2, 1), (3, 2, 2, 1), (2, 2, 2, 2)],
    5: [(4, 3, 2, 0), (4, 3, 2, 1), (3, 2, 3, 2), (3, 2, 3, 2)],
    6: [(6, 3, 2, 0), (3, 3, 3, 3), (3, 3, 3, 3), (3, 3, 3, 3)],
    7: [(7, 2, 2, 2), (4, 4, 3, 3), (4, 4, 3, 3), (4, 3, 4, 3)],
    8: [(6, 5, 4, 0), (5, 4, 4, 3), (5, 4, 4, 3), (4, 4, 4, 4)],
}


def three_squares(n):
    """Return a,b,c >= 0 with a^2+b^2+c^2=n, or None."""
    if n < 0:
        return None
    for a in range(isqrt(n) + 1):
        rem = n - a * a
        for b in range(isqrt(rem) + 1):
            c2 = rem - b * b
            c = isqrt(c2)
            if c * c == c2:
                return a, b, c
    return None


def four_squares(n):
    """Return a,b,c,d >= 0 with sum of squares n."""
    for a in range(isqrt(n) + 1):
        rep = three_squares(n - a * a)
        if rep is not None:
            return (a,) + rep
    raise AssertionError(("four-square search failed", n))


def autocorr(vec, shift):
    d = len(vec)
    return sum(vec[r] * vec[(r + shift) % d] for r in range(d))


def verify_quotient(v, d, occ):
    """Verify the complete projected autocorrelation system exactly."""
    assert v % d == 0
    h = v // d
    wanted_sizes = [v // 2 - 1, v // 2, v // 2, v // 2]
    assert len(occ) == 4
    assert [sum(x) for x in occ] == wanted_sizes
    assert all(len(x) == d and min(x) >= 0 for x in occ)

    for shift in range(d):
        got = sum(autocorr(x, shift) for x in occ)
        want = h * (v - 2) + (v + 1 if shift == 0 else 0)
        assert got == want, (v, d, shift, got, want, occ)


def construct_d2(v):
    assert v % 2 == 0
    q = v // 2
    values = list(four_squares(2 * q + 1))

    # Modulo four, the parity pattern is forced: exactly one odd square when
    # q is even and exactly three odd squares when q is odd.  Put the unique
    # coordinate of parity q-1 into the smaller block.
    idx = next(i for i, x in enumerate(values) if x % 2 == (q - 1) % 2)
    e1 = values.pop(idx)
    assert all(x % 2 == q % 2 for x in values)
    es = [e1] + values
    sizes = [q - 1, q, q, q]

    # For q>=4 every four-square coordinate is <=sqrt(2q+1)<=q-1.
    # If a brute representation chosen above is awkward in a tiny case,
    # find a bounded representation exhaustively.  This branch is exact.
    if any(abs(e) > k for e, k in zip(es, sizes)):
        found = None
        lim = isqrt(2 * q + 1)
        for a in range(lim + 1):
            for b in range(lim + 1):
                for c in range(lim + 1):
                    rem = 2 * q + 1 - a * a - b * b - c * c
                    if rem < 0:
                        continue
                    d = isqrt(rem)
                    if d * d != rem:
                        continue
                    rr = [a, b, c, d]
                    for j in range(4):
                        cand = [rr[j]] + rr[:j] + rr[j + 1 :]
                        if (
                            cand[0] % 2 == (q - 1) % 2
                            and all(x % 2 == q % 2 for x in cand[1:])
                            and all(x <= k for x, k in zip(cand, sizes))
                        ):
                            found = cand
                            break
                    if found is not None:
                        break
                if found is not None:
                    break
            if found is not None:
                break
        assert found is not None
        es = found

    assert sum(e * e for e in es) == 2 * q + 1
    occ = []
    for k, e in zip(sizes, es):
        assert (k + e) % 2 == 0
        occ.append(((k + e) // 2, (k - e) // 2))
    verify_quotient(v, 2, occ)
    return occ


def construct_d3(v):
    assert v % 6 == 0
    s = v // 6

    choice = None
    for j in (0, 1, 2):
        rep = three_squares(2 * s - j)
        if rep is not None and not (j == 2 and s < 2):
            choice = j, rep
            break
    assert choice is not None
    j, (a, b, c) = choice

    if j == 0:
        n1 = (s, s, s - 1)       # Eisenstein norm 1
    elif j == 1:
        n1 = (s + 1, s - 1, s - 1)  # norm 4
    else:
        n1 = (s + 1, s - 2, s)   # norm 7

    occ = [
        n1,
        (s + a, s - a, s),
        (s + b, s - b, s),
        (s + c, s - c, s),
    ]
    verify_quotient(v, 3, occ)
    return occ


def inverse_d4(k, u, p, q):
    nums = (k + u + 2 * p, k - u + 2 * q, k + u - 2 * p, k - u - 2 * q)
    assert all(x % 4 == 0 for x in nums), (k, u, p, q, nums)
    return tuple(x // 4 for x in nums)


def construct_d4(v):
    assert v % 4 == 0
    s = v // 4

    if s <= 8:
        occ = SMALL_D4[s]
        verify_quotient(v, 4, occ)
        return occ

    # Order-two Fourier coordinates.
    abc = three_squares(s)
    if abc is not None:
        u1 = 1
    else:
        abc = three_squares(s - 2)
        assert abc is not None
        u1 = 3
    us = [u1] + [2 * x for x in abc]
    sizes = [2 * s - 1, 2 * s, 2 * s, 2 * s]
    assert sum(u * u for u in us) == 4 * s + 1

    # Forced parities of the real and imaginary parts of the order-four
    # Fourier coordinates.
    parity = []
    for k, u in zip(sizes, us):
        parity.extend([((k + u) // 2) % 2, ((k - u) // 2) % 2])
    assert sum(parity) in (1, 5), (s, abc, us, parity)

    vals = [None] * 8
    odd_slots = [i for i, bit in enumerate(parity) if bit]
    even_slots = [i for i, bit in enumerate(parity) if not bit]

    if len(odd_slots) == 1:
        vals[odd_slots[0]] = 1
        rep4 = four_squares(s)
        for idx, x in zip(even_slots[:4], rep4):
            vals[idx] = 2 * x
        for idx in even_slots[4:]:
            vals[idx] = 0
    else:
        assert len(odd_slots) == 5 and len(even_slots) == 3
        for idx in odd_slots:
            vals[idx] = 1
        rep3 = three_squares(s - 1)
        if rep3 is None:
            rep3 = three_squares(s - 3)
            assert rep3 is not None
            vals[odd_slots[0]] = 3
        for idx, x in zip(even_slots, rep3):
            vals[idx] = 2 * x

    assert sum(x * x for x in vals) == 4 * s + 1

    occ = []
    for i, (k, u) in enumerate(zip(sizes, us)):
        p, q = vals[2 * i], vals[2 * i + 1]
        row = inverse_d4(k, u, p, q)
        assert min(row) >= 0, (v, i, k, u, p, q, row)
        occ.append(row)

    verify_quotient(v, 4, occ)
    return occ


def verify_number_theory_escape(limit):
    """Finite consistency checks of the two elementary escape lemmas."""
    for n in range(limit + 1):
        if n >= 2:
            assert three_squares(n) is not None or three_squares(n - 2) is not None
        assert any(three_squares(n + j) is not None for j in range(3))


def main():
    verify_number_theory_escape(MAX_V)
    d2 = d3 = d4 = 0
    for v in range(2, MAX_V + 1, 2):
        construct_d2(v)
        d2 += 1
        if v % 6 == 0:
            construct_d3(v)
            d3 += 1
        if v % 4 == 0:
            construct_d4(v)
            d4 += 1

    print(f"exact d=2 quotient certificates: {d2}")
    print(f"exact d=3 quotient certificates: {d3}")
    print(f"exact d=4 quotient certificates: {d4}")
    print(f"all quotient autocorrelation identities verified for even v <= {MAX_V}")
    print("ALL EXACT LOW-ORDER QUOTIENT CHECKS PASSED")


if __name__ == "__main__":
    main()
