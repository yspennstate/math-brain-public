import sympy as sp

x = sp.symbols("x", positive=True)
m = sp.Rational(1, 3)

# Multiplicative normalizing constants are irrelevant for logarithmic
# derivatives, mode location, curvature ratios, and tail-ratio identities.
k_cl = x**(-sp.Rational(3, 2)) * sp.exp(-sp.Rational(1, 2) / x)
k_fr = sp.sqrt(4*x - 1) / x**2

ld_cl = sp.factor(sp.diff(sp.log(k_cl), x))
ld_fr = sp.factor(sp.diff(sp.log(k_fr), x))
assert sp.simplify(ld_cl - (1 - 3*x)/(2*x**2)) == 0
assert sp.simplify(ld_fr - 2*(1 - 3*x)/(x*(4*x - 1))) == 0
assert sp.simplify(ld_cl.subs(x, m)) == 0
assert sp.simplify(ld_fr.subs(x, m)) == 0

curv_cl = sp.simplify((sp.diff(k_cl, x, 2) / k_cl).subs(x, m))
curv_fr = sp.simplify((sp.diff(k_fr, x, 2) / k_fr).subs(x, m))
assert curv_cl == -sp.Rational(27, 2)
assert curv_fr == -54

# Exact tail comparison: -k' = (k/x) * R(x).
Rcl = sp.factor(-sp.diff(k_cl, x) / (k_cl / x))
Rfr = sp.factor(-sp.diff(k_fr, x) / (k_fr / x))
assert sp.simplify(Rcl - (3*x - 1)/(2*x)) == 0
assert sp.simplify(Rfr - 2*(3*x - 1)/(4*x - 1)) == 0

# Exact rational identities giving uniform tail-ratio bounds for x >= 1.
assert sp.simplify((Rcl - 1) - (x - 1)/(2*x)) == 0
assert sp.simplify((sp.Rational(3, 2) - Rcl) - 1/(2*x)) == 0
assert sp.simplify((Rfr - sp.Rational(4, 3)) - 2*(x - 1)/(3*(4*x - 1))) == 0
assert sp.simplify((sp.Rational(3, 2) - Rfr) - 1/(2*(4*x - 1))) == 0

print("R19 I0084 C030 exact kernel self-check")
print("PASS classical log derivative =", ld_cl)
print("PASS free log derivative =", ld_fr)
print("PASS common mode x=1/3")
print("PASS k_cl''(m)/k_cl(m) =", curv_cl)
print("PASS k_fr''(m)/k_fr(m) =", curv_fr)
print("PASS classical tail ratio (-k')/(k/x) =", Rcl)
print("PASS free tail ratio (-k')/(k/x) =", Rfr)
print("PASS exact rational tail-ratio identities imply for x>=1:")
print("     1 <= R_cl < 3/2 and 4/3 <= R_fr < 3/2")
