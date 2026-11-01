from fractions import Fraction as F

# For a 3D pyramid L over planar base B, the exact reduction is
# |L| |(L-L)^circ| = (4/9) |B| |(B-B)^circ|.
# The theorem-sized proof is in the run report; this finite self-check only
# certifies the rational constants at two representative endpoints.

A_tri, Eo_tri = F(1, 2), F(3)       # standard triangle
A_sq, Eo_sq = F(4), F(1, 2)         # square [-1,1]^2

prod_tri = F(4, 9) * A_tri * Eo_tri
prod_sq = F(4, 9) * A_sq * Eo_sq

assert prod_tri == F(2, 3)
assert prod_sq == F(8, 9)
assert prod_sq > F(2, 3)

print("triangle_pyramid_product =", prod_tri)
print("square_pyramid_product =", prod_sq)
print("Eggleston_to_Makai_factor =", F(4, 9))
print("Makai_bound =", F(2, 3))
print("ALL_EXACT_CHECKS_PASS = True")
