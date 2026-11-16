"""Lemma 3.5 of arXiv 2609.26771v2 by enumeration.

B_n = monic polynomials of degree n over F_2 with constant term 1 (bit masks).  For every n <= 18 and every L:
the fraction of P in B_n with deg gcd(P, P*) >= L (gcd in F_2[x]) against 8 * 2^(-L/2), and against the sum
the proof actually reaches, sum_{h >= L} 2^floor(h/2) 2^(1-h).  Also: the gcd is reciprocal with constant term 1,
and the number of monic reciprocal polynomials of degree h with constant term 1 is 2^floor(h/2).
"""


def rev(p, n):
    out = 0
    for i in range(n + 1):
        if p >> i & 1:
            out |= 1 << (n - i)
    return out


def gcd2(a, b):
    while b:
        while a.bit_length() >= b.bit_length():
            a ^= b << (a.bit_length() - b.bit_length())
            if a == 0:
                break
        a, b = b, a
    return a


def main():
    for h in range(1, 13):
        c = 0
        for mid in range(1 << (h - 1)) if h > 1 else [0]:
            r = 1 | (1 << h) | (mid << 1) if h > 1 else 3
            if rev(r, h) == r:
                c += 1
        assert c == 1 << (h // 2), (h, c)
    print("monic reciprocal polynomials of degree h with constant term 1 over F_2: 2^floor(h/2) for h = 1..12", flush=True)
    worst8 = 0.0
    worstsum = 0.0
    for n in range(2, 19):
        total = 1 << (n - 1)
        hist = [0] * (n + 1)
        for mid in range(total):
            p = 1 | (1 << n) | (mid << 1)
            g = gcd2(p, rev(p, n))
            d = g.bit_length() - 1
            assert g & 1 and rev(g, d) == g
            hist[d] += 1
        tail = 0
        line = []
        for L in range(n, 0, -1):
            tail += hist[L]
            frac = tail / total
            bound8 = 8 * 2 ** (-L / 2)
            s = sum(2 ** (h // 2) * 2.0 ** (1 - h) for h in range(L, n + 1))
            assert frac <= s + 1e-12, (n, L, frac, s)
            assert frac <= bound8
            worst8 = max(worst8, frac / bound8)
            worstsum = max(worstsum, frac / s)
            if L in (2, 4, 8, 12):
                line.append("L=%d: %.5f" % (L, frac))
        print("  n = %2d: P(deg gcd >= L)  %s" % (n, "  ".join(reversed(line))), flush=True)
    print("Lemma 3.5 holds for every n <= 18 and every L; largest fraction / (8 * 2^(-L/2)) = %.4f, largest fraction / (sum in the proof) = %.4f" % (worst8, worstsum), flush=True)
    print("all assertions passed")


if __name__ == "__main__":
    main()
