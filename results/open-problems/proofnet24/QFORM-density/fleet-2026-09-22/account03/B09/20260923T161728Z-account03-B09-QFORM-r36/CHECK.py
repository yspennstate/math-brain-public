from math import e, sqrt, gamma


def beta(a,b):
    return gamma(a)*gamma(b)/gamma(a+b)

C3 = e/(6*sqrt(2))*beta(1/6,1/12)
Cbranch = C3*(400/27)**(1/6)
assert 5.6557 < C3 < 5.6559
assert 8.8634 < Cbranch < 8.8637

# Diffuse stress family B_{m,eps}: singular values 1,1,1,eps.
m = 16
eps = 1e-8
Z3 = 1 + 3*eps*eps
max_column_leverage = 1/m
assert max_column_leverage <= 0.5
new_bound = C3 * Z3**(-1/6)

# Any physical 3x3 minor taking one column from each of the first three groups.
det_minor = m**(-1.5)
partner_bound = 3 * det_minor**(-1/3)
assert abs(partner_bound - 12.0) < 1e-12

# Full-rank cross-fiber bound for r=4, product singular values eps.
full_product_bound = 2*e*eps**(-0.25)
assert full_product_bound > 500

print(f"C3={C3:.15f}")
print(f"Cbranch={Cbranch:.15f}")
print(f"Z3={Z3:.15f}")
print(f"max_column_leverage={max_column_leverage:.15f}")
print(f"new_bound={new_bound:.15f}")
print(f"partner_bound={partner_bound:.15f}")
print(f"full_product_bound={full_product_bound:.15f}")
print("STATUS=QFORM_COLUMN_DIFFUSE_E3_CHECK_PASS")
