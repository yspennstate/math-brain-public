"""Phase of the dominant saddle term of the biased MAJ coefficient at class (i, j) = (a m, b m), bias P.
Per unit m the exponent is f(z) = (a+b) log(z-1) + (1-a) log((1-P)+Pz) + (1-b+1/m) log(P+(1-P)z) - log z.
Envelope theorem: d(phase)/di = Im[log(z-1) - log((1-P)+Pz)], d(phase)/dj = Im[log(z-1) - log(P+(1-P)z)] at the saddle.
Also checks against the exact coefficients: sign of A(i, j) over a window around the typical class."""
import cmath
import sys
from fractions import Fraction
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from forced_exact import pmul, ppow

P = 0.75
a = b = 0.25


def fp(z):
    return (a + b) / (z - 1) + (1 - a) * P / ((1 - P) + P * z) + (1 - b) * (1 - P) / (P + (1 - P) * z) - 1 / z


def f(z):
    return (a + b) * cmath.log(z - 1) + (1 - a) * cmath.log((1 - P) + P * z) + (1 - b) * cmath.log(P + (1 - P) * z) - cmath.log(z)


def newton(z):
    for _ in range(100):
        h = 1e-7
        d = (fp(z + h) - fp(z - h)) / (2 * h)
        z = z - fp(z) / d
    return z


w = newton(complex(0.33, 0.94))
print("saddle", w, "|w|", abs(w), "|fp|", abs(fp(w)))
print("|exp f|", abs(cmath.exp(f(w))), "phase per m", f(w).imag)
di = (cmath.log(w - 1) - cmath.log((1 - P) + P * w)).imag
dj = (cmath.log(w - 1) - cmath.log(P + (1 - P) * w)).imag
print(f"dtheta/di = {di:.6f} rad ({di / cmath.pi:.6f} pi), dtheta/dj = {dj:.6f} rad ({dj / cmath.pi:.6f} pi)")

# exact sign pattern of A around (m/4, m/4)
k = int(sys.argv[1]) if len(sys.argv) > 1 else 81
m = (k - 1) // 2
Pf = Fraction(3, 4)
u, wd = Pf.numerator, Pf.denominator
X, Y = [wd - u, u], [u, wd - u]
c = m // 4
rows = []
for i in range(c - 4, c + 5):
    row = ""
    for j in range(c - 4, c + 5):
        poly = pmul(pmul(ppow(X, m - i), ppow(Y, m - j + 1)), ppow([-1, 1], i + j))
        maj = Fraction(sum(poly[m + 1:]), wd ** (2 * m - i - j + 1))
        d = (-1) ** j * Pf ** (2 * m - i - j)
        A = -2 * (maj - (1 - Pf) * d) - d
        row += "+" if A > 0 else ("-" if A < 0 else "0")
    rows.append(f"i={i:3d} " + row)
print(f"k={k} m={m}: sign of A(i,j), j = {c - 4}..{c + 4}")
print("\n".join(rows))
