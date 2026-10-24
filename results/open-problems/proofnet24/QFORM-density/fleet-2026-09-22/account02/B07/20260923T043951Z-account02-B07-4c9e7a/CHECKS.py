import itertools, math
import numpy as np

SEED = 20260923043951
rng = np.random.default_rng(SEED)

def e2(N):
    s = np.linalg.svd(N, compute_uv=False)
    x = s*s
    return 0.5*((x.sum())**2 - (x*x).sum())

def anchored_W(M):
    m,n = M.shape
    out = 0.0
    for rr in itertools.combinations(range(1,m),2):
        for cc in itertools.combinations(range(1,n),2):
            out += np.linalg.det(M[np.ix_((0,)+rr,(0,)+cc)])**2
    return out

max_identity_rel = 0.0
min_lift_ratio = float('inf')
count = 0
for m,n in [(4,4),(5,6),(7,5),(8,8)]:
    for _ in range(250):
        M = rng.normal(size=(m,n))
        if abs(M[0,0]) < 0.05:
            M[0,0] += 0.2 if M[0,0] >= 0 else -0.2
        b = M[0,0]
        r,c,D = M[0,1:], M[1:,0], M[1:,1:]
        N = b*D - np.outer(c,r)
        Z = np.sum(N*N)
        W = anchored_W(M)
        max_identity_rel = max(max_identity_rel,
                               abs(W-e2(N)/(b*b))/max(1.0,W))
        s = np.linalg.svd(M,compute_uv=False)
        T = np.sum(s[2:]**2)
        rhs = 0.5*T*Z
        if rhs > 1e-14:
            min_lift_ratio = min(min_lift_ratio,W/rhs)
        assert W + 1e-8 >= rhs
        count += 1

min_zero_b_ratio = float('inf')
for m,n in [(4,4),(5,6),(7,5)]:
    for _ in range(250):
        M = rng.normal(size=(m,n))
        M[0,0] = 0.0
        r,c,D = M[0,1:], M[1:,0], M[1:,1:]
        N = -np.outer(c,r)
        Z = np.sum(N*N)
        W = anchored_W(M)
        s = np.linalg.svd(M,compute_uv=False)
        T = np.sum(s[2:]**2)
        rhs = 0.5*T*Z
        if rhs > 1e-14:
            min_zero_b_ratio = min(min_zero_b_ratio,W/rhs)
        assert W + 2e-8 >= rhs

# Sharp equality witness M=I_3.
M = np.eye(3)
N = M[0,0]*M[1:,1:] - np.outer(M[1:,0],M[0,1:])
W = anchored_W(M)
Z = np.sum(N*N)
T = np.sum(np.linalg.svd(M,compute_uv=False)[2:]**2)
sharp_ratio = W/(0.5*T*Z)
assert abs(sharp_ratio-1.0) < 1e-12

# Live-collar constants.
theta = 1/16
Lambda = 1
kappa = 1/(256*math.sqrt(3))
tau = 1/128
omega = 121*theta**3/(2*7200**2)
Dprime_per_F = 9*math.sqrt(3*math.e)*(theta**2/6)**(-1/6)
Dprime_universal = Dprime_per_F*Lambda/kappa
terminal_core = (324*math.sqrt(math.pi)*(tau+tau**2)*omega**(-0.5)
                 *(Lambda/kappa)**3)

print('SEED',SEED)
print('random_nonzero_b_cases',count)
print('max_anchored_identity_relative_error',max_identity_rel)
print('min_W_over_half_TZ_nonzero_b',min_lift_ratio)
print('min_W_over_half_TZ_zero_b',min_zero_b_ratio)
print('sharp_I3_W_Z_T_ratio',W,Z,T,sharp_ratio)
print('omega_theta_1_16',omega)
print('Dprime_paid_cap_per_F',Dprime_per_F)
print('Dprime_paid_cap_Lambda1',Dprime_universal)
print('terminal_six_coordinate_core_cap',terminal_core)
print('QFORM_INCIDENT_E2_ANCHOR_LIFT_CHECK_PASS')
