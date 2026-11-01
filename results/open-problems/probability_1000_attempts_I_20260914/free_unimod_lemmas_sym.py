"""Symbolic verification of the two identities and the two lemmas behind C = 1."""
import sympy as sp

a, b, s, D, m, mu = sp.symbols('a b s D m mu', positive=True)
A, B = a**2 + s, b**2 + s
Phi = sp.expand(b*A*(1-A) + a*B*(1-B))
Psi = sp.expand(b*B*(3*a**2-s) + a*A*(3*b**2-s))
sub = {a: (D + sp.sqrt(D**2 - 4*m))/2, b: (D - sp.sqrt(D**2 - 4*m))/2}
Phi_dm = sp.simplify(sp.expand(sp.simplify(Phi.subs(sub))))
Psi_dm = sp.simplify(sp.expand(sp.simplify(Psi.subs(sub))))
claimPhi = D*(3*m**2 + m*(1-D**2) + s*(1-2*m) - s**2)
claimPsi = D*(3*m**2 + s*(6*m - D**2) - s**2)
print("Phi identity holds:", sp.simplify(Phi_dm - claimPhi) == 0)
print("Psi identity holds:", sp.simplify(Psi_dm - claimPsi) == 0)

# Lemma A: Psi >= 0 with m <= D^2/4 forces s <= (3/4) D^2
p = 3*m**2 + s*(6*m - D**2) - s**2
pmax = sp.simplify(p.subs(m, D**2/4))          # p is increasing in m, so bound at m = D^2/4
print("\nLemma A: p at m = D^2/4 is", sp.factor(pmax))
print("  its positive root in s:", sp.solve(sp.Eq(pmax, 0), s))

# Lemma B: with 0 <= s <= 3/4 and D <= 1, q = Phi/D >= 0.  q is concave in s, so check the two ends.
q = 3*m**2 + m*(1-D**2) + s*(1-2*m) - s**2
print("\nLemma B: q at s = 0 is", sp.factor(q.subs(s, 0)), " (nonnegative for D <= 1)")
q34 = sp.simplify(q.subs(s, sp.Rational(3, 4)))
print("  q at s = 3/4 is", sp.factor(q34))
print("  it decreases in m on (0, D^2/4]; at m = D^2/4 it equals",
      sp.factor(sp.simplify(q34.subs(m, D**2/4))))
print("  d/dm at m = D^2/4:", sp.factor(sp.simplify(sp.diff(q34, m).subs(m, D**2/4))))
