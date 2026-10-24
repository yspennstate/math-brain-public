#!/usr/bin/env python3
"""Rational-log interval certificate for J_A > M_A on biased two-bit AND."""

from fractions import Fraction


def ln_interval(x, terms=1200):
    """Return rational lower/upper bounds for ln(x), x>0, by atanh series."""
    if x == 1:
        return Fraction(0), Fraction(0)
    if x < 1:
        lo, hi = ln_interval(1/x, terms)
        return -hi, -lo
    z = (x - 1) / (x + 1)
    s = sum(z ** (2*k + 1) / (2*k + 1) for k in range(terms)) * 2
    rem = 2 * z ** (2*terms + 1) / ((2*terms + 1) * (1-z*z))
    return s, s + rem


LN2_LO, LN2_HI = ln_interval(Fraction(2))


def log2_interval(x):
    lo, hi = ln_interval(x)
    return lo / LN2_HI, hi / LN2_LO


def entropy_interval(probs):
    lo = hi = Fraction(0)
    for p in probs:
        if not p:
            continue
        l, u = log2_interval(p)
        lo -= p*u
        hi -= p*l
    return lo, hi


def sub(a, b):
    return a[0]-b[1], a[1]-b[0]


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def scale(c, a):
    return c*a[0], c*a[1]


def decimal_bounds(a, digits=18):
    scale10 = 10**digits
    lo = a[0].numerator * scale10 // a[0].denominator
    hi = -((-a[1].numerator * scale10) // a[1].denominator)
    return f"{lo//scale10}.{lo%scale10:0{digits}d}", f"{hi//scale10}.{hi%scale10:0{digits}d}"


def main():
    # g(x,y)=(-1)^(xy), P[x=1]=1/8, P[y=1]=1/4.
    # Its biased squared Fourier masses are exactly (225,7,3,21)/256.
    H = entropy_interval([Fraction(225,256), Fraction(7,256), Fraction(3,256), Fraction(21,256)])
    h_r = entropy_interval([Fraction(3,32), Fraction(29,32)])
    h_child = entropy_interval([Fraction(3,4), Fraction(1,4)])
    M = sub(H, h_r)
    J = sub(h_r, scale(Fraction(1,8), h_child))
    gap = sub(J, M)
    assert gap[0] > Fraction(1195,10000)  # rigorous J-M > 0.1195 bits
    print("status: PASS")
    print("randomness: NONE")
    print("p=1/8 q=1/4")
    print("squared biased Fourier masses: 225/256, 7/256, 3/256, 21/256")
    print("M interval:", decimal_bounds(M))
    print("J interval:", decimal_bounds(J))
    print("J-M interval:", decimal_bounds(gap))
    print("certified: J-M > 0.1195 bits")


if __name__ == "__main__":
    main()
