import math
import numpy as np

# Constants in QFORM-HUB-LOWRANK-SCREEN-AMBIGUITY-v1.
for r in range(1, 8):
    a = (6*r + 5) / (2*(2*r + 3))
    theta = 1 / (2*(2*r + 3))
    C_density = (2*r + 3)/(2*r - 1) * 2**a
    C_l2 = (2*r + 3)/(2*r + 1) * 2**a
    C_collision = 2*C_l2
    b = (2*r + 3)/4
    beta = (2*r + 3)/2
    assert b > 1
    assert abs(2*b/(b-1) - 2*(2*r+3)/(2*r-1)) < 1e-12
    assert abs(2*beta/(beta-1) - 2*(2*r+3)/(2*r+1)) < 1e-12
    assert theta > 0
    print(r, f'{C_density:.15f}', f'{C_l2:.15f}', f'{C_collision:.15f}')

assert abs(((7/3)*2**(17/14)) - 5.413937135414093) < 1e-12

# Numerical GL(r) invariance check for Xi_r.
rng = np.random.default_rng(230923)
for r in (1,2,3):
    ni = r + 7
    nj = r + 8
    wI = rng.normal(size=ni)
    U = rng.normal(size=(ni,r))
    V = rng.normal(size=(nj,r))
    wJ = rng.normal(size=nj)
    PI = np.column_stack([wI,U])
    PJ = np.column_stack([V,wJ])
    GI = PI.T @ PI
    GV = V.T @ V
    GJ = PJ.T @ PJ
    Xi = np.linalg.det(GI)**2 * np.linalg.det(GV) * np.linalg.det(GJ)
    assert Xi > 0
    for _ in range(10):
        S = rng.normal(size=(r,r))
        while abs(np.linalg.det(S)) < 0.2:
            S = rng.normal(size=(r,r))
        U2 = U @ S
        V2 = V @ np.linalg.inv(S).T
        PI2 = np.column_stack([wI,U2])
        PJ2 = np.column_stack([V2,wJ])
        Xi2 = (np.linalg.det(PI2.T @ PI2)**2
               * np.linalg.det(V2.T @ V2)
               * np.linalg.det(PJ2.T @ PJ2))
        assert abs(Xi2/Xi - 1) < 1e-9

print('QFORM_B03_R23_LOWRANK_CHECK_PASS')
