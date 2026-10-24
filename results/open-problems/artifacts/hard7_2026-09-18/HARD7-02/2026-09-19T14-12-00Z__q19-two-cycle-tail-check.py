import sympy as sp

lam, a, b = sp.symbols("lam a b")
r, c, R, alpha = sp.symbols("r c R alpha", positive=True)

M = sp.Matrix([[0, a], [b, 0]])
charpoly = sp.factor(M.charpoly(lam).as_expr())
assert sp.expand(charpoly - (lam**2-a*b)) == 0

# If a*b = r^2 z*w, the eigenvalue modulus is r*sqrt(|z*w|).
# For a Pareto radial tail P(r>t)=t^{-alpha}, setting c=|z*w|:
threshold = sp.simplify(R/sp.sqrt(c))
tail = sp.simplify(threshold**(-alpha))
expected = sp.simplify(c**(alpha/2)*R**(-alpha))
assert sp.simplify(tail/expected) == 1

print("charpoly =", charpoly)
print("eigenvalue_relation = lambda^2 = a*b")
print("Pareto_two_cycle_tail =", expected)
print("NOTE = finite 2x2 mechanism only; this is not a proof of the limiting ESD tail")
print("ALL_EXACT_CHECKS_PASS = True")
