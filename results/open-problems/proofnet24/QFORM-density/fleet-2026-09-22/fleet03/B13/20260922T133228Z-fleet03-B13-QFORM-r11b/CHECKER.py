from fractions import Fraction
from itertools import combinations
from math import pi, sqrt, comb

# Exact tetrahedral Parseval frame V=(1/2)M.
M = [
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 1],
]
V = [[Fraction(x, 2) for x in row] for row in M]

# Verify VV^T=I_3 exactly.
G = [[sum(V[i][k]*V[j][k] for k in range(4)) for j in range(3)] for i in range(3)]
assert G == [[Fraction(int(i==j),1) for j in range(3)] for i in range(3)]

def det3(A):
    return (
        A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
        - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
        + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
    )

minor_squares = []
for S in combinations(range(4), 3):
    T = [[V[i][j] for j in S] for i in range(3)]
    d = det3(T)
    minor_squares.append(d*d)

assert minor_squares == [Fraction(1,4)]*4
assert sum(minor_squares, Fraction(0,1)) == 1

C3 = 2*pi + 3*sqrt(3)
Cstar = C3 + sqrt(C3*C3 + 3*pi*pi)
expected = {
    3: 2*C3*comb(3,3),
    4: 2*C3*comb(4,3),
    5: 2*C3*comb(5,3),
}
assert 22.9586 < expected[3] < 22.9587
assert 91.8347 < expected[4] < 91.8348
assert 229.5867 < expected[5] < 229.5868
assert 48.3660 < 2*Cstar < 48.3661

print('PASS=True')
print('tetra_minor_squares=', [str(x) for x in minor_squares])
print('minor_square_sum=', sum(minor_squares, Fraction(0,1)))
print('C3=', repr(C3))
print('rank3_m3_bound=', repr(expected[3]))
print('rank3_m4_bound=', repr(expected[4]))
print('rank3_m5_bound=', repr(expected[5]))
print('Cstar=', repr(Cstar))
print('same_sign_m4_bound=', repr(2*Cstar))
