"""Checks of the elementary core of arXiv 2609.26771v2 (Kogler, the Odlyzko-Poonen conjecture), from the statements.

P_n = monic 0-1 polynomials of degree n with constant term 1 (2^(n-1) of them), stored as bit masks.
P* is the reversed polynomial.  [P P*]_(n-k) = r_k(P) = sum_j p_j p_(j+k), the aperiodic autocorrelation.

Part 1  Theorem 1.3 by enumeration: the number of P in P_n having some Q in P_n, Q not P or P*, with
        Q Q* = P P* modulo 4 (and, separately, exactly), against the bound 8 (3/4)^floor((n-1)/4).
Part 2  Proposition 2.1 and the steps of its proof, for all 1 <= d <= e <= 10: a in B_d, b in B_e, P = s(ab),
        Q = s(ab*), m = floor((e-1)/2), D_k = ([P P* - Q Q*]_k / 2) mod 2.
          (a) P P* - Q Q* has even coefficients;
          (b) with a and c = b + b* fixed, D_k depends only on b_1..b_k, and flipping b_k changes D_k by
              lambda_k = [(a + a*) c]_k            (e <= 8);
          (c) P(D_1 = .. = D_m = 0 | a) <= (3/4)^(m-j), j the first index with a_j != a_(d-j);
          (d) P(a != a*, P P* = Q Q* mod 4) <= 2 (3/4)^m.
Part 3  Lemma 3.1 and formula (1.1): for every reducible P in P_n and every monic factorisation P = A B the twin
        A B* is again in P_n; the fraction of reducible P against sqrt(2 / (pi n)).
"""
import math
import sys
import time

import sympy as sp

x = sp.symbols("x")


def rev(p, n):
    out = 0
    for i in range(n + 1):
        if p >> i & 1:
            out |= 1 << (n - i)
    return out


def clmul(a, b):
    out = 0
    i = 0
    while b >> i:
        if b >> i & 1:
            out ^= a << i
        i += 1
    return out


def autocorr(p, n):
    return [(p & (p >> k)).bit_count() for k in range(n + 1)]


