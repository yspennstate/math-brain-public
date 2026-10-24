import math
import numpy as np

C_diffuse = 3*2**(4/3)
C_square = 8*2**(3/4)
C_pair = 16*math.sqrt(2)

assert C_diffuse < 7.56
assert C_square < 13.455
assert C_pair < 22.628

# Carrier spectrum regression: Q=a H^2+2 nu H L+lambda V^2.
a, nu, lam = 1.5, 2.0, 1.7
B = np.array([[a, nu, 0.0], [nu, 0.0, 0.0], [0.0, 0.0, lam]])
vals = np.linalg.eigvalsh(B)
small = (math.sqrt(a*a+4*nu*nu)-abs(a))/2
assert abs(small-1.3860009363293826) < 1e-12
assert min(abs(vals)) > 1.0
assert nu*nu >= 1+abs(a)

# Grid check for the heavy-row pair branch. Write x=p_i^2, z=q_i^2,
# h=x+z>1/2. If |lambda|x<1/8 and nu^2=N>=1+|a0|,
# the physical pair determinant has magnitude >=N/4 and sigma_min>=1/8.
min_det_ratio = 10.0
min_kappa = 10.0
argmin = None
for N in [1.0, 1.25, 2.0, 4.0, 10.0, 100.0]:
    Amax = N-1.0
    for x in np.linspace(0.0, 0.124, 125):
        for z in np.linspace(max(0.501-x, 0.0), min(1.0-x, 1.0), 100):
            if x+z <= 0.5:
                continue
            # Worst cancellation has lambda*x with magnitude near 1/8 and sign matching A.
            s = 0.124
            A = Amax
            b = math.sqrt(N*z)
            M = np.array([[s, b], [b, A]])
            det = abs(np.linalg.det(M))
            sv = np.linalg.svd(M, compute_uv=False)
            kappa = min(sv)
            ratio = det/N
            if ratio < min_det_ratio:
                min_det_ratio = ratio
                argmin = (N, x, z, det, kappa)
            min_kappa = min(min_kappa, kappa)
# This grid uses s=0.124<1/8 and h>0.5, so it should exceed the analytic 1/4 determinant ratio.
assert min_det_ratio > 0.25
assert min_kappa > 0.125

# Diffuse Walsh frame: max joint row leverage exactly 1/2 and target spectrum exact.
p=np.array([1,1,-1,-1],dtype=float)/2
q=np.array([1,-1,1,-1],dtype=float)/2
assert abs(p@p-1)<1e-14 and abs(q@q-1)<1e-14 and abs(p@q)<1e-14
assert abs(np.max(p*p+q*q)-0.5)<1e-14

print('C_diffuse=', C_diffuse)
print('C_square_branch=', C_square)
print('C_pair_branch=', C_pair)
print('carrier_eigenvalues=', vals.tolist())
print('carrier_small_abs=', small)
print('grid_min_det_over_N=', min_det_ratio)
print('grid_min_kappa=', min_kappa)
print('grid_argmin=', argmin)
print('max_joint_leaf_leverage=', float(np.max(p*p+q*q)))
print('STATUS=PASS')
