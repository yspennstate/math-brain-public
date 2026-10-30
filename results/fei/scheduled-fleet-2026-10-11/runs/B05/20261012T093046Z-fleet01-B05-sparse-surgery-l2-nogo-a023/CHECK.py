#!/usr/bin/env python3
"""Exact local operator certificate and finite Walsh checks for the no-go."""

from fractions import Fraction as F
import math


G = (
    (F(5,16), F(-3,16), F(-3,16), F(3,16)),
    (F(-3,16), F(9,16), F(5,16), F(-9,16)),
    (F(-3,16), F(5,16), F(9,16), F(-9,16)),
    (F(3,16), F(-9,16), F(-9,16), F(13,16)),
)


def quad(c):
    return sum(c[i] * G[i][j] * c[j] for i in range(4) for j in range(4))


def lower_amplification(r):
    s = (r + 2) // 3
    M = 2 ** (r - s)
    A = (F(13,16) ** s) * (F(5,4) ** (r - s))
    # Numerical form of the rigorous reverse-triangle lower bound.
    L = ((math.sqrt(M * float(A)) - math.sqrt((13/16) ** r)) ** 2) / (M - 1)
    return s, M - 1, A, L


def fwht(a):
    a = list(map(float, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x / len(a) for x in a]


def caps(q, k):
    q = q[:]
    for b in range(k):
        bit = 1 << b
        for t in range(1 << k):
            if not t & bit:
                q[t] += q[t | bit]
    return q


def bent(k):
    r = k // 2
    return [(-1.0 if sum(((x>>j)&1)*((x>>(r+j))&1)
                            for j in range(r)) % 2 else 1.0)
            for x in range(1 << k)]


def edit_points(r):
    s = (r + 2) // 3
    pts = []
    for code in range(1 << (r-s)):
        x = 0
        for j in range(r):
            # fixed pairs are state 3; free pairs are state 1 or 3
            left = 1
            right = 1 if j < s else ((code >> (j-s)) & 1)
            x |= left << j
            x |= right << (r+j)
        pts.append(x)
    pts.pop()  # remove the all-state-3 point; count is now odd
    return pts


def direct_amplification(r):
    k = 2*r
    g = bent(k)
    h = g[:]
    pts = edit_points(r)
    for x in pts:
        h[x] *= -1
    a, b = fwht(g), fwht(h)
    rho = [(y-x)/x for x, y in zip(a,b)]
    prho = caps(rho, k)
    # caps() computes sums, convert to upper averages.
    prho = [z * 2 ** (t.bit_count()-k) for t,z in enumerate(prho)]
    n0 = sum(x*x for x in rho) / len(rho)
    n1 = sum(x*x for x in prho) / len(prho)
    return len(pts), n1/n0, max(abs(x) for x in rho)


def main():
    fixed = (F(0),F(0),F(0),F(-1))
    free = (F(0),F(1),F(0),F(-1))
    assert quad(fixed) / sum(x*x for x in fixed) == F(13,16)
    assert quad(free) / sum(x*x for x in free) == F(5,4)

    rows = []
    for r in range(6, 181):
        s,m,A,L = lower_amplification(r)
        assert m % 2 == 1
        assert F(m,2**r) < F(1,2**s)
        rows.append((r,s,m,float(A),L))
    # Exact exponential base is greater than one after cubing blocks.
    assert F(13,16) * F(5,4) ** 2 == F(325,256) > 1
    assert rows[-1][3] > rows[60][3] > rows[0][3]

    direct = []
    for r in range(4,10):
        m,observed,maxrho = direct_amplification(r)
        s,_,A,L = lower_amplification(r)
        assert observed + 1e-11 >= L
        assert maxrho <= 2*m/(2**r) + 1e-12
        direct.append((r,s,m,observed,L,maxrho))

    print("local_gram_fixed=13/16")
    print("local_gram_free_signed_pair=5/4")
    print("three_block_growth=(13/16)*(5/4)^2=325/256>1")
    print("analytic_parameter_rows=175")
    for r in (30,60,90,120,150,180):
        row=rows[r-6]
        print(f"r={r} s={row[1]} m={row[2]} A={row[3]:.8g} L={row[4]:.8g}")
    print("direct_walsh_rows=6")
    for row in direct:
        print("  r=%d s=%d m=%d observed=%.12g lower=%.12g maxrho=%.12g" % row)
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
