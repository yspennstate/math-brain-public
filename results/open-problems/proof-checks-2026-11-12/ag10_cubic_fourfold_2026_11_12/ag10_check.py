# Numerical inputs of the irrationality argument for the very general cubic fourfold
# (Katzarkov-Kontsevich-Pantev-Yu, arXiv 2508.05105, Theorem 6.8 and Corollary 6.12), and the list of
# admissible Hassett discriminants.
import sympy as sp

q, x = sp.symbols("q x")
# Quantum multiplication by the hyperplane class P on the span of 1, P, P^2, P^3, P^4 (columns = images):
# P*1 = P, P*P = P^2, P*P^2 = P^3 + 6q, P*P^3 = P^4 + 15qP, P*P^4 = 6qP^2.
A = sp.Matrix([
    [0, 0, 6 * q, 0, 0],
    [1, 0, 0, 15 * q, 0],
    [0, 1, 0, 0, 6 * q],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
])
cp = sp.factor(A.charpoly(x).as_expr())
print("characteristic polynomial of P*:", cp)
print("relation P^5 = 27 q P^2 (quantum powers):", sp.simplify(A ** 5 - 27 * q * A ** 2) == sp.zeros(5, 5))
K = (3 * A).subs(q, 1)
print("eigenvalues of c1* = 3P* at q = 1 (value: algebraic multiplicity):", K.eigenvals())
print("kernel dimension of c1* on the ambient part:", len(K.nullspace()), " kernel of its square:", len((K * K).nullspace()))
amb, prim = 5, 22
print("even cohomology: ambient %d + primitive %d = %d" % (amb, prim, amb + prim))
print("generalized 0-eigenspace: 2 ambient + 22 primitive = 24; rational Hodge classes in it (very general cubic): 2")
print("a surface atom with h^{2,0} > 0 carries at least 3 Hodge classes (H^0, an ample class, H^4): 2 < 3")


def admissible(d):
    if d <= 6 or d % 6 not in (0, 2) or d % 4 == 0 or d % 9 == 0:
        return False
    return all(not (p % 2 == 1 and p % 3 == 2) for p in sp.primefactors(d))


adm = [d for d in range(7, 201) if admissible(d)]
print("admissible discriminants up to 200:", adm)
print("divisors known to consist of rational cubics: 14, 26, 38, 42; all admissible:", all(d in adm for d in (14, 26, 38, 42)))
# d admissible  <=>  d > 6 and d divides 2(n^2 + n + 1) for some n  (Hassett); cross-check of the two descriptions
alt = sorted(d for d in range(7, 201) if d % 2 == 0 and any((2 * (n * n + n + 1)) % d == 0 for n in range(d)))
print("second description (d divides 2(n^2+n+1)) gives the same list:", alt == adm)
