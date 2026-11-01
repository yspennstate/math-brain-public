import sympy as sp

# PROB20-07 exact checker: same-coordinate fixed-point exclusion
# and first all-coordinate fixed-pair chamber exclusion.

# -----------------------------------------------------------------------------
# Part I. Two fixed points sharing coordinate 3.
# x=(p+d,q-d,r), y=(p-d,q+d,r), p+q+r=1, d>0.
# -----------------------------------------------------------------------------
a, p, q, d = sp.symbols('a p q d', positive=True)
r = 1 - p - q
b = 1 - 3*a

x = [p+d, q-d, r]
y = [p-d, q+d, r]


def U(z):
    return [
        z[0]**2,
        2*z[0]*z[1],
        2*z[0]*z[2],
        z[1]**2,
        2*z[1]*z[2],
        z[2]**2,
    ]

Ux = U(x)
Uy = U(y)

# lambda=1, assuming p>=q: positive source atoms 12,22,23.
src_1 = sp.factor((Uy[1]-Ux[1]) + (Uy[3]-Ux[3]) + (Uy[4]-Ux[4]))
assert sp.simplify(src_1 - 4*d*(1-q)) == 0

tgt_1 = 2*d/b
c = sp.simplify(1 - 1/(2*b))
# tgt_1 <= src_1 gives q <= c(a).
assert sp.simplify(tgt_1 - 4*d*(1-c)) == 0

# lambda=v=(q+d)/(q-d): only source atom 22 and target coordinate 2 active.
v = (q+d)/(q-d)
src_v = sp.factor(Uy[3] - v*Ux[3])
tgt_v = sp.factor(((y[1]-a) - v*(x[1]-a))/b)
assert sp.simplify(src_v - 2*d*(q+d)) == 0
assert sp.simplify(tgt_v - 2*a*d/(b*(q-d))) == 0

# Endpoint-control identity.
endpoint_gap = sp.factor(c**2 - a/b)
expected_gap = (4*a-1)*(12*a-1)/(4*(3*a-1)**2)
assert sp.simplify(endpoint_gap - expected_gap) == 0

# -----------------------------------------------------------------------------
# Part II. All-coordinate fixed pair.
# X>Y, coordinate 1 decreases; coordinates 2,3 increase.
# x2=t(A+Y), y2=t(A+X), x3=(1-t)(B+Y), y3=(1-t)(B+X).
# Mass relation: tA+(1-t)B = C = 1-(X+Y).
# -----------------------------------------------------------------------------
X, Y, A, B, t = sp.symbols('X Y A B t', positive=True)
nu = X - Y
S = X + Y
P = X*Y
C = 1 - S

xx = [X, t*(A+Y), (1-t)*(B+Y)]
yy = [Y, t*(A+X), (1-t)*(B+X)]

r1 = Y/X
r2 = (A+X)/(A+Y)
lam = sp.simplify(r1*r2)

UX = U(xx)
UY = U(yy)
Brel = sp.simplify((C - t*A)/(1-t))

# Mixed-parent changes.
m12 = sp.factor(yy[0]*yy[1] - xx[0]*xx[1])
m13 = sp.factor(sp.simplify((yy[0]*yy[2] - xx[0]*xx[2]).subs(B, Brel)))
assert sp.simplify(m12 + nu*t*A) == 0
assert sp.simplify(m13 + nu*(1-t)*Brel) == 0

# At lambda=r1*r2, source positive atoms are 13,22,23,33.
src = sp.factor(sp.simplify(sum(UY[i]-lam*UX[i] for i in [2,3,4,5]).subs(B, Brel)))
expected_src = nu*(A*(1+P)+P*S)/(X*(A+Y))
assert sp.simplify(src - expected_src) == 0

# Fixed-point target differences are (y-a)-lambda(x-a).
T = [
    sp.factor(sp.simplify(((yy[k]-a)-lam*(xx[k]-a)).subs(B, Brel)))
    for k in range(3)
]

# Coordinates 2 and 3 are active; their unscaled sum simplifies as claimed.
sum_23 = sp.factor(sp.simplify(T[1] + T[2]))
expected_sum_23 = nu*(A*(1-2*a)+P)/(X*(A+Y))
assert sp.simplify(sum_23 - expected_sum_23) == 0

# Endpoint a=1/12, b=3/4: target-source scalar gap.
a0 = sp.Rational(1, 12)
b0 = sp.Rational(3, 4)
scalar_gap = sp.factor((A*(1-2*a0)+P)/b0 - (A*(1+P)+P*S))
expected_scalar_gap = -(A*(9*P-1) + P*(9*S-12))/9
assert sp.simplify(scalar_gap - expected_scalar_gap) == 0

# Lower-family floor approaches 1/12 from below.
s = sp.symbols('s', positive=True)
tfloor = (1 - 9*s**2)/(12 - 27*s**2)
assert sp.factor(sp.Rational(1,12) - tfloor) == 9*s**2/(4*(4-9*s**2))

print('ALL EXACT FIXED-POINT CHECKS PASSED')
