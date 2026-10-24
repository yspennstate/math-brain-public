import numpy as np
import groups as g
import domination as d

for name, T in [('Z4', g.cyclic(4)), ('S3', g.S3()), ('D4', g.D4()), ('Q8', g.Q8()),
                ('Z2xZ2', g.direct_product(g.cyclic(2), g.cyclic(2)))]:
    g.check_group(T)
    print(name, len(T), 'group ok')
rng = np.random.default_rng(1)
Q = g.random_equivariant_contraction(g.S3(), rng)
P1 = g.determinantal_law(Q)
P2 = g.inclusion_exclusion_law(Q)
print('law check: max abs diff', np.abs(P1 - P2).max(), 'sum', P1.sum(), 'min', P1.min())
print('mu_.5 >= mu_.4 deficit', d.deficit(g.product_law(4, .5), g.product_law(4, .4)))
print('mu_.4 >= mu_.5 deficit', d.deficit(g.product_law(4, .4), g.product_law(4, .5)))
