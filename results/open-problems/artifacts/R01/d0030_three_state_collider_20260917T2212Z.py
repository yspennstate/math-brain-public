#!/usr/bin/env python3
import sympy as sp

a = sp.symbols("a", positive=True)
t = sp.Symbol("t")

K = sp.Matrix([
    [1-a, 0,   a],
    [1-a, a,   0],
    [1-a, a,   0],
])
pi = sp.Matrix([[1-a, a**2, a*(1-a)]])
Pi = sp.Matrix([[1-a, a**2, a*(1-a)]]*3)

assert all(sp.simplify(x) == 0 for x in list(pi*K-pi))
assert sp.simplify(K*K-Pi) == sp.zeros(3)

# For 0<a<=1/2, row TVs from pi are a^2 and a(1-a), so phi(1)=a(1-a).
row_tvs = [a**2, a*(1-a), a*(1-a)]
assert sp.simplify((a*(1-a)-a**2) - a*(1-2*a)) == 0

# Joint law J[y,(x,z)] of Y=X_1 and E=(X_0,X_2).
cols = [(x,z) for x in range(3) for z in range(3)]
J = sp.zeros(3, 9)
for y in range(3):
    for j,(x,z) in enumerate(cols):
        J[y,j] = sp.factor(pi[0,x]*K[x,y]*K[y,z])

py = sp.Matrix([sum(J[y,j] for j in range(9)) for y in range(3)])
pe = sp.Matrix([sum(J[y,j] for y in range(3)) for j in range(9)])
assert all(sp.simplify(py[i]-pi[0,i]) == 0 for i in range(3))

idx = [j for j in range(9) if pe[j] != 0]
Jr = J[:,idx]
per = sp.Matrix([pe[j] for j in idx])

# Squared singular values of the normalized joint matrix equal the eigenvalues below.
A = sp.simplify(
    sp.diag(*[1/v for v in py])
    * Jr
    * sp.diag(*[1/v for v in per])
    * Jr.T
)
char = sp.factor(A.charpoly(t).as_expr())
expected = sp.factor((t-1)*(t-a)*(t-a*(2-a)))
assert sp.simplify(char-expected) == 0

# For 0<a<1, a(2-a)>a, hence HGR^2(Y,E)=a(2-a).
assert sp.simplify((a*(2-a)-a) - a*(1-a)) == 0

print("stationarity: PASS")
print("K^2 = Pi exact two-step refresh: PASS")
print("row TV values:", [sp.factor(x) for x in row_tvs])
print("for 0<a<=1/2: phi(1)=a(1-a)")
print("HGR squared eigenvalues:", [1, a, sp.factor(a*(2-a))])
print("rho(sigma(X1),sigma(X0,X2)) = sqrt(a(2-a))")
print("rho^2 - 2 phi(1) =", sp.factor(a*(2-a)-2*a*(1-a)))
print("ALL_EXACT_CHECKS_PASS")
