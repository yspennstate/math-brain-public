"""Exact symbolic checker for PROB20-07 run 2026-09-15T205430Z.

Checks the algebra in the theorem eliminating chamber A
    r1*r3 <= 1
for fully-three-coordinate period-two candidates at the endpoint floor a=1/12.

Requires sympy only. This is an algebra checker, not independent proof review.
"""

import sympy as sp

X, Y, A, B, t = sp.symbols("X Y A B t", positive=True)
a = sp.Rational(1, 12)
b = sp.Rational(3, 4)
S = X + Y
P = X * Y
C = 1 - S
u = X - Y

# Chamber-A parameterization, with C=t*A+(1-t)*B.
Bexpr = sp.factor((C - t*A) / (1 - t))
x2 = t * (A + Y)
y2 = t * (A + X)
x3 = (1 - t) * (Bexpr + Y)
y3 = (1 - t) * (Bexpr + X)

assert sp.simplify(X + x2 + x3 - 1) == 0
assert sp.simplify(Y + y2 + y3 - 1) == 0

r2 = (A + X) / (A + Y)
r3 = sp.factor((Bexpr + X) / (Bexpr + Y))

# lambda = r2^2: source atoms 23,33 only.
lam22 = sp.factor(r2**2)
src22 = sp.factor(
    2*x2*x3*(r2*r3 - lam22) + x3**2*(r3**2 - lam22)
)
src22_expected = sp.factor(
    u * (A - C) * (A*(2 - S) + 2*P + S*C) / (A + Y)**2
)
assert sp.simplify(src22 - src22_expected) == 0

targ22 = sp.factor((X - a) - lam22*(Y - a))
targ22_expected = sp.factor(
    u * (A**2 + 2*a*A - P + a*S) / (A + Y)**2
)
assert sp.simplify(targ22 - targ22_expected) == 0

# Relax P <= S^2/4 and verify the factorization yielding A >= L(S).
Fweak = sp.factor(
    b*(A - C)*(A*(2 - S) + S**2/sp.Integer(2) + S*C)
    - (A**2 + 2*a*A - S**2/sp.Integer(4) + a*S)
)
Fweak_expected = -(
    (2*A + S) * (9*A*S - 6*A + 9*S**2 - 33*S + 20)
) / 24
assert sp.simplify(Fweak - Fweak_expected) == 0

L = sp.factor((9*S**2 - 33*S + 20) / (6 - 9*S))
activity_margin = sp.factor(a*L + a*S - S**2/sp.Integer(4))
activity_expected = -(
    27*S**3 - 18*S**2 - 27*S + 20
) / (36*(3*S - 2))
assert sp.simplify(activity_margin - activity_expected) == 0

# lambda = r2*r3 using independent B and t=(C-B)/(A-B).
B2 = sp.symbols("B2", real=True)
tt = sp.factor((C - B2) / (A - B2))
x2b = tt * (A + Y)
y2b = tt * (A + X)
x3b = (1 - tt) * (B2 + Y)
y3b = (1 - tt) * (B2 + X)
r2b = (A + X) / (A + Y)
r3b = (B2 + X) / (B2 + Y)
lam23 = sp.factor(r2b * r3b)

src23 = sp.factor(y3b**2 - lam23*x3b**2)
src23_expected = sp.factor(
    u * (A - C)**2 * (B2 + X) / ((A - B2)*(A + Y))
)
assert sp.simplify(src23 - src23_expected) == 0

N23 = A*B2 + a*(A + B2 + S) - P
targ23 = sp.factor((X - a) - lam23*(Y - a))
targ23_expected = sp.factor(
    u * N23 / ((A + Y)*(B2 + Y))
)
assert sp.simplify(targ23 - targ23_expected) == 0

K = B2**2 + B2*S + P
H = sp.factor(b*K - B2 - a)
J = sp.factor(b*K*C + a*(B2 + S) - P)
Q = sp.factor(J - L*H)

NQ = (
    B2**2*(162*S - 126)
    + B2*(270*S**2 - 531*S + 246)
    + P*(270*S - 198)
    + 20 - 27*S
)
assert sp.simplify(Q - NQ/(36*(2 - 3*S))) == 0

# Endpoint reductions used to prove NQ>0.
N0 = sp.factor(NQ.subs({B2: 0, P: S**2/4}))
NC = sp.factor(NQ.subs({B2: C, P: S**2/4}))
assert sp.simplify(
    N0 - (3*S - 2)*(45*S**2 - 3*S - 20)/2
) == 0
assert sp.simplify(
    NC + (9*S - 7)*(9*S**2 - 60*S + 40)/2
) == 0

# H<0 is reduced to a convex endpoint check after P <= S^2/4.
Bsym = sp.symbols("Bsym", real=True)
h = sp.factor(b*(Bsym**2 + Bsym*S + S**2/4) - Bsym - a)
h0 = sp.factor(h.subs(Bsym, 0))
hC = sp.factor(h.subs(Bsym, C))
assert sp.simplify(h0 - (9*S**2 - 4)/48) == 0
assert sp.simplify(hC - (9*S**2 + 12*S - 16)/48) == 0

print("ALL EXACT CHAMBER-A CHECKS PASSED")
print("Fweak factor:", sp.factor(Fweak))
print("activity margin:", activity_margin)
print("Q numerator:", sp.factor(NQ))
print("N(B=0,P=S^2/4):", N0)
print("N(B=1-S,P=S^2/4):", NC)
print("h endpoints:", h0, hC)
