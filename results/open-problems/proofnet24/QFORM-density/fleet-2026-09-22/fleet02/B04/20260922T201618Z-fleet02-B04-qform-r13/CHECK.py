import math
import mpmath as mp
import numpy as np

mp.mp.dps = 50

H = np.array([[1,2,2],[2,1,-2],[2,-2,1]], dtype=float) / 3.0
B = 2.0 * H
C = 0.3 * np.eye(3)
D = -0.4 * np.eye(3)
u = np.ones(3) / math.sqrt(3.0)
eta = 0.2

A = np.zeros((7,7))
A[0,0] = 1.0
A[0,1:4] = eta*u
A[1:4,0] = eta*u
A[1:4,1:4] = C + eta**2*np.outer(u,u)
A[1:4,4:7] = B
A[4:7,1:4] = B.T
A[4:7,4:7] = D

evals = np.linalg.eigvalsh(A)
svB = np.linalg.svd(B, compute_uv=False)
orth_err = np.max(np.abs(H.T @ H - np.eye(3)))

C32 = mp.sqrt(mp.e/2) * mp.mpf(4)**(-mp.mpf(1)/4) * mp.beta(mp.mpf(1)/4, mp.mpf(1)/8)
main_bound = C32 / mp.sqrt(2)
s3_lower = (mp.sqrt(1649)+1)/20 - (mp.sqrt(101)+1)/50

M = np.array([[1,1,0],[1,2,1],[0,1,-1]], dtype=float)
partner_evals = np.linalg.eigvalsh(3*M)
partner_bound = 16*mp.sqrt(60)/mp.sqrt(3)/(mp.mpf(18)**(mp.mpf(1)/4))

print(f"H_orthogonality_max_error = {orth_err:.3e}")
print("cross_singular_values =", [f"{x:.12f}" for x in svB])
print("main_A_eigenvalues =", [f"{x:.12f}" for x in evals])
print("rigorous_s3_lower_via_Weyl =", mp.nstr(s3_lower, 18))
print("C_3_2 =", mp.nstr(C32, 18))
print("main_density_bound =", mp.nstr(main_bound, 18))
print("partner_active_eigenvalues =", [f"{x:.12f}" for x in partner_evals])
print("partner_density_bound =", mp.nstr(partner_bound, 18))
