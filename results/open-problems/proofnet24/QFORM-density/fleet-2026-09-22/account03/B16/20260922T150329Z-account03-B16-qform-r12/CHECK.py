from math import isclose

# Constants from the proofs.
K_product_general = 6 * 2 ** (-1/3)
# Scaling c=2b gives 3 |b|^{-2/3}.
K_product_2b = K_product_general * 2 ** (-2/3)
assert isclose(K_product_2b, 3.0, rel_tol=0, abs_tol=1e-12)

K_square_L3 = 8 / (3 ** (3/4))
# Plug M=3 |s|^{-2/3}; the coefficient becomes exactly 8 / sqrt(|as|).
K_final = K_square_L3 * (3 ** (3/4))
assert isclose(K_final, 8.0, rel_tol=0, abs_tol=1e-12)

# Determinant identity for S=[[0,s],[s,c]] and scalar pivot a:
# det(S)=-s^2, det(B)=a det(S), hence
# (|a det(B)|)^(1/4)=sqrt(|a s|).
for a,s in [(2.0,3.0),(-5.0,0.7),(1.0,-4.0)]:
    detB = -a*s*s
    lhs = (abs(a*detB)) ** 0.25
    rhs = abs(a*s) ** 0.5
    assert isclose(lhs, rhs, rel_tol=1e-12, abs_tol=1e-12)

print('PASS')
print('K_product_general=', K_product_general)
print('K_product_2b=', K_product_2b)
print('K_square_L3=', K_square_L3)
print('K_final=', K_final)
