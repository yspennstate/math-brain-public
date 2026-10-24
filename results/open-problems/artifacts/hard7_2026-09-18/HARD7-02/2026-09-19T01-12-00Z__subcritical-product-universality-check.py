import sympy as sp

# HARD7-02 run 5 exact finite-core self-check.
# The point is to separate the forest product invariant from the cyclic obstruction:
# on a tree, swapping the two directed weights on one edge preserves the characteristic
# polynomial because only the edge product enters; on a triangle, the same operation
# preserves every undirected edge product but can change the spectrum through directed
# cycle monomials.

lam = sp.symbols("lam")


def charpoly(A):
    M = sp.Matrix(A)
    return sp.expand((lam * sp.eye(M.rows) - M).det())


# Triangle.  The unordered edge products are (2,77,15) before and after swapping
# only the directed pair on edge {1,2}.
A = [[0, 1, 7],
     [2, 0, 3],
     [11, 5, 0]]
B = [[0, 2, 7],
     [1, 0, 3],
     [11, 5, 0]]

products_A = (A[0][1] * A[1][0], A[0][2] * A[2][0], A[1][2] * A[2][1])
products_B = (B[0][1] * B[1][0], B[0][2] * B[2][0], B[1][2] * B[2][1])

pA = charpoly(A)
pB = charpoly(B)

assert products_A == products_B == (2, 77, 15)
assert pA == lam**3 - 94 * lam - 103
assert pB == lam**3 - 94 * lam - 101
assert pA != pB

# Path 1--2--3.  The same swap on edge {1,2} preserves the characteristic
# polynomial; here only the two edge products 2 and 15 enter.
P = [[0, 1, 0],
     [2, 0, 3],
     [0, 5, 0]]
Q = [[0, 2, 0],
     [1, 0, 3],
     [0, 5, 0]]

pP = charpoly(P)
pQ = charpoly(Q)
assert pP == pQ == lam**3 - 17 * lam

print(f"triangle_pair_products_A={products_A}")
print(f"triangle_pair_products_B={products_B}")
print(f"triangle_charpoly_A={pA}")
print(f"triangle_charpoly_B={pB}")
print(f"path_charpoly_before={pP}")
print(f"path_charpoly_after={pQ}")
print("ALL_EXACT_CHECKS_PASS=True")
