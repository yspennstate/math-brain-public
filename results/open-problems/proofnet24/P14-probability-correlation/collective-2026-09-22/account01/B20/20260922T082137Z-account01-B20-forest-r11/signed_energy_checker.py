import sympy as sp

a,N,p,T = sp.symbols("a N p T", positive=True)
E = p - T - (2-p)*a**2

# From A^2 >= 4 N^2 a, A^2 <= 2(1+a)(N+tau), and tau <= E.
gap = sp.expand((1+a)*(N+E) - 2*N**2*a)
expected = sp.expand(
    N + N*a + p + a*p - T - a*T
    - 2*a**2 + p*a**2 - 2*a**3 + p*a**3
    - 2*N**2*a
)
assert sp.simplify(gap-expected) == 0

# Universal relaxation p<=1,T>=0 gives E<=1-a^2.
univ = sp.expand((1+a)*(N+1-a**2) - 2*N**2*a)
univ_poly = sp.expand(a**3+a**2+(2*N**2-N-1)*a-(N+1))
assert sp.simplify(univ+univ_poly) == 0

# Matching charge: x1*x2+y1*y2 <= one half of endpoint square energy.
x1,x2,y1,y2,b = sp.symbols("x1 x2 y1 y2 b", nonnegative=True)
square_slack = sp.expand(
    (x1**2+x2**2+y1**2+y2**2)/2 - (x1*x2+y1*y2)
)
assert sp.simplify(square_slack - ((x1-x2)**2 + (y1-y2)**2)/2) == 0

print("FOREST_SIGNED_ENERGY_CHECK")
print("spectral_gap =", sp.factor(gap))
print("universal_polynomial =", sp.factor(univ_poly))
print("matching_square_slack =", sp.factor(square_slack))
print("STATUS=PASS")
