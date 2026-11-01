import json, math
import numpy as np

rng = np.random.default_rng(20260923)

# Main rank-tail inequality: s_3(B+R) >= s_{r+3}(B)-s_{r+1}(R).
main_trials = 10000
main_violations = 0
min_main_margin = float('inf')
for _ in range(main_trials):
    m = int(rng.integers(5, 15))
    r = int(rng.integers(0, m-2))
    B = rng.normal(size=(m,m)); B = (B+B.T)/2
    R = rng.normal(size=(m,m)); R = (R+R.T)/2
    sB = np.linalg.svd(B, compute_uv=False)
    sR = np.linalg.svd(R, compute_uv=False)
    sF = np.linalg.svd(B+R, compute_uv=False)
    rhs = sB[r+2] - sR[r]
    margin = sF[2] - rhs
    min_main_margin = min(min_main_margin, float(margin))
    if margin < -1e-10:
        main_violations += 1

# Exact equality/sharpness construction.
r = 3
mu = 2.0
m = r+5
B = np.diag([mu]*(r+3)+[0.0]*(m-r-3))
R = np.diag([-mu]*r+[0.0]*(m-r))
sB = np.linalg.svd(B, compute_uv=False)
sR = np.linalg.svd(R, compute_uv=False)
sF = np.linalg.svd(B+R, compute_uv=False)
sharp_lhs = float(sF[2])
sharp_rhs = float(sB[r+2] - sR[r])

# Partner-style family from report Section 6.
D = np.diag([2.,-2.,2.,-2.,2.])
B12 = np.zeros((2,5)); B12[0,0] = 1.; B12[1,1] = 1.
B11 = np.zeros((2,2))
B0 = np.block([[B11,B12],[B12.T,D]])
U = np.zeros((7,2)); U[0,0] = 1.; U[1,1] = 1.
ell2 = (9-math.sqrt(17))/8
g = 2*ell2
partner_trials = 5000
partner_violations = 0
min_partner_margin = float('inf')
for _ in range(partner_trials):
    Theta = rng.normal(size=(2,2)); Theta = (Theta+Theta.T)/2
    Theta *= 10**rng.uniform(-1,3)
    Q,_ = np.linalg.qr(rng.normal(size=(7,7)))
    vals = np.zeros(7)
    vals[:2] = rng.uniform(-1000,1000,size=2)
    vals[2:] = rng.uniform(-0.2,0.2,size=5)
    R2 = Q @ np.diag(vals) @ Q.T
    H = B0 + U@Theta@U.T + R2
    sH = np.linalg.svd(H, compute_uv=False)
    sR2 = np.linalg.svd(R2, compute_uv=False)
    rhs = g - sR2[2]
    margin = sH[2]-rhs
    min_partner_margin = min(min_partner_margin, float(margin))
    if margin < -1e-10:
        partner_violations += 1

c53 = 2*math.sqrt(48*math.pi)/(7/4)
gamma66 = g-0.2
c66 = 2*math.sqrt(42*math.pi)/gamma66

out = {
    'main_trials': main_trials,
    'main_violations': main_violations,
    'min_main_margin': min_main_margin,
    'sharpness_lhs': sharp_lhs,
    'sharpness_rhs': sharp_rhs,
    'sharpness_abs_error': abs(sharp_lhs-sharp_rhs),
    'partner_trials': partner_trials,
    'partner_violations': partner_violations,
    'min_partner_margin': min_partner_margin,
    'ell_half_squared': ell2,
    'partner_protected_gap_before_tail': g,
    'partner_gap_after_tail_0p2': gamma66,
    'constant_eq_5_3': c53,
    'constant_eq_6_6': c66,
}
print(json.dumps(out, indent=2, sort_keys=True))
