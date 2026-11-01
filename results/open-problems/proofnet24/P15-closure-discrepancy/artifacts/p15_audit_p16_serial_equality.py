import sympy as sp
from itertools import product

s_im1, s_i, s_ip1, h_i, c_im1, c_i = sp.symbols(
    "s_im1 s_i s_ip1 h_i c_im1 c_i", integer=True
)
delta = s_im1 + s_i + s_ip1 - 6
m_i = s_i*(s_i-1)/2 - h_i
e_im1 = s_im1*s_i - c_im1
e_i = s_i*s_ip1 - c_i
expr = sp.expand(2*m_i + e_im1 + e_i - 5*s_i)
identity = sp.expand(s_i*delta - (2*h_i + c_im1 + c_i))
assert sp.expand(expr-identity) == 0

triples = sorted({tuple(sorted(t)) for t in product(range(1, 7), repeat=3) if sum(t) == 6})
products = [(t, t[0]*t[1]*t[2]) for t in triples]
assert triples == [(1, 1, 4), (1, 2, 3), (2, 2, 2)]
assert products == [((1, 1, 4), 4), ((1, 2, 3), 6), ((2, 2, 2), 8)]

a, b, c, d = sp.symbols("a b c d")
eq1 = a+b+c-6
eq2 = b+c+d-6
assert sp.expand(eq2-eq1) == d-a

print("P15 independent audit of P16-D5-NEAREST-SERIAL-EQUALITY-21")
print("degree_incidence_identity =", identity)
print("positive_sorted_triples_sum_6 =", triples)
print("products =", products)
print("unique_minimizer_product =", min(products, key=lambda q: q[1]))
print("difference_of_consecutive_equalities =", sp.expand(eq2-eq1))
print("AUDIT_EXACT_CHECKS_PASSED")
