"""Exhaust AG10 Prop 5.10: two divisorial ends and one divisorial end. Prints the solutions found."""
from math import isqrt

print("two divisorial ends, D >= 3:")
for D in range(3, 9):
    for e in range(1, 10 - D):
        for f in range(e, 10 - D):
            disc = e * f * (D + e) * (D + f)
            r = isqrt(disc)
            if r * r != disc:
                continue
            num = e * f + r
            if num % D:
                continue
            m = num // D
            # Gram determinant check
            assert D * m * m - 2 * e * f * m - e * f * (D + e + f) == 0
            if m % e or m % f or m > e * f:
                print("  rejected", (D, e, f, m), "m/e", m / e, "m/f", m / f)
                continue
            print("  D", D, "(e,f,m)", (e, f, m), "degrees", D + e, D + f)

print("one divisorial end (a, e), 1 <= e < a <= 9, ae square, D = a - e > 0:")
for a in range(2, 10):
    for e in range(1, a):
        if isqrt(a * e) ** 2 == a * e:
            print("  (a,e)", (a, e), "D", a - e, "|Delta|", 8 - (a - e))

print("two conic ends: D = 8/m integer:", [(m, 8 // m) for m in range(1, 9) if 8 % m == 0])

# Lemma 5.9 enumeration
def classes(n, sq, deg, xmax=6, ymax=4):
    from itertools import product
    out = []
    for x in range(0, xmax + 1):
        for ys in product(range(-ymax, ymax + 1), repeat=n):
            if x * x - sum(y * y for y in ys) == sq and 3 * x - sum(ys) == deg:
                out.append((x,) + ys)
    return out

print("A(S) deg5:", classes(4, 0, 2))
print("A(S) deg6:", classes(3, 0, 2))
print("A2(S) deg6:", classes(3, 1, 3))
