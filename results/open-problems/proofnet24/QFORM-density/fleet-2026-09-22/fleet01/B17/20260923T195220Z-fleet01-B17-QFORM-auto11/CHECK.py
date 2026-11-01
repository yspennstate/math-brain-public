import sympy as sp

rt2, rt3, rt6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)
B = sp.eye(3) - sp.Rational(2,3)*sp.ones(3)
assert sp.simplify(B*B - sp.eye(3)) == sp.zeros(3)

# Small-two-sheet comparison at a=1/10.
k = 4 - 2*rt3
Rsmall = sp.Rational(25,128)*rt6*(9-4*rt3)
assert sp.Rational(433,250)**2 < 3
assert 467366 < 270000*sp.Rational(433,250)
assert float(sp.N(Rsmall,50)) < 1

# Large-two-sheet rational envelope.
large = sp.Rational(11,2)*(sp.Rational(23,25))**4

# Exact connected cone-tip source formula pinned to fleet02/B17 checker.
p0 = (
    -sp.Rational(165, 4)
    + 12*rt3
    + 15*rt2
    + 22*rt3*sp.log((sp.sqrt(6)+3*rt2)/6)
    + rt3*sp.log((1+rt2-1/rt3)/(1+rt2+1/rt3))
)
assert float(sp.N(large-p0,50)) < 0
assert float(sp.N(p0-3*rt2,50)) < 0

# Partner irrational null direction and finite-fragment coefficient.
d0 = sp.Matrix([1,1,4-3*rt2])
assert sp.simplify((d0.T*B*d0)[0]) == 0
Bd0 = sp.simplify(B*d0)
assert Bd0 == sp.Matrix([-3+2*rt2,-3+2*rt2,-rt2])
norm2 = sp.simplify((d0.T*d0)[0])
assert sp.simplify(norm2 - 12*(rt2-1)**2) == 0
CF = sp.simplify(4*rt6/sp.sqrt(norm2))
assert abs(float(sp.N(CF-(4+2*rt2),50))) < 1e-40

# Concrete R=39 substitution in p_R <= p0 + C_F/R.
R39 = sp.N(p0 + (4+2*rt2)/39,50)
target = sp.N(3*rt2,50)
assert R39 < target

print("PASS QFORM_B17_HOUSEHOLDER_TWOSHEET_GLOBAL_CLOSURE")
print("small ratio bound =", sp.N(Rsmall,40))
print("large side rational bound =", sp.N(large,40))
print("p_*(0) =", sp.N(p0,50))
print("3sqrt2-p_*(0) =", sp.N(3*rt2-p0,50))
print("q(d0) =", sp.simplify((d0.T*B*d0)[0]))
print("C_F(d0) =", sp.N(CF,40))
print("R=39 combined bound =", R39)
print("R=39 gap to 3sqrt2 =", target-R39)
