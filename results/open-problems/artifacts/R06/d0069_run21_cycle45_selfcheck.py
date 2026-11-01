from fractions import Fraction

# Exact arithmetic in Q(sqrt(5)) represented as a + b/sqrt(5).
# Multiplication: (a+b/r)(c+d/r) = (ac+bd/5) + (ad+bc)/r, r=sqrt(5).
def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def mul(x, y):
    a, b = x
    c, d = y
    return (a*c + b*d/Fraction(5), a*d + b*c)

def power(x, n):
    out = (Fraction(1), Fraction(0))
    for _ in range(n):
        out = mul(out, x)
    return out

def fmt(x):
    a, b = x
    if b == 0:
        return str(a)
    if a == 0:
        return f"{b}/sqrt(5)"
    return f"{a} + {b}/sqrt(5)"

z = (Fraction(0), Fraction(1))  # 1/sqrt(5)
four = (Fraction(4), Fraction(0))

# T_{L,r}(z) = 4 z (z^r + z^(L-r)).
def transfer(L, r):
    return mul(mul(four, z), add(power(z, r), power(z, L-r)))

for L in (4, 5):
    vals = {r: transfer(L, r) for r in range(1, L)}
    print("L", L, vals)

# L=4: values are 24/25 for r=1,3 and 8/(5 sqrt(5)) for r=2.
assert transfer(4, 1) == (Fraction(24,25), Fraction(0))
assert transfer(4, 2) == (Fraction(0), Fraction(8,5))
assert transfer(4, 3) == (Fraction(24,25), Fraction(0))
print("L4_MIN_TRANSFER", "8/(5*sqrt(5))")
# sqrt(3) * 8/(5 sqrt(5)) > 1 iff 192 > 125.
assert 192 > 125
print("L4_PRODUCT_GT_ONE_CERT", 192, ">", 125)

# L=5: r=2,3 minimize: 4/25 + 4/(5 sqrt(5)).
assert transfer(5, 1) == (Fraction(4,5), Fraction(4,25))
assert transfer(5, 2) == (Fraction(4,25), Fraction(4,5))
assert transfer(5, 3) == (Fraction(4,25), Fraction(4,5))
assert transfer(5, 4) == (Fraction(4,5), Fraction(4,25))
print("L5_MIN_TRANSFER", "4/25 + 4/(5*sqrt(5))")
# 2*T_min > 1 iff 8 sqrt(5) > 17 iff 320 > 289.
assert 320 > 289
print("L5_PRODUCT_GT_ONE_CERT", 320, ">", 289)

print("ALL_EXACT_FINITE_CHECKS_PASS")
