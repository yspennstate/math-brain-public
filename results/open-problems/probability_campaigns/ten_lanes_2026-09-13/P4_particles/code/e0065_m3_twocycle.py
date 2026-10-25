# E0065 / Problem 12 : exact 2-cycle certificate for the m=3 extremal family.
# The operator commutes with the transposition rho = (2 3), so a 2-cycle of the form
# {x, rho(x)} solves V(x) = rho(x), i.e. V1 = x1, V2 = x3, V3 = x2.
import sympy as sp

L = sp.symbols('L', positive=True)
x1, x2, x3 = sp.symbols('x1 x2 x3')
xs = [x1, x2, x3]
PR = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
SIG = {(0, 0): 0, (0, 1): 2, (0, 2): 1, (1, 1): 2, (1, 2): 0, (2, 2): 1}

def build(Lv):
    P = {}
    for p in PR:
        row = [Lv, Lv, Lv]
        row[SIG[p]] += (1 - 3 * Lv)
        P[p] = row
    return P

def Vof(P):
    V = [sp.Integer(0)] * 3
    for (i, j), row in P.items():
        c = xs[i] * xs[j] * (1 if i == j else 2)
        for k in range(3):
            V[k] += row[k] * c
    return [sp.expand(v) for v in V]

V = Vof(build(L))

# rho = (2 3) equivariance check:  V(rho x) = rho(V x)
sw = {x2: x3, x3: x2}
lhs = [sp.expand(v.subs(sw, simultaneous=True)) for v in V]
rhs = [V[0], V[2], V[1]]
print("V commutes with the transposition (2 3):",
      all(sp.expand(lhs[k] - rhs[k]) == 0 for k in range(3)))

sub = {x3: 1 - x1 - x2}
# V(x) = rho(x)
e1 = sp.expand(V[0].subs(sub) - x1)
e2 = sp.expand(V[1].subs(sub) - (1 - x1 - x2))
print("\nsolving V(x) = rho(x) ...", flush=True)
sols = sp.solve([e1, e2], [x1, x2], dict=True)
for s in sols:
    a = sp.simplify(s[x1]); b = sp.simplify(s[x2]); c = sp.simplify(1 - a - b)
    print("  x =", (a, b, c))
    print("     is it a fixed point (x2 = x3)?", sp.simplify(b - c) == 0)
    for Lv in [sp.Rational(1, 13), sp.Rational(1, 12), sp.Rational(1, 20), sp.Rational(1, 11)]:
        pt = [sp.nsimplify(sp.simplify(z.subs(L, Lv))) for z in (a, b, c)]
        inside = all(sp.simplify(z) >= 0 for z in pt) and sp.simplify(sum(pt) - 1) == 0
        print(f"     L={Lv}: x = {[sp.nsimplify(sp.radsimp(z)) for z in pt]}  "
              f"num={[float(z) for z in pt]}  in simplex: {inside}")

# EXACT certificate at one rational L below 1/12
print("\n--- exact certificate at L = 1/13 ---")
Lv = sp.Rational(1, 13)
Vn = [sp.expand(v.subs(L, Lv)) for v in Vof(build(Lv))]
for s in sols:
    a = sp.simplify(s[x1].subs(L, Lv)); b = sp.simplify(s[x2].subs(L, Lv)); c = sp.simplify(1 - a - b)
    if sp.simplify(b - c) == 0:
        continue
    pt = {x1: a, x2: b, x3: c}
    img = [sp.simplify(sp.expand(v).subs(pt)) for v in Vn]
    img2 = [sp.simplify(sp.expand(v).subs({x1: img[0], x2: img[1], x3: img[2]})) for v in Vn]
    print("  x      =", [sp.radsimp(z) for z in (a, b, c)], [float(z) for z in (a, b, c)])
    print("  V(x)   =", [sp.radsimp(z) for z in img], [float(z) for z in img])
    print("  V^2(x) =", [sp.radsimp(z) for z in img2], [float(z) for z in img2])
    print("  V^2(x) == x exactly:", all(sp.simplify(img2[k] - [a, b, c][k]) == 0 for k in range(3)))
    print("  V(x)  != x         :", any(sp.simplify(img[k] - [a, b, c][k]) != 0 for k in range(3)))
    print("  in the open simplex:", all(sp.simplify(z) > 0 for z in (a, b, c)))
