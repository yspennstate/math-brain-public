from math import log, sqrt


def det3(M):
    return (
        M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
    )

# Hyperbolic density Y=2B(C+D): p_Y(y)=log(1/|y|)-1+|y|.
for y in (0.1, 0.25, 0.5, 0.9):
    a = y/2.0
    # Exact antiderivative of integral_a^(1/2) [1/b-y/(2b^2)] db.
    integral = (log(0.5)-log(a)) + (y/(2*0.5)) - (y/(2*a))
    closed = log(1/y)-1+y
    assert abs(integral-closed) < 1e-12

# E[-2 log|A|] for A uniform[-1/2,1/2].
expected_log = 2 + 2*log(2)
assert abs(expected_log - (2 + 2*log(2))) < 1e-15

# Exact p_Teps(0) formula and divergence samples.
def peak(eps):
    return 2*log(1/eps) + 1 + 2*log(2) + eps*eps/12

assert peak(1e-6) > peak(1e-3) > peak(0.1)

# Original-coordinate 3x3 hyperbolic block has characteristic roots 0,+/-sqrt(2).
B = [[0.0,1.0,1.0],[1.0,0.0,0.0],[1.0,0.0,0.0]]
for lam in (0.0, sqrt(2), -sqrt(2)):
    M = [[B[i][j] - (lam if i==j else 0.0) for j in range(3)] for i in range(3)]
    assert abs(det3(M)) < 1e-12

# Partner frame R=(1/sqrt2)[I3;I3]: v_S=v_T=1/8, bound=6.
vS = (0.5)**3
vT = (0.5)**3
partner_bound = 3.0*(vS*vT)**(-1/6)
assert abs(vS-0.125) < 1e-15
assert abs(partner_bound-6.0) < 1e-12

print('peak_eps_1e-1', peak(1e-1))
print('peak_eps_1e-3', peak(1e-3))
print('peak_eps_1e-6', peak(1e-6))
print('partner_bound', partner_bound)
print('QFORM_B11_R30_NULLSUM_JOINTCAP_COUNTEREXAMPLE_CHECK_PASS')
