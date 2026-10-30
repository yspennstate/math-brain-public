from fractions import Fraction

# Exact r=1 witness.
a, b, c, d, e = 0, 1, 1, 2, 0
R = [[a, b, c], [b, e, d], [c, d, Fraction(c*d, b)]]
det = (
    R[0][0]*(R[1][1]*R[2][2]-R[1][2]*R[2][1])
    - R[0][1]*(R[1][0]*R[2][2]-R[1][2]*R[2][0])
    + R[0][2]*(R[1][0]*R[2][1]-R[1][1]*R[2][0])
)
factorized = -Fraction((a*d-b*c)*(b*d-c*e), b)
assert det == factorized == 2
print("R =", R)
print("det(R) =", det)
