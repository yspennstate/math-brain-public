import math
import numpy as np

c = 0.5 * math.sqrt(3/5)
beta = (3/16) * math.sqrt(3/5)
khalf = c * beta * (0.5**2) / (2 * math.sqrt(c*c*(0.5**2) + 4*beta*beta))

print(f"c={c:.15f}")
print(f"beta={beta:.15f}")
print(f"kappa_half={khalf:.15f}")
print(f"kappa_half_over_16={khalf/16:.15f}")
print(f"23/kappa_half={23/khalf:.12f}")
print(f"beta_over_32={beta/32:.15f}")
print(f"46/beta={46/beta:.12f}")
print(f"fixed_source_hadamard={6*(125/36)**(1/6):.12f}")
print(f"fixed_source_aligned={12*2**(-1/3):.12f}")

def hadamard(n):
    H = np.array([[1.0]])
    while H.shape[0] < n:
        H = np.block([[H, H], [H, -H]])
    return H

for m in (8, 16, 256):
    U = hadamard(m)[:, :2] / math.sqrt(m)
    u1, u2 = U[:, 0], U[:, 1]
    C = np.outer(u1, u1)
    B = np.outer(u1, u1) + np.outer(u2, u2)
    A = np.block([[C, B], [B, C]])
    eig, vec = np.linalg.eigh(A)
    mask = np.abs(eig) > 1e-9
    lev = np.sum(vec[:, mask]**2, axis=1)
    a = A[0, 0]
    b = A[1:, 0]
    S = A[1:, 1:] - np.outer(b, b) / a
    se, sv = np.linalg.eigh(S)
    smask = np.abs(se) > 1e-9
    slev = np.sum(sv[:, smask]**2, axis=1)
    print(
        f"aligned m={m}: eig={np.round(eig[mask],12).tolist()} "
        f"full_maxlev={lev.max():.12f} "
        f"schur_eig={np.round(se[smask],12).tolist()} "
        f"schur_maxlev={slev.max():.12f} theory_mu={4/(3*m):.12f}"
    )

print("QFORM_B08_R28_CHECK_PASS")
