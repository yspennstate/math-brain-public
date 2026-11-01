import math
import numpy as np

KAPPA0 = 2.0**-6
ETA = 2.0**-20
DELTA = ETA**2

c_def = math.pi / KAPPA0
c_scalar = 8.0 * 2.0**0.25 * (KAPPA0**3 * ETA)**(-0.25)
c_pair = 64.0 * (KAPPA0**3)**(-0.25) * DELTA**(-0.125)
eps_self = (1.0 + 121.0*math.sqrt(2.0))*ETA
eps_carrier = eps_self + 2.0**-6

print(f"definite_pair_bound={c_def:.15f}")
print(f"scalar_schur_bound={c_scalar:.15f}")
print(f"second_pair_bound={c_pair:.15f}")
print(f"self_rank2_error={eps_self:.15f}")
print(f"carrier_error={eps_carrier:.15f}")
print(f"carrier_s3_floor={1.0-eps_carrier:.15f}")

rng = np.random.default_rng(20260923)
max_det_res = 0.0
max_completion_res = 0.0
max_rank3 = 0.0
checked = 0

for _ in range(1000):
    q = 8
    a, b = rng.normal(size=2)
    off = 2.0 + abs(rng.normal())
    B = np.array([[a, off], [off, b]], dtype=float)
    if np.linalg.det(B) >= -0.2:
        B = np.array([[0.2, off], [off, -0.3]], dtype=float)

    F = rng.normal(size=(q-2, 2))
    G = rng.normal(size=(q-2, q-2))
    G = (G + G.T)/2.0
    A = np.block([[B, F.T], [F, G]])
    Binv = np.linalg.inv(B)
    S = G - F @ Binv @ F.T

    for __ in range(2):
        pair = rng.choice(q-2, size=2, replace=False)
        pair = [int(pair[0]), int(pair[1])]
        idx = [0, 1, 2+pair[0], 2+pair[1]]
        det4 = np.linalg.det(A[np.ix_(idx, idx)])
        rhs = np.linalg.det(B) * np.linalg.det(S[np.ix_(pair, pair)])
        den = max(1.0, abs(det4), abs(rhs))
        max_det_res = max(max_det_res, abs(det4-rhs)/den)

    L = np.block([[B, F.T], [F, F @ Binv @ F.T]])
    diff = A-L
    target = np.block([
        [np.zeros((2,2)), np.zeros((2,q-2))],
        [np.zeros((q-2,2)), S]
    ])
    max_completion_res = max(max_completion_res, np.linalg.norm(diff-target, ord=2))
    s = np.linalg.svd(L, compute_uv=False)
    max_rank3 = max(max_rank3, s[2])
    checked += 1

print(f"random_instances={checked}")
print(f"max_normalized_det_identity_residual={max_det_res:.6e}")
print(f"max_completion_identity_residual={max_completion_res:.6e}")
print(f"max_third_singular_value_rank2_completion={max_rank3:.6e}")

assert c_def < 202.0
assert c_scalar < 6889.0
assert c_pair < 46341.0
assert eps_self < 0.000165
assert eps_carrier < 0.015790
assert 1.0-eps_carrier > 0.9842
assert max_det_res < 1e-12
assert max_completion_res < 1e-12
assert max_rank3 < 1e-12
print("QFORM_B19_R42_SCHUR_PAIR_CHECK_PASS")
