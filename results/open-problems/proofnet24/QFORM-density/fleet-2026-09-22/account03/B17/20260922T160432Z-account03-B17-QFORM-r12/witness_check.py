"""Independent arithmetic checks for account03/B17 QFORM r12.
Pure Python, no external packages.
"""
from math import log, pi, sqrt

# Exact-formula numerical checks for the rotated six-variable witness.
I0 = -3.0/16.0 + 5.0*log(2.0)/8.0
I1 = sqrt(2.0)*(8.0 + 21.0*log(2.0))/18.0
p_rot_via_integrals = 2.0*sqrt(2.0)*I1 - 4.0*I0
p_rot_closed = 91.0/36.0 + 13.0*log(2.0)/6.0
assert abs(p_rot_via_integrals - p_rot_closed) < 1e-14

# Compressed active matrix B = [[0,-1,0],[-1,0,0],[0,0,1]].
# Characteristic polynomial is (1-x)^2(-1-x), hence eigenvalues {1,1,-1}.
def det3(M):
    return (
        M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
    )
B = [[0.0,-1.0,0.0],[-1.0,0.0,0.0],[0.0,0.0,1.0]]
assert abs(det3(B) + 1.0) < 1e-15
# Direct eigenvector tests: (1,-1,0) -> +1; (1,1,0) -> -1; e3 -> +1.
def mv(M,v):
    return [sum(M[i][j]*v[j] for j in range(3)) for i in range(3)]
def same(a,b,tol=1e-14):
    return max(abs(x-y) for x,y in zip(a,b)) < tol
assert same(mv(B,[1.0,-1.0,0.0]), [1.0,-1.0,0.0])
assert same(mv(B,[1.0,1.0,0.0]), [-1.0,-1.0,0.0])
assert same(mv(B,[0.0,0.0,1.0]), [0.0,0.0,1.0])

# Compare exact witnesses and the known lower bound.
p_diag_m2 = 2.0*pi - 7.0/3.0
lower = 3.0*sqrt(2.0)
assert p_rot_closed > p_diag_m2
assert p_rot_closed < lower

# Account04/B18 local-triple bound versus the new aggregate-bank bound.
# For B_m=diag(1/m,1/m,-1/m), a=-1/m and det=-1/m^3,
# partner bound is 2 sqrt(pi) m; new bound is 2 pi.
for m in [2,3,4,8,16,64,256]:
    partner = 2.0*sqrt(pi)*m
    aggregate = 2.0*pi
    assert partner > aggregate

print("PASS")
print("I0=", repr(I0))
print("I1=", repr(I1))
print("p_rot=", repr(p_rot_closed))
print("p_diag_m2=", repr(p_diag_m2))
print("known_lower_3sqrt2=", repr(lower))
print("rotation_increment=", repr(p_rot_closed-p_diag_m2))
print("gap_to_3sqrt2=", repr(lower-p_rot_closed))
print("aggregate_bank_upper_2pi=", repr(2.0*pi))
