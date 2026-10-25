# E0065 / Problem 12 : exact analysis of the extremal vertex-ansatz QSO found for m = 3.
# sigma: (11)->1, (12)->3, (13)->2, (22)->3, (23)->1, (33)->2   (1-indexed types)
# P_{ij,.} = L*(1,1,1) + (1-3L) e_{sigma(ij)}
import sympy as sp

L = sp.symbols('L', positive=True)
x1, x2, x3 = sp.symbols('x1 x2 x3', nonnegative=True)
xs = [x1, x2, x3]
PR = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
SIG = {(0, 0): 0, (0, 1): 2, (0, 2): 1, (1, 1): 2, (1, 2): 0, (2, 2): 1}

def build(Lv):
    P = {}
    for p in PR:
        row = [Lv, Lv, Lv]
        row[SIG[p]] = row[SIG[p]] + (1 - 3 * Lv)
        P[p] = row
    return P

def Vof(P):
    V = [sp.Integer(0)] * 3
    for (i, j), row in P.items():
        c = xs[i] * xs[j] * (1 if i == j else 2)
        for k in range(3):
            V[k] += row[k] * c
    return [sp.expand(v) for v in V]

P = build(L)
V = Vof(P)
print("row sums:", [sp.simplify(sum(r)) for r in P.values()])
print("sum V - (sum x)^2 =", sp.simplify(sp.expand(sum(V) - (x1 + x2 + x3) ** 2)))
print("V1 =", sp.factor(V[0]))

# Jacobian, columns sum to 2 on the simplex
Jm = sp.Matrix(3, 3, lambda k, l: sp.diff(V[k], xs[l]))
print("column sums of J at sum x = 1:",
      [sp.simplify(sum(Jm[k, l] for k in range(3)).subs(x3, 1 - x1 - x2)) for l in range(3)])

# fixed points on the simplex: substitute x3 = 1 - x1 - x2 and solve V1 = x1, V2 = x2
sub = {x3: 1 - x1 - x2}
e1 = sp.expand(V[0].subs(sub) - x1)
e2 = sp.expand(V[1].subs(sub) - x2)
print("\nsolving the fixed point system symbolically in L ...", flush=True)
sols = sp.solve([e1, e2], [x1, x2], dict=True)
print("number of solutions:", len(sols))
for s in sols:
    print("  ", {k: sp.simplify(v) for k, v in s.items()})

# the symmetric guess: is the centre a fixed point?
c = {x1: sp.Rational(1, 3), x2: sp.Rational(1, 3)}
print("\ncentre is a fixed point:", sp.simplify(e1.subs(c)) == 0 and sp.simplify(e2.subs(c)) == 0)
Jc = Jm.subs({x1: sp.Rational(1, 3), x2: sp.Rational(1, 3), x3: sp.Rational(1, 3)})
ev = sp.Matrix(Jc).eigenvals()
print("eigenvalues of J at the centre:", {sp.simplify(k): v for k, v in ev.items()})
for k in ev:
    ks = sp.simplify(k)
    if sp.simplify(ks - 2) == 0:
        continue
    r2 = sp.simplify(sp.Abs(ks) ** 2)
    print("  tangent eigenvalue:", ks, "   |.|^2 =", sp.simplify(sp.expand(r2)))
    sol = sp.solve(sp.Eq(sp.simplify(sp.expand(r2)), 1), L)
    print("     |tangent eigenvalue| = 1 at L =", sol, [sp.nsimplify(s) for s in sol])
