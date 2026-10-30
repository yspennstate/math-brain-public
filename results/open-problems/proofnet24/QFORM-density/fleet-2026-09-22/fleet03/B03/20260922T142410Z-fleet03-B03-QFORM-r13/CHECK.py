from fractions import Fraction
from math import sqrt


def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]


def det3(M):
    return (
        M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
    )


tests = [
    (3, (1,2), (-2,1), ((4,1),(2,5))),
    (-2, (3,-1), (1,4), ((2,-3),(5,1))),
    (5, (-2,7), (3,-4), ((-1,6),(2,3))),
    (7, (5,1), (-3,2), ((8,-2),(4,-5))),
]

for raw_d, raw_a, raw_b, raw_B in tests:
    d = Fraction(raw_d)
    a = [Fraction(x) for x in raw_a]
    b = [Fraction(x) for x in raw_b]
    B = [[Fraction(x) for x in row] for row in raw_B]
    C = [[B[i][j]-a[i]*b[j]/d for j in range(2)] for i in range(2)]
    dB_minus_ab = [[d*B[i][j]-a[i]*b[j] for j in range(2)] for i in range(2)]
    assert det2(dB_minus_ab) == d*d*det2(C)
    M = [
        [d,b[0],b[1]],
        [a[0],B[0][0],B[0][1]],
        [a[1],B[1][0],B[1][1]],
    ]
    assert det3(M) == d*det2(C)

old = 16/(3**0.25)
generic = 8.0
one_side = 2**(11/4)
square = 4*sqrt(2)
assert generic < old
assert one_side < generic
assert square < one_side

print('PASS exact Schur determinant identities on', len(tests), 'rational instances')
print('previous_B09_constant=', repr(old))
print('new_rectangular_constant=', repr(generic))
print('new_one_physical_side_constant=', repr(one_side))
print('new_square_constant=', repr(square))
