"""CN1019 refined bound for n = 3. With c_23 = w1, c_13 = w2, c_12 = w3 (w_z on the edge opposite z) and pi on the simplex,
h_z = a_z / (a_z + b_z),  a_z = w_z (1 - pi_z),  b_z = sum_{x != z} w_x pi_x,
and F = 1 - 2 e2 + 2 e3 sum_z h_z, so F >= 1/3 + (2/3) sum pi^3 = 1 - 2 e2 + 2 e3  iff  sum_z h_z >= 1.
Clear denominators, homogenise with pi1 + pi2 + pi3 = 1, and print the numerator's coefficients' signs.
"""
import sympy as sp

p1, p2, p3, w1, w2, w3 = sp.symbols("p1 p2 p3 w1 w2 w3", nonnegative=True)
p = [p1, p2, p3]
w = [w1, w2, w3]
S = p1 + p2 + p3
a = [w[z] * (S - p[z]) for z in range(3)]
b = [sum(w[x] * p[x] for x in range(3) if x != z) for z in range(3)]
d = [a[z] + b[z] for z in range(3)]
num = sp.expand(sum(a[z] * d[(z + 1) % 3] * d[(z + 2) % 3] for z in range(3)) - d[0] * d[1] * d[2])
P = sp.Poly(num, p1, p2, p3, w1, w2, w3)
neg = [(m, c) for m, c in P.terms() if c < 0]
print("terms", len(P.terms()), "negative", len(neg))
for m, c in neg[:20]:
    print(m, c)
print(sp.factor(num))
