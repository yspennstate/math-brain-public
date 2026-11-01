from math import sqrt

# Deterministic algebra regression for fleet03/B10 r24.
# No simulation: two explicit Parseval fixtures.

def dot(x, y):
    return sum(a*b for a, b in zip(x, y))

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return [list(x) for x in zip(*A)]

def gram(rows):
    return matmul(transpose(rows), rows)

def max_abs(A, B):
    return max(abs(A[i][j]-B[i][j]) for i in range(len(A)) for j in range(len(A[0])))

def fixture(rho, eta):
    c = 1-rho
    q0 = [1/sqrt(2), 1/sqrt(2), 0.0, 0.0]
    q1 = [sqrt(eta/2), -sqrt(eta/2), sqrt(1-eta), 0.0]
    q2 = [0.0, 0.0, 0.0, 1.0]
    s = [sqrt(rho)*x for x in q0]
    rows = [[sqrt(c), 0.0, 0.0]]
    for i in range(4):
        rows.append([s[i], q1[i], q2[i]])
    parseval_err = max_abs(gram(rows), [[1,0,0],[0,1,0],[0,0,1]])

    # Mixed rows are complement indices 0 and 1.
    rho_m = s[0]**2+s[1]**2
    # H_M is diagonal diag(eta,0) in this fixture.
    det_G = (1-rho_m)*(1-eta)

    # Lambda = [[0,2,0],[2,0,0],[0,0,1]], so |det Lambda|=4.
    det_lambda = 4.0
    det_B = det_G*det_lambda

    # Top transverse eigenvector is q1 direction; slopes are explicit.
    z0 = q1[0]/s[0]
    z1 = q1[1]/s[1]
    weighted_mean = 0.5*z0+0.5*z1
    weighted_second = 0.5*z0*z0+0.5*z1*z1
    return parseval_err, rho_m, det_G, det_B, z0, z1, weighted_mean, weighted_second

m = fixture(0.01, 0.5)
h = fixture(0.01, 0.9)

assert m[0] < 1e-12 and h[0] < 1e-12
assert abs(m[1]-0.01) < 1e-12
assert abs(m[2]-0.495) < 1e-12
assert abs(m[3]-1.98) < 1e-12
assert abs(h[7]-90.0) < 1e-10
assert abs(h[6]) < 1e-12
assert abs(h[4]*abs(h[5])-90.0) < 1e-10

C_part = (103680.0**(1/3))*(2.0**(7/6))
C_gate = C_part*((4096.0/63.0)**(1/3))
assert C_gate < 425

print(f"moderate_parseval_error={m[0]:.3e}")
print(f"moderate_rho_M={m[1]:.12f}")
print(f"moderate_det_G={m[2]:.12f}")
print(f"moderate_det_B={m[3]:.12f}")
print(f"universal_gate_constant={C_gate:.12f}")
print(f"hard_parseval_error={h[0]:.3e}")
print(f"hard_weighted_slope_mean={h[6]:.12f}")
print(f"hard_weighted_slope_second_moment={h[7]:.12f}")
print(f"hard_extreme_slope_product={h[4]*abs(h[5]):.12f}")
print("PASS")
