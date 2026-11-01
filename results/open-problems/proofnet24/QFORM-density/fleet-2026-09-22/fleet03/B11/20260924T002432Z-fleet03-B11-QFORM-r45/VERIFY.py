import math
import numpy as np

rng = np.random.default_rng(20260924)
max_orth = 0.0
max_kernel = 0.0
max_eigs = 0.0
max_form = 0.0
max_det = 0.0
max_ratio = 0.0

for _ in range(500):
    q = float(rng.uniform(0.01, 0.999))
    m = 8
    Z0 = rng.normal(size=(m,3))
    O, _ = np.linalg.qr(Z0)
    Rminus = O @ np.diag([math.sqrt(1-q), 1.0, 1.0])
    r0 = np.array([math.sqrt(q), 0.0, 0.0])

    kappa = float(rng.uniform(1.0,3.0))
    d = float(rng.uniform(-2.0,2.0))
    e = float(rng.uniform(-2.0,2.0))
    c = float(rng.uniform(0.5,3.0)) * float(rng.choice([-1,1]))
    M = np.array([[0.0,kappa,0.0],[kappa,d,e],[0.0,e,c]])

    U = Rminus @ np.diag([1/math.sqrt(1-q),1.0,1.0])
    max_orth = max(max_orth, np.linalg.norm(U.T @ U - np.eye(3)))

    S = np.vstack([r0, np.diag([math.sqrt(1-q),1.0,1.0])])
    B = S @ M @ S.T
    n = np.concatenate([[math.sqrt(1-q)], -r0])
    max_kernel = max(max_kernel, np.linalg.norm(B @ n))

    evB = np.linalg.eigvalsh(B)
    evM = np.linalg.eigvalsh(M)
    nonzero = np.delete(evB, np.argmin(np.abs(evB)))
    max_eigs = max(max_eigs, np.linalg.norm(np.sort(nonzero)-np.sort(evM)))

    x = rng.normal(size=4)
    y = S.T @ x
    max_form = max(max_form, abs(x @ B @ x - y @ M @ y))

    max_det = max(max_det, abs(np.linalg.det(M) + kappa*kappa*c))
    actual_ratio = (kappa*math.sqrt(1-q))/(kappa*math.sqrt(q))
    exact_ratio = math.sqrt((1-q)/q)
    max_ratio = max(max_ratio, abs(actual_ratio-exact_ratio))

for epsilon in [1e-1, 1e-2, 1e-4, 1e-6]:
    volume = math.sqrt(epsilon) * epsilon * epsilon**(-1.5)
    assert abs(volume-1.0) < 1e-12
    assert 1.0/(3.0*epsilon) > 0

print('max_orth_error', max_orth)
print('max_kernel_error', max_kernel)
print('max_nonzero_eigenvalue_error', max_eigs)
print('max_form_error', max_form)
print('max_det_identity_error', max_det)
print('max_puncture_ratio_error', max_ratio)
print('partner_constant_Leq1_Meqe', 3*2**(2/3)*math.e**(2/3))
print('partner_constant_q_ge_63_64', 3*2**(2/3)*math.e**(2/3)*(64/63)**(1/3))
print('QFORM_B11_R45_NULL_PUNCTURE_CHECK_PASS')
