from fractions import Fraction

# Exact Gaussian rational arithmetic: pair (real, imag).
def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def mul(x, y):
    return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])

def conj(x):
    return (x[0], -x[1])

ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))
I = (Fraction(0), Fraction(1))

# In C[C2], with a^2=1, let e=(1+a)/2 and r=(1-e)+i e.
# Then r=c0*1+c1*a with:
c0 = (Fraction(1,2), Fraction(1,2))
c1 = (Fraction(-1,2), Fraction(1,2))
r = (c0, c1)

def star(x):
    # a=a^{-1}; involution conjugates coefficients.
    return (conj(x[0]), conj(x[1]))

def conv(x, y):
    # C2 convolution: (x0+x1 a)(y0+y1 a), a^2=1.
    return (
        add(mul(x[0], y[0]), mul(x[1], y[1])),
        add(mul(x[0], y[1]), mul(x[1], y[0])),
    )

unitarity = conv(star(r), r)
quotient_scalar = add(c0, c1)   # quotient sends lamp a -> 1
coordinate = (3, -2)           # w=s1^3 s2^{-2}

assert unitarity == (ONE, ZERO)
assert quotient_scalar == I
assert coordinate == (3, -2)

print("r coefficients at (1,a):", r)
print("r^* r coefficients at (1,a):", unitarity)
print("lamp-forgetting quotient q(r):", quotient_scalar)
print("free-word exponent coordinate for w=s1^3 s2^{-2}:", coordinate)
print("ALL ASSERTIONS PASSED")
