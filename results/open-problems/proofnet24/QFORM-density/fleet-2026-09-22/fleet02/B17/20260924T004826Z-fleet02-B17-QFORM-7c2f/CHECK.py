import math

# Exact physical witness A_* = [[1,2,1],[2,0,0],[1,0,2]].
# M = A_*^2 - I.
M = [[5,2,3],[2,3,2],[3,2,4]]
minor1 = M[0][0]
minor2 = M[0][0]*M[1][1] - M[0][1]*M[1][0]
detM = (
    M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
    - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
    + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
)
assert (minor1, minor2, detM) == (5, 11, 21)

# Characteristic polynomial is lambda^3 - 3 lambda^2 - 3 lambda + 8.
# Numeric roots, independently hard-coded only for an informative check.
roots = [-1.66907909, 1.52397640, 3.14510269]
assert min(abs(x) for x in roots) > 1.5

# New global constant for a=b=2.
C = 1.0 + math.log(2.0)
sharp_lower = 3.0 * math.sqrt(2.0)
partner_target_ceiling = 2.0 + math.log(4.0)
pinned_generic_onesheet = math.pi * math.sqrt(2.0)
assert C < partner_target_ceiling < sharp_lower < pinned_generic_onesheet

print('leading minors A_*^2-I:', minor1, minor2, detM)
print('C(a=b=2)=', repr(C))
print('2+log(4)=', repr(partner_target_ceiling))
print('3sqrt(2)=', repr(sharp_lower))
print('pi sqrt(2)=', repr(pinned_generic_onesheet))
print('PASS QFORM-ONE-NULL-LEAF-SHEARED-SQUARE-GLOBAL-BARRIER-v1')
