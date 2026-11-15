# Exact checks of the formulas of Sections 2 and 3. Needs SymPy. Usage: python3 check_path_law.py
#
# 1. For l = 1, ..., 5 the spanning trees of G_l are enumerated by brute force, and the total weight of the trees whose
#    N-F path is each of the four simple paths is compared with Lemma 2.
# 2. The drift identities, the conserved coordinate and the equilibria are checked as rational functions of a, c, h, l.
import itertools
import sympy as sp

a, c, h, l = sp.symbols("a c h l", positive=True)
A, B, C, D, R = sp.symbols("A B C D R", positive=True)


def graph(L):
    """Edges of G_L as (x, y, weight). Vertices: 'N', 'u', 'v', 'F', ('x', i), ('y', i)."""
    E = [("N", "u", A), ("N", "v", B), ("u", "v", R)]
    for side, start, wt in (("x", "u", C), ("y", "v", D)):
        prev = start
        for i in range(1, L + 1):
            nxt = "F" if i == L else (side, i)
            E.append((prev, nxt, wt)); prev = nxt
    return E


def tree_path(edges):
    """The N-F path of a spanning tree given by its edge list, or None if the edges do not form a spanning tree."""
    adj = {}
    for x, y, _ in edges:
        adj.setdefault(x, []).append(y); adj.setdefault(y, []).append(x)
    seen = {"N": None}; stack = ["N"]
    while stack:
        x = stack.pop()
        for y in adj.get(x, []):
            if y not in seen:
                seen[y] = x; stack.append(y)
    return seen


ok = True
for L in range(1, 6):
    E = graph(L); V = {x for e in E for x in e[:2]}
    tot = {"Nu..F": 0, "Nv..F": 0, "Nuv..F": 0, "Nvu..F": 0}; ntrees = 0
    for T in itertools.combinations(E, len(V) - 1):
        seen = tree_path(T)
        if len(seen) != len(V):
            continue
        ntrees += 1
        p = ["F"]
        while p[-1] != "N":
            p.append(seen[p[-1]])
        p.reverse()
        key = ("Nu" if p[1] == "u" else "Nv") + ("" if len(p) == L + 2 else ("v" if p[1] == "u" else "u")) + "..F"
        wt = 1
        for _, _, x in T:
            wt *= x
        tot[key] += wt
    common = C ** (L - 1) * D ** (L - 1)
    Z = C * D * (A + B) + L * A * B * (C + D) + L * R * (A + B) * (C + D)
    want = {"Nu..F": A * C * (D + L * B + L * R), "Nv..F": B * D * (C + L * A + L * R), "Nuv..F": L * A * R * D, "Nvu..F": L * B * R * C}
    good = all(sp.expand(tot[k] - common * want[k]) == 0 for k in tot) and sp.expand(sum(tot.values()) - common * Z) == 0
    ok &= good
    ok &= (ntrees == 2 + 6 * L)
    print("l =", L, "spanning trees:", ntrees, "(2 + 6 l =", 2 + 6 * L, ")", "path weights match Lemma 2:", good)

# normalised quantities: b = 1 - a, d = 1 - c
b, d = 1 - a, 1 - c
Q = l * a * b + c * d + l * h
q1 = a * c * (l * b + d + l * h) / Q; q2 = b * d * (l * a + c + l * h) / Q; q3 = l * a * h * d / Q; q4 = l * b * h * c / Q
fa = q1 + q3 - a; fc = q1 + q4 - c; fh = q3 + q4 - h
g = a * d + b * c - a * b - c * d / l
checks = {
    "q1 + q2 + q3 + q4 = 1": sp.simplify(q1 + q2 + q3 + q4 - 1),
    "f_a = l a b (c - a)/Q": sp.simplify(fa - l * a * b * (c - a) / Q),
    "f_c = c d (a - c)/Q": sp.simplify(fc - c * d * (a - c) / Q),
    "f_h = l h (g - h)/Q": sp.simplify(fh - l * h * (g - h) / Q),
    "f_a/(ab) + l f_c/(cd) = 0": sp.simplify(fa / (a * b) + l * fc / (c * d)),
    "f_a - f_c = -(l a b + c d)(a - c)/Q": sp.simplify(fa - fc + (l * a * b + c * d) * (a - c) / Q),
    "g on the diagonal = (1 - 1/l) a (1 - a)": sp.simplify(g.subs(c, a) - (1 - 1 / l) * a * (1 - a)),
    "Q at the equilibrium = 2 l a (1 - a)": sp.simplify(Q.subs({c: a, h: (1 - 1 / l) * a * (1 - a)}) - 2 * l * a * (1 - a)),
}
for name, val in checks.items():
    ok &= (val == 0)
    print(name, ":", val == 0)
print("ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
