import sympy as sp

# Exact symbolic self-check for HARD7-02 run 4.
# It verifies the finite-tree gauge identity on a 3-vertex path and shows
# why the analogous entrywise twist is NOT a similarity on a dense 3-cycle.

lam = sp.symbols('lam')
a, b, c, d, e, f = sp.symbols('a b c d e f')
t = sp.symbols('t', nonzero=True)

# Tree/path: twist each oriented edge by t forward and t^{-1} backward.
A_path = sp.Matrix([
    [0, a, 0],
    [b, 0, c],
    [0, d, 0],
])
A_path_tw = sp.Matrix([
    [0, t*a, 0],
    [b/t, 0, t*c],
    [0, d/t, 0],
])
cp_path = sp.expand((lam*sp.eye(3) - A_path).det())
cp_path_tw = sp.expand((lam*sp.eye(3) - A_path_tw).det())
path_diff = sp.simplify(cp_path_tw - cp_path)

# Triangle: the same uniform upper/lower twist leaves a cycle holonomy and
# therefore is generically NOT diagonally similar to the untwisted matrix.
A_tri = sp.Matrix([
    [0, a, c],
    [b, 0, e],
    [d, f, 0],
])
A_tri_tw = sp.Matrix([
    [0, t*a, t*c],
    [b/t, 0, t*e],
    [d/t, f/t, 0],
])
cp_tri = sp.expand((lam*sp.eye(3) - A_tri).det())
cp_tri_tw = sp.expand((lam*sp.eye(3) - A_tri_tw).det())
tri_diff = sp.factor(cp_tri_tw - cp_tri)

print('PATH_BASE =', cp_path)
print('PATH_TWIST =', cp_path_tw)
print('PATH_DIFFERENCE =', path_diff)
print('PATH_TREE_EQUAL =', path_diff == 0)
print('TRIANGLE_DIFFERENCE =', tri_diff)
print('TRIANGLE_GENERIC_NONZERO =', tri_diff != 0)
print('ALL_EXACT_CHECKS_PASS =', path_diff == 0 and tri_diff != 0)
