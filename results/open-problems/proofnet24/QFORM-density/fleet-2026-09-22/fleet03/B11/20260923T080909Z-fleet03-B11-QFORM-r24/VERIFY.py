from math import sqrt, e
from itertools import combinations


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def cross(a,b):
    return [
        a[1]*b[2]-a[2]*b[1],
        a[2]*b[0]-a[0]*b[2],
        a[0]*b[1]-a[1]*b[0],
    ]


def norm2(a):
    return dot(a,a)

# Threshold arithmetic.
Delta0 = 1/64
tau = Delta0**(1/3)
eta = Delta0 + tau
gap = 1 - 3*eta
assert abs(tau - 1/4) < 1e-14
assert abs(eta - 17/64) < 1e-14
assert abs(gap - 13/64) < 1e-14

localized_constant = 8192 * 2**0.25 / 13
assert localized_constant < 749.384

# Explicit partner example: R=[e1,v,w].
R = [
    [1.0, 0.0, 0.0],
    [0.0, 1/sqrt(3), 1/sqrt(2)],
    [0.0, 1/sqrt(3), -1/sqrt(2)],
    [0.0, 1/sqrt(3), 0.0],
]
cols = [[row[j] for row in R] for j in range(3)]
for i in range(3):
    for j in range(3):
        target = 1.0 if i == j else 0.0
        assert abs(dot(cols[i],cols[j]) - target) < 1e-12

weights = {}
for i,j in combinations(range(4),2):
    weights[(i,j)] = norm2(cross(R[i],R[j]))
expected = {
    (0,1): 5/6,
    (0,2): 5/6,
    (0,3): 1/3,
    (1,2): 2/3,
    (1,3): 1/6,
    (2,3): 1/6,
}
for edge,val in expected.items():
    assert abs(weights[edge]-val) < 1e-12
W = sum(weights.values())
assert abs(W-3) < 1e-12
p = {edge:w/W for edge,w in weights.items()}
Delta = sum(
    p[e1]*p[e2]
    for e1 in p for e2 in p
    if set(e1).isdisjoint(e2)
)
assert abs(Delta-1/9) < 1e-12
assert Delta > 1/64

# H0 has eigenvalues {1,1,-1}: direct polynomial identity H0^2=I and trace=1.
H0 = [[0,0,1],[0,1,0],[1,0,0]]
def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
assert matmul(H0,H0) == [[1,0,0],[0,1,0],[0,0,1]]
assert sum(H0[i][i] for i in range(3)) == 1
# Since H0 is real symmetric, H0^2=I gives eigenvalues +/-1; trace 1 forces {1,1,-1}.

partner_constant = 3*(2*e)**(2/3)
assert partner_constant < 9.276

print(f"threshold_tau={tau:.12f}")
print(f"threshold_eta={eta:.12f}")
print(f"localized_gap={gap:.12f}")
print(f"localized_constant={localized_constant:.12f}")
print("wedge_weights=" + repr({k: round(v,12) for k,v in weights.items()}))
print(f"plucker_total={W:.12f}")
print(f"disjoint_Delta={Delta:.12f}")
print(f"partner_constant={partner_constant:.12f}")
print("QFORM_B11_R24_PLUCKER_STABILITY_CHECK_PASS")