def part1(nmax):
    print("Part 1. P in P_n with a twin Q (Q not P, P*) having Q Q* = P P* mod 4, and with an exact twin", flush=True)
    for n in range(2, nmax + 1):
        mod4 = {}
        exact = {}
        top = 1 | (1 << n)
        for mid in range(1 << (n - 1)):
            p = top | (mid << 1)
            r = autocorr(p, n)
            k4 = 0
            for v in r:
                k4 = k4 * 4 + (v & 3)
            mod4.setdefault(k4, []).append(p)
            exact.setdefault(tuple(r), []).append(p)

        def bad(groups):
            c = 0
            for g in groups.values():
                if len(g) == 1:
                    continue
                for p in g:
                    ps = rev(p, n)
                    if any(q != p and q != ps for q in g):
                        c += 1
            return c

        b4 = bad(mod4)
        bx = bad(exact)
        total = 1 << (n - 1)
        bound = 8 * 0.75 ** ((n - 1) // 4)
        assert b4 / total <= bound + 1e-12
        assert bx <= b4
        print("  n = %2d: %7d of %7d mod 4 (fraction %.5f), %6d exact (fraction %.5f); bound %.4f" % (n, b4, total, b4 / total, bx, bx / total, bound), flush=True)


def part2(emax, flip_emax):
    print("Part 2. Proposition 2.1 for 1 <= d <= e <= %d" % emax, flush=True)
    worst = 0.0
    npairs = 0
    nflip = 0
    for e in range(1, emax + 1):
        m = (e - 1) // 2
        Be = [1 | (1 << e) | (mid << 1) for mid in range(1 << (e - 1))] if e > 1 else [3]
        for d in range(1, e + 1):
            n = d + e
            Bd = [1 | (1 << d) | (mid << 1) for mid in range(1 << (d - 1))] if d > 1 else [3]
            count_event = 0
            for a in Bd:
                astar = rev(a, d)
                ra = a ^ astar
                j = None
                for i in range(1, d):
                    if (a >> i & 1) != (a >> (d - i) & 1):
                        j = i
                        break
                zero_first_m = 0
                table = {}
                for b in Be:
                    bstar = rev(b, e)
                    P = clmul(a, b)
                    Q = clmul(a, bstar)
                    rp = autocorr(P, n)
                    rq = autocorr(Q, n)
                    diff = [rp[n - k] - rq[n - k] for k in range(n + 1)]
                    assert all(v % 2 == 0 for v in diff), "odd coefficient in P P* - Q Q*"
                    D = [(v // 2) % 2 for v in diff]
                    table[b] = D
                    npairs += 1
                    if all(D[k] == 0 for k in range(1, m + 1)):
                        zero_first_m += 1
                    if a != astar and all(v % 4 == 0 for v in diff):
                        count_event += 1
                if a != astar:
                    assert j is not None and j <= m
                    assert zero_first_m / len(Be) <= 0.75 ** (m - j) + 1e-12, ("step (c) fails", d, e, a)
                if e <= flip_emax:
                    for b in Be:
                        c = b ^ rev(b, e)
                        lam = clmul(ra, c)
                        for k in range(1, m + 1):
                            b2 = b ^ (1 << k) ^ (1 << (e - k))
                            D, D2 = table[b], table[b2]
                            assert D[1:k] == D2[1:k], ("D_i changes for i < k", d, e, a, b, k)
                            assert (D[k] ^ D2[k]) == (lam >> k & 1), ("flip rule fails", d, e, a, b, k)
                            nflip += 1
            prob = count_event / (len(Bd) * len(Be))
            bound = 2 * 0.75 ** m
            assert prob <= bound + 1e-12, ("Proposition 2.1 fails", d, e, prob, bound)
            worst = max(worst, prob / bound)
        print("  e = %2d done (d = 1..%d)" % (e, e), flush=True)
    print("  %d pairs (a, b): coefficients of P P* - Q Q* always even; step (c) and Proposition 2.1 hold for every (d, e); largest probability / bound = %.4f; flip rule checked %d times" % (npairs, worst, nflip), flush=True)


def to_poly(p):
    return sp.Poly(sum(x ** i for i in range(p.bit_length()) if p >> i & 1), x, domain="ZZ")


def part3(nmax_twin, nmax_frac, budget_s):
    print("Part 3. Reducible P in P_n; twins A B* of every factorisation; fraction against sqrt(2/(pi n))", flush=True)
    t0 = time.time()
    for n in range(2, nmax_frac + 1):
        red = 0
        minus1 = 0
        twins = 0
        top = 1 | (1 << n)
        for mid in range(1 << (n - 1)):
            p = top | (mid << 1)
            ev = sum((-1) ** i for i in range(n + 1) if p >> i & 1)
            if ev == 0:
                minus1 += 1
            P = to_poly(p)
            if n <= nmax_twin:
                _, fl = P.factor_list()
                facs = [f for f, k in fl for _ in range(k)]
                if len(facs) > 1:
                    red += 1
                    seen = set()
                    for mask in range(1, (1 << len(facs)) - 1):
                        A = sp.Poly(1, x, domain="ZZ")
                        B = sp.Poly(1, x, domain="ZZ")
                        for i, f in enumerate(facs):
                            if mask >> i & 1:
                                A = A * f
                            else:
                                B = B * f
                        key = tuple(A.all_coeffs())
                        if key in seen:
                            continue
                        seen.add(key)
                        assert A.LC() == 1 and B.LC() == 1 and A.eval(0) == 1 and B.eval(0) == 1, ("A(0), B(0)", p)
                        Bs = sp.Poly(list(reversed(B.all_coeffs())), x, domain="ZZ")
                        Q = A * Bs
                        co = Q.all_coeffs()
                        assert Q.degree() == n and co[0] == 1 and co[-1] == 1 and all(v in (0, 1) for v in co), ("twin not in P_n", p)
                        twins += 1
            else:
                if ev == 0 or not P.is_irreducible:
                    red += 1
        total = 1 << (n - 1)
        s = math.sqrt(2 / (math.pi * n))
        extra = "; %d twins A B*, all in P_n" % twins if n <= nmax_twin else ""
        print("  n = %2d: reducible %6d of %6d = %.4f; P(-1) = 0 for %.4f; sqrt(2/(pi n)) = %.4f; n * (reducible - sqrt) = %+.3f%s" % (n, red, total, red / total, minus1 / total, s, n * (red / total - s), extra), flush=True)
        if time.time() - t0 > budget_s:
            print("  time budget reached after n = %d" % n, flush=True)
            break


def main():
    part1(int(sys.argv[1]) if len(sys.argv) > 1 else 20)
    part2(10, 8)
    part3(11, int(sys.argv[2]) if len(sys.argv) > 2 else 15, 100)
    print("all assertions passed")


if __name__ == "__main__":
    main()
